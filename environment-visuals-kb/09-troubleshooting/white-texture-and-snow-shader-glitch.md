---
id: white-texture-and-snow-shader-glitch
title: 白块纹理 glitch 与雪着色器冲突
category: 09-troubleshooting
version: 1.0.0
updated: 2026-10-22
tags: [白块, glitch, 雪, Simplicity of Snow, BDS, 排错]
kind: tutorial
source: https://www.nexusmods.com/skyrimspecialedition/mods/2347
summary: 202X 白块 = 雪着色器冲突，官方解法 Simplicity of Snow；另记 MM 的灰/黑山体与 SSE Engine Fixes 冲突两组高频症状。
aliases: [白纹理, white glitch, better dynamic snow, 灰山]
---

# 白块纹理 glitch 与雪着色器冲突

## 202X 白块（一手源：Nexus 2347 files 页）

- 作者原话：**"White texture glitch is a snow shader conflict,
  Simplicity of snow fixes it"**。
- 同页：**"Not compatible with BDS 3.X"**（Better Dynamic Snow 3.x）——
  看到白块先查这两个。
- 位置：Whiterun 视差网格文件说明里，但根因是雪着色器，不限于 Whiterun。

## MM 灰/黑/白山体（一手源：Nexus 11052 readme）

- **灰/白**：`MajesticMountains.esp` 被禁用或位置过低，雪材质设置被其它 mod 恢复；
  且**必须重跑 DynDOLOD**。
- **黑**：重装通常解决。
- **夜间岩石/山体发光**：关游戏雪着色器（用 Better Dynamic Snow 或
  整体发光时）。
- **雪花色不对**：weather mod 与 MM 的顺序——LOOT 常把天气放下面，需手调。
- **SSE Engine Fixes 冲突**：`skse/plugins/EngineFixes.ini` 设
  `BSLightingShaderForceAlphaTest = false`。

## 一般"贴图不对"排查顺序（社区经验）

1. 该贴图被谁覆盖？MO2 里看冲突列表，确认赢家是你想要的包。
2. 该网格指向的贴图路径是否被改（换 mesh 的 mod 会把 UV 指到别处）。
3. 是否 LOD 未重生成（远景与近景不一致）。
4. 是否雪/天气着色器在改同材质。

## 相关

- [Majestic Mountains](../03-landscape/majestic-mountains.md)
- [视差异常排错](parallax-artifacts.md)
