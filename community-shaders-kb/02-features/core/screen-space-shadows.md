---
id: screen-space-shadows
title: Screen Space Shadows 屏幕空间阴影
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [阴影, 屏幕空间, 草, 性能]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/screen-space-shadows
summary: 用屏幕空间阴影补齐草、地图、远景与自阴影；是 Bend Studio 方案的定制实现，相对更吃性能。
---

# Screen Space Shadows 屏幕空间阴影

> 分类：核心特性（1.5.0+ 并入） · 状态：已发布

补齐了原版阴影体系缺的那一档：**草阴影、世界地图阴影、远景阴影、自阴影**。

## 实现来源

这是 **Bend Studio「Inside Bend: Screen Space Shadows」方案的定制实现**，针对 Skyrim 的世界做了视觉改进。

> ⚠️ 官方明确提示：**相对其它功能，这一项可能比较吃性能。** 低端机优先考虑它的取舍。

## 与 ENB 的关系

替代 ENB 的 Shadow / Detailed Shadow 一类方案。这也是[官方功能对照矩阵](../../00-overview/feature-matrix.md)里少数 **CS / ENB / CS VR / ENB VR 四方齐备**的功能。

## 性能取舍

官方给出的高开销功能候选就包括它所在的阴影体系。请配合 [Performance Overlay 的 Profiling](../../04-development/testing-and-debugging.md) 实测，而不是凭猜测关闭。

## 贡献者

doodlum、alandtse、FlayaN。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
