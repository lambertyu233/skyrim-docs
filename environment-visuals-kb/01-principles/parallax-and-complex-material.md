---
id: parallax-and-complex-material
title: 视差与 Complex Material 原理
category: 01-principles
version: 1.0.0
updated: 2026-10-22
tags: [视差, parallax, complex material, 原理, 着色器]
kind: concept
source: https://modding.wiki/en/skyrim/developers/complex-parallax-materials
summary: Skyrim 视差靠 ENB/CS 着色器实现：地形视差把高度图塞进地表 alpha，Complex Material 用环境遮罩四通道承载 glossiness/金属度/视差。
aliases: [地形视差, complex parallax, POM, 高度图]
---

# 视差与 Complex Material 原理

## 一句话

视差（parallax）是法线贴图的进阶：**法线只骗光照，视差真的扭曲纹理本身**——
表面看起来有真实凹凸和深度（一手源：Hein84 的 Vivid Landscapes 页面释义：
"the depth-information doesn't get simply drawn on the surface, it rather warps
the texture itself in the desired direction"）。

## 依赖链（这是排错的关键）

Skyrim **原生不支持**地形视差，必须叠一层：

- **ENBSeries**（`enbseries.ini` 的 `[EFFECT]` 段开启
  `EnableTerrainParallax` / `EnableComplexParallax`，一手源：modding.wiki）；或
- **Community Shaders**（Extended Materials 功能，实现 Contact Refinement
  Parallax Mapping，CRPM，作者自测约 0.22ms 开销，一手源：modding.wiki
  CS Extended Materials 页）。

**没有 ENB/CS 就没有视差**。装了视差材质却看不到效果，99% 是这条链断了。

## 地形视差（Terrain Parallax）

- 高度图放在**地表漫反射贴图的 alpha 通道**里。
- **亮度 127 = 平坦**（不产生偏移，但仍参与计算；不是"关闭"开关）。
  （一手源：modding.wiki Complex Material 指南）

## Complex Material（网格视差 + PBR 化）

ENB 把**环境遮罩贴图（environment mask）**的四个通道重新定义：

| 通道 | 内容 |
|---|---|
| R | 环境贴图遮罩（同原版语义） |
| G | glossiness 光泽度图（暗=更光滑的镜面；粗糙度图**取反**即可得到） |
| B | metallic 金属度图（255=全金属，0=非金属） |
| A | parallax 高度图（255=平坦且不计算；与地形视差的 127 规则不同） |

坑（一手源，modding.wiki）：

- **G 通道 ≤4/255 的值会被当成黑色，直接禁用 complex material**——
  这是压缩精度问题，写通道图时注意 grayscale 2.2。
- 金属观感强依赖 ENB 预设的 `[ENVIRONMENT] COLOR POW` 变量。
- 皮肤着色器只支持 G 通道 glossiness（R 仍是原版 specular）。

## 配套工具链（社区经验，Nexus 125527）

- **Auto Parallax**：给视差网格自动打标记，防止"无对应贴图的视差网格"出现**蓝块**。
- **ParallaxGen**：批量给既有材质生成视差贴图并修补网格；每次增删网格/贴图后需重跑。
- **Terrain Parallax Blending Fix**：修地形视差与地表混合的接缝。
- **SSE Parallax Shader Fix**（aers / shadowking97）：修原版视差着色器 bug；
  Community Shaders 的 Extended Materials 出现后其必要性下降。

## 与其它条目的关系

- 视差版材质包选哪个 → [Skyrim 202X](../02-textures/skyrim-202x.md)、
  [Vivid Landscapes](../02-textures/vivid-landscapes.md)、[Skyland AIO](../02-textures/skyland-aio.md)。
- 视差异常排错 → [视差异常排错](../09-troubleshooting/parallax-artifacts.md)。
- 渲染框架侧 → `community-shaders-kb` 的 Extended Materials 条目。
