---
id: bug-fixes-sse
title: Bug Fixes SSE
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [稳定性, bug 修复, 引擎, SKSE, meh321]
aliases: [Bug Fixes SSE, 33261, 引擎 bug 修复, meh321 修复]
source: https://www.nexusmods.com/skyrimspecialedition/mods/33261
summary: meh321 出品的引擎函数级 bug 修复集合；体量小、无配置、与 Scrambled Bugs 内容有交集——注意它接管了后者移出的「魔法效果条件」修复。
---

# Bug Fixes SSE

Nexus：`skyrimspecialedition/mods/33261`，作者 **meh321**
（来源：STEP wiki 与整合包清单的标注）。

## 定位

小而专的**引擎 bug 修复**集合。它与 `Scrambled Bugs`、
`SSE Engine Fixes` 是**互补而非替代**关系：

| | Bug Fixes SSE | Scrambled Bugs | SSE Engine Fixes |
|---|---|---|---|
| 层次 | 引擎函数的具体 bug | 玩法机制层 bug + 可选 patch | 内存/文件/引擎级稳定性 |
| 配置 | 基本无 | `ScrambledBugs.json` 逐项开关 | 有 ini |
| 体量 | 小 | 中 | 大（含 preloader） |

## 一条容易对不上的历史

**Scrambled Bugs 的官方 Q&A 明确写过**：
"魔法效果条件修复（magic effect conditions fix）**已被移除并加入 Bug Fixes SSE**。"

含义：
- 你在看老教程，发现它让你在 Scrambled Bugs 里找这个开关 → 现在**找不到**，去 Bug Fixes SSE 里。
- 两个 mod **同时安装是正常的**，且在现代 modlist 里是标准组合。

## 与 vr 侧

meh321 的这套修复在 VR 上通常另有实现或移植（社区口径），
具体选择请核对发布页的 Requirements 与文件说明。

## 相关

- [Scrambled Bugs](../09-diagnostics/scrambled-bugs.md)
- [SSE Engine Fixes](../09-diagnostics/sse-engine-fixes.md)
- [powerofthree's Tweaks（引擎修复与调整）](../09-diagnostics/po3-tweaks.md)
- [Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md)
