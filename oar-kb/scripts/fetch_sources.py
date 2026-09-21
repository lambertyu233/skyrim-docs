#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取 OAR 相关一手来源，存到 _raw/ 便于后续核对。

用法：python scripts/fetch_sources.py [name ...]
不带参数则抓全部。纯标准库。
"""
import os
import re
import sys
import time
import urllib.request
import urllib.error

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "_raw")

SOURCES = {
    # ---- GitHub 官方仓库 ----
    "gh-readme": "https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/README.md",
    "gh-docs-index": "https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/docs/README.md",
    # ---- Nexus 描述页 / 论坛 ----
    "nexus-oar": "https://www.nexusmods.com/skyrimspecialedition/mods/92109",
    "nexus-detection": "https://www.nexusmods.com/skyrimspecialedition/mods/104806",
    # ---- Patreon 开发日志 ----
    "patreon-status-update": "https://bakemono.app/p/patreon/25643772/79535580",
}


def html_to_text(html: str) -> str:
    html = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"(?is)<br\s*/?>", "\n", html)
    html = re.sub(r"(?is)</(p|div|li|h[1-6]|tr|section|article)>", "\n", html)
    html = re.sub(r"(?s)<[^>]+>", "", html)
    import html as _h
    text = _h.unescape(html)
    text = re.sub(r"[ \t\u00a0]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text.strip()


def fetch(name: str, url: str) -> None:
    os.makedirs(RAW, exist_ok=True)
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7",
    })
    try:
        data = urllib.request.urlopen(req, timeout=45).read()
    except Exception as exc:  # noqa: BLE001
        print("ERR  %-24s %s: %s" % (name, type(exc).__name__, exc))
        return
    body = data.decode("utf-8", "replace")
    if url.endswith(".md") or "<html" not in body[:2000].lower():
        out = body
        ext = ".md"
    else:
        out = html_to_text(body)
        ext = ".txt"
    path = os.path.join(RAW, name + ext)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("SOURCE: %s\n\n%s\n" % (url, out))
    print("OK   %-24s %7d bytes -> %s" % (name, len(out), os.path.relpath(path, ROOT)))


def main() -> int:
    names = sys.argv[1:] or list(SOURCES)
    for i, n in enumerate(names):
        if n not in SOURCES:
            print("SKIP %s (unknown)" % n)
            continue
        fetch(n, SOURCES[n])
        if i + 1 < len(names):
            time.sleep(1.2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
