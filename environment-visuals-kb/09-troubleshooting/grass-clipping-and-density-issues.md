---
id: grass-clipping-and-density-issues
title: 草穿模 / 不显示 / 密度异常排错
category: 09-troubleshooting
version: 1.0.0
updated: 2026-10-22
tags: [草, 穿模, 密度, NGIO, Landscape Fixes, 排错]
kind: tutorial
source: https://www.nexusmods.com/skyrimspecialedition/mods/42161
summary: 穿模=NGIO/Landscape Fixes 缺失或 ini 错；不显示=iMaxGrassTypesPerTexure 不够或草 mod 被覆盖；密度不对=iMinGrassSize 与草 LOD 缓存过期。
aliases: [草穿模, 草不显示, 草太少, 草太多, grass clipping, 密度异常]
---

# 草穿模 / 不显示 / 密度异常排错

## 症状 → 病因（一手源汇总）

| 症状 | 病因 | 处置 |
|---|---|---|
| 草从石头/地板/木箱里长出 | 没 NGIO 或没 Landscape Fixes | 装 [NGIO](../04-flora/no-grass-in-objects.md) + [Landscape Fixes](../04-flora/landscape-fixes-for-grass-mods.md) |
| 草该密的地方稀疏/整类草不见 | `iMaxGrassTypesPerTexure` 低于草 mod 要求（Verdant 需 15） | 按草 mod 要求设 ini（见[草地 INI](../04-flora/grass-ini-settings.md)） |
| 草比原版还少 | ini 被"奇怪编辑"；MO2 profile ini 与 Documents ini 不一致 | SFO FAQ 原话：删 Documents 下两个 ini 让游戏重建，再检查 MO2 profile |
| 苔原草不高 | **不是 bug**——SFO FAQ："it's a tundra, it's supposed to look like that" |
| 草 LOD 与近景差太多 | 改了草/NGIO 没重建缓存 + 重跑 DynDOLOD | 见[LOD 流程](../08-practices/lod-generation-workflow.md) |
| 切区卡顿/冻结 | NGIO 射线生成开销 | 升 NGIO 1.6.3+（生成快约 60%，一手源：changelog） |
| ENB Complex Grass 下草发怪 | 草包没有 normal map（Folkvangr）或 ENB 版本旧（Tamrielic 需 0.473+） | 关 Complex Grass 或打 Patch Compendium |
| 草被雪/地形"切断一条线" | lush→no-grass 边界 | Landscape Fixes 的 cell 级修正就是干这个的 |

## 顺序纪律（一手源）

- Landscape Fixes **放顶部**且早于改地形高度的 mod。
- NGIO 生成缓存 → DynDOLOD 草 LOD；改设置（除两距离值）→ 重建缓存。

## 相关

- [草类生态](../04-flora/grass-mods-overview.md)、[草地 INI 设置](../04-flora/grass-ini-settings.md)
