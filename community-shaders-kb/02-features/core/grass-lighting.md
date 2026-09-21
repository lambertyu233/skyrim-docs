---
id: grass-lighting
title: Grass Lighting 草体光照
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [草地, 光照, Complex Grass]
aliases: [草体光照, 草的光照, grass lighting, 草颜色太亮]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/grass-lighting
summary: 替换草着色器，加入顶点法线方向性光照、背面次表面散射，并修好 ENB 版 Complex Grass 的 UV 映射。
---

# Grass Lighting 草体光照

> 分类：核心特性（1.5.0+ 并入） · 状态：已发布

替换草着色器，提供更进阶的着色，含 **Complex Grass** 支持。

## More Advanced Grass Shading 更进阶的草着色

- **用顶点法线着色**，为光照加入**方向性**（草叶不再是一块均匀亮度的贴片）；
- 在草的**背面加入次表面散射**。

## Complex Grass 复杂草

- **修正了为 ENB 制作的 Complex Grass 的 UV 映射**；
- 支持**法线与高光贴图**；
- 基于**逆向出的游戏物体光照代码**实现。

> ⚠️ **ENB 的 complex grass 设置与 CS 不是一回事**，别照搬 ENB 的参数。

## 需求

1. 安装 [Community Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/86492) 及其全部前置（该特性已包含在核心安装里）。
2. **确认你的草 MOD 是否支持 Complex Grass**。若不支持，可能需要装一份 complex grass 更新：
   - [Vanilla Complex Grasses for ENB](https://www.nexusmods.com/skyrimspecialedition/mods/68640)（**虽然名字里有 ENB，但它同样适用于 CS**）；
   - [Complex Grass - The Official Patch Compendium](https://www.nexusmods.com/skyrimspecialedition/mods/67304)；
   - 或其它来源。

## 相关条目

- [Grass Collision 草体碰撞](grass-collision.md)
- [Grass Optimizations 草优化](../additional/grass-optimizations.md)

## 贡献者

doodlum（VR 之外全部功能的原始实现）。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
