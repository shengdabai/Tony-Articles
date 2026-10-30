#!/usr/bin/env python3
"""Translate pre-2026 Chinese articles into reviewable, resumable English Markdown.

The script uses a local Ollama model, preserves Markdown links and source facts,
and records a deterministic Chinese-to-English filename map after every file.
"""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.request
import urllib.parse
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
ZH_DIR = REPO / "articles" / "zh"
EN_DIR = REPO / "articles" / "en"
MAP_FILE = REPO / ".tools" / "translation-map.json"
DATE_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")
URL_RE = re.compile(r"https?://[^\s)>]+")
HAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
CRITICAL_QUANTITY_EQUIVALENTS = {
    "一万倍": re.compile(r"\b(?:10,?000|ten[ -]thousand)(?:[ -]fold|\s+times)\b", re.I),
}
HAN_ALLOWED_SOURCES = {
    # The article teaches Chinese platform-prohibited wording; retaining the
    # original terms beside their English glosses adds necessary reader value.
    "2022-05-01-视频号直播间违禁词分享给你.md",
    "2023-05-16-华杉一生不败这回彻底理解孙子兵法 新加坡南洋理工大学演讲实录.md",
    "2021-05-23-国士无双.md",
    "2021-06-12-说说语言.md",
    "2023-05-02-如何与孩子聊ChatGPTAI大时代的完整版家长指南.md",
    "2023-04-30-学习能力到底是什么.md",
}
TERM_REPLACEMENTS = {
    "Teacher Xiao Lai": "Li Xiaolai",
    "Teacher Xiaolai": "Li Xiaolai",
    "Shendaibai": "Tony Sheng",
    "Shangdabai": "Tony Sheng",
    "Shengdabai": "Tony Sheng",
    "Dabai": "Tony",
    "Fukien": "Fukuyama",
    "Video Number": "WeChat Channels",
    "Video Account": "WeChat Channels",
    "Video Channel": "WeChat Channels",
    "Video号": "WeChat Channels",
    "video号": "WeChat Channels",
    "WeChat号": "WeChat Channels",
    "Ma叔": "Uncle Mao",
    "Mao叔": "Uncle Mao",
    "Cat叔": "Uncle Mao",
    "Maomao叔": "Uncle Mao",
    "猫叔": "Uncle Mao",
    "槽边往事": "Stories from the Trough",
    "和菜头": "He Caitou",
    "点击上方蓝字关注盛大白": "Tap the blue text above to follow Tony Sheng",
    "点击上方蓝字关注大白": "Tap the blue text above to follow Tony",
    "点个在看你最好看": "Tap Like—it looks good on you",
    "侥幸": "counting on luck",
    "Star爷": "Stephen Chow",
    "星爷": "Stephen Chow",
    "模拟实战": "practice through simulation",
    "实战": "real-world practice",
    "cutting the garlic bulb": "harvesting the chives",
    "Cutting the garlic bulb": "Harvesting the chives",
    "garlic bulb": "chive",
    "Garlic bulb": "Chive",
    "GPT韭菜": "GPT Chives",
    "韭菜": "chive",
    "爆款": "viral hit",
    "恶性": "destructive",
    "企业微信": "WeCom",
    "视频号": "WeChat Channels",
    "公众号": "WeChat Official Account",
    "李笑来": "Li Xiaolai",
    "Li Xiaolai老师": "Li Xiaolai",
    "笑来老师": "Li Xiaolai",
    "盛大白": "Tony Sheng",
    "大白": "Tony",
    "微信": "WeChat",
    "得到": "Dedao",
    "陪跑": "hands-on coaching",
    "Hu妞 Lawyer": "Lawyer Huniu",
    "虎妞律师": "Lawyer Huniu",
    "S叔": "Spenser",
    "樊登老师": "Fan Deng",
    "樊登": "Fan Deng",
    "讲究": "done right",
    "莫名其妙地凑热闹 心急火燎地随大流 操碎了别人的心肝": "Joining the crowd for no reason, rushing to follow the herd, and worrying yourself sick over other people's affairs",
    "初心": "original purpose",
    "勇气": "courage",
    "动森": "Animal Crossing",
    "狸语": "Animalese",
    "所谓的": "so-called",
    "教研": "curriculum development",
    "鹰派": "hawkish",
    "鸽派": "dovish",
    "精彩": "remarkable",
    "蜗居假象": "snail-shell illusion",
    "隔行如隔山": "every profession is a world unto itself",
    "任性": "act on a whim",
    "Just哥历险记": "Brother Gang's Adventure",
    "Just哥": "Brother Gang",
    "刚哥": "Brother Gang",
    "历险记": "Adventure",
    "创业者": "entrepreneur",
    "熨斗": "iron",
    "不服气": "unwilling to accept defeat",
    "少儿英语": "children's English education",
    "语言学家": "linguist",
    "linguist语言家": "linguist",
    "语言家": "linguist",
    "language学家": "linguist",
    "学家": "scholar",
    "帝王": "king",
    "挂心间": "keep it close to heart",
    "文字稿": "written transcript",
    "稿": " transcript",
    "引流": "audience acquisition",
    "二胎": "second-child",
    "启蒙": "first introduction",
    "手抄报": "handwritten school poster",
    "抄报": "handwritten school poster",
    "同学": "classmate",
    "留学": "study-abroad",
    "谷爱凌": "Eileen Gu",
    "传销": "pyramid scheme",
    "高考加分": "bonus points on the Gaokao",
    "加分": "bonus points",
    "轿子": "sedan chair",
    "网红": "influencer",
    "轿工": "sedan-chair carriers",
    "条薮": "switches",
    "扫把": "brooms",
    "竹条": "bamboo switches",
    "自卑": "low self-esteem",
    "社恐": "social anxiety",
    "classmate们": "classmates",
    "们": "",
    "在犯罪边缘疯狂试探": "frantically testing the boundaries of acceptable behavior",
    "疯狂试探": "frantically testing the boundaries",
    "董奉，字君异，侯官（今福建省福州市）人，东汉著名医家，与南阳张机、谯郡华佗齐名，并称“建安三神医”。": "Dong Feng, courtesy name Junyi, was from Houguan (present-day Fuzhou in Fujian). A renowned physician of the Eastern Han, he was ranked alongside Zhang Ji of Nanyang and Hua Tuo of Qiao Commandery as one of the Three Divine Physicians of Jian'an.",
    "所谓“提示”，就是我输入给AI程序的一个词、一个短语、一句话或一段话。输入“提示”，AI才能回答问题或根据“提示”完成任务。": "A prompt is a word, phrase, sentence, or paragraph that I give an AI system. The AI needs that prompt before it can answer a question or complete a task.",
    "哦": "",
    "一手知识": "first-hand knowledge",
    "二手知识": "second-hand knowledge",
    "三手知识": "third-hand knowledge",
    "四手知识": "fourth-hand knowledge",
    "一手": "first-hand",
    "鸡汤": "inspirational fluff",
    "干货": "practical substance",
    "渣男": "toxic men",
    "良性循环": "positive feedback loop",
    "学霸": "top student",
    "通俗": "plain-language",
    "雏形": "prototype",
    "经营理念": "management philosophy",
    "杠精": "contrarian troll",
    "郎兹": "Leil Lowndes",
    "啰嗦": "Verbosity",
    "混沌": "Chaos",
    "趋炎附势": "currying favor with the powerful",
    "traffic红利": "traffic dividend",
    "红利": "dividend",
    "烦躁": "agitated",
    "人脉": "professional network",
    "打卡": "daily check-ins",
    "达人": "expert",
    "Butterfly号": "Butterfly Channel",
    "龟兔赛跑": "the tortoise and the hare",
    "带货": "product sales",
    "白酒": "baijiu",
    "心理咨询师": "counselor",
    "浓郁": "rich",
    "维权": "rights protection",
    "认同s": "agrees with",
    "认同ing": "accepting",
    "认同": "agreement",
    "灌输": "rote transmission",
    "加油": "keep going",
    "门槛": "barrier to entry",
    "be刻意": "be forced",
    "刻意": "deliberate",
    "机核网": "GCORES",
    "这样重": "So Heavy",
    "这样轻": "So Light",
    "涉案金额": "amount involved in the case",
    "涉案": "case-related",
    "孙子兵法": "The Art of War",
    "始计篇": "Laying Plans",
    "作战篇": "Waging War",
    "谋攻篇": "Attack by Stratagem",
    "军形篇": "Tactical Dispositions",
    "兵势篇": "Energy",
    "虚实篇": "Weak Points and Strong",
    "军争篇": "Maneuvering",
    "九变篇": "Variation of Tactics",
    "行军篇": "The Army on the March",
    "地形篇": "Terrain",
    "九地篇": "The Nine Situations",
    "火攻篇": "Attack by Fire",
    "用间篇": "The Use of Spies",
    "某某某": "so-and-so",
    "朋友圈": "WeChat Moments",
    "95后": "person born after 1995",
    "90后": "post-1990 generation",
    "00后": "post-2000 generation",
    "困境": "difficult circumstances",
    "标的物": "subject-matter asset",
    "标的": "subject matter",
    "十多分钟": "just over ten minutes",
    "逆袭": "comeback",
    "剽悍一只猫视频号": "Uncle Mao's WeChat Channels account",
    "剽悍一只猫": "Uncle Mao",
    "General渡": "Bandu",
    "general渡": "Bandu",
    "般渡": "Bandu",
    "最, 最佳, 最具, 最爱, 最赚, 最优, 最优秀": "most, best, leading, favorite, most profitable, optimal, outstanding",
    "中国第一, 全网第一, 销量第一": "number one in China, number one online, number one in sales",
}


