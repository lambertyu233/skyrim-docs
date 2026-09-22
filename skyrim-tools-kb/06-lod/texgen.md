---
id: texgen
title: TexGen（LOD 贴图生成）
category: 06-lod
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [LOD, 贴图, 图集, 生成器, 官方文档]
aliases: [LOD 贴图, 纹理生成, 图集生成, texture atlas]
source: https://dyndolod.info/DynDOLOD-Reference
summary: 随 DynDOLOD 一起分发的小工具：按当前已启用的 mod 生成自定义的物体 LOD 贴图，让远处建筑与近处渲染看起来一致；v3 起还能出草地 billboard。
---

# TexGen

## 做什么

**随 DynDOLOD 分发**的独立程序。它扫描你**当前启用的 mod**，
生成一套自定义的**物体 LOD 贴图**。

**为什么需要它**：远景用的是预烘焙的 LOD 贴图/图集，
如果它还是原版贴图，而你近处的建筑换了材质——
就会出现**远近同一栋房子颜色/材质对不上**的割裂感。
TexGen 的作用就是让这两者对齐。

## 在流程里的位置

`xLODGen（地形）` → **`TexGen`** → `DynDOLOD` → `xLODGen（Occlusion）`

**必须先跑 TexGen 再跑 DynDOLOD**——后者要消费 TexGen 产出的贴图。
输出同样要放进**独立输出 mod**（STEP 的命名习惯：`TexGen Output`）。

## 设置要点（STEP 指南口径）

- 按**渲染分辨率**选档：1080p = HD、1440p = QHD、2160p = 4K。
- **草地 LOD**：只有生成草地 LOD 时才勾 Grass；用/不用 ENB Complex Grass 时勾选不同
  （"HD grass" 对应 ENB Complex Grass）。
- 显存相关的贴图尺寸与压缩格式取舍：
  - 显存 ≤ 4 GB：LOD 贴图尺寸偏小、法线用较省的格式；
  - 显存较大：可以提高尺寸与压缩质量。
  （具体数值给在 STEP 指南里，随版本变化，**以你所用 DynDOLOD 版本的推荐值为准**）

## 与 xLODGen 的分工（易混点）

| | xLODGen | TexGen |
|---|---|---|
| 产出 | **地形** LOD 的网格与贴图 | **物体** LOD 用的图集贴图 |
| 位置 | 流程第一步 + 最后一步（遮挡） | 流程中间 |
| 是否随 DynDOLOD 分发 | 否 | **是** |

## 相关

- [xLODGen（地形 LOD 生成）](../06-lod/xlodgen.md)、[DynDOLOD（物体与树木远景）](../06-lod/dyndolod.md)、[遮挡数据生成（Occlusion）](../06-lod/occlusion.md)
- `community-shaders-kb/`（ENB / Complex Grass 侧的话题）
