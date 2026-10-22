---
id: grass-mods-overview
title: 草类 mod 生态总览
category: 04-flora
version: 1.0.0
updated: 2026-10-22
tags: [草, grass, 生态, 选型, 性能]
kind: concept
source: https://www.nexusmods.com/skyrimspecialedition/mods/44899
summary: 现代草 mod 五大路线与互斥规则：致密高性能（Cathedral/Folkvangr）、ENB 复杂草（Tamrielic）、GoS  tweak（Verdant）、摄影测量（Origins of Forest）、区域混合（Skoglendi）。
aliases: [草地, 草 mod, 致密草地, ENB complex grass, GoS]
---

# 草类 mod 生态总览

## 铁律：**全境草 mod 一次只装一个**

一手源证据链：

- Verdant 页："GENERALLY ALL GRASS MODS ARE INCOMPATIBLE…… install AFTER……
  and allow it to OVERWRITE ALL files"（Nexus 60220）。
- sinitar 指南："Between the grass mods that affect all Skyrim regions,
  **install only one**"（社区经验，二手转述）。
- 区域小 mod 可叠在全境包之上（同上）。

## 主要选手（均一手源：各自 Nexus 页）

| mod | 作者 | 特征 |
|---|---|---|
| **Cathedral Landscapes** | The Community / DrJacopo | 致密、3× 可生长表面、自带地形 LOD；21954 |
| **Folkvangr** | Grumbledoook | 高质量 + 匹配地表；**建议关 ENB Complex Grass**（无 normal map，开了会怪）；44899 |
| **Verdant** | Preeum | **Grass on Steroids（GoS）tweak** 内建，中低配友好；1K/512 版；60220（LE 页）/ SE 有单独页 |
| **Tamrielic Grass** | Ciathyza | Complex Grass 版需 **ENB v0.473+**；NGIO 可选依赖；46217 |
| **Northern Grass SE** | BrosisJK | 经典北欧风 |
| **Origins of Forest** | forbeatn | 3D 森林地被；45719 |
| **Cathedral - 3D Pine Grass** | The Community | 松林 3D 草 |
| **Skoglendi** | JPSteel2 | 现代流行款；93944 |
| **Kyne's Grass** | mnikjom 等 | 多作者素材混合 |
| **DrJacopo's 3D Landscapes and Grass Library** | DrJacopo | **modder 资源库**（80687），内含 WIP 的 Cathedral - 3D Landscapes |

## ENB Complex Grass 专项

- ENB 的 Complex Grass 需要草的 normal map；没有的包（如 Folkvangr）
  开了会"looks weird"（一手源：44899 页）。
- Tamrielic 的 Complex Grass 版反过来**要求** ENB 0.473+。
- 社区有 "ENB Complex Grass - Patch Compendium" 给各草包补 normal map
  （社区经验：sinitar 指南）。

## 性能（社区经验 + 一手源混合）

- 密草是帧数第一杀手；FNIS 之前先确认 `iMinGrassSize`。
- GoS 路线（Verdant）以少量草型实现密度，中低配首选。
- "Cathedral Landscapes - Skoglendi - 3D Pines - Blended"（114540，
  Hawksbill）展示了手混三家之草的区域混合思路（一手源：该页）。

## 相关

- [草地 INI 设置](../04-flora/grass-ini-settings.md)
- [No Grass In Objects](../04-flora/no-grass-in-objects.md)
- [Landscape Fixes For Grass Mods](../04-flora/landscape-fixes-for-grass-mods.md)
