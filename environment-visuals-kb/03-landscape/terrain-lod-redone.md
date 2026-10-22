---
id: terrain-lod-redone
title: Terrain LOD Redone
category: 03-landscape
version: 1.0.0
updated: 2026-10-22
tags: [Terrain LOD Redone, 地形 LOD, T4GTR43UM3R, 远景]
kind: reference
source: https://www.nexusmods.com/skyrimspecialedition/mods/9135
summary: T4GTR43UM3R 的地形远景重制：高分辨率 LOD 贴图/法线 + 高模 LOD 网格，几乎消除远景条纹；单 BSA + dummy 插件，load order 尽量靠上。
aliases: [地形远景, TLR, 远景条纹, lod terrain]
---

# Terrain LOD Redone

- **作者**：T4GTR43UM3R（一手源：Nexus 9135；与 T4GTR34UM3R 仅数字顺序不同，
  应为同一人的另一个账号——**未获作者确认，标注为存疑**）
- **Nexus**：skyrimspecialedition/mods/9135；最终 v1.42

## 它做什么（一手源：发布页）

- 重做地形 LOD 漫反射贴图以更好适配 LOD 雪；
- 重做 LOD 法线提升远景细节；
- **高模 LOD 网格**几乎消除"stripe effect"（远景条纹）；
- Solstheim 世界直接烘焙苔原草进 LOD 贴图；
- 世界地图兼容。

## 安装要点（一手源：发布页）

- 整包打进**一个 BSA + dummy 插件**；**load order 尽量高**（置顶附近）。
- 用 Open Cities 等改 LOD 网格的 mod，必须让它们覆盖本 mod 的 LOD 文件。
- 不想多一个插件：可把 BSA 按进 `Skyrim.ini` 后删掉 esp（作者给了方法）。
- FAQ：装后**不强制**跑 DynDOLOD/xLODGen；与 Spring Grass Overhaul、Skyland
  自带的 LOD 文件可混用；v1.3 起概念变更，**建议卸载旧版再装新版**。
- v1.1 起**删掉所有 LOD 贴图 mipmap**（大面积贴图 mip 无收益，只占空间）。

## 与 xLODGen 的关系

本包是**预生成**地形 LOD 资产；xLODGen 是**为自己的 load order 现生成**。
两者哲学不同：简单列表用预生成包省事；有世界改动的列表必须 xLODGen
（见 [LOD 生成完整流程](../08-practices/lod-generation-workflow.md)）。

## 相关

- [LOD 层级原理](../01-principles/lod-principles.md)
- [水缝与 LOD 条纹排错](../09-troubleshooting/water-seams-and-lod-stripes.md)
