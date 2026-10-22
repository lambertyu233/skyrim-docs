---
id: cathedral-assets-optimizer
title: Cathedral Assets Optimizer（G'k）
category: 07-mesh-tools
version: 1.0.0
updated: 2026-10-22
tags: [Cathedral Assets Optimizer, CAO, Gk, 资产, 工具]
kind: tool
source: https://www.nexusmods.com/skyrimspecialedition/mods/24469
summary: Cathedral 系列的资产生成/优化工具：批量处理贴图/网格/LOD 资产，Cathedral Weathers 等大包构建管线的一环。
aliases: [资产优化, cathedral 工具, LE 移植, bc7, asset optimizer]
---

# Cathedral Assets Optimizer（G'k）

- **作者**：**G_k**（上传者 Gka1；一手源：Nexus 23316；
  Cathedral Weathers Credits 列表亦署名 "Cathedral Assets Optimizer by G'k"）
- **Nexus**：skyrimspecialedition/mods/**23316**；当前 **v5.3.15**
  （2026-03-23，另有 v7.0 BETA），23,921 endorsements
- **许可**：GPL-3.0（GitLab 仓库，一手源：发布页 LICENSE 说明）

## 定位（一手源：发布页 + thegamercodex 转述）

**资产生成/优化自动化工具**：批量处理 **BSA / meshes / textures / animations**：

- 贴图：**BC7 重压缩**、分辨率过超时降采样、修 mipmap；
- 网格：**LE → SE 格式转换**（几何不变、二进制头不同——不转换则游戏加载崩溃）、
  结构优化（内建 nifly/NifOpt）；
- 动画：LE → SE（hkx）；
- 常见用途：LE mod 移植 SE；给 4K 重包瘦身降显存；修坏 mipmap（远处闪烁）。

## 用户层面的意义

- 解释 Cathedral 包"为什么能又大又省"：构建期就做过压缩/格式/尺寸分层。
- 自己做 Cathedral 风格资产包时的参考实现（输出规格见
  [DDS 压缩格式](../01-principles/texture-formats-and-compression.md)）。
- 注意：**只转格式不保运行**——Papyrus 等 LE 专属内容它不管；
  Defender 会拖慢它（建议加白名单，一手源：发布页）。

## 相关

- [SSE NIF Optimizer](sse-nif-optimizer.md)、[DynDOLOD](dyndolod.md)