PROMPT = """You are translating one fragment of a personal essay from Chinese into publication-quality English.

Requirements:
- Return only the translated Markdown fragment. No preface, notes, or fenced wrapper.
- Preserve every claim, example, number, proper noun, URL, Markdown link target, heading level, list, emphasis, and paragraph boundary.
- Do not add facts, citations, arguments, or advice. Do not summarize or omit material.
- Write idiomatic contemporary English rather than word-for-word Chinglish.
- Re-create awkward Chinese phrasing as natural English while keeping the exact idea. Avoid canned transitions such as "In summary" unless the source genuinely needs one.
- Preserve the author's first-person voice, emotional temperature, humor, and uncertainty.
- Translate Chinese headings and link labels, but never alter URLs.
- Use established English product names: 视频号 = WeChat Channels; 公众号 = WeChat Official Account; 微信 = WeChat; 得到 = Dedao.
- Render 李笑来 naturally as Li Xiaolai. Do not append "teacher" mechanically when 老师 is only an honorific.
- In the author's own branding, 大白 and 盛大白 refer to Tony Sheng; use Tony rather than leaving the Chinese characters in an English title.
- In politics and social science, 福山 refers to Francis Fukuyama. 视频号助手 means a WeChat Channels assistant tool, not a generic "video assistant."
- Translate 黑别人 by meaning (smear, attack, or bad-mouth someone), never literally as "blacken people."
- If a Chinese book, course, or column has no established English title, translate its meaning into a fluent descriptive title; never create awkward literal compounds.
- Translate culture-specific terms into the clearest English equivalent. Keep pinyin or Chinese in parentheses only when an English reader genuinely needs it.
- Use straight apostrophes and natural English punctuation.

Markdown fragment:
<<<
{fragment}
>>>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="qwen3:8b")
    parser.add_argument("--year", action="append", help="Translate only this year; repeatable")
    parser.add_argument("--source", action="append", help="Translate only this Chinese basename; repeatable")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-chars", type=int, default=12_000)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--oldest-first", action="store_true")
    return parser.parse_args()


def load_map() -> dict[str, str]:
    if not MAP_FILE.exists():
        return {}
    data = json.loads(MAP_FILE.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in data.items()):
        raise ValueError(f"invalid translation map: {MAP_FILE}")
    return data


def save_map(mapping: dict[str, str]) -> None:
    lock_path = MAP_FILE.with_suffix(".lock")
    with lock_path.open("a+", encoding="utf-8") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        current = load_map()
        current.update(mapping)
        mapping.clear()
        mapping.update(current)
        tmp = MAP_FILE.with_suffix(f".{os.getpid()}.tmp")
        tmp.write_text(json.dumps(dict(sorted(mapping.items())), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        tmp.replace(MAP_FILE)
        fcntl.flock(lock, fcntl.LOCK_UN)


def split_markdown(raw: str, max_chars: int) -> list[str]:
    paragraphs = re.split(r"(\n\s*\n)", raw)
    chunks: list[str] = []
    current = ""
    for part in paragraphs:
        if len(part) > max_chars:
            if current.strip():
                chunks.append(current.strip())
                current = ""
            lines = part.splitlines(keepends=True)
            buf = ""
            for line in lines:
                if len(buf) + len(line) > max_chars and buf:
                    chunks.append(buf.strip())
                    buf = ""
                buf += line
            if buf.strip():
                chunks.append(buf.strip())
            continue
        if len(current) + len(part) > max_chars and current.strip():
            chunks.append(current.strip())
            current = ""
        current += part
    if current.strip():
        chunks.append(current.strip())
    return chunks


def ollama_translate(fragment: str, model: str, attempts: int = 3) -> str:
    urls: list[str] = []
    def mask(match: re.Match[str]) -> str:
        urls.append(match.group(0))
        return f"__URL_{len(urls) - 1:04d}__"
    masked_fragment = URL_RE.sub(mask, fragment)
    payload = {
        "model": model,
        "prompt": PROMPT.format(fragment=masked_fragment),
        "stream": False,
        "think": False,
        "options": {
            "temperature": 0.15,
            "num_ctx": 32768,
            "num_predict": min(8_000, max(1_200, len(fragment) * 2)),
        },
    }
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=1800) as response:
                text = json.load(response)["response"].strip()
            text = re.sub(r"^```(?:markdown)?\s*\n", "", text, flags=re.I)
            text = re.sub(r"\n```\s*$", "", text)
            for index, url in enumerate(urls):
                token = f"__URL_{index:04d}__"
                if token not in text:
                    text += f"\n\n[Source {index + 1}]({url})"
                else:
                    text = text.replace(token, url)
            if not text:
                raise ValueError("empty model response")
            return text.strip()
        except Exception as exc:  # bounded retry for local model startup/timeouts
            last_error = exc
            if attempt < attempts:
                time.sleep(attempt * 2)
    raise RuntimeError(f"translation failed after {attempts} attempts: {last_error}")


def source_title(raw: str, fallback: str) -> str:
    for line in raw.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1)
    return fallback


def translated_title(translated: str) -> str | None:
    for line in translated.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()
    return None


def translate_title(title: str, model: str) -> str:
    prompt = f"""Translate this Chinese essay title into a concise, idiomatic English publication title.
