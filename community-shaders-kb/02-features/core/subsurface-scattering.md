---
id: subsurface-scattering
title: Subsurface Scattering 次表面散射
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [皮肤, 散射, 材质, 角色]
aliases: [SSS 次表面散射, 次表面散射, subsurface scattering, 皮肤通透]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/subsurface-scattering
summary: 屏幕空间的次表面散射，用于角色皮肤；着色器与虚幻引擎同款，人类与兽族各有独立 profile。
---

# Subsurface Scattering 次表面散射

> 分类：核心特性（1.5.0+ 并入） · 状态：已发布

为**角色**加入屏幕空间次表面散射，模拟真实皮肤。官方定位很明确：**这是为「写实的皮肤着色」设计的**。

## 特性

- 这套次表面散射着色器**与虚幻引擎里那套相同**，至今仍在很多游戏里使用（**包括 Fallout 4**）。
- **次表面 profile 可在游戏内配置**，**人类种族一套、兽族一套**。
- **默认关闭原版角色光照**——因为它「不太好」，关掉能让皮肤着色更真实。
- **兼容所有皮肤与身体 MOD**。

## 与 True PBR 里那个 SSS 的区别

别混淆两个同名的东西：

| | 本条目（角色的 SSS） | [True PBR 的 Subsurface Scattering](../../04-development/pbr-for-artists.md) |
|---|---|---|
| 作用对象 | **角色皮肤**（屏幕空间） | **任意材质的纹理槽位**（槽 8） |
| 配置方式 | CS 菜单里的 profile | 网格 flag + 纹理 + JSON 参数 |

两者都叫 Subsurface Scattering，但一个是角色后处理、一个是 PBR 材质技法。

## 相关条目

- [True PBR 美术师指南](../../04-development/pbr-for-artists.md)（材质级 SSS、与双层材质互斥）
- [Advanced Skin](../additional/advanced-skin.md)（开发中的进阶皮肤方案，TBA）
- [Hair Specular](../additional/hair-specular.md)

## 贡献者

doodlum、jiaye、alandtse。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
