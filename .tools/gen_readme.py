import os, re, urllib.parse, sys
BUILD = os.environ.get("ARTICLES_REPO", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
adir = os.path.join(BUILD, "articles")
files = sorted(f for f in os.listdir(adir) if f.endswith(".md"))
date_re = re.compile(r'^(\d{4}-\d{2}-\d{2})-(.*)\.md$')
items = []
for f in files:
    m = date_re.match(f)
    if not m: continue
    items.append((m.group(1), m.group(2), f))
items.sort(key=lambda x: (x[0], x[2]))
total, first, last = len(items), items[0][0], items[-1][0]
L = ["# Tony Articles · 盛大白文章集", "",
     "> 盛大白(Tony)公众号文章归档 + 每日新作。",
     f"> 共 **{total}** 篇文章,时间跨度 {first} → {last}。",
     "> 每天中午 12:00 自动推送一篇新文章 —— 基于当日笔记,捕捉有独特价值、引发思考、与我相关的内容点创作。",
     "", "---", "", "## 文章索引(按时间线)", ""]
cur = None
for date, title, f in items:
    ym = date[:7]
    if ym != cur:
        L += ["", f"### {ym}", ""]; cur = ym
    L.append(f"- {date} · [{title or f}](articles/{urllib.parse.quote(f)})")
open(os.path.join(BUILD, "README.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print(f"README 更新: {total} 篇")
