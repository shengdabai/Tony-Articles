#!/usr/bin/env python3
"""
Prepare English Tony Articles for X Articles publishing.

The script uses git sparse checkout plus GPT Image 2 via the local Codex CLI
to produce X-ready article packages.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import shutil
import subprocess
import tempfile
import textwrap
from pathlib import Path
from typing import Iterable
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
READY_DIR = ROOT / "x-ready"
GPT_IMAGE_SCRIPT = Path("/Users/tonysheng/.codex/skills/gpt-image-2/scripts/gen.sh")
TOP_LEVEL_PACKAGE_FILES = {"cover.png", "x-article-copy.html", "ending-image.png", "manifest.json"}
DATE_RE = re.compile(r"^(20\d{2}-\d{2}-\d{2})-(.+)\.md$")
FOOTNOTE_DEF_RE = re.compile(r"^\[\^(\d+)\]:\s*(.*)$")
FOOTNOTE_REF_RE = re.compile(r"\[\^(\d+)\]")
SOURCE_HEADING_RE = re.compile(r"^##\s+(Sources|References)\s*$", re.IGNORECASE | re.MULTILINE)
INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")


def atomic_write(path: Path, data: str | bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    if isinstance(data, bytes):
        tmp.write_bytes(data)
    else:
        tmp.write_text(data, encoding="utf-8")
    tmp.replace(path)


def sync_2026_articles(work_dir: Path) -> list[Path]:
    clone_dir = work_dir / "repo"
    subprocess.run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            "--filter=blob:none",
            "--sparse",
            "https://github.com/shengdabai/Tony-Articles.git",
            str(clone_dir),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=60,
    )
    subprocess.run(
        ["git", "-C", str(clone_dir), "sparse-checkout", "set", "articles/en"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=60,
    )
    return sorted((clone_dir / "articles" / "en").glob("2026-*.md"), key=lambda p: p.name)


def select_article(files: list[Path], date: str | None, latest: bool) -> Path:
    if not files:
        raise RuntimeError("No 2026 English articles found. Run sync first.")
    if date:
        matches = [p for p in files if p.name.startswith(date + "-")]
        if not matches:
            raise RuntimeError(f"No article found for {date}.")
        return matches[-1]
    if latest:
        return files[-1]
    today = dt.date.today().isoformat()
    matches = [p for p in files if p.name.startswith(today + "-")]
    return matches[-1] if matches else files[-1]


def parse_article(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = path.stem
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()

    match = DATE_RE.match(path.name)
    if not match:
        raise RuntimeError(f"Unexpected article filename: {path.name}")
    date, slug = match.groups()

    body_lines: list[str] = []
    footnotes: list[str] = []
    skip_intro_meta = True
    for line in lines[1:]:
        if skip_intro_meta:
            if line.strip() == "---" or not line.strip() or line.startswith(">"):
                continue
            skip_intro_meta = False
        footnote_match = FOOTNOTE_DEF_RE.match(line)
        if footnote_match:
            footnotes.append(f"{footnote_match.group(1)}. {footnote_match.group(2).strip()}")
        else:
            body_lines.append(line)

    body = "\n".join(body_lines).strip()
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip() and not p.startswith("## ")]
    thesis = article_promise(paragraphs) or first_plain_sentence(paragraphs) or title
    return {
        "date": date,
        "slug": slug,
        "title": title,
        "body": body,
        "footnotes": footnotes,
        "thesis": thesis,
        "sections": section_cards(body),
        "tagline": cover_tagline(body, title),
    }


def article_promise(paragraphs: Iterable[str]) -> str:
    priority = [
        "The real teacher is",
        "The better question is",
        "The practical lesson is",
        "The difference is",
        "The goal is",
    ]
    cleaned = [FOOTNOTE_REF_RE.sub("", re.sub(r"\s+", " ", p)).strip() for p in paragraphs]
    for phrase in priority:
        for paragraph in cleaned:
            if phrase in paragraph:
                sentences = re.split(r"(?<=[.!?])\s+", paragraph)
                for sentence in sentences:
                    if phrase in sentence:
                        return sentence.strip()[:190]
    return ""


def section_cards(body: str) -> list[tuple[str, str]]:
    parts = re.split(r"^##\s+", body, flags=re.MULTILINE)
    cards: list[tuple[str, str]] = []
    for part in parts[1:]:
        lines = part.strip().splitlines()
        if not lines:
            continue
        heading = lines[0].strip()
        content = "\n".join(lines[1:]).strip()
        clean = FOOTNOTE_REF_RE.sub("", re.sub(r"\s+", " ", content)).strip()
        sentence = re.split(r"(?<=[.!?])\s+", clean)[0].strip() if clean else ""
        cards.append((heading, sentence[:105]))
    return cards[:6]


def cover_tagline(body: str, title: str) -> str:
    headings = re.findall(r"^##\s+(.+)$", body, flags=re.MULTILINE)
    short = []
    for heading in headings:
        cleaned = re.sub(r"^(The|A|An)\s+", "", heading).strip()
        cleaned = re.sub(r"[,;:.!?]+", "", cleaned)
        words = cleaned.split()
        short.append(" ".join(words[:3]))
        if len(short) == 2:
            break
    if len(short) >= 2:
        return " -> ".join(short)
    title_words = title.split()
    return " ".join(title_words[:5])


def first_plain_sentence(paragraphs: Iterable[str]) -> str:
    for paragraph in paragraphs:
        clean = re.sub(r"\s+", " ", paragraph)
        clean = FOOTNOTE_REF_RE.sub("", clean)
        clean = clean.replace("*", "").strip()
        if len(clean) < 40:
            continue
        sentence = re.split(r"(?<=[.!?])\s+", clean)[0].strip()
        return sentence[:190]
    return ""


def wrap_text_chars(text: str, max_chars: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        if len(test) <= max_chars:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def tspans(lines: list[str], x: int, y: int, line_height: int) -> str:
    escaped = [html.escape(line) for line in lines]
    return "\n".join(
        f'<tspan x="{x}" y="{y + i * line_height}">{line}</tspan>' for i, line in enumerate(escaped)
    )


def render_svg_to_png(svg_path: Path, png_path: Path, width: int, height: int) -> None:
    magick = shutil.which("magick")
    if not magick:
        raise RuntimeError("ImageMagick `magick` command not found; cannot render PNG.")
    subprocess.run(
        [magick, "-size", f"{width}x{height}", str(svg_path), str(png_path)],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=60,
    )


def crop_to_size(src: Path, out: Path, width: int, height: int) -> None:
    magick = shutil.which("magick")
    if not magick:
        raise RuntimeError("ImageMagick `magick` command not found; cannot crop generated image.")
    subprocess.run(
        [
            magick,
            str(src),
            "-resize",
            f"{width}x{height}^",
            "-gravity",
            "center",
            "-extent",
            f"{width}x{height}",
            "-strip",
            str(out),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=60,
    )


def gpt_image(prompt: str, out: Path, width: int, height: int, timeout_sec: int, force: bool) -> None:
    if out.exists() and not force:
        return
    if not GPT_IMAGE_SCRIPT.exists():
        raise RuntimeError(f"GPT Image 2 script not found: {GPT_IMAGE_SCRIPT}")
    out.parent.mkdir(parents=True, exist_ok=True)
    raw = out.with_name(out.stem + "-raw-gpt-image-2.png")
    atomic_write(out.with_suffix(".prompt.txt"), prompt + "\n")
    subprocess.run(
        [
            "bash",
            str(GPT_IMAGE_SCRIPT),
            "--timeout-sec",
            str(timeout_sec),
            "--prompt",
            prompt,
            "--out",
            str(raw),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=timeout_sec + 30,
    )
    crop_to_size(raw, out, width, height)
    raw.unlink(missing_ok=True)


def cover_prompt(article: dict) -> str:
    return (
        "Create a compelling abstract editorial cover image for an English X Article. "
        f"Title: {article['title']}. "
        f"Core idea: {article['thesis']}. "
        "Make it visually arresting for English-speaking readers on X: sophisticated, "
        "curiosity-provoking, cinematic but not generic, with a strong abstract metaphor "
        "for the essay's idea. Use rich contrast, depth, and one memorable visual hook. "
        "No readable text, no letters, no logos, no UI, no screenshots, no social-media mockups. "
        "Wide 5:2 composition, modern editorial art direction, suitable as a serious essay cover."
    )


def ending_prompt(article: dict) -> str:
    section_text = "; ".join(f"{title}: {summary}" for title, summary in article.get("sections", [])[:4])
    return (
        "Create a thoughtful abstract ending image for an English long-form X Article. "
        f"Title: {article['title']}. "
        f"Core idea: {article['thesis']}. "
        f"Argument notes: {section_text}. "
        "The image should feel like a visual aftertaste: memorable, reflective, slightly surprising, "
        "and likely to make readers pause, save, or share. Avoid literal diagrams. "
        "No readable text, no letters, no logos, no UI, no screenshots. "
        "16:9 composition, modern abstract editorial illustration, high visual quality."
    )


def save_gpt_images(article: dict, package_dir: Path, timeout_sec: int, force: bool) -> None:
    gpt_image(cover_prompt(article), package_dir / "cover.png", 3000, 1200, timeout_sec, force)
    gpt_image(ending_prompt(article), package_dir / "ending-image.png", 1600, 900, timeout_sec, force)


def save_svg_cover(article: dict, out: Path) -> None:
    width, height = 3000, 1200
    title_lines = wrap_text_chars(article["title"].upper(), 18)[:4]
    thesis_lines = wrap_text_chars(article["thesis"], 26)[:6]
    tagline_lines = wrap_text_chars(article["tagline"], 28)[:2]
    out.parent.mkdir(parents=True, exist_ok=True)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="3000" height="1200" fill="#101820"/>
  <rect x="1960" y="0" width="1040" height="1200" fill="#F2E9DC"/>
  <g stroke="#18313A" stroke-width="3" opacity="0.75">
    <path d="M80 0 L-540 1200"/><path d="M260 0 L-360 1200"/><path d="M440 0 L-180 1200"/>
    <path d="M620 0 L0 1200"/><path d="M800 0 L180 1200"/><path d="M980 0 L360 1200"/>
    <path d="M1160 0 L540 1200"/><path d="M1340 0 L720 1200"/><path d="M1520 0 L900 1200"/>
    <path d="M1700 0 L1080 1200"/><path d="M1880 0 L1260 1200"/><path d="M2060 0 L1440 1200"/>
  </g>
  <rect x="1880" y="120" width="940" height="960" fill="none" stroke="#E05A47" stroke-width="8"/>
  <line x1="2050" y1="220" x2="2680" y2="220" stroke="#12B5CB" stroke-width="10"/>
  <line x1="2050" y1="980" x2="2680" y2="980" stroke="#12B5CB" stroke-width="10"/>
  <text x="160" y="170" font-family="Arial, Helvetica, sans-serif" font-size="46" font-weight="700" fill="#12B5CB">TONY'S DAILY ESSAY</text>
  <text x="160" y="245" font-family="Arial, Helvetica, sans-serif" font-size="42" font-weight="700" fill="#F2E9DC">{html.escape(article["date"])}</text>
  <text font-family="Arial, Helvetica, sans-serif" font-size="154" font-weight="800" fill="#F7F1E8">
    {tspans(title_lines, 160, 470, 168)}
  </text>
  <text font-family="Arial, Helvetica, sans-serif" font-size="58" fill="#101820">
    {tspans(thesis_lines, 2045, 365, 76)}
  </text>
  <text font-family="Arial, Helvetica, sans-serif" font-size="36" font-weight="700" fill="#E05A47">
    {tspans(tagline_lines, 2045, 860, 48)}
  </text>
</svg>
"""
    svg_path = out.with_suffix(".svg")
    atomic_write(svg_path, svg)
    render_svg_to_png(svg_path, out, width, height)


