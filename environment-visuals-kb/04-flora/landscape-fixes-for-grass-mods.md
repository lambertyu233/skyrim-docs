---
id: landscape-fixes-for-grass-mods
title: Landscape Fixes For Grass Mods（code1k / Arthmoor）
category: 04-flora
version: 1.0.0
updated: 2026-10-22
tags: [Landscape Fixes, 草, 接缝, code1k, Arthmoor]
kind: reference
source: https://www.nexusmods.com/skyrimspecialedition/mods/9005
summary: 改地形记录消掉"草从物体里长出/路径被草盖住/雪区长绿草"等问题；SE 版由 code1k 维护（LE 原作者 Arthmoor），v5.9（2026-09）。
aliases: [草地补丁, 草穿模, 地形接缝]
---

# Landscape Fixes For Grass Mods（code1k / Arthmoor）

- **作者**：SE 版 **code1k**；LE 原版 **Arthmoor**
  （一手源：Nexus 9005；Bethesda.net 移植页注明 "Created by Arthmoor"）
- **Nexus**：skyrimspecialedition/mods/9005；当前 **v5.9**（2026-09-27），
  56,601 endorsements；Light 插件
- **定位**：性能优化 + Bug Fixes + Lore-Friendly

## 它做什么（一手源：发布页 + Bethesda 页描述）

- **改地形记录**（cell 级）让草不在石头/墙/物体位置生长，减少穿模；
- 恢复被草盖住的**小径与细节**，清理部分道路的过度生长；
- 移除看不到的位置的草（Whiterun 墙内、Falkreath 建筑内等）**提性能**；
- 修若干**纹理接缝**（如 cell 6,-11）；为 USSEP XLCN 转发记录；
- v5.9 起主文件 FOMOD 化，捆绑 Vanilla Military Camps 与
  Generic Grass Limiter（火山/雪原等不兼容纹理的通用限草器）。

## 安装纪律（一手源：Bethesda.net 页 + 9005 页）

- **放在 load order 顶部区域**，且必须**早于任何改这些区域地形高度的 mod**。
- 与 NGIO 分工：NGIO 动态射线防长草；本 mod 静态改地形记录——
  两者可互补（社区常见组合）。
- 与 Open Cities 兼容（v2.0 起"full fix for open cities"）。
- 有 Verdant 专用 tweaks 文件（changelog）。

## 中文翻译（一手源）

Nexus 73098（FirstAstor 译）。

## 相关

- [No Grass In Objects](../04-flora/no-grass-in-objects.md)
- [草穿模排错](../09-troubleshooting/grass-clipping-and-density-issues.md)
