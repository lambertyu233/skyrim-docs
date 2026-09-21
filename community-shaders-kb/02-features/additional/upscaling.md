---
id: upscaling
title: Upscaling 超分与帧生成
category: 02-features
kind: additional
status: released
version: 1.1.0
updated: 2026-09-21
tags: [超分, 帧生成, DLSS, FSR, 性能, 排错]
aliases: [插帧, XeSS, 帧生成怎么开, 超分辨率, upscale]
source: https://www.nexusmods.com/skyrimspecialedition/mods/156952
summary: 原生集成的超分套件（DLSS / FSR 3.1 + FSR 帧生成）。注意：XeSS 不受支持，帧生成仅在 ≥120Hz 生效。
---

# Upscaling 超分与帧生成

> 分类：附加特性 · 状态：已发布（Nexus 版本 1.4.0）

原生集成进游戏的完整超分套件，大幅提升性能同时改善画面保真度。

## 支持范围（重要更正）

| 技术 | 支持情况 |
|------|---------|
| **NVIDIA DLSS** 超分 | ✅ 支持（官方 Nexus 页写 **DLSS 4**，用户 wiki 写 **DLSS 4.5**，以你下载时的文件说明为准） |
| **AMD FSR 3.1** 超分 | ✅ 支持 |
| **AMD FSR Frame Generation** 帧生成 | ✅ 支持 |
| **Intel XeSS** | ❌ **不支持** |

> ⚠️ **XeSS 不受支持。** 作者原话大意：Intel 的文档质量极差，尝试联系 Intel 游戏开发者计划时被多次误导、拒绝提供帮助、几乎没有任何支持，因此不做。
>
> 网上仍能找到把 XeSS 列为支持方案的二手文章——**那是错的**。

## 相比 Skyrim Upscaler（DLSS / FSR2 / XeSS）的改进

官方列的对比清单：

- DLSS 下的**闪烁显著减少**
- 使用最新的超分更新
- **可在 HDR 下运行**
- **绝大多数菜单里保留 TAA**
- **支持帧生成**
- **屏幕边缘不再被拉伸**
- **全分辨率后处理**
- **为纹理锐度优化了 mip bias**
- **修正了天空运动矢量**
- **改进了反应性（reactive）与透明遮罩**
- **完整支持原生 AA（Native AA）**
- 修正了 facegen、截图、阴影、视频
- 修正了雨遮挡与 skylighting

## 默认行为

- 默认设为 **Quality**，具体走 **DLSS 还是 FSR 取决于 GPU**；
- **帧生成默认开启**。

## 帧生成

- 可**最多把帧率翻倍**，且**帧间隔（frame pacing）显著改善**，体感更顺滑可靠。
- 官方称**输入延迟应该没有可感知的增加**：帧生成使用 **UI 遮罩**，并在菜单中**自动禁用自己**以减少鼠标光标延迟；配合 DLSS 时，进入菜单会**降低超分分辨率**来补偿帧生成的缺席。
- **对 Skyrim 极其重要**：Skyrim 通常是 **CPU 瓶颈**，帧生成能在**不受 draw call 上限影响**的情况下提高帧率。

### 硬性条件

> ⚠️ **帧生成仅对 120 Hz 及以上的刷新率生效。**
>
> ⚠️ 想用帧生成**必须使用 Windowed 或 Borderless Windowed 模式**。

## 安装与需求

1. 安装 Community Shaders 及其全部前置。
2. **安装 SSE Display Tweaks**——用它来跑更高帧率并控制垂直同步。
3. 想用帧生成就用 **Windowed / Borderless Windowed**。
4. **把本 MOD 装在 CS 下面。**

## 相关条目

- [不兼容 MOD 清单](../../03-reference/incompatible-mods.md)（Skyrim Upscaler、Display Tweaks 的 BorderlessUpscale）
- [实战常见坑](../../06-community/common-pitfalls.md)（帧生成不生效的排查）

## 贡献者

doodlum（主要贡献者）。

---
*本条目依据官方 Nexus 发布页精修整理；如与官方页面不一致，以官方为准。*