def save_svg_ending(article: dict, out: Path) -> None:
    width, height = 1600, 900
    boxes = article.get("sections") or [
        ("Core idea", article["thesis"]),
        ("Context", "The situation determines whether knowledge can be retrieved."),
        ("Practice", "Good practice changes the surface while preserving the structure."),
        ("Transfer", "The goal is usable knowledge, not stored information."),
        ("AI role", "AI should multiply retrieval and feedback."),
        ("Question", "What context are you building around yourself?"),
    ]
    coords = [(70, 175), (590, 175), (1110, 175), (1110, 520), (590, 520), (70, 520)]
    colors = ["#12B5CB", "#E05A47", "#253F5B", "#12B5CB", "#E05A47", "#253F5B"]
    out.parent.mkdir(parents=True, exist_ok=True)
    box_svg = []
    for i, ((label, desc), (x, y)) in enumerate(zip(boxes, coords)):
        label_lines = textwrap.wrap(label, width=24)[:2]
        desc_lines = textwrap.wrap(desc, width=28)[:3]
        box_svg.append(
            f"""<rect x="{x}" y="{y}" width="420" height="235" rx="22" fill="#FFFFFF" stroke="{colors[i]}" stroke-width="6"/>
  <text font-size="28" font-weight="700" fill="#101820">{tspans(label_lines, x + 28, y + 58, 34)}</text>
  <text font-size="29" fill="#31434B">{tspans(desc_lines, x + 28, y + 138, 36)}</text>"""
        )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#101820"/>
    </marker>
  </defs>
  <rect width="1600" height="900" fill="#F7F1E8"/>
  <rect x="0" y="0" width="1600" height="115" fill="#101820"/>
  <text x="70" y="76" font-family="Arial, Helvetica, sans-serif" font-size="66" font-weight="800" fill="#F7F1E8">Closing Map</text>
  <g font-family="Arial, Helvetica, sans-serif">
    {''.join(box_svg)}
  </g>
  <g stroke="#101820" stroke-width="6" fill="none" marker-end="url(#arrow)">
    <path d="M490 292 L582 292"/><path d="M1010 292 L1102 292"/><path d="M1320 410 L1320 512"/>
    <path d="M1110 638 L1018 638"/><path d="M590 638 L498 638"/><path d="M280 520 L280 418"/>
  </g>
  <text x="70" y="835" font-family="Arial, Helvetica, sans-serif" font-size="32" fill="#101820">{html.escape(article['title'])} - Tony's Daily Essay</text>
