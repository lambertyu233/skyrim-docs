---
id: xlodgen
title: xLODGen（Sheson，beta）
category: 07-mesh-tools
version: 1.0.0
updated: 2026-10-22
tags: [xLODGen, 地形 LOD, Sheson, STEP 论坛, beta]
kind: tool
source: https://forum.step-project.com/topic/13451-xlodgen-terrain-lod-beta-for-fnv-fo3-fo4-fo4vr-tes5-sse-tes5vr-enderal/
summary: 地形 LOD 生成器：2018 年起取代 Oscape；beta 版不在 Nexus 发布，官方渠道是 STEP 论坛帖；含遮挡剔除生成。
aliases: [SSELODGen, TES5LODGen, Oscape]
---

# xLODGen（Sheson，beta）

- **作者**：**Sheson**（一手源：其 Nexus 论坛回帖）
- **分发**：**beta 版不在 Nexus**——官方渠道是 **STEP 论坛帖**
  forum.step-project.com（Sheson 自己在回帖里指向该帖；
  Nolvus 指南亦从该帖下载 "xLODGen beta 93"）
- **谱系**：xEdit 的 LOD 生成功能拆出 → TES5LODGen（LE）/ SSELODGen（SE 旧版）/
  FO4LODGen；**Nexus 上的 SSELODGen 已完全过时**（社区经验：fkmods 教程 2026-05）

## 职责（一手源：Sheson 回帖）

"Use xLODGen to generate terrain LOD and vanilla/CK style object and tree
LOD. DynDOLOD is the improved version of xLODgen for…… tree and object LOD."

- 现代流程中：**地形 LOD 用 xLODGen beta**，物体/树木用 DynDOLOD。
- beta 后来加入：**遮挡（occlusion）生成**、**季节 mod 支持**。
- xLODGen 不生成 noise 材质（地形 LOD 上那层"老电视雪花"）——
  生成地面与原地面**色差可能来自 noise**（社区经验：fkmods 教程）。

## 使用要点（一手源：Nolvus 指南 + FO4 版教程通用）

- MO2 里配 `-sse`（或 `-FO4` 等）与 `-o:"输出路径"`；
  **输出必须在 MO2/Vortex/UAC 管控目录之外**，否则 LOD 会坏。
- **Object LOD 与 Terrain LOD 分开生成**（地形 LOD 极少需要更新）。
- 生成时装 **SSE Terrain Tamriel**（Nexus 54680）补边缘地形，**生成后可卸**。

## 相关

- [DynDOLOD](dyndolod.md)、[SSE Terrain Tamriel](../08-practices/lod-generation-workflow.md)
- [LOD 层级原理](../01-principles/lod-principles.md)
