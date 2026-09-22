---
id: loot
title: LOOT（插件排序）
category: 04-loadorder
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [排序, 冲突, 加载顺序, 自动化, 官方文档]
aliases: [排序工具, load order, 插件排序, masterlist, BOSS, loot 排序]
source: https://loot.github.io/docs/help/Introduction-To-Load-Orders
summary: 自动计算满足全部依赖、且最大化每个插件效果的加载顺序；能查缺失前置/不兼容/循环依赖，但它只解决「顺序」不解决「冲突」。
---

# LOOT

## 官方定位

> **"LOOT can automatically calculate a load order that satisfies all plugin dependencies
> and maximises each plugin's impact on your game."**

除了排序，它还做**错误检查**（缺失前置、不兼容、循环依赖），
并提供大量**插件级使用说明、已知 bug 警告、以及给 Wrye Bash 的 Bash Tag 建议**。

## 必须记住的加载顺序硬规则（官方 Introduction To Load Orders）

- **Master 插件永远在非 master 之前加载**。是"主"由文件内部 flag 决定，
  但 Skyrim SE / VR / FO4 里 `.esm` 与 `.esl` **扩展名本身即视为主文件**。
- **Skyrim 的 `Skyrim.esm` 永远最先加载**；存在 `Update.esm` 时它必然加载，
  且在其它 master 之后（除非显式指定位置）。
- **常规 `.esm`+`.esp` 上限 255 个**；Skyrim SE / VR **额外**可加载 **4096 个 `.esl`**。
- 显示位次 `00`–`FE` 是十六进制；**ESL 在列表里显示为 FE，但实际按其顺序位加载**。
- 位次是 FormID 的前两位——这就是"为什么顺序会影响引用"的根本原因。

## 排序结果落在哪

- Skyrim 的**激活插件**顺序：`%LOCALAPPDATA%\Skyrim Special Edition\plugins.txt`
- 全部插件顺序：同目录的 `loadorder.txt`
- 备份加载顺序 = 备份这两个文件。

## 它的边界（本库最重要的一句提醒）

LOOT **只管插件级顺序**。两个插件改同一条记录时，仍然是"后加载者全胜"——
LOOT 不会替你把两边的值合并。**记录级冲突要用 xEdit 做补丁**（或 Synthesis 自动生成）。

> 官方自己也写了："mod users should still possess a working knowledge of mod load ordering"——
> 它不打算取代理解。

## 自定义元数据

有些插件必须排在特定位置，而插件本身无法表达。
LOOT 提供 **masterlist**（社区维护的主清单）+ **用户自定义元数据**机制来补足。
实践中"某个 mod 需要排在 X 之后"的社区说法，最终都落在这一层。

## 相关

- [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)（记录级冲突）
- [脏编辑与清理（ITM / UDR）](../04-loadorder/dirty-edits-cleaning.md)（LOOT 会报 UDR/ITM 数量，清理在 xEdit）
- [Bash Patch（Wrye Bash 的记录合并）](../04-loadorder/bashed-patch.md)（Bash Tag 建议的去处）
- [Vortex（Nexus 官方管理器）](../03-managers/vortex.md)（Vortex 内置的排序引擎即 LOOT）
- [术语表（工具语境）](../00-overview/glossary.md)（ESL / Rule of one / 插件顺序 vs 安装顺序）
