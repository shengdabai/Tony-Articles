import os, re, urllib.parse
BUILD = os.environ.get("ARTICLES_REPO", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
adir = os.path.join(BUILD, "articles")
date_re = re.compile(r'^(\d{4}-\d{2}-\d{2})-(.*)\.md$')

def collect(sub):
    d = os.path.join(adir, sub) if sub else adir
    if not os.path.isdir(d): return []
    out = []
    for f in os.listdir(d):
        m = date_re.match(f)
        if m: out.append((m.group(1), m.group(2), f))
    out.sort(key=lambda x: (x[0], x[2]))
    return out

def enc(sub, f):
    return f"articles/{sub}/{urllib.parse.quote(f)}" if sub else f"articles/{urllib.parse.quote(f)}"

legacy = collect("")
en = collect("en")
zh = collect("zh")

# 按日期分组, 同日期内按索引配对 en[i]<->zh[i]
from collections import defaultdict
en_by_date = defaultdict(list); zh_by_date = defaultdict(list)
for d,t,f in en: en_by_date[d].append((t,f))
for d,t,f in zh: zh_by_date[d].append((t,f))
all_dates = sorted(set(list(en_by_date)+list(zh_by_date)), reverse=True)
pairs = []  # (date, zh_tf_or_None, en_tf_or_None)
for d in all_dates:
    zl, el = zh_by_date.get(d,[]), en_by_date.get(d,[])
    for i in range(max(len(zl),len(el))):
        pairs.append((d, zl[i] if i<len(zl) else None, el[i] if i<len(el) else None))

legacy_by_year = defaultdict(list)
for d,t,f in legacy: legacy_by_year[d[:4]].append((d,t,f))

L = []
L.append("# Tony Articles · 盛大白的每日深度思考")
L.append("")
L.append("[![每日更新](https://img.shields.io/badge/更新-每日中午12:00-brightgreen)]() [![双语](https://img.shields.io/badge/语言-中文%20%2F%20English-blue)]()")
L.append("")
L.append("> 每天一篇，关于成长、学习、AI 与自我进化的深度思考。中英双语。")
L.append("")
L.append("---\n")
L.append("## 这是什么 · What This Is\n")
L.append("**中文**\n")
L.append("这里是我每天的一篇深度思考。不是碎片化的灵感速记，而是一套完整写作工作流的产物——")
L.append("我把每天的观察、阅读、对话随手记进笔记系统，再用一套固定的创作流程，把这些零散的火花打磨成一篇有出处、有逻辑、能引发思考的文章。\n")
L.append("这套流程大致是这样跑的：\n")
L.append("1. **采集** — 从我的笔记系统里召回当天积累的观察与素材；")
L.append("2. **选题** — 只挑那个最有张力、最贴近我价值理念的点：跨领域的连接、用工程化方法突破个人边界、让人和系统持续自我进化；")
L.append("3. **求证** — 给文章里每一个关键事实找到真实出处，不靠记忆硬写；")
L.append("4. **自我反驳** — 主动找反例、找逻辑漏洞，把论点逼到墙角再立起来；")
L.append("5. **成文与打磨** — 写初稿、调节奏、配类比，让它读起来像人话；")
L.append("6. **双语再创作** — 中英两版各自地道，不是机翻。\n")
L.append("每天中午 12:00，这套流程自动跑完一轮，把成稿发布到这里。\n")
L.append("**English**\n")
L.append("A daily deep-dive on growth, learning, AI, and self-evolution — in both Chinese and English.\n")
L.append("Each piece is the output of a complete writing workflow, not a quick note. Throughout the day I capture observations, readings, and conversations into my note system; then a fixed creative pipeline turns those scattered sparks into a sourced, reasoned, thought-provoking article:\n")
L.append("1. **Gather** — recall the day's raw material from my notes;")
L.append("2. **Choose** — pick the single idea with the most tension, closest to what I care about: cross-domain connections, engineering past personal limits, systems that keep evolving themselves;")
L.append("3. **Verify** — find a real source for every key fact, never write from memory alone;")
L.append("4. **Steelman the opposition** — hunt for counter-examples and logic holes, then rebuild the argument stronger;")
L.append("5. **Draft & polish** — rhythm, analogy, prose that reads like a human wrote it;")
L.append("6. **Bilingual re-creation** — Chinese and English versions each in their own voice, not machine translation.\n")
L.append("Published here every day at noon (China time).\n")
L.append("---\n")
L.append("## 📅 每日新作 · Daily Articles\n")
if pairs:
    for d, ztf, etf in pairs:
        parts = []
        if ztf: parts.append(f"[🇨🇳 {ztf[0]}]({enc('zh', ztf[1])})")
        if etf: parts.append(f"[🇬🇧 {etf[0]}]({enc('en', etf[1])})")
        L.append(f"- **{d}** — " + "  ·  ".join(parts))
else:
    L.append("*首篇即将发布…*")
L.append("\n---\n")
L.append("## 📚 往期公众号存档 · Archive (2021–2024)\n")
L.append(f"共 {len(legacy)} 篇早年公众号文章，按年份归档：\n")
for y in sorted(legacy_by_year, reverse=True):
    L.append(f"- **[{y} 年文章 ({len(legacy_by_year[y])} 篇)](archive/{y}.md)**")
L.append("\n---\n")
L.append("*盛大白 · Tony — 中文教育者，终身学习者，相信用 AI 让人变强而非变懒。*")
open(os.path.join(BUILD,"README.md"),"w",encoding="utf-8").write("\n".join(L)+"\n")

arch=os.path.join(BUILD,"archive"); os.makedirs(arch,exist_ok=True)
for y,items in legacy_by_year.items():
    A=[f"# {y} 年文章存档","",f"共 {len(items)} 篇 · [← 返回主页](../README.md)","","---",""]
    cur=None
    for d,t,f in items:
        ym=d[:7]
        if ym!=cur: A+=["",f"### {ym}",""];cur=ym
        A.append(f"- {d} · [{t or f}](../{enc('',f)})")
    open(os.path.join(arch,f"{y}.md"),"w",encoding="utf-8").write("\n".join(A)+"\n")
print(f"每日 {len(pairs)} 篇 · 历史 {len(legacy)} · 年份 {sorted(legacy_by_year)}")
