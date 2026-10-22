---
id: parallax-artifacts
title: 视差异常排错（蓝块 / 无效果 / 白块）
category: 09-troubleshooting
version: 1.0.0
updated: 2026-10-22
tags: [视差, parallax, 蓝块, 排错, Auto Parallax]
kind: tutorial
source: https://www.nexusmods.com/skyrimspecialedition/mods/125527
summary: 三大症状对三因：蓝块=视差网格无贴图（Auto Parallax）；无效果=没 ENB/CS 或 ini 没开；效果怪=贴图与网格版本不匹配。
aliases: [视差排错, blue mesh, 视差无效, parallax bug]
---

# 视差异常排错（蓝块 / 无效果 / 白块）

## 症状 → 病因对照（一手源：Nexus 125527 + modding.wiki）

| 症状 | 病因 | 处置 |
|---|---|---|
| **蓝色/无贴图网格** | 视差网格没有对应视差贴图 | 装 **Auto Parallax**（防止 "blue meshes in game for parallax-enabled meshes with no corresponding texture"，一手源：125527 页） |
| **装了视差包毫无效果** | ① 没装 ENB/CS；② `enbseries.ini` 的 `[EFFECT]` 没开 TerrainParallax/ComplexParallax | 按[视差原理](../01-principles/parallax-and-complex-material.md)检查依赖链 |
| **地形视差"平坦处也歪"** | 高度图值不对：127=平坦（仍计算）；255=平坦且不计算（complex material 规则） | 检查 alpha 通道语义用对没有 |
| **complex material 整个失效** | 环境遮罩 G 通道 ≤4/255 被判黑 | 压缩精度问题；grayscale 2.2 重写通道图 |
| **金属不像金属** | ENB `[ENVIRONMENT] COLOR POW` 不适合你的 B 通道金属度 | 调预设或降金属度值 |
| **视差贴图远处过锐/撕裂** | 视差贴图分辨率过高 | 视差贴图本就该"略糊"（125527 作者将其缩到 12.5%/原尺寸，一手源） |

## 版本匹配纪律（一手源：mythiq 对 202X 的转述 + 125527 页）

- **视差网格必须配同时代视差贴图**——"mixing a parallax mesh with a
  non-parallax texture produces visible artefacts"。
- 202X 的 Parallax Meshes 分 Whiterun / Riften Ground 等，各配各的。
- 每次增删视差网格/贴图后，用 ParallaxGen 的 `--upgrade-shaders` 重跑修补。

## 已知历史问题（一手源）

- 202X 文件页："**-SSE Parallax Shader Fix no longer needed, if you got ENB**"。
- CS 的 Extended Materials 已知会让"环境遮罩 alpha 通道非法"的 mod 内容变形
  （如 Immersive Creatures 的 Durzog）——modding.wiki 明说。

## 相关

- [视差与 Complex Material](../01-principles/parallax-and-complex-material.md)
- [ENB 预设与 CS 衔接](../08-practices/enb-presets-and-cs-bridge.md)
