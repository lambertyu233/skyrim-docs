---
id: update-and-uninstall
title: 更新、合并与卸载 mod
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 更新, 卸载, 合并, 回收站]
aliases: [更新 mod, 卸载 mod, 合并 mod, uninstall merge]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 用 Check all for update 查更新，全量替换用 Replace、部分更新用 Merge；卸载分"仅当前 profile"与"全局删除（进回收站）"。
kind: tutorial
---

# 更新、合并与卸载 mod

## 检查更新

- 在左窗格右键 → `Check all for update`。它按 Nexus 查各 mod 的新版本与 endorsement 状态，并把筛选视图切到 `<Update>`。
- 检测成败**取决于 meta 信息是否正确**（Nexus ID 与版本号）。有些作者版本号规则很怪，MO 可能识别不了——所以**建议在 Nexus 上 Track 所有已装 mod**，以跟踪中心为准。
- MO **不会**自动轮询更新（作者不想给 Nexus 添无谓流量）；每次更新后版本号变绿/变红即反映结果（见 [界面总览](ui-layout.md)）。

## 更新

1. 下载新版本归档。
2. 安装到**原来同一个 mod**上：
   - **全量替换**（新版本包含全部资源）→ 选 `Replace`；
   - **只更新部分文件** → 选 `Merge`。
3. 更新后**务必重新评估文件冲突**，并按需调整优先级（见 [冲突解决与优先级](conflict-resolution.md)）。

## 卸载

- **仅从当前 profile 卸载**：在左窗格**取消勾选**该 mod 即可——这是 profile 级操作，不影响其它 profile。
- **从所有 profile 卸载**：左窗格右键 → `Remove`，mod 文件夹会被**删除到回收站**。
  - 误删可从回收站**还原该文件夹**，MO 会重新认得它；但它会被当作**新 mod**处理：未勾选、且排在优先级最末。

> 相关：[安装 mod](install-mods.md)（Merge/Replace 与备份）、[启用 mod 与激活插件](enable-and-activate.md)（批量勾选/空格键）、[备份与恢复](backup-and-restore.md)。