Return only the English title, without Markdown or quotation marks. Preserve meaning; do not invent a stronger claim.
Use WeChat Channels for 视频号, WeChat Official Account for 公众号, Li Xiaolai for 李笑来/笑来, Francis Fukuyama for 福山, and Tony for the author's brand 大白/盛大白.

Chinese title: {title}
"""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {"temperature": 0.1, "num_predict": 120},
    }
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        result = json.load(response)["response"].strip().strip('"')
    if not result or HAN_RE.search(result):
        raise ValueError("title-only translation is not English")
    return result


def translate_line_strict(line: str, model: str) -> str:
    urls: list[str] = []
    def mask(match: re.Match[str]) -> str:
        urls.append(match.group(0))
        return f"__URL_{len(urls) - 1:04d}__"
    masked = URL_RE.sub(mask, line)
    prompt = f"""Translate this Markdown line completely into idiomatic English.
Translate every Chinese character, including mixed fragments inside English words. Return one Markdown line only.
Preserve placeholders, Markdown, numbers, and proper nouns. Use WeChat Channels for 视频号, WeChat Official Account for 公众号, Li Xiaolai for 李笑来/笑来, Tony for 大白/盛大白, and Uncle Mao for 猫叔.

Line: {masked}
"""
    for attempt in range(1, 4):
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "think": False,
            "options": {"temperature": 0.1 + attempt * 0.05, "num_predict": 500},
        }
        request = urllib.request.Request(
            "http://127.0.0.1:11434/api/generate",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request, timeout=300) as response:
            result = normalize_english(json.load(response)["response"].strip())
        for index, url in enumerate(urls):
            result = result.replace(f"__URL_{index:04d}__", url)
        if result and not HAN_RE.search(result):
            return result
    residual = "".join(HAN_RE.findall(result))
    raise ValueError(f"could not fully translate line (residual={residual}): {line[:160]}")


def repair_untranslated_lines(translated: str, model: str) -> str:
    lines = translated.splitlines()
    for index, line in enumerate(lines):
        if not HAN_RE.search(line):
            continue
        lines[index] = translate_line_strict(line, model)
    return "\n".join(lines)


def normalize_english(text: str) -> str:
    for old, new in TERM_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = re.sub(r"100条+", "100 Tips", text)
    text = text.replace("https://https://", "https://")
    text = text.replace("asedan chair", "a sedan chair")
    text = re.sub(r"(?<=[A-Za-z])(?:大哥|姐姐|姐|公子)", "", text)
    return text


def slugify(title: str, source_name: str) -> str:
    ascii_title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_title.lower()).strip("-")
    if not slug:
        slug = "article-" + hashlib.sha1(source_name.encode("utf-8")).hexdigest()[:10]
    return slug[:96].rstrip("-")


def strip_translated_header(translated: str) -> str:
    lines = translated.splitlines()
    for index, line in enumerate(lines):
        if re.match(r"^#\s+", line):
            lines = lines[index + 1 :]
            break
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].lstrip().startswith(">") and re.search(r"Published|publication|date", lines[0], re.I):
        while lines and lines[0].lstrip().startswith(">"):
            lines.pop(0)
        while lines and not lines[0].strip():
            lines.pop(0)
        if lines and re.fullmatch(r"-{3,}", lines[0].strip()):
            lines.pop(0)
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(lines).strip()


def rewrite_chinese_header(source_path: Path, date: str, target_name: str) -> None:
    raw = source_path.read_text(encoding="utf-8", errors="replace")
    lines = raw.splitlines()
    h1 = next((index for index, line in enumerate(lines) if re.match(r"^#\s+", line)), None)
    if h1 is None:
        return
    body_start = h1 + 1
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1
    if body_start < len(lines) and lines[body_start].lstrip().startswith(">") and re.search(r"发布日期|Published", lines[body_start]):
        while body_start < len(lines) and lines[body_start].lstrip().startswith(">"):
            body_start += 1
        while body_start < len(lines) and not lines[body_start].strip():
            body_start += 1
        if body_start < len(lines) and re.fullmatch(r"-{3,}", lines[body_start].strip()):
            body_start += 1
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1
    title_line = lines[h1]
    source_link = urllib.parse.quote(source_path.name)
    target_link = urllib.parse.quote(target_name)
    meta = f"> 发布日期:{date} · [中文](../zh/{source_link}) | [English](../en/{target_link})"
    updated = "\n".join(lines[:h1] + [title_line, "", meta, "", "---", ""] + lines[body_start:]).rstrip() + "\n"
    if updated != raw:
        tmp = source_path.with_suffix(".md.tmp")
        tmp.write_text(updated, encoding="utf-8")
        tmp.replace(source_path)


def rewrite_english_header(target_path: Path, date: str, source_name: str) -> None:
    raw = target_path.read_text(encoding="utf-8", errors="replace")
    lines = raw.splitlines()
    h1 = next((index for index, line in enumerate(lines) if re.match(r"^#\s+", line)), None)
    if h1 is None:
        return
    body_start = h1 + 1
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1
    if body_start < len(lines) and lines[body_start].lstrip().startswith(">") and re.search(r"发布日期|Published", lines[body_start]):
        while body_start < len(lines) and lines[body_start].lstrip().startswith(">"):
            body_start += 1
        while body_start < len(lines) and not lines[body_start].strip():
            body_start += 1
        if body_start < len(lines) and re.fullmatch(r"-{3,}", lines[body_start].strip()):
            body_start += 1
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1
    source_link = urllib.parse.quote(source_name)
    target_link = urllib.parse.quote(target_path.name)
    meta = f"> Published: {date} · [中文](../zh/{source_link}) | [English](../en/{target_link})"
    updated = "\n".join(lines[:h1] + [lines[h1], "", meta, "", "---", ""] + lines[body_start:]).rstrip() + "\n"
    if updated != raw:
        tmp = target_path.with_suffix(".md.tmp")
        tmp.write_text(updated, encoding="utf-8")
        tmp.replace(target_path)


def validate(source: str, translated: str, allow_han: bool = False) -> None:
    source_urls = set(URL_RE.findall(source))
    translated_urls = set(URL_RE.findall(translated))
    if source_urls != translated_urls:
        missing = sorted(source_urls - translated_urls)
        added = sorted(translated_urls - source_urls)
        raise ValueError(f"URL drift; missing={missing[:3]} added={added[:3]}")
    if len(translated) < max(120, int(len(source) * 0.22)):
        raise ValueError("translation is suspiciously short")
    for source_quantity, english_pattern in CRITICAL_QUANTITY_EQUIVALENTS.items():
        if source_quantity in source and not english_pattern.search(translated):
            raise ValueError(f"critical quantity drift: {source_quantity}")
    body = translated.split("---", 1)[-1]
    if not allow_han and HAN_RE.search(body):
        raise ValueError("English body still contains untranslated Chinese")
    if not re.search(r"^#\s+\S", translated, re.M):
        raise ValueError("missing H1 title")
    title = translated_title(translated) or ""
    if HAN_RE.search(title):
        raise ValueError("English title still contains Chinese")


def translate_file(source_path: Path, model: str, max_chars: int, mapping: dict[str, str], force: bool) -> Path:
    match = DATE_FILE_RE.match(source_path.name)
    if not match:
        raise ValueError(f"unexpected filename: {source_path.name}")
    date = match.group(1)
    raw = source_path.read_text(encoding="utf-8", errors="replace").strip()
    allow_han = source_path.name in HAN_ALLOWED_SOURCES
    chunks = split_markdown(raw, max_chars)
    cache_key = hashlib.sha256((model + "\0" + str(max_chars) + "\0" + PROMPT + "\0" + raw).encode("utf-8")).hexdigest()[:20]
    cache_dir = REPO / ".tools" / "translation-cache" / cache_key
    cache_dir.mkdir(parents=True, exist_ok=True)
    translated_chunks: list[str] = []
    for index, chunk in enumerate(chunks):
        cache_file = cache_dir / f"{index:04d}.md"
        if cache_file.exists():
            translated_chunk = cache_file.read_text(encoding="utf-8")
        else:
            translated_chunk = ollama_translate(chunk, model)
            cache_tmp = cache_file.with_suffix(".tmp")
            cache_tmp.write_text(translated_chunk, encoding="utf-8")
            cache_tmp.replace(cache_file)
        translated_chunks.append(translated_chunk)
    translated = "\n\n".join(translated_chunks).strip()
    translated = normalize_english(translated)
    if not allow_han:
        translated = repair_untranslated_lines(translated, model)
    translated = normalize_english(translated)
    title = translated_title(translated)
    if not title or HAN_RE.search(title):
        title = translate_title(source_title(raw, match.group(2)), model)
    slug = slugify(title, source_path.name)
    target_name = mapping.get(source_path.name)
    if not target_name:
        target_name = f"{date}-{slug}.md"
        if target_name in set(mapping.values()) or (EN_DIR / target_name).exists():
            suffix = hashlib.sha1(source_path.name.encode("utf-8")).hexdigest()[:8]
            target_name = f"{date}-{slug}-{suffix}.md"
    target_path = EN_DIR / target_name
    if target_path.exists() and not force and mapping.get(source_path.name) == target_name:
        return target_path
    body = strip_translated_header(translated)
    zh_link = f"../zh/{source_path.name}"
    en_link = f"../en/{target_name}"
    final = (
        f"# {title}\n\n"
        f"> Published: {date} · [中文]({zh_link}) | [English]({en_link})\n\n"
        f"---\n\n{body}\n"
    )
    validate(raw, final, allow_han=allow_han)
    EN_DIR.mkdir(parents=True, exist_ok=True)
    tmp = target_path.with_suffix(".md.tmp")
    tmp.write_text(final, encoding="utf-8")
    tmp.replace(target_path)
    rewrite_chinese_header(source_path, date, target_name)
    rewrite_english_header(target_path, date, source_path.name)
    mapping[source_path.name] = target_name
    save_map(mapping)
    return target_path


def main() -> int:
    args = parse_args()
    mapping = load_map()
    years = set(args.year or ["2021", "2022", "2023", "2024"])
    sources = [
        path
        for path in sorted(ZH_DIR.glob("20*.md"), reverse=not args.oldest_first)
        if path.name[:4] in years
    ]
    if args.source:
        wanted = set(args.source)
        sources = [path for path in sources if path.name in wanted]
    if args.limit:
        sources = sources[: args.limit]
    completed = 0
    failures: list[str] = []
    for index, path in enumerate(sources, 1):
        mapping.update(load_map())
        mapped = mapping.get(path.name)
        if mapped and (EN_DIR / mapped).exists() and not args.force:
            rewrite_chinese_header(path, path.name[:10], mapped)
            rewrite_english_header(EN_DIR / mapped, path.name[:10], path.name)
            print(f"[{index}/{len(sources)}] skip {path.name}", flush=True)
            continue
        last_error: Exception | None = None
        for file_attempt in range(1, 4):
            try:
                target = translate_file(path, args.model, args.max_chars, mapping, args.force)
                completed += 1
                print(f"[{index}/{len(sources)}] ok   {path.name} -> {target.name}", flush=True)
                last_error = None
                break
            except Exception as exc:
                last_error = exc
                print(f"[{index}/{len(sources)}] retry {file_attempt}/3 {path.name}: {exc}", file=sys.stderr, flush=True)
        if last_error is not None:
            failures.append(f"{path.name}: {last_error}")
            print(f"[{index}/{len(sources)}] FAIL {path.name}: {last_error}", file=sys.stderr, flush=True)
    print(f"translated {completed}; mapped {len(mapping)}; failures {len(failures)}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
