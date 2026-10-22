---
id: water-seams-and-lod-stripes
title: 水缝与地形 LOD 条纹排错
category: 09-troubleshooting
version: 1.0.0
updated: 2026-10-22
tags: [水缝, LOD 条纹, stripe, 远景, 排错]
kind: tutorial
source: https://www.nexusmods.com/skyrimspecialedition/mods/2182
summary: 水缝=水 mod 的 cell/worldspace 记录被覆盖（Synthesis 转发）；LOD 条纹=地形 LOD 未重生成或用了旧 mesh；两件事都指向"改了世界就要重跑"。
aliases: [water seam, 远景条纹, 色差水]
---

# 水缝与地形 LOD 条纹排错

## 水缝 / 水面色块不一致（一手源：Nexus 37061）

Water for ENB 官方排查逻辑：

- 症状：奇怪接缝、不同色块的水。
- 病因：**水 mod 的插件记录被其它 mod 覆盖**（cell 记录与
  worldspace 记录都要"转发/forward"）。
- 处置：① 尽量把水 mod 在 load order 里抬高（不总可行）；
  ② **首选 Synthesis patcher**（官方为 Shades of Skyrim ENB/CS 提供专用
  patcher）；③ 手搓 xEdit 补丁转发记录。
- 世界空间记录被覆盖的特定表现：**高精度水与远处 LOD 水之间的突兀缝**。

## 地形 LOD 条纹（一手源：Nexus 9135）

- 症状：远景地面一道道"梳齿"条纹。
- 病因：LOD 网格/贴图与当前世界不匹配；旧版概念（分件）导致的混乱。
- 处置：Terrain LOD Redone 的**高模 LOD 网格**就是为"几乎消除 stripe effect"
  而做；v1.3 起整包单 BSA，**建议卸载旧版再装**。

## 远景与近景贴图不一致（一手源：TexGen/Nolvus）

- 没跑 TexGen 或 TexGen 产物没覆盖包自带 LOD → 远处贴图对不上。
- 改世界后没重跑 → 同上。见[LOD 生成完整流程](../08-practices/lod-generation-workflow.md)。

## 水面反射与天空（一手源：STEP）

- 水面反射勾了 Sky 会**加重 LOD 水缝**——STEP 建议水面反射只选除 Sky 外的项。

## 相关

- [Realistic Water Two](../05-water/realistic-water-two.md)、
  [Water for ENB](../05-water/water-for-enb.md)
- [Terrain LOD Redone](../03-landscape/terrain-lod-redone.md)
