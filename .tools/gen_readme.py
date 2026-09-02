#!/usr/bin/env python3
"""生成 Tony-Articles 主 README、双语索引与年份存档页。"""
import json, os, re, urllib.parse
from collections import defaultdict

BUILD = os.environ.get("ARTICLES_REPO", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
adir = os.path.join(BUILD, "articles")
date_re = re.compile(r'^(\d{4}-\d{2}-\d{2})-(.*)\.md$')

def article_title(path, fallback):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                m = re.match(r'^#\s+(.+?)\s*$', line)
                if m:
                    return m.group(1)
    except OSError:
        pass
    return fallback

def collect_dir(d):
    if not os.path.isdir(d): return []
    out = []
    for f in os.listdir(d):
        m = date_re.match(f)
        if m: out.append((m.group(1), article_title(os.path.join(d, f), m.group(2)), f))
    out.sort(key=lambda x: (x[0], x[2]), reverse=True)
    return out

def collect(sub):
    return collect_dir(os.path.join(adir, sub) if sub else adir)

def enc(sub, f, base="articles"):
    return f"{base}/{sub}/{urllib.parse.quote(f)}" if sub else f"{base}/{urllib.parse.quote(f)}"

en = collect("en")
zh = collect("zh")
news_zh = collect_dir(os.path.join(BUILD, "ai-news", "zh"))
news_en = collect_dir(os.path.join(BUILD, "ai-news", "en"))

en_by_file = {f: (d, t, f) for d, t, f in en}
translation_map_path = os.path.join(BUILD, ".tools", "translation-map.json")
try:
    with open(translation_map_path, encoding="utf-8") as fh:
        translation_map = json.load(fh)
except (OSError, ValueError, TypeError):
    translation_map = {}

def linked_english(zh_file):
    mapped = translation_map.get(zh_file)
    if mapped in en_by_file:
        return mapped
    try:
        raw = open(os.path.join(adir, "zh", zh_file), encoding="utf-8", errors="replace").read(1200)
    except OSError:
        return None
    m = re.search(r'\.\./en/([^\n)]+\.md)', raw)
    return urllib.parse.unquote(m.group(1)) if m and urllib.parse.unquote(m.group(1)) in en_by_file else None

pairs = []
used_en = set()
for d, t, f in zh:
    ef = linked_english(f)
    etf = (en_by_file[ef][1], ef) if ef else None
    if ef:
        used_en.add(ef)
    pairs.append((d, (t, f), etf))
for d, t, f in en:
    if f not in used_en:
        pairs.append((d, None, (t, f)))
pairs.sort(key=lambda item: (item[0], item[1][1] if item[1] else item[2][1]), reverse=True)

by_year = defaultdict(list)
for pair in pairs:
    by_year[pair[0][:4]].append(pair)

def render_daily():
    if not pairs:
        return ['*首篇即将发布 · First piece coming soon…*']
    out = []
    for d, ztf, etf in pairs:
        parts = []
        if ztf: parts.append(f'[🇨🇳 中文 · {ztf[0]}]({enc("zh", ztf[1])})')
        if etf: parts.append(f'[🇬🇧 English · {etf[0]}]({enc("en", etf[1])})')
        out.append(f'- **{d}** — ' + '  ·  '.join(parts))
    return out

def render_news():
    zh_d = defaultdict(list); en_d = defaultdict(list)
    for d,t,f in news_zh: zh_d[d].append((t,f))
    for d,t,f in news_en: en_d[d].append((t,f))
    dates = sorted(set(list(zh_d)+list(en_d)), reverse=True)[:14]
    if not dates:
        return ['*首条 AI 热点即将发布 · First AI daily coming soon…*']
    out = []
    for d in dates:
        zl, el = zh_d.get(d,[]), en_d.get(d,[])
        for i in range(max(len(zl),len(el))):
            ztf = zl[i] if i<len(zl) else None
            etf = el[i] if i<len(el) else None
            parts = []
            if ztf: parts.append(f'[🇨🇳 中文 · {ztf[0]}]({enc("zh", ztf[1], base="ai-news")})')
            if etf: parts.append(f'[🇬🇧 English · {etf[0]}]({enc("en", etf[1], base="ai-news")})')
            out.append(f'- **{d}** — ' + '  ·  '.join(parts))
    return out

README = '''<div align="center">

# 🌱 Tony Articles

**盛大白的每日深度思考 · Tony's Daily Deep-Dives**

[![Last commit](https://img.shields.io/github/last-commit/shengdabai/Tony-Articles?style=flat-square&label=%E6%9C%80%E8%BF%91%E6%9B%B4%E6%96%B0%20last%20commit)](https://github.com/shengdabai/Tony-Articles/commits/main) [![Stars](https://img.shields.io/github/stars/shengdabai/Tony-Articles?style=social)](https://github.com/shengdabai/Tony-Articles/stargazers) [![Follow @shengdabai](https://img.shields.io/github/followers/shengdabai?style=social&label=Follow%20%40shengdabai)](https://github.com/shengdabai)

[![每日更新 / Daily](https://img.shields.io/badge/更新-每日中午%2012%3A00-brightgreen?style=flat-square)](#-全部文章--all-articles) [![中英双语 / Bilingual](https://img.shields.io/badge/语言-中文%20%2F%20English-blue?style=flat-square)](#-中文阅读) [![知识花园 / Garden](https://img.shields.io/badge/Knowledge%20Garden-notes.zturnsgo.com-orange?style=flat-square)](https://notes.zturnsgo.com/) [![文章 / Articles](https://img.shields.io/badge/文章-{TOTAL_N}%20篇-lightgrey?style=flat-square)](#-全部文章--all-articles)

**[🇨🇳 中文文章（由近到远）](articles/zh/README.md)** ｜ **[🇬🇧 English Articles (Newest First)](articles/en/README.md)** ｜ **[📚 全部双语文章](#-全部文章--all-articles)** ｜ **[🌐 知识花园 Garden](https://notes.zturnsgo.com/)**

</div>

---

## 📚 全部文章 · All Articles

> 中文版与英文版均按发布日期由近到远排列。2021–2024 年旧文已补齐英文重写版。
> Both language editions are ordered newest to oldest. The 2021–2024 archive now includes English re-creations.

{DAILY_LIST}

---

## 📰 AI 圈每日热点 · AI Daily News

> 每天中午 12:00 自动整理过去 24 小时 AI 圈最值得关心的 6-8 条精选,面向 AI 工具、Agent、独立开发和自我进化系统,中英双语。
> Curated daily at 12:00 — the 6-8 most signal-rich items from the past 24 hours of AI, with a focus on AI tooling, agents, independent builders, and self-evolving systems.

{NEWS_LIST}

---

## 🇨🇳 中文阅读

### 这里是什么

我是盛大白(Tony),一名自由职业中文培训师。**这个仓库是我每天的一篇深度思考。**

不是碎片化的灵感速记,不是 AI 一键生成的口水文,而是**一套完整写作工作流的产物**——
我把每天的观察、阅读、对话、突然冒出来的念头随手记进笔记系统,
再由一套固定的创作流程,把这些零散的火花打磨成一篇有出处、有逻辑、能引发思考的文章。

> 如果你想看更生鲜的、未经打磨的笔记原貌,欢迎逛我的[**知识花园 / Notes Garden** 🌐](https://notes.zturnsgo.com/)——
> 那里是这些文章的素材源头,也是我每天真正在用的第二大脑。

### 为什么做这件事

我相信几件事:

- **跨时空连接** —— 真正有力的洞见,常常来自不同领域、不同时代、不同学科的意外撞击。
- **工程化破界** —— 用系统化的方法把「想清楚一件事」变成可以每天重复的流程,而不是等灵感。
- **自进化系统** —— 不是写完一篇就完事,而是让人和这套写作系统都在持续迭代、复利成长。
- **用 AI 让人变强,而不是变懒** —— AI 是放大镜,不是替身。如果一个工具让你停止思考,那你用错了。
- **长期主义、践行导向** —— 受李笑来影响,写作是体力活,只要你愿意,随时都可以。

如果上面这些理念让你有共鸣,这个仓库就是为你准备的。

### 每天的文章是怎么「长」出来的

一篇文章,从我的笔记到发布到这里,要经过 13 个阶段的工程化流水线。简化成 6 大步骤:

**① 采集 · Gather**
> 流程从我的笔记系统里召回当天积累的素材开始——可能是清晨听到的一句话,可能是地铁上读到的一段文字,可能是和朋友的一次争论。不依赖记忆,只读真实记录下的痕迹。

**② 选题 · Choose**
> 一天可能记了几十条笔记。选题这一步只挑那个**最有张力、最贴近我价值理念**的点——通常是一个能引发「咦?这事儿原来可以这么看」的反常识连接。其他都先放下。

**③ 求证 · Verify**
> 给文章里每一个关键事实——年份、数字、引用、人名、事件——找到真实出处。**不靠记忆硬写**。这是最耗时但最关键的一步,文章的可信度全在这里。

**④ 自我反驳 · Steelman the opposition**
> 主动找反例、找逻辑漏洞、找幸存者偏差。一个论点要是经不起自己反驳,就更经不起读者反驳。把它逼到墙角,要么推翻、要么重建得更强。

**⑤ 成文与打磨 · Draft & polish**
> 写初稿,调节奏,配类比,让它读起来像「人话」——不是 AI 那种四平八稳的辞令,而是有呼吸、有起伏、有温度的文字。

**⑥ 双语再创作 · Bilingual re-creation**
> 中英两版各自地道。**不是机器翻译**——而是用各自语言的内在节奏重新写一遍,让英文读者读到的是英文该有的样子,中文读者读到的是中文该有的样子。

整套流程每天中午 12:00 自动跑完一轮,产物推送到这里。

### 你会在这里读到什么

- 关于**学习与自我进化**:怎么让自己持续变强,怎么避开学习的陷阱。
- 关于 **AI 与人的关系**:在 AI 时代什么是不可被复制的、什么是真正属于你的护城河。
- 关于**跨时空连接**:历史里的人和今天的我们,有什么惊人的共通处。
- 关于**践行与长期主义**:那些「听过 100 遍但还没做到」的事,如何真正做到。
- 关于**作为中文教师的观察**:语言、文化、教育、技术,在我这个独特位置上交织的视角。

### 怎么跟我互动

- ⭐ **Star** 一下这个仓库,新文章会更稳定地推到你的 GitHub 主页
- 👀 点 **Watch → Custom → Releases**(我会定期发月度精选 Release)
- 💬 在 [Issues](https://github.com/shengdabai/Tony-Articles/issues) 里告诉我你想看什么主题
- 🌐 逛我的[**知识花园**](https://notes.zturnsgo.com/),看原始笔记
- 📚 按时间翻阅[全部中文文章](articles/zh/README.md)，共 {TOTAL_N} 篇

### 同系列仓库 · 一起逛逛

这几个仓库出自同一套「在公开处用工程化方法做事」的实践,可以串着看:

- 🌿 **[tony-knowledge-garden](https://github.com/shengdabai/tony-knowledge-garden)** —— 公开的知识花园:AI、中文教学、学习方法的原始笔记与连接。
- 🔎 **[Small-yet-smart-programs](https://github.com/shengdabai/Small-yet-smart-programs)** —— 自托管扫描器,每天发掘「小而美、可复制、能赚钱」的产品机会。
- 🛠️ **[Tony-Claude-Code-Skills](https://github.com/shengdabai/Tony-Claude-Code-Skills)** —— 我自己在用的 Claude Code skills、agents 与 Codex 工作流合集。

---

## 🇬🇧 Read in English

### What This Is

I am Tony (盛大白), a freelance Chinese-language teacher. **This repo is my daily deep-dive — one piece every day.**

Not a quick note. Not AI-generated filler. Each piece is the output of **a complete writing workflow**: throughout the day I capture observations, readings, conversations, and stray thoughts into my note system; then a fixed creative pipeline turns those scattered sparks into a sourced, reasoned, thought-provoking article.

> If you want to see the rawer, unpolished version of these ideas, visit my [**Notes Garden** 🌐](https://notes.zturnsgo.com/) — that is where the source material lives, and where I actually think every day.

### Why I Do This

A few beliefs:

- **Cross-domain connections** — the most powerful insights usually come from unexpected collisions between different fields, eras, and disciplines.
- **Engineering past personal limits** — turn deep thinking into a repeatable system, instead of waiting for inspiration.
- **Self-evolving systems** — finishing one piece is not the point; both the writer and the system should keep improving with compound interest.
- **Use AI to amplify yourself, not replace yourself** — AI is a magnifying glass, not a stand-in. If a tool makes you stop thinking, you are using it wrong.
- **Long-termism, executed daily** — writing is a manual craft. If you are willing, you can always start, anytime.

If any of this resonates, this repo is for you.

### How Each Article Comes To Be

Every article goes through a 13-stage engineered pipeline, condensed into 6 steps:

**① Gather**
> The process starts by recalling the day's raw material from my note system — a sentence overheard at dawn, a paragraph on the subway, an argument with a friend. Never from memory; always from a real captured trace.

**② Choose**
> A day might produce dozens of notes. This step picks the single one with the **most tension and closest fit to what I care about** — usually an unexpected connection that surprises me. Everything else gets dropped.

**③ Verify**
> For every key fact in the piece — years, numbers, quotes, names, events — find a real source. **Never write from memory alone.** This is the slowest but most critical step; the credibility of the whole article lives here.

**④ Steelman the opposition**
> Actively hunt for counter-examples, logic holes, survivorship bias. If an argument cannot survive my own attack, it definitely cannot survive the reader. Push it into a corner, then either kill it or rebuild it stronger.

**⑤ Draft & polish**
> Write the draft, tune the rhythm, find the analogies. Make it sound like a human wrote it — not AI flat, balanced phrasing, but prose with breath, rise, and warmth.

**⑥ Bilingual re-creation**
> The Chinese and English versions are each native in their own language. **Not machine translation** — I re-write each in its own internal rhythm, so English readers get English-shaped prose and Chinese readers get Chinese-shaped prose.

The whole pipeline runs automatically once a day at noon (China time), and pushes here.

### What You Will Find Here

- On **learning and self-evolution**: how to keep getting stronger, how to dodge the common traps.
- On **AI and human work**: in the age of AI, what cannot be replicated, what is actually *yours*.
- On **cross-time connections**: striking parallels between historical figures and us today.
- On **execution and long-termism**: ideas you have heard a hundred times but still have not acted on — how to actually do them.
- On **the view from a Chinese-language teacher**: language, culture, education, and technology, intersecting at this peculiar vantage point.

### How to Engage

- ⭐ **Star** the repo — new pieces show up more reliably on your GitHub home
- 👀 Watch → Custom → **Releases** (monthly best-of as Releases)
- 💬 [Open an Issue](https://github.com/shengdabai/Tony-Articles/issues) to suggest a topic
- 🌐 Browse my [**Notes Garden**](https://notes.zturnsgo.com/) for the raw material
- 📚 Browse [all English articles, newest first](articles/en/README.md) — {TOTAL_N} pieces

### Sibling repos · worth a look

All from the same practice of *doing things in public, with an engineering mindset*:

- 🌿 **[tony-knowledge-garden](https://github.com/shengdabai/tony-knowledge-garden)** — my public knowledge garden: raw notes and connections on AI, Chinese teaching, and learning.
- 🔎 **[Small-yet-smart-programs](https://github.com/shengdabai/Small-yet-smart-programs)** — a self-hosted scanner that surfaces small, replicable, profitable product ideas every day.
- 🛠️ **[Tony-Claude-Code-Skills](https://github.com/shengdabai/Tony-Claude-Code-Skills)** — the Claude Code skills, agents, and Codex workflows I actually use.

---

## 📚 年份导航 · Browse by Year

全部文章已统一放进 `articles/zh/` 与 `articles/en/`，每个年份页同样按由近到远排列。

All pieces now live under `articles/zh/` and `articles/en/`. Every year page is also ordered newest first.

{YEAR_LIST}

---

## 👤 关于我 · About Me

**盛大白 Tony Sheng**

- 自由职业中文培训师 · Freelance Chinese-language teacher
- 教过 6000+ 学员 · Taught 6,000+ learners
- 终身学习者 · Lifelong learner
- 相信「用 AI 让人变强,而不是变懒」 · Believer that *AI should make you stronger, not lazier*

**找到我 · Find me:**

- 🌐 知识花园 / Notes Garden: [notes.zturnsgo.com](https://notes.zturnsgo.com/)
- 🏠 个人网站 / Website: [zturnsgo.com](https://zturnsgo.com/)
- 💻 GitHub: [@shengdabai](https://github.com/shengdabai)

---

<div align="center">

*「写作是体力活,只要你愿意,随时都可以。」*

*Writing is a manual craft. If you are willing, you can always start, anytime.*

**[⬆ 回到顶部 · Back to top](#-tony-articles)**

</div>
'''

year_lines = []
for y in sorted(by_year, reverse=True):
    n = len(by_year[y])
    year_lines.append(f'- 📂 **[{y} 年文章 · {y} Articles ({n} 篇)](archive/{y}.md)**')

out = (README
       .replace('{DAILY_LIST}', '\n'.join(render_daily()))
       .replace('{NEWS_LIST}', '\n'.join(render_news()))
       .replace('{YEAR_LIST}', '\n'.join(year_lines))
       .replace('{TOTAL_N}', str(len(zh))))

open(os.path.join(BUILD, 'README.md'), 'w', encoding='utf-8').write(out)

arch = os.path.join(BUILD, 'archive'); os.makedirs(arch, exist_ok=True)
for y, items in by_year.items():
    A = [f'# 📂 {y} 年文章存档 · {y} Archive', '',
         f'共 **{len(items)} 篇** · {len(items)} pieces · [← 返回主页 / Back to home](../README.md)',
         '', '---', '']
    for d, ztf, etf in items:
        parts = []
        if ztf:
            parts.append(f'[🇨🇳 {ztf[0]}](../{enc("zh", ztf[1])})')
        if etf:
            parts.append(f'[🇬🇧 {etf[0]}](../{enc("en", etf[1])})')
        A.append(f'- {d} · ' + ' · '.join(parts))
    A += ['', '---', '', '[← 返回主页 / Back to home](../README.md)']
    open(os.path.join(arch, f'{y}.md'), 'w', encoding='utf-8').write('\n'.join(A) + '\n')

def write_language_index(lang, items):
    is_zh = lang == "zh"
    title = "中文文章 · 由近到远" if is_zh else "English Articles · Newest First"
    intro = "全部中文版按发布日期倒序排列。" if is_zh else "All English editions, ordered by publication date from newest to oldest."
    lines = [f'# {title}', '', intro, '', '[← 返回主页 / Back to home](../../README.md)', '', '---', '']
    cur = None
    for d, t, f in items:
        ym = d[:7]
        if ym != cur:
            cur = ym
            lines += ['', f'## {ym}', '']
        lines.append(f'- {d} · [{t}](./{urllib.parse.quote(f)})')
    lines += ['', '---', '', '[← 返回主页 / Back to home](../../README.md)']
    open(os.path.join(adir, lang, 'README.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')

write_language_index("zh", zh)
write_language_index("en", en)

print(f'✓ README 已生成 · 中文 {len(zh)} 篇 · 英文 {len(en)} 篇 · 年份 {sorted(by_year)}')
