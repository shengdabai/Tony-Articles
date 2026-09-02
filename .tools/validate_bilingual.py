#!/usr/bin/env python3
"""Validate the bilingual article archive and its newest-first indexes."""

from __future__ import annotations

import json
import re
import sys
import urllib.parse
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
ARTICLES = REPO / "articles"
ZH = ARTICLES / "zh"
EN = ARTICLES / "en"
MAP_FILE = REPO / ".tools" / "translation-map.json"
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-.+\.md$")
URL_RE = re.compile(r"https?://[^\s)>]+")
HAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
CRITICAL_QUANTITY_EQUIVALENTS = {
    "一万倍": re.compile(r"\b(?:10,?000|ten[ -]thousand)(?:[ -]fold|\s+times)\b", re.I),
}
HAN_ALLOWED_SOURCES = {
    "2022-05-01-视频号直播间违禁词分享给你.md",
    "2023-05-16-华杉一生不败这回彻底理解孙子兵法 新加坡南洋理工大学演讲实录.md",
    "2021-05-23-国士无双.md",
    "2021-06-12-说说语言.md",
    "2023-05-02-如何与孩子聊ChatGPTAI大时代的完整版家长指南.md",
    "2023-04-30-学习能力到底是什么.md",
}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def article_files(directory: Path) -> list[Path]:
    return sorted((path for path in directory.glob("20*.md") if DATE_RE.match(path.name)), reverse=True)


def first_h1(raw: str) -> str | None:
    match = re.search(r"^#\s+(.+?)\s*$", raw, re.M)
    return match.group(1) if match else None


def linked_basename(raw: str, language: str) -> str | None:
    match = re.search(rf"\.\./{language}/([^\n)]+\.md)", raw)
    return urllib.parse.unquote(match.group(1)) if match else None


def validate_index(path: Path, expected: list[Path], errors: list[str]) -> None:
    if not path.exists():
        fail(f"missing index: {path.relative_to(REPO)}", errors)
        return
    raw = path.read_text(encoding="utf-8")
    dates = re.findall(r"^- (\d{4}-\d{2}-\d{2}) · ", raw, re.M)
    if dates != sorted(dates, reverse=True):
        fail(f"index is not newest-first: {path.relative_to(REPO)}", errors)
    if len(dates) != len(expected):
        fail(f"index count mismatch: {path.relative_to(REPO)} has {len(dates)}, expected {len(expected)}", errors)


def main() -> int:
    errors: list[str] = []
    root_articles = [path for path in ARTICLES.glob("20*.md") if DATE_RE.match(path.name)]
    if root_articles:
        fail(f"{len(root_articles)} dated articles remain outside zh/en", errors)

    zh_files = article_files(ZH)
    en_files = article_files(EN)
    if len(zh_files) != len(en_files):
        fail(f"language count mismatch: zh={len(zh_files)} en={len(en_files)}", errors)

    try:
        mapping = json.loads(MAP_FILE.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot read translation map: {exc}", errors)
        mapping = {}

    legacy_sources = [path for path in zh_files if path.name[:4] in {"2021", "2022", "2023", "2024"}]
    if set(mapping) != {path.name for path in legacy_sources}:
        missing = sorted({path.name for path in legacy_sources} - set(mapping))
        extra = sorted(set(mapping) - {path.name for path in legacy_sources})
        fail(f"translation map mismatch: missing={missing[:5]} extra={extra[:5]}", errors)

    mapped_targets = list(mapping.values())
    if len(mapped_targets) != len(set(mapped_targets)):
        fail("translation map contains duplicate English targets", errors)

    for zh_path in zh_files:
        raw = zh_path.read_text(encoding="utf-8", errors="replace")
        date = DATE_RE.match(zh_path.name).group(1)
        if not first_h1(raw):
            fail(f"missing H1: {zh_path.relative_to(REPO)}", errors)
        if date not in raw[:1200]:
            fail(f"missing date metadata: {zh_path.relative_to(REPO)}", errors)
        en_name = mapping.get(zh_path.name) or linked_basename(raw[:1600], "en")
        if not en_name:
            fail(f"missing English mapping/link: {zh_path.relative_to(REPO)}", errors)
            continue
        en_path = EN / en_name
        if not en_path.exists():
            fail(f"missing English file: {en_path.relative_to(REPO)}", errors)
            continue
        en_raw = en_path.read_text(encoding="utf-8", errors="replace")
        if linked_basename(en_raw[:1600], "zh") != zh_path.name:
            fail(f"English backlink mismatch: {en_path.relative_to(REPO)}", errors)
        if date not in en_raw[:1200] or not first_h1(en_raw):
            fail(f"English header invalid: {en_path.relative_to(REPO)}", errors)
        if zh_path.name in mapping:
            if set(URL_RE.findall(raw)) != set(URL_RE.findall(en_raw)):
                fail(f"URL drift: {en_path.relative_to(REPO)}", errors)
            body = en_raw.split("---", 1)[-1]
            if zh_path.name not in HAN_ALLOWED_SOURCES and HAN_RE.search(body):
                fail(f"untranslated Chinese remains: {en_path.relative_to(REPO)}", errors)
            for source_quantity, english_pattern in CRITICAL_QUANTITY_EQUIVALENTS.items():
                if source_quantity in raw and not english_pattern.search(en_raw):
                    fail(f"critical quantity drift ({source_quantity}): {en_path.relative_to(REPO)}", errors)

    validate_index(ZH / "README.md", zh_files, errors)
    validate_index(EN / "README.md", en_files, errors)

    if errors:
        print("BILINGUAL ARCHIVE INVALID", file=sys.stderr)
        for error in errors[:80]:
            print(f"- {error}", file=sys.stderr)
        if len(errors) > 80:
            print(f"- ... {len(errors) - 80} more", file=sys.stderr)
        return 1
    print(f"BILINGUAL ARCHIVE OK: {len(zh_files)} Chinese + {len(en_files)} English, newest-first indexes verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
