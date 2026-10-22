---
id: grass-ini-settings
title: 草地 INI 设置与密度调校
category: 04-flora
version: 1.0.0
updated: 2026-10-22
tags: [INI, 草地, 密度, iMinGrassSize, iMaxGrassTypesPerTexure]
kind: tutorial
source: https://www.nexusmods.com/skyrim/mods/60220
summary: [GRASS] 段两个关键值：iMaxGrassTypesPerTexure 决定草 mod 能否全貌工作，iMinGrassSize 反向调密度；改 NGIO 设置要重建草缓存。
aliases: [草地 ini, 草密度, grass settings]
---

# 草地 INI 设置与密度调校

## `[GRASS]` 段两个关键值（一手源：Verdant 页）

- **`iMaxGrassTypesPerTexure=15`**："Always, even with SFO"——
  Verdant 每种地表纹理下挂了 15 种草，不到 15 很多草不显示。
  **装任何密草 mod 先查它自己的要求**。
- **`iMinGrassSize=70`**：Verdant 作者个人值。**值越小草越密**
  （60=极密，100=性能）；作者明确不支持低于 60。
  掉帧时先调它（社区经验：sinitar 指南建议试 80/100/120）。

## 常见组合参照（一手源：各页 + STEP）

- Cathedral Landscapes 默认 `iMinGrassSize=60`（一手源：21954 changelog）。
- 各草 mod 通常**自带 ini**（Folkvangr："I've included the grass ini settings
  that I use. I do recommend keeping these settings"，一手源：44899）。
- STEP 指南：用 Cathedral Landscapes 时 Visuals 的 Grass 项无需再调
  （一手源：STEP wiki）。

## `[Display]` 相关（社区经验）

- `fWindGrassMultiplier`：加大风吹草动（sinitar 指南推荐值 3.5/7/11 实验）。
- Grass Fade 等 View Distance 值：STEP 推荐 Grass Fade=18000（最大）。

## 改设置后的连带动作（一手源：Nolvus LODGEN 章）

- 改了 **NGIO 的 `OverwriteGrassDistance/FadeRange` 之外**的任何东西
  （包括换草 mod、改 NGIO 其它设置）→ **必须重建草缓存**
  （删除 Grass Cache mod 后重跑生成）。
- 仅这两个距离值可直接改，无需重建。

## 相关

- [草类生态](../04-flora/grass-mods-overview.md)
- [No Grass In Objects](../04-flora/no-grass-in-objects.md)
- [游戏 INI 显示设置](../08-practices/ini-and-display-settings.md)