</svg>
"""
    svg_path = out.with_suffix(".svg")
    atomic_write(svg_path, svg)
    render_svg_to_png(svg_path, out, width, height)


def x_article_markdown(article: dict) -> str:
    main_body, sources = split_article_body_and_sources(article)
    body = FOOTNOTE_REF_RE.sub(r"[\1]", main_body).strip()
    body = re.sub(r"^##\s+(.+)$", r"**\1**", body, flags=re.MULTILINE)
    source_lines = "\n".join(f"- {note}" for note in sources)
    lead = f"**Core idea:** {article['thesis']}\n\n" if article["thesis"] not in body[:1400] else ""
    source_block = f"\n\n**Sources**\n\n{source_lines}" if source_lines else ""
    return f"""**{article["title"]}**

{lead}{body}{source_block}
"""


def split_article_body_and_sources(article: dict) -> tuple[str, list[str]]:
    body = article["body"].strip()
    sources = list(article.get("footnotes") or [])
    source_match = SOURCE_HEADING_RE.search(body)
    if not source_match:
        return body, dedupe_sources(sources)

    main_body = body[: source_match.start()].strip()
    remaining_body = body[source_match.end() :]
    next_heading = re.search(r"^#{1,2}\s+.+$", remaining_body, flags=re.MULTILINE)
    if next_heading:
        source_body = remaining_body[: next_heading.start()].strip()
        trailing_body = remaining_body[next_heading.start() :].strip()
        main_body = "\n\n".join(part for part in (main_body, trailing_body) if part)
    else:
        source_body = remaining_body.strip()
    for raw_line in source_body.splitlines():
        line = raw_line.strip()
        if not line or line == "---":
            continue
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"^\[\^(\d+)\]:\s*", r"\1. ", line)
        sources.append(clean_plain_text(line))
    return main_body, dedupe_sources(sources)


def clean_plain_text(text: str) -> str:
    text = FOOTNOTE_REF_RE.sub("", text)
    text = INLINE_LINK_RE.sub(lambda m: f"{m.group(1)} ({m.group(2)})", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\1", text)
    text = text.replace("*", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def dedupe_sources(sources: Iterable[str]) -> list[str]:
    """Keep the first readable form of each source in its original order."""
    unique: list[str] = []
    seen: set[str] = set()
    for source in sources:
        cleaned = source_display_text(source)
        key = source_identity_key(source, cleaned)
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(cleaned)
    return unique


def source_display_text(source: str) -> str:
    source = re.sub(r"^\s*\[\^\d+\]:\s*", "", source)
    source = re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", source)
    return clean_plain_text(source)


def source_identity_key(source: str, cleaned: str) -> str:
    urls = INLINE_LINK_RE.findall(source)
    if not urls:
        urls = re.findall(r"https?://[^\s)]+", source)
        url = urls[0] if urls else ""
    else:
        url = urls[0][1]
    if url:
        return f"url:{canonical_source_url(url)}"
    return "text:" + re.sub(r"\s+", " ", cleaned).strip().casefold()


def canonical_source_url(url: str) -> str:
    parsed = urlsplit(html.unescape(url).strip())
    hostname = (parsed.hostname or "").lower()
    if not hostname:
        return url.strip().casefold()
    port = parsed.port
    netloc = hostname
    if parsed.username:
        netloc = f"{parsed.username}@{netloc}"
    if port and (parsed.scheme.lower(), port) not in {("http", 80), ("https", 443)}:
        netloc = f"{netloc}:{port}"
    path = parsed.path.rstrip("/") or "/"
    return urlunsplit((parsed.scheme.lower(), netloc, path, parsed.query, ""))


def inline_markdown_html(text: str) -> str:
    placeholders: dict[str, str] = {}

    def stash(value: str) -> str:
        key = f"@@HTML{len(placeholders)}@@"
        placeholders[key] = value
        return key

    text = FOOTNOTE_REF_RE.sub(lambda m: stash(f"<sup>{html.escape(m.group(1))}</sup>"), text)
    text = INLINE_LINK_RE.sub(
        lambda m: stash(
            f'<a href="{html.escape(m.group(2), quote=True)}">{html.escape(m.group(1), quote=False)}</a>'
        ),
        text,
    )
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = escaped.replace("*", "")
    for key, value in placeholders.items():
        escaped = escaped.replace(key, value)
    return escaped


def paragraph_chunks(text: str, max_chars: int = 220) -> list[str]:
    clean = re.sub(r"\s+", " ", text).strip()
    if not clean:
        return []
    if len(clean) <= max_chars:
        return [clean]

    sentences = re.split(r"(?<=[.!?])\s+", clean)
    chunks: list[str] = []
    current = ""
    for sentence in sentences:
        candidate = f"{current} {sentence}".strip()
        if current and len(candidate) > max_chars:
            chunks.append(current)
            current = sentence
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


def markdown_blocks(body: str) -> list[tuple[str, object]]:
    blocks: list[tuple[str, object]] = []
    paragraph_lines: list[str] = []
    list_items: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph_lines
        if paragraph_lines:
            blocks.append(("p", " ".join(line.strip() for line in paragraph_lines).strip()))
            paragraph_lines = []

    def flush_list() -> None:
        nonlocal list_items
        if list_items:
            blocks.append(("ul", list_items))
            list_items = []

    for raw_line in body.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped == "---":
            flush_paragraph()
            flush_list()
            continue
        heading = re.match(r"^##\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            flush_list()
            blocks.append(("h2", clean_plain_text(heading.group(1))))
            continue
        unordered = re.match(r"^[-*]\s+(.+)$", stripped)
        if unordered:
            flush_paragraph()
            list_items.append(unordered.group(1).strip())
            continue
        flush_list()
        paragraph_lines.append(stripped)

    flush_paragraph()
    flush_list()
    return blocks


def short_version_items(article: dict, limit: int = 4) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    for heading, summary in article.get("sections", [])[:limit]:
        heading = clean_plain_text(heading)
        summary = clean_plain_text(summary)
        if heading and summary:
            items.append((heading, summary))
    return items


def render_short_version(article: dict) -> str:
    items = short_version_items(article)
    if not items:
        return ""
    lis = "\n".join(
        f"<li><strong>{inline_markdown_html(label)}</strong> {inline_markdown_html(summary)}</li>"
        for label, summary in items
    )
    return f"<h2>The Short Version</h2>\n<ul>\n{lis}\n</ul>"


def render_copy_article_body(article: dict) -> tuple[str, str]:
    main_body, sources = split_article_body_and_sources(article)
    subtitle = article.get("thesis") or article["title"]
    parts = [
        f"<h1>{inline_markdown_html(article['title'])}</h1>",
        f'<p class="subtitle">{inline_markdown_html(subtitle)}</p>',
    ]
    plain_lines = [clean_plain_text(article["title"]), clean_plain_text(subtitle)]

    blocks = markdown_blocks(main_body)
    intro_paragraphs = 0
    short_inserted = False
    first_paragraph_after_heading = False

    for kind, value in blocks:
        if kind == "h2":
            if not short_inserted:
                short_html = render_short_version(article)
                if short_html:
                    parts.append(short_html)
                    plain_lines.append("The Short Version")
                    for label, summary in short_version_items(article):
                        plain_lines.append(f"- {label}: {summary}")
                    short_inserted = True
            heading = str(value)
            parts.append(f"<h2>{inline_markdown_html(heading)}</h2>")
            plain_lines.append(heading)
            first_paragraph_after_heading = True
            continue

        if kind == "ul":
            items = [str(item) for item in value]
            list_html = "\n".join(f"<li>{inline_markdown_html(item)}</li>" for item in items)
            parts.append(f"<ul>\n{list_html}\n</ul>")
            for item in items:
                plain_lines.append(f"- {clean_plain_text(item)}")
            first_paragraph_after_heading = False
            continue

        paragraph = str(value)
        chunks = paragraph_chunks(paragraph)
        for chunk in chunks:
            clean_chunk = clean_plain_text(chunk)
            if not clean_chunk:
                continue
            if first_paragraph_after_heading and 80 <= len(clean_chunk) <= 260:
                parts.append(f'<blockquote class="callout"><strong>{inline_markdown_html(chunk)}</strong></blockquote>')
            elif intro_paragraphs == 1:
                parts.append(f'<p class="lead"><strong>{inline_markdown_html(chunk)}</strong></p>')
            elif len(clean_chunk) <= 170 and re.search(r"\b(is not|not only|only|must|cannot|wrong|scarce|matters)\b", clean_chunk, re.IGNORECASE):
                parts.append(f'<p class="key"><strong>{inline_markdown_html(chunk)}</strong></p>')
            else:
                parts.append(f"<p>{inline_markdown_html(chunk)}</p>")
            plain_lines.append(clean_chunk)
            intro_paragraphs += 1
            first_paragraph_after_heading = False

        if intro_paragraphs >= 4 and not short_inserted:
            short_html = render_short_version(article)
            if short_html:
                parts.append(short_html)
                plain_lines.append("The Short Version")
                for label, summary in short_version_items(article):
                    plain_lines.append(f"- {label}: {summary}")
                short_inserted = True

    if not short_inserted:
        short_html = render_short_version(article)
        if short_html:
            parts.insert(2, short_html)
            plain_lines.insert(2, "The Short Version")
            for label, summary in reversed(short_version_items(article)):
                plain_lines.insert(3, f"- {label}: {summary}")

    if sources:
        parts.append("<h2>Sources</h2>")
        parts.append('<ol class="sources">')
        plain_lines.append("Sources")
        for note in sources:
            parts.append(f"<li>{inline_markdown_html(note)}</li>")
            plain_lines.append(clean_plain_text(note))
        parts.append("</ol>")

    plain_text = "\n".join(line for line in plain_lines if line.strip()) + "\n"
    return "\n".join(parts), plain_text


def copy_page_css(include_shell: bool) -> str:
    css = """
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif; color: #0f1419; background: #ffffff; }
  article { max-width: 700px; margin: 34px auto; line-height: 1.58; font-size: 19px; }
  h1 { font-size: 38px; line-height: 1.08; margin: 0 0 12px; font-weight: 850; letter-spacing: 0; }
  .subtitle { color: #536471; font-size: 21px; line-height: 1.36; margin: 0 0 26px; }
  h2 { font-size: 25px; line-height: 1.2; margin: 34px 0 13px; font-weight: 850; letter-spacing: 0; }
  p { margin: 0 0 13px; }
  .lead { font-size: 21px; line-height: 1.42; margin-bottom: 18px; }
  .key { margin-top: 4px; margin-bottom: 17px; }
  blockquote { margin: 20px 0; padding: 4px 0 4px 18px; border-left: 4px solid #0f1419; font-size: 21px; line-height: 1.38; }
  blockquote.callout { background: #f7f9f9; border-left-color: #1d9bf0; padding: 14px 16px 14px 18px; border-radius: 0 8px 8px 0; }
  ul, ol { margin: 12px 0 18px; padding-left: 1.25em; }
  li { margin: 0 0 9px; }
  strong { font-weight: 850; }
  em { font-style: italic; }
  code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.92em; }
  .sources { font-size: 15px; line-height: 1.45; color: #536471; }
  a { color: #1d9bf0; }
  @media (max-width: 760px) {
    article { max-width: none; margin: 24px auto; padding: 0 19px; font-size: 18px; line-height: 1.55; }
    h1 { font-size: 31px; line-height: 1.1; }
    .subtitle { font-size: 19px; }
    h2 { font-size: 23px; margin-top: 32px; }
    blockquote { font-size: 19px; }
  }
"""
    if not include_shell:
        return css
    return css + """
  body { margin: 0; background: #f7f9f9; }
  .shell { max-width: 920px; margin: 0 auto; padding: 24px 18px 52px; }
  .toolbar { position: sticky; top: 0; z-index: 2; display: flex; align-items: center; gap: 10px; padding: 12px 0; background: #f7f9f9; border-bottom: 1px solid #d6dde2; }
  button { border: 1px solid #0f1419; background: #0f1419; color: #fff; border-radius: 6px; padding: 9px 14px; font-size: 14px; font-weight: 750; cursor: pointer; }
  button.secondary { background: #fff; color: #0f1419; }
  .status { font-size: 13px; color: #536471; }
  .shell article { background: #fff; margin-top: 24px; padding: 42px 46px; border: 1px solid #d6dde2; border-radius: 8px; }
  @media (max-width: 760px) {
    .shell { padding: 12px 10px 36px; }
    .toolbar { flex-wrap: wrap; }
    .shell article { padding: 28px 18px; }
    .status { flex-basis: 100%; }
  }
"""


def x_article_copy_files(article: dict) -> tuple[str, str, str]:
    article_body, plain_text = render_copy_article_body(article)
    title = html.escape(article["title"], quote=False)
    body_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} - X Article Body</title>
<style>{copy_page_css(False)}</style>
</head>
<body>
<article id="x-article-body">
{article_body}
</article>
</body>
</html>
"""
    copy_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} - X Article Rich Copy</title>
<style>{copy_page_css(True)}</style>
</head>
<body>
<div class="shell">
  <div class="toolbar">
    <button id="copy-rich" type="button">Copy rich text</button>
    <button id="select-body" class="secondary" type="button">Select article</button>
    <span id="status" class="status">Optimized for X Article: short paragraphs, section breaks, bullets, and key insight callouts.</span>
  </div>
  <article id="x-article-body" contenteditable="true" spellcheck="false">
{article_body}
  </article>
</div>
<script>
const article = document.getElementById('x-article-body');
const statusEl = document.getElementById('status');
const plainText = {inline_js_json(plain_text)};
function selectArticle() {{
  const range = document.createRange();
  range.selectNodeContents(article);
  const selection = window.getSelection();
  selection.removeAllRanges();
  selection.addRange(range);
}}
document.getElementById('select-body').addEventListener('click', () => {{
  selectArticle();
  statusEl.textContent = 'Article selected. Press Command+C, then paste into X Article.';
}});
document.getElementById('copy-rich').addEventListener('click', async () => {{
  const richHtml = article.innerHTML;
  try {{
    if (navigator.clipboard && window.ClipboardItem) {{
      await navigator.clipboard.write([new ClipboardItem({{
        'text/html': new Blob([richHtml], {{ type: 'text/html' }}),
        'text/plain': new Blob([plainText], {{ type: 'text/plain' }})
      }})]);
      statusEl.textContent = 'Copied rich text. Paste into X Article now.';
      return;
    }}
  }} catch (err) {{}}
  selectArticle();
  document.execCommand('copy');
  statusEl.textContent = 'Copied or selected the article. Paste into X Article now.';
}});
</script>
</body>
</html>
"""
    return copy_html, body_html, plain_text


def inline_js_json(value: str) -> str:
    """Serialize data for an inline script without allowing a script-tag escape."""
    return (
        json.dumps(value, ensure_ascii=False)
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def save_x_article_copy_assets(article: dict, package_dir: Path) -> bool:
    copy_html, body_html, plain_text = x_article_copy_files(article)
    copy_path = package_dir / "x-article-copy.html"
    meta_dir = package_dir / "_meta"
    body_path = meta_dir / "x-article-copy-body.html"
    atomic_write(copy_path, copy_html)
    atomic_write(body_path, body_html)
    atomic_write(meta_dir / "x-article-copy.txt", plain_text)

    rtf_path = meta_dir / "x-article-copy.rtf"
    rtf_path.unlink(missing_ok=True)
    textutil = shutil.which("textutil")
    if not textutil:
        return False
    try:
        subprocess.run(
            [
                textutil,
                "-convert",
                "rtf",
                "-output",
                str(rtf_path),
                str(body_path),
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return rtf_path.is_file() and rtf_path.stat().st_size > 0


def teaser_markdown(article: dict) -> str:
    return f"""**X Teaser Post**

Cover: `cover.png`
Article asset: `x-article-copy.html`
Ending image: `ending-image.png`

Today I wrote a new essay:

{article["title"]}

Core idea:

{article["thesis"]}

Read the full essay in X Articles.
"""


def cleanup_legacy_assets(package_dir: Path) -> None:
    for pattern in [
        "inline-01-argument-map.*",
        "inline-01-learning-loop.*",
        "cover.svg",
        "ending-image.svg",
    ]:
        for old in package_dir.glob(pattern):
            old.unlink(missing_ok=True)


def organize_package_files(package_dir: Path) -> None:
    meta_dir = package_dir / "_meta"
    meta_dir.mkdir(exist_ok=True)
    for item in package_dir.iterdir():
        if item.name == "_meta" or item.name in TOP_LEVEL_PACKAGE_FILES:
            continue
        target = meta_dir / item.name
        if target.exists():
            if target.is_dir():
                shutil.rmtree(target)
            else:
                target.unlink()
        item.replace(target)


def expose_package_reference_files(package_dir: Path) -> None:
    meta_dir = package_dir / "_meta"
    copies = {
        "x-article.md": "x-article.md",
        "x-teaser-post.md": "x-teaser-post.md",
        "README.md": "README.md",
        "cover.prompt.txt": "cover-prompt.md",
        "ending-image.prompt.txt": "ending-image-prompt.md",
        "original.md": "original-source.md",
    }
    for src_name, dst_name in copies.items():
        src = meta_dir / src_name
        if src.exists():
            atomic_write(package_dir / dst_name, src.read_text(encoding="utf-8"))


def package_article(path: Path, image_mode: str, timeout_sec: int, force_images: bool) -> Path:
    article = parse_article(path)
    package_dir = READY_DIR / f"{article['date']}-{article['slug']}"
    package_dir.mkdir(parents=True, exist_ok=True)
    cleanup_legacy_assets(package_dir)

    meta_dir = package_dir / "_meta"
    atomic_write(meta_dir / "original.md", path.read_text(encoding="utf-8"))
    atomic_write(meta_dir / "x-article.md", x_article_markdown(article))
    rtf_available = save_x_article_copy_assets(article, package_dir)
    atomic_write(meta_dir / "x-teaser-post.md", teaser_markdown(article))
    if image_mode == "gpt-image-2":
        save_gpt_images(article, package_dir, timeout_sec, force_images)
    else:
        save_svg_cover(article, package_dir / "cover.png")
        save_svg_ending(article, package_dir / "ending-image.png")
    manifest = {
        "date": article["date"],
        "title": article["title"],
        "source_file": f"articles/en/{path.name}",
        "x_article": "_meta/x-article.md",
        "rich_article_copy": "x-article-copy.html",
        "plain_article_copy": "_meta/x-article-copy.txt",
        "image_mode": image_mode,
        "cover": {"file": "cover.png", "width": 3000, "height": 1200, "ratio": "5:2"},
        "ending_image": {"file": "ending-image.png", "width": 1600, "height": 900, "ratio": "16:9"},
        "upload_order": ["cover.png", "x-article-copy.html", "ending-image.png"],
    }
    if rtf_available:
        manifest["rtf_article_copy"] = "_meta/x-article-copy.rtf"
    atomic_write(package_dir / "manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    atomic_write(
        meta_dir / "README.md",
        f"""**{article["title"]}**

X publishing package for {article["date"]}.

**Files**

- `cover.png`: 3000 x 1200 cover image, exactly 5:2.
- `x-article-copy.html`: recommended rich-text copy page for X Articles.
{("- `x-article-copy.rtf`: rich-text fallback for copying from TextEdit." if rtf_available else "- RTF fallback was not generated because `textutil` was unavailable or failed.")}
- `x-article-copy.txt`: plain-text fallback with no Markdown markers or blank-line gaps.
- `x-article.md`: legacy Markdown-style article source.
- `ending-image.png`: abstract visual to upload at the end of the article.
- `x-teaser-post.md`: short post copy for promoting the article.
- `original.md`: downloaded source article.
- `cover.prompt.txt` / `ending-image.prompt.txt`: GPT Image 2 prompts used for image generation.

**Manual Upload Flow**

1. Open X Articles.
2. Upload `cover.png` as the cover.
3. Open `x-article-copy.html`, click `Copy rich text`, then paste into the article editor.
4. Upload `ending-image.png` at the end of the article.
5. Publish only after checking line breaks and image placement.
""",
    )
    organize_package_files(package_dir)
    expose_package_reference_files(package_dir)
    return package_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync English Tony Articles and prepare X publishing assets.")
    parser.add_argument("--date", help="Prepare article for YYYY-MM-DD.")
    parser.add_argument("--latest", action="store_true", help="Prepare the latest 2026 English article.")
    parser.add_argument("--all-2026", action="store_true", help="Prepare packages for every 2026 English article.")
    parser.add_argument(
        "--image-mode",
        choices=["gpt-image-2", "svg"],
        default="gpt-image-2",
        help="Image generation route. Default uses GPT Image 2 via local Codex CLI.",
    )
    parser.add_argument("--force-images", action="store_true", help="Regenerate images even when PNGs already exist.")
    parser.add_argument("--image-timeout-sec", type=int, default=300, help="Timeout per GPT Image 2 image.")
    args = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix="tony-articles-") as tmp:
        synced = sync_2026_articles(Path(tmp))
        if args.all_2026:
            targets = synced
        else:
            targets = [select_article(synced, args.date, args.latest)]
        packages = [
            package_article(target, args.image_mode, args.image_timeout_sec, args.force_images)
            for target in targets
        ]

    print(f"Synced {len(synced)} English 2026 article(s).")
    for package in packages:
        print(f"Generated {package}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
