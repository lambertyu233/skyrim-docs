---
id: feature-matrix
title: 官方功能对照矩阵与路线图
category: 00-overview
version: 1.0.0
updated: 2026-09-21
tags: [概览, 对照, ENB, VR, 路线图, 官方]
source: https://github.com/community-shaders/skyrim-community-shaders/wiki
summary: 官方 Developer Wiki 的 CS / ENB / CS VR / ENB VR 全功能对照表，以及官方承认的潜在未来功能依赖图。
---

# 官方功能对照矩阵与路线图

本条目译自**官方 GitHub Developer Wiki** 的「Current list of features and versions」。它回答一个别的页面都答不了的问题：**同一项功能，CS 和 ENB 谁有、VR 分支有没有**。

> 官方用户 wiki（modding.wiki）面向玩家；这份矩阵只存在于 Developer Wiki，属于「进阶信息」。原表会随版本变动，权威版本请看 [Developer Wiki 原文](https://github.com/community-shaders/skyrim-community-shaders/wiki)。

## 读法

- `Yes` = 已实现；`WIP` = 开发中（Work In Progress）；`No` = 无；`Beta` = 测试阶段；`n.a.` = 不适用。
- `No*` = CS/ENB 本身不做，但**可由第三方 MOD 达到**。
- 原表个别单元格为空，本表以 `—` 表示「原表未给出」。

## Grass（草地）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Grass Collisions 草体碰撞 | Yes | Yes | Yes | No |
| Grass Lighting 草体光照 | Yes | Yes | Yes | No |
| Procedural grass 程序化草地 | WIP | No | WIP | No |

## Water（水）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Water Parallax 水体视差 | Yes | Yes | Yes | No |
| Water Blending 水体融合 | Yes | Yes | Yes | — |
| Water caustics 水底焦散 | Yes | Yes | Yes | No |
| Screen Space Reflections 屏幕空间反射 | Yes | Yes | Yes | No |

## Lights（光照）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Particle Lights 粒子光源 | Yes | Yes | Yes | Yes |
| Light Limit Fix 灯光上限修复 | Yes | Yes | Yes | No |
| Indirect Lighting / SSGI 间接光照 | Yes | Yes | Yes | — |
| Tree LoD Lighting 树木 LOD 光照 | Yes | No | Yes | No |
| Image Based Lighting 基于图像光照 | Yes | Yes | Yes | — |
| Inverse Square Lighting 平方反比光照 | Yes | No | Yes | No |
| Linear Lighting 线性光照 | WIP | No | WIP | No |

## Shadows（阴影）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Normalmap Shadows 法线贴图阴影 | No | Yes | No | Yes |
| Screen-Space Shadows 屏幕空间阴影 | Yes | Yes | Yes | Yes |
| Distant Shadows 远景阴影 | Yes | Yes | Yes | — |
| Ambient Occlusion 环境光遮蔽 | Yes | Yes | Yes | Yes |
| Interior Sun Shadows 室内阳光阴影 | Yes | No | Yes | No |
| Effect Shadows 特效阴影 | Yes | No | Yes | No |

## Rain（雨）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Wet Surfaces 湿润表面 | Yes | Yes | Yes | Yes |
| Puddles 积水 | Yes | No | Yes | No |
| Dynamic rain drops 动态雨滴 | Yes | Yes | Yes | — |

## Sky（天空与天气）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Sun Rays 阳光光束 | Yes | Yes | Yes | Yes |
| Sun Glare 太阳眩光 | WIP | Yes | Yes | — |
| Volumetric Rays 体积光束 | Yes | Yes | Yes | Yes |
| Procedural Sun 程序化太阳 | WIP | Yes | Yes | — |
| Cloud Shadows 云影 | Yes | Yes | Yes | Yes |
| Skylighting 天空光照 | Yes | Yes | Yes | — |
| Sky Sync 天空同步 | Yes | No* | Yes | No |
| Volumetric Clouds 体积云 | WIP | No | WIP | No |
| Atmospheric Scattering 大气散射 | WIP | Yes | WIP | Yes |
| Custom weather system 自定义天气系统 | WIP | No | WIP | No |

## Terrain（地形）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Terrain Parallax 地形视差 | Yes | Yes | Yes | No |
| Terrain Blending 地形融合 | WIP | Yes | Yes | No |
| Terrain Shadows 地形阴影 | Yes | Yes | Yes | No |
| Terrain Helper | Yes | Yes | Yes | Yes |
| Terrain Variation 地形变化 | Yes | No | Yes | No |

## Actors（角色）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Skin Specular 皮肤高光 | WIP | Yes | Yes | — |
| Subsurface Scattering 次表面散射 | Yes | Yes | Yes | Yes |
| Hair Specular 头发高光 | Yes | No | Yes | No |
| Advanced Skin Shaders 进阶皮肤着色 | WIP | No | WIP | No |

## Objects（物体与材质）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Object Parallax 物体视差 | Yes | Yes | Yes | Yes |
| Physically Based Rendering PBR | Yes | No | Yes | No |
| Dynamic Cubemaps 动态立方体贴图 | Yes | Yes | Yes | Yes |
| Extended Translucency 扩展半透明 | Yes | No | Yes | No |
| Dynamic snow cover 动态积雪覆盖 | WIP | No | WIP | No |

## Screen effects（屏幕特效 / 后处理）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Depth of Field 景深 | WIP | Yes | n.a. | n.a. |
| Bloom 泛光 | WIP | Yes | Yes | Yes |
| HDR rendering HDR 渲染 | Yes | Yes | Yes | Yes |
| Eye Adaptation 眼睛适应 | WIP | Yes | Yes | — |
| Lens Effects 镜头特效 | WIP | Yes | WIP | — |
| Customizable Post-Processing 可自定义后处理 | WIP | Yes | WIP | Yes |
| Lut Loading LUT 加载 | WIP | Yes | WIP | Yes |
| Motion Blur 动态模糊 | WIP | Yes | WIP | Yes |
| HDR output HDR 输出 | WIP | No | WIP | No |

## Performance（性能）

| 功能 | CS | ENB | CS VR | ENB VR |
|------|:--:|:---:|:-----:|:------:|
| Upscaling Technologies 超分辨率 | Beta | No* | WIP | No* |
| FSR AA / DLAA | Yes | No* | Yes | No* |
| Framegen (DLSS) 帧生成 | Yes | No* | No | No* |

> 上表里 CS 一列大量 `Yes` / `WIP`、ENB 一列成片 `No` 的结构，正是官方对自身定位的表述：**CS 是在引擎层「补上游戏本身缺的东西」，ENB 是在游戏之上「注入一层后处理」**（ENB 在少数项目如 Depth of Field、Bloom、Normalmap Shadows 上仍领先，而这几项恰是 CS 标注 `WIP` 的领域）。

## 官方承认的潜在未来功能（依赖关系）

官方强调：**以下只是「潜在功能」的依赖图，不构成任何承诺或路线图**。它解释了为什么某些功能迟迟不来——它们在依赖链下游。

```
Deferred（延迟渲染地基）
├── Subsurface Scattering ──> Dynamic Snow Cover
├── SSGI ──> Skylighting
├── Better Water ──> Improved Water Lod
├── Better SSR
├── Terrain Blending
└── Tesselation ├──> Water
                └──> Tesselated Landscape

PBR ├──> Sparkly Snow
    ├──> Better Water
    ├──> Procedural Grass
    ├──> Skin Specular
    ├──> Linear Lighting
    └──> Dynamic Snow Cover

Image Based Lighting ──> TOD/Weather
Linear Lighting ──> TOD/Weather、Postprocessing
Sky Sync ──> TOD/Weather
Dynamic Snow Cover ──> TOD/Weather
Postprocessing ──> Motion Blur、Depth of Field、Bloom、TOD/Weather、Eye Adaptation

TOD/Weather ├──> Physical Sky
            ├──> Misc. Weather Elements
            ├──> Simple Height Fog
            ├──> Volumetric Fog/Clouds
            ├──> Procedural Sun
            └──> (Postprocessing)

Water Parallax ──> Better Water ──> Improved Water Lod

独立支线：Full Ray Tracing（完整光线追踪）
```

要读懂这张图的关键：**`Deferred`（延迟渲染重构）和 `TOD/Weather`（时间与天气系统重构）是两个巨型枢纽**。绝大多数「玩家呼声很高但一直 WIP」的功能（体积云、大气散射、自定义天气、后处理全家桶）都挂在它们下游。

## 相关条目

- 想直接看**玩家视角**的功能清单与下载入口，见 [功能总览](../02-features/core)。
- 想知道**哪些功能已并入核心、装旧版时该删什么**，见 [不兼容 MOD - 版本演进](../03-reference/incompatible-mods.md)。
- 想了解**当前版本号与支持策略**，见 [版本与支持策略](version-and-support.md)。
