---
id: water-effects
title: Water Effects 水特效
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [水, 焦散, 视差, 纹理]
aliases: [水特效, water effects, 水面效果, 水波]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/water-effects
summary: 模拟水下焦散并为水面加入为水专门设计的简化视差；视差需支持位移图的水 MOD。
---

# Water Effects 水特效

> 分类：核心特性（1.4.7+ 并入） · 状态：已发布

模拟水下**焦散**，并为水面加入**优化过的视差**支持。

## Caustics 焦散

水下（**仅限大面积水域与河流**）可以看到**焦散**，并且：**越往深处走，焦散越大、并逐渐淡出**。

- 焦散的**形状随水面曲率变化**；
- **在物体底部会被禁用**。

实现方式是把一张纹理**滚动、叠加**。它是一份**松散文件（loose file）**，可以被 MOD 替换。

> 💡 如果你要替换这张纹理，**请存成 BC4** 以获得最佳性能。

## Parallax 视差

视差为水面补出**深度**，模拟更多细节。

- 每张滚动纹理的**高度会被加总并混合**——这是一套**更简单的、专为水设计**的视差算法。

## 需求

1. 安装 [Community Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/86492) 及其全部前置（该特性已在核心安装里）。
2. **要让视差可见，需要一个提供位移图（displacement map）的兼容水 MOD**，例如 **Water for ENB** 或 **Simplicity of Seas**。

> 另见 [Unified Water](unified-water.md)（把真实水体瓦片延伸到 LOD，消除远处接缝）与 [Dynamic Cubemaps](dynamic-cubemaps.md)（水反射可横跨整个屏幕）。

## 贡献者

doodlum、davo、jiaye。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
