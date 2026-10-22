---
id: tree-mods-overview
title: 树木 overhaul 生态总览
category: 04-flora
version: 1.0.0
updated: 2026-10-22
tags: [树木, 选型, 生态, trees, 森林]
kind: concept
source: https://www.nexusmods.com/skyrimspecialedition/mods/50961
summary: 五条技术路线：原版风替换（HLT/EVT）、摄影测量重制（NOTWL）、区域特化（Aspens/Bent Pines）、3D 植物扩张（S3D）、致密化（SFO/HLT scale）。
aliases: [树 mod, 白桦, 松树, EVT, Enhanced Vanilla Trees]
---

# 树木 overhaul 生态总览

## 技术路线（一手源：各发布页）

| 路线 | 代表 | 特征 |
|---|---|---|
| 原版风精细替换 | **Happy Little Trees**（50961）、Enhanced Vanilla Trees | 蒙皮动画、低开销、树 LOD 指南齐全 |
| 摄影测量重制 | **Nature of the Wild Lands**（63604） | 400+ 新模型、atlas 优化、SSS、3D LOD |
| 区域特化 | **Aspens Ablaze**（39998，白桦）、Bent Pines II（8306）、Blubbos Reach 树 | 只改一类树，与其它树 mod 共存 |
| 3D 植物扩张 | **Skyrim 3D Trees and Plants**（12371，mathy79） | 加新树种/植株，非替换 |
| 树+草一体 | SFO（树为主）、Seasonal Landscapes | 自带季节或草配套 |

## 共同纪律（一手源：STEP 论坛 + 各页）

1. **两个全境树 mod 互斥**（EVT 与 HLT 不能共存，STEP 原话：
   "EVT and HLT both change vanilla trees, so they are not compatible without
   custom patching"）。
2. **换树 mod 后必须重生成 LOD**（TexGen + DynDOLOD，STEP 论坛回帖）。
3. 区域特化 mod（Aspens 等）通常可叠在全境树 mod 之上，注意 LOOT 排序
   （Aspens Ablaze 的插件应在 HLT 之后，STEP 用户实测需手动规则）。
4. 树 mod 是**帧数大户**：NOTWL 3.00 起做 atlas + 减面 + navcut 优化
   （一手源：changelog），HLT 自称 GTX 970 上约 -5 FPS。

## 快速选型（社区经验）

- 要"原版味 + 高性能"：HLT（+Treescale.esm 松树 +20%）。
- 要"现代摄影测量观感"：NOTWL（3.10+ 带 SSS 与 3D LOD）。
- 只想秋天红叶：Aspens Ablaze 叠在任意全境包上。

## 相关

- [Happy Little Trees](../04-flora/happy-little-trees.md)、
  [Aspens Ablaze](../04-flora/aspens-ablaze.md)、
  [Nature of the Wild Lands](../04-flora/nature-of-the-wild-lands.md)、
  [Skyrim Flora Overhaul](../04-flora/sfo.md)
- [LOD 生成完整流程](../08-practices/lod-generation-workflow.md)
