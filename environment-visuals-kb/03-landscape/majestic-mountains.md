---
id: majestic-mountains
title: Majestic Mountains
category: 03-landscape
version: 1.0.0
updated: 2026-10-22
tags: [Majestic Mountains, 山脉, T4GTR34UM3R, 网格, LOD]
kind: reference
source: https://www.nexusmods.com/skyrimspecialedition/mods/11052
summary: 完整的山脉重制（非单纯贴图）：8192×4096 单贴图合并、全山投影阴影、MOSS 苔藓 ESP、DynDOLOD LOD 包，v4.02（2022-10）。
aliases: [MM, 雪山, moss]
---

# Majestic Mountains

- **作者**：**T4GTR34UM3R**（一手源：Nexus 11052）
- **Nexus**：skyrimspecialedition/mods/11052；2017-07-23 上传，
  当前 **v4.02**（2022-10-16），53,162 endorsements
- **依赖**：**DynDOLOD**（作者标注 required，一手源：readme）

## 它是什么（一手源：readme）

不是 retexture，是**山脉完全重制**：

- 两张原版 4K 山脉贴图合并为**一张 8192×4096**，重调 UV，自制匹配 LOD；
- **所有山脉投影阴影**；重做顶点色与预烘焙 AO；
- 滥用多层视差着色器制造岩层变化，避免"叠石头"观感；
- 移除顶点色获得雪网格→雪地面的过渡；
- **MOSS**：可选 ESP 给山体投影苔藓材质，分绿苔（Reach）与褐苔
  （Tundra/Rift）两版，打断 tiling；
- **SUN**：两个日照方向 ESP（North 默认 / South），**只启用一个**。

## 三个版本

default / **Darkside** / **Lightside**——STEP 推荐 Lightside 与指南光照最搭
（一手源：STEP wiki）。选哪个取决于你的天气/ENB。

## 加载顺序与坑（均一手源：Nexus 11052 readme/posts）

- `MajesticMountains.esp` 放在本 mod 其它部件**之上**。
- `MajesticMountains_Landscape.esm` 与改地形的 ESM（如 Beyond Skyrim: Bruma）
  冲突→把该 ESM 在 load order 里往上放。
- **用 MOSS ESP 后必须重跑 DynDOLOD**（作者 2021-07-29 回帖：
  CK 曾吞掉 ESM flag，4.02 已重新加回）。
- **SSE Engine Fixes** 疑似导致问题时：`skse/plugins/EngineFixes.ini` 里
  `BSLightingShaderForceAlphaTest = false`。
- 雪花色异常 → 检查 weather mod 与 MM 的顺序（LOOT 常把天气放下面）。
- 灰/白山体 → MM.esp 被禁或位置过低，且需重跑 DynDOLOD。
- 黑山体/岩石 → 重装通常解决。
- **与其它山脉 retexture 不兼容**（MM 专用 retexture 除外）；与主流雪 mod 兼容。
- MM 网格面数高于 SMIM → **让 MM 覆盖 SMIM 网格**。
- "HD LODs" 用了 MM 的山脉 LOD 贴图，安装时别覆盖它。

## 相关

- [DynDOLOD](../07-mesh-tools/dyndolod.md)（LOD 包在 MM 可选文件）
- [Blended Roads](../03-landscape/blended-roads.md)（同作者）
- [Terrain LOD Redone](../03-landscape/terrain-lod-redone.md)（同社区地形 LOD 方案）
