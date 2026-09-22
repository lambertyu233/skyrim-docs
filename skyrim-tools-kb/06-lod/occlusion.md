---
id: occlusion
title: 遮挡数据生成（Occlusion）
category: 06-lod
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [LOD, 遮挡, 性能, 远景, 排错]
aliases: [遮挡数据, 远景破洞, 地形破洞, FPS 优化]
source: https://stepmodifications.org/wiki/SkyrimSE:2.2.0
summary: 用 xLODGen 重新烘焙「从哪看不到哪」的数据：修掉远处地形的破洞，同时省掉不该画的远景——是 LOD 流程的最后一步。
---

# 遮挡数据生成（Occlusion）

## 它是什么

游戏用**遮挡数据**判断"站在 A 点看不到哪片区域"，从而**不渲染**那些区域。
原版遮挡数据是按原版地形算的；装了改地形/加建筑的 mod 之后，
数据与现实不符，就会出现两个方向的症状：

- **该剔的没剔** → 白画远景，掉帧；
- **不该剔的剔了** → 远处地形上出现**破洞**。

## 官方点名的重灾区

STEP 的 SkyrimSE 指南原文大意：**水面上方的远景破洞**是出了名的严重，
重新生成遮挡数据正是为了修它。

## 怎么做

在流程**最后一步**用 **xLODGen**：

1. 跑完 `xLODGen（地形）→ TexGen → DynDOLOD`；
2. 再用 xLODGen 更新遮挡数据；
3. 输出同样归入独立输出 mod。

## 刷新时机

与所有 LOD 生成一致：**任何影响外景物体的改动（增删/移动 mod）之后都要重跑**。
只改了室内、UI、身形之类的 mod 则通常不必。

## 相关

- [xLODGen（地形 LOD 生成）](../06-lod/xlodgen.md)（执行者）、[DynDOLOD（物体与树木远景）](../06-lod/dyndolod.md)、[TexGen（LOD 贴图生成）](../06-lod/texgen.md)
- [排错索引：从症状找答案](../../01-navigation/troubleshooting-index.md)（远景相关的症状索引）
