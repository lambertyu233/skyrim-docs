---
id: unreliable-sources-and-fabrications
title: 不可信来源与已知编造
category: 10-sources
version: 1.0.0
updated: 2026-10-22
tags: [不可信来源, 黑名单, 编造, CSDN, toolify, 证据纪律]
kind: reference
source: https://www.nexusmods.com/skyrimspecialedition/mods/659
summary: 本库排除的内容农场/AI 聚合站清单，与已识别的具体编造案例；建库时就 sources 目录先查不可信来源的纪律。
aliases: [内容农场, ai 聚合, 讹传, 假消息, fake mods]
---

# 不可信来源与已知编造

## 排除清单（建库纪律，与 AGENTS.md 一致）

以下类别**不作为本库来源**：

- **CSDN**（及各转载站）：`oar-kb/09-sources/unreliable-sources.md` 已取证 12 处编造。
- **toolify 一类 AI 聚合站**：内容由机器拼贴，作者/版本/需求 routinely 错。
- 各种"MOD 站"镜像（1mod/xmodhub/qiyou/lagofast 等）：**描述可参考
  （它们转录 Nexus 原文），但作者/版本/日期以 Nexus 文件信息页为准**。
- 无出境的"2026 最佳 mod 榜单"类文章：可用于发现候选，事实必须回 Nexus 核实。

## 已识别的具体编造/错误（本库核实记录）

| 说法 | 事实 | 出处 |
|---|---|---|
| "Water for ENB 作者 paganmetalfan" | mindflux；paganmetalfan 是 Watercolor for ENB | Nexus 37061 |
| "SE 上装 ENB 必配 ENBoost 防爆显存" | STEP：64 位 SE >4GB 内存时 ENBoost 冗余 | STEP wiki |
| "Skyrim 3D Trees and Plants 是 Pfuscher 的" | mathy79（Nexus 12371） | IGN 视频 Credits |
| "RUSTIC 全是 fadingsignal" | Clutter/Soulgems/Cooking 是 Gamwich(+Saerileth) | SETOG（Nexus 5883） |
| "Nexus 上的 SSELODGen 就是地形 LOD 工具" | 那是个过时旧版；现行是 STEP 论坛的 xLODGen beta | fkmods 教程 + Sheson 回帖 |
| "T4GTR34UM3R 和 T4GTR43UM3R 是两个人" | 至少 Terrain LOD Redone 与 MM/Blended Roads 高度疑似同一人；**未确认，存疑** | Nexus 9135 vs 11052/8834 |

## 证据分级（本库用法）

- **一手源**：Nexus 发布页/文件页/日志/作者回帖、官方仓库、官方站
  （enbdev.com、dyndolod.info）、STEP/modding.wiki 的机制文档。
- **社区经验**：Nolvus/sinitar 等整合指南、论坛高赞回帖、榜单——
  用于"怎么做"，不用于"是什么"。
- **存疑**：单一二手转述——本库显式标注，不当事实用。

## 相关

- [作者归属勘误](author-attribution-corrections.md)、
  [过时与改名页面](outdated-pages-and-renames.md)
