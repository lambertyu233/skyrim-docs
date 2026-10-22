---
id: lod-principles
title: LOD 层级原理
category: 01-principles
version: 1.0.0
updated: 2026-10-22
tags: [LOD, 远景, 原理, 地形 LOD, 物体 LOD]
kind: concept
source: https://www.nexusmods.com/skyrimspecialedition/mods/32382
summary: 远景分地形 LOD / 物体 LOD / 树木 LOD 三类；xLODGen 管地形，DynDOLOD 管物体与树木，改世界内容后必须重跑。
aliases: [树木 LOD, pop-in, 地平线]
---

# LOD 层级原理

## 为什么需要 LOD

原版 Skyrim 超过约 500 米后，世界退化为**平铺地表 + 广告牌树**——房子、塔、
独立树木全部消失，走近时"凭空弹出"（pop-in）。LOD（Level of Detail）就是在
远处用低模/贴图集维持世界轮廓。

## 三类 LOD 与责任工具（一手源：Sheson 在 Nexus 论坛的多次说明）

| 类型 | 内容 | 工具 |
|---|---|---|
| 地形 LOD | 远处地面网格 + 贴图 | **xLODGen**（beta，地形 LOD 功能 2018 年起取代 Oscape） |
| 物体 LOD | 建筑、废墟、石头等静态物 | **DynDOLOD** |
| 树木 LOD | 广告牌树 / 3D 树 LOD | **DynDOLOD** |

Sheson 原话（一手源，Nexus 论坛）："Use xLODGen to generate terrain LOD and
vanilla/CK style object and tree LOD. DynDOLOD is the improved version of
xLODgen for Skyrim/Enderal/SE/VR tree and object LOD."

## 关键事实

- **DynDOLOD 只做物体/树木，不做地形**——地形必须 xLODGen beta。
  xLODGen beta **不在 Nexus 发布**，官方渠道在 STEP 论坛
  （forum.step-project.com，一手源：Nolvus 指南 + Sheson 回帖指向该论坛帖）。
  Nexus 上的 "SSELODGen" 是**完全过时**的旧版（社区经验：fkmods 教程，2026-05）。
- **TexGen** 生成与当前材质匹配的 LOD 贴图（缝合物体 LOD 贴图集），
  是 DynDOLOD 工作流的前置步骤。
- **SSE Terrain Tamriel**（Nexus 54680，Sheson）：给世界边缘补回地形数据，
  生成地形 LOD 时装着，**生成后即可卸载/关掉**（一手源：该页描述）。
- 改**世界内容**（新地块、城市 overhaul、草设置）后必须重跑对应工具；
  仅调 `OverwriteGrassDistance/FadeRange` 不必重建草缓存
  （一手源：Nolvus LODGEN 章）。

## 与预生成 LOD 包的关系

预生成包（如 MM 自带 LOD atlas、Terrain LOD Redone、HD LODs）在简单列表下
"也能用"，但它们不认识你的 modlist——**有世界改动就得自己生成**。

## 相关

- [LOD 生成完整流程](../08-practices/lod-generation-workflow.md)
- [DynDOLOD](../07-mesh-tools/dyndolod.md)、[xLODGen](../07-mesh-tools/xlodgen.md)
- 排错：[水缝与 LOD 条纹](../09-troubleshooting/water-seams-and-lod-stripes.md)
