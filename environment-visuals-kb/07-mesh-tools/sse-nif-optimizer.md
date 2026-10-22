---
id: sse-nif-optimizer
title: SSE NIF Optimizer（ousnius）
category: 07-mesh-tools
version: 1.0.0
updated: 2026-10-22
tags: [NIF, 网格工具, ousnius, 优化, NifSkope]
kind: tool
source: https://www.nexusmods.com/skyrimspecialedition/mods/4089
summary: 网格清理事实标准：转 BSTriShape、补切线、清 NiSkinData、重算包围球、删未引用块；GitHub 开源（ousnius/SSE-NIF-Optimizer + nifly，GPLv3）。
aliases: [SSE NIF Optimizer, nif 优化, nifly, BSTriShape, 切线]
---

# SSE NIF Optimizer（ousnius）

- **作者**：**ousnius**（一手源：Nexus 4089）
- **Nexus**：skyrimspecialedition/mods/4089；当前 **v3.2.1**（2024-10-06）
- **源码**：GitHub `ousnius/SSE-NIF-Optimizer` 与 `ousnius/nifly`（GPLv3，
  一手源：发布页）

## 它做什么（一手源：发布页）

- 把 NIF 转成 **SSE 格式（BSTriShape、NiSkinPartition 调整）**；
- head parts 转 **BSDynamicTriShape**（**只对 head parts 用这个选项**）；
- 三角化几何与蒙皮分区；清理无用顶点权重的 NiSkinData；
- **重算几何与骨骼包围球**；给需要的网格**加切线**；
- 删掉不需要的法线/切线（如 body meshes）；去全白顶点色；
- 重名网格改名（游戏要求唯一）；清头字符串；删未被引用的块；
- 可**回转 LE 格式**；可扫描贴图 SSE 兼容性。

## 纪律（一手源：发布页）

- **先备份 NIF**；
- **不要对整个 meshes 文件夹一次跑**；
- **head parts 选项只能用于 head parts**（头盔是普通网格，不是 head part）；
- SSE 的 UV 精度更低——UV 超出 0-1 范围的先回 NifSkope 重整；
- 看新格式需**最新 NifSkope**（jonwd7 的 releases）。

## 在环境美化里的位置

用户层面**很少直接跑它**——它主要是 mod 作者/移植工具。
但排错时值得知道：LE 网格"爆炸"、缺切线导致的法线错误，
标准答案就是用它过一遍（一手源：Nexus Wiki "Porting Skyrim mods to
Skyrim Special Edition"："The easiest way is to use Ousnius' SSE NIF
Optimizer"）。

## 相关

- [Cathedral Assets Optimizer](cathedral-assets-optimizer.md)（同类但侧重 LOD/资产）
- [视差与 Complex Material](../01-principles/parallax-and-complex-material.md)（切线是视差前提）
