#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync_scripts.py — 把技能 stock 版脚本同步到各资料库

动机：五件套脚本（build_index / validate_kb / check_index_ui / check_links / fix_links）
在技能与每个资料库中各有一份副本。副本一多，某次只改了一处、其余仍是旧版，
就会变成「技能里是这个行为、库里是那个行为」的隐性分叉 —— 排查这类问题极费时间。

本脚本按**字节**比较两边，把不一致的库内副本用技能 stock 版覆盖（覆盖前先备份到
`_raw/pre-sync-<日期>/`），并报告每个脚本的指纹数。指纹数为 1 才算真正统一。

用法：
  managed python scripts/sync_scripts.py                 # 检查 + 同步所有库
  managed python scripts/sync_scripts.py --check         # 只检查不改（退出码非 0 表示有分叉）
  managed python scripts/sync_scripts.py --kb oar-kb     # 只处理一个库

退出码：0 = 全部一致（或已同步成功）；1 = --check 下发现分叉 / 同步出错。
"""
import argparse
import datetime
import hashlib
import os
import shutil
import sys

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_DIR = os.path.join(WORKSPACE, ".workbuddy", "skills", "build-maintainable-kb", "scripts")
SYNC_FILES = [
    "build_index.py",
    "validate_kb.py",
    "check_index_ui.py",
    "check_links.py",
    "fix_links.py",
]
# 每个库独有的脚本（抓取器 / 生成器）不参与同步
LOCAL_ONLY = {"fetch_sources.py", "fetch_mediawiki.py", "gen_features.py"}


def digest(path):
    if not os.path.isfile(path):
        return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def find_kbs():
    """发现所有资料库：工作区下「含 manifest.json 的一级目录」。

    不按目录名后缀（`*-kb`）判断 —— 新库可能叫 `01-navigation` 这类名字，
    用命名巧合当判据会让它被静默漏掉（同步不到、也检查不到）。
    """
    out = []
    for name in sorted(os.listdir(WORKSPACE)):
        d = os.path.join(WORKSPACE, name)
        if os.path.isdir(d) and os.path.isfile(os.path.join(d, "manifest.json")):
            out.append(name)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只检查，不写入")
    ap.add_argument("--kb", help="只处理指定库")
    args = ap.parse_args()

    if not os.path.isdir(SKILL_DIR):
        print("找不到技能脚本目录：%s" % SKILL_DIR)
        return 1

    stock = {}
    for fn in SYNC_FILES:
        src = os.path.join(SKILL_DIR, fn)
        if not os.path.isfile(src):
            print("技能缺少 %s（stock 基准不完整）" % fn)
            return 1
        stock[fn] = digest(src)
    print("技能 stock（%s）" % SKILL_DIR)
    for fn in SYNC_FILES:
        print("  %s  %s" % (fn, stock[fn][:12]))

    kbs = [args.kb] if args.kb else find_kbs()
    diverged, synced, missing = [], [], []
    today = datetime.date.today().isoformat()

    for kb in kbs:
        kdir = os.path.join(WORKSPACE, kb, "scripts")
        if not os.path.isdir(kdir):
            missing.append(kb)
            continue
        for fn in SYNC_FILES:
            dst = os.path.join(kdir, fn)
            if not os.path.isfile(dst):
                missing.append("%s/%s" % (kb, fn))
                continue
            if digest(dst) == stock[fn]:
                continue
            diverged.append("%s/scripts/%s" % (kb, fn))
            if not args.check:
                backup = os.path.join(WORKSPACE, kb, "_raw", "pre-sync-%s" % today)
                os.makedirs(backup, exist_ok=True)
                shutil.copy2(dst, os.path.join(backup, fn))
                shutil.copy2(os.path.join(SKILL_DIR, fn), dst)
                synced.append("%s/scripts/%s" % (kb, fn))

    print("")
    if diverged:
        print("发现分叉: %d" % len(diverged))
        for d in diverged:
            print(" - %s" % d)
        if args.check:
            print("（--check 模式，未写入）")
        else:
            print("已用 stock 版覆盖 %d 处，原文件备份到各库 _raw/pre-sync-%s/" % (len(synced), today))
    else:
        print("脚本已全部一致，无分叉。")

    if missing:
        print("缺失: %d" % len(missing))
        for m in missing:
            print(" - %s" % m)

    if args.check and (diverged or missing):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
