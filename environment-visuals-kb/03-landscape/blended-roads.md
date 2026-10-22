---
id: blended-roads
title: Blended Roads
category: 03-landscape
version: 1.0.0
updated: 2026-10-22
tags: [Blended Roads, 道路, 3D 路面, T4GTR34UM3R]
kind: reference
source: https://www.nexusmods.com/skyrimspecialedition/mods/5760
summary: 把路面石"混"进地面网格而不是贴一层贴图，消除道路 UV 瑕疵；与 Real Roads 互斥，需要带 alpha 的道路贴图配合。
aliases: [混路, 3d 道路, real roads]
---

# Blended Roads

- **作者**：**T4GTR34UM3R**（与 Majestic Mountains 同作者，一手源：xmodhub 转录 +
  Skyland AIO 页 Credits "T4gtr34um3r"）
- **Nexus**：skyrimspecialedition/mods/**8834**（SE 版，一手源：Lux Via /
  IGN 视频 / Pale Pass Extension 等多个页面的 Credits 均链接至 8834；
  LE 原版为 skyrim/mods/8837 一系）

## 解决什么问题（一手源：作者页）

原版道路是"地面上再铺一层带 UV 的 mesh/贴图"，接缝与 UV 瑕疵难避免。
Blended Roads **把路面材质直接混合进地面网格**——不再有独立路面层，
"eliminates a lot of road uvw issues"。

## 关键事实

- **v1.4 起每种道路独立法线**（Rift 落叶、Reach 苔藓），道路贴图由
  Majestic Mountains 提供（一手源：changelog）。
- **与 Real Roads 互斥**（Real Roads 是另一条 3D 道路技术路线）。
- 兼容 SMIM 桥梁。
- 其它包的道路贴图**通常没有 alpha 通道，混不进去**——需要作者提供兼容版；
  Pfuscher 为其出了 "Blended Roads Retexture"（可选文件，一手源：Nexus 2347 files）。
- Skyland AIO **捆绑 Blended Roads 网格**（经作者许可，一手源：AIO Credits）。
- 已知问题：mesh 内可混合、mesh 间不行；碰撞略浮（几乎不可见）；
  积雪路面投影处理见其 readme。

## 搭配建议（社区经验 + 一手源混合）

- 202X 页面称其为 "a must have for life like roads"。
- STEP 指南中 Cathedral Landscapes 安装即选 Blended Roads 选项。

## 相关

- [Majestic Mountains](../03-landscape/majestic-mountains.md)
- [Terrain LOD Redone](../03-landscape/terrain-lod-redone.md)（道路 LOD 配套）
