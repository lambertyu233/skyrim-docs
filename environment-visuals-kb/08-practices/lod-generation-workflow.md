---
id: lod-generation-workflow
title: LOD 生成完整流程
category: 08-practices
version: 1.0.0
updated: 2026-10-22
tags: [LOD, 流程, DynDOLOD, xLODGen, TexGen, 草缓存]
kind: tutorial
source: https://www.nexusmods.com/skyrimspecialedition/mods/32382
summary: 世界层稳定后的标准六步：xLODGen 地形 → TexGen 贴图 → DynDOLOD 物体树木 → NGIO 草缓存 → DynDOLOD 草 LOD；每步的"何时必须重跑"。
aliases: [LOD 流程, 远景生成流程, dyndolod 教程, grass cache]
---

# LOD 生成完整流程

**前提**：世界层（地形/城市/树/草/水/天气）**全部装完并稳定后再跑**。
中途加世界 mod = 重跑。MO2 用户全程在 MO2 里通过 executables 跑工具。

## 六步（一手源：Nolvus 指南 + 各工具页）

1. **xLODGen beta → 地形 LOD**
   - 装 **SSE Terrain Tamriel**（54680）→ LOOT → 跑 xLODGen
     （`-sse`，只勾 Terrain LOD，LOD4/8/16/32 四档设置）→ 输出建成 mod
     → **卸载 SSE Terrain Tamriel**。
2. **TexGen → LOD 贴图**
   - MO2 配 `TexGenx64.exe -sse` → Start → "Zip & Exit" → 产物当 mod 装，
     **覆盖其它包提供的 LOD 贴图**。
3. **DynDOLOD → 物体/树木 LOD**
   - MO2 配 `DynDOLODx64.exe -sse` → 选预设（Low/Medium/High/Ultra）→
     输出建成 "DynDOLOD Output" mod。
4. **NGIO → 草缓存**（若用 No Grass In Objects）
   - 按 NGIO ini 设好 → 生成 grass cache → 建成 "Grass Cache" mod。
5. **重跑 DynDOLOD → 草 LOD**（吃草缓存）
6. 进游戏验证：地平线、树 LOD、草 LOD、水缝、条纹。

## 何时必须重跑（一手源汇总）

| 变更 | 重跑项 |
|---|---|
| 新地形/风景 mod、城市 overhaul、世界补丁 | xLODGen + TexGen + DynDOLOD |
| 换树 mod | TexGen + DynDOLOD |
| 换/调草 mod、NGIO 设置（除两距离值） | NGIO 缓存 + DynDOLOD |
| MM 装/卸 MOSS ESP | DynDOLOD（作者原话） |
| Cathedral Landscapes ≥3.0.2 | DynDOLOD（+40% 草 LOD） |
| 仅调 `OverwriteGrassDistance/FadeRange` | **都不用** |

## 成本与耐心（社区经验）

中列表 + 中档：地形约 40 分钟、TexGen 约 20 分钟、DynDOLOD 20 分钟-2 小时。
Ultra + 大列表可 2-4 小时、输出 2-5GB。

## 常见事故（一手源/社区经验）

- 输出目录在 MO2/Vortex/UAC 管控内 → LOD 全坏（xLODGen 的 `-o:` 必须指外面）。
- TexGen 产物没覆盖包自带 LOD → 远景贴图与近景不匹配。
- 忘了装/卸 SSE Terrain Tamriel → 边缘缺地形。
- FOMOD "Respect Enable Parents" 乱用 → CTD（FO4 教程的警告通用于各游戏：
  mod 作者不要预勾选）。

## 相关

- [DynDOLOD](../07-mesh-tools/dyndolod.md)、[xLODGen](../07-mesh-tools/xlodgen.md)
- [LOD 层级原理](../01-principles/lod-principles.md)
- [No Grass In Objects](../04-flora/no-grass-in-objects.md)
- 排错：[水缝与 LOD 条纹](../09-troubleshooting/water-seams-and-lod-stripes.md)
