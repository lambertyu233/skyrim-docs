---
id: dyndolod
title: DynDOLOD（Sheson）
category: 07-mesh-tools
version: 1.0.0
updated: 2026-10-22
tags: [DynDOLOD, LOD, Sheson, TexGen, 远景]
kind: tool
source: https://www.nexusmods.com/skyrimspecialedition/mods/32382
summary: 物体/树木 LOD 生成的事实标准：按你的 load order 现生成远处模型与贴图（TexGen 缝图），支持动态远景；官方站 dyndolod.info。
aliases: [远景生成, 物体 LOD, 树木 LOD, lod 工具, 地平线弹出]
---

# DynDOLOD（Sheson）

- **作者**：**Sheson**（一手源：Nexus 32382 + 论坛回帖）
- **Nexus**：skyrimspecialedition/mods/32382；官方站 **dyndolod.info**
- **支持**：Skyrim SE/AE、Skyrim VR、Skyrim LE、Fallout 4、Enderal
- **组成**：**工具本体** + **DynDOLOD Resources**（资产，装成普通 mod）
  + **TexGen**（LOD 贴图生成器）

## 职责边界（一手源：Sheson 论坛原话）

"DynDOLOD is just the advanced version of xLODGen for object and tree LOD
generation"——**只做物体与树木 LOD；地形 LOD 归 xLODGen**。
可生成持久 3D 物体（棚屋/塔/废墟/独立树）、带阴影的改良树 LOD、
**动态远景**（远处瀑布/风车动画）等。

## 工作流要点（一手源：Nolvus 指南 + Sheson 回帖）

1. 先 xLODGen 生成地形 LOD（beta）；
2. 装 DynDOLOD Resources；MO2 里给 `TexGenx64.exe` 配 `-sse` 参数；
3. 跑 **TexGen** 生成与当前材质匹配的 LOD 贴图（"Zip & Exit" 产出当 mod 装）；
4. 跑 **DynDOLODx64.exe**（`-sse`），选预设 Low/Medium/High/Ultra；
5. 输出 `/DynDOLOD_Output`，在 MO2 里建成 "DynDOLOD Output" mod 启用。
6. **每次改动世界内容（新地块/城市 overhaul/草设置/MOSS ESP）都要重跑**。

## 成本（社区经验：thegamercodex）

- 大列表 + Ultra：**2-4 小时**生成；输出 2-5GB。
- 低端 GPU 开高档位会掉帧（LOD 是额外 draw call）——有质量档位可调。

## 排错锚点（一手源：各页）

- MM 装了 MOSS ESP → 必须重跑 DynDOLOD（作者回帖）。
- Cathedral Landscapes 3.0.2+ → 重跑以获取 +40% 草 LOD 多样性。
- 换树 mod（HLT/EVT）后 → TexGen + DynDOLOD 都要重跑（STEP 论坛）。
- RW2 的瀑布 LOD 问题按 5.7.1 官方回复处理（"Not a bug"）。

## 相关

- [xLODGen](xlodgen.md)、[LOD 层级原理](../01-principles/lod-principles.md)
- [LOD 生成完整流程](../08-practices/lod-generation-workflow.md)
