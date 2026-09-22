#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""selftest_new_kb.py — 自检：从技能 stock 脚本新建一个资料库，是否会继承当前的索引页 UI。

动机：索引页的外观与交互**只写在 `build_index.py` 的 `HTML_TEMPLATE` 里**。
新建库时若要"自动带上当前 UI"（例如收起/展开两个半圆把手），
唯一途径就是从技能 `scripts/` 复制脚本过去 —— 一旦有人新库里另写了一份
`build_index.py`（或者从某个旧库里抄），新库就会静默地长成旧样子：
构建成功、校验通过、UI 却是错的。这个脚本把这件事变成一条可执行的断言。

做法：在**系统 temp 目录**里造一个最小资料库（manifest + 1 条目 + 复制来的五件套），
依次跑 `build_index` / `validate_kb` / `check_index_ui`，再对产物 `index.html` 断言：
  - 含 `#navtoggle`（侧栏收缩把手）与 `#navfab`（收起后的唤出把手）；
  - 两者都带 `.navfab` 类（样式统一）；
  - 不含已废弃的 `.navtoggle{}` 方框样式与 `78px` 窄条；
  - 产物全部为 LF。
跑完即删临时目录，**不会碰任何真实资料库**。

用法：
  托管 python selftest_new_kb.py
退出码：0 = 新建库继承当前 UI；1 = 有不符（会逐条打印）。
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

SKILL_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(os.path.dirname(os.path.dirname(SKILL_SCRIPTS)))
FIVE = ["build_index.py", "validate_kb.py", "check_index_ui.py", "check_links.py", "fix_links.py"]

ENTRY = """---
id: demo
title: 自检条目
category: 01-demo
version: 1.0.0
updated: 2000-01-01
tags: [自检, 示例]
aliases: [selftest, demo entry]
source: https://example.com
summary: 用于验证新建资料库是否自动带上当前的索引页 UI（收起/展开两个半圆把手）。
---

# 自检条目

这是一条用于自检的正文。

- 第一项
- 第二项
"""


def build_temp_kb():
    tmp = tempfile.mkdtemp(prefix="newkb-selftest-")
    kb = os.path.join(tmp, "demo-kb")
    os.makedirs(os.path.join(kb, "01-demo"))
    os.makedirs(os.path.join(kb, "scripts"))
    for fn in FIVE:
        shutil.copy2(os.path.join(SKILL_SCRIPTS, fn), os.path.join(kb, "scripts", fn))
    with open(os.path.join(kb, "manifest.json"), "w", encoding="utf-8", newline="") as f:
        json.dump({
            "kb": {"name": "自检示例库",
                   "description": "验证新建库是否继承当前索引页 UI",
                   "source_name": "selftest"},
            "categories": [{"dir": "01-demo", "title": "示例分类"}],
        }, f, ensure_ascii=False, indent=2)
    with open(os.path.join(kb, "01-demo", "demo.md"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return tmp, kb


def main():
    if not os.path.isdir(SKILL_SCRIPTS):
        print("找不到技能 scripts 目录：%s" % SKILL_SCRIPTS)
        return 1
    missing = [fn for fn in FIVE if not os.path.isfile(os.path.join(SKILL_SCRIPTS, fn))]
    if missing:
        print("技能缺少 stock 脚本：%s" % ", ".join(missing))
        return 1

    fails = []
    tmp, kb = build_temp_kb()
    try:
        print("临时库：%s" % kb)
        for label, script in [("build_index", "build_index.py"),
                              ("validate_kb", "validate_kb.py"),
                              ("check_index_ui", "check_index_ui.py")]:
            r = subprocess.run([sys.executable, os.path.join(kb, "scripts", script)],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
            lines = [l for l in (r.stdout or "").strip().splitlines() if l.strip()]
            print("  %-15s rc=%d  %s" % (label, r.returncode, lines[-1] if lines else "(无输出)"))
            if r.returncode != 0:
                fails.append("%s 退出码 %d\n%s\n%s" % (label, r.returncode, r.stdout, r.stderr))

        html_path = os.path.join(kb, "index.html")
        exists = os.path.isfile(html_path)
        raw = open(html_path, "rb").read() if exists else b""
        t = raw.decode("utf-8")

        checks = [
            ("index.html 已生成", exists),
            ("含 #navtoggle（侧栏收起把手）", 'id="navtoggle"' in t),
            ("含 #navfab（收起后唤出的把手）", 'id="navfab"' in t),
            ("#navtoggle 带 .navfab 类（样式统一）",
             bool(re.search(r'<button id="navtoggle"[^>]*class="navfab"', t))),
            ("#navfab 带 .navfab 类（样式统一）",
             bool(re.search(r'<button id="navfab"[^>]*class="navfab"', t))),
            ("已废弃的 .navtoggle{} 方框样式无残留", ".navtoggle{" not in t),
            ("已废弃的 78px 窄条无残留", "78px" not in t),
            ("产物全部为 LF", raw.count(b"\r") == 0),
        ]
        print("\n产物断言：")
        for name, good in checks:
            print("  %s  %s" % ("PASS" if good else "FAIL", name))
            if not good:
                fails.append(name)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("")
    if fails:
        print("结果：失败 %d 项" % len(fails))
        for x in fails:
            print("  - %s" % x)
        print("\n提示：新库必须从技能 scripts/ 复制五件套；不要另写 build_index.py，")
        print("      也不要在库里单独改 UI —— 改技能 stock 版再 sync_scripts.py 推送。")
        return 1
    print("结果：新建库已自动继承当前索引页 UI —— 全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
