---
id: skyrim-202x
title: Skyrim 202X（Pfuscher）
category: 02-textures
version: 1.0.0
updated: 2026-10-22
tags: [202X, 材质, Pfuscher, 视差, 高清]
kind: reference
source: https://www.nexusmods.com/skyrimspecialedition/mods/2347
summary: 最大规模的高分辨率材质工程：约 2200 个文件分三部分发布，v10.5.2（2025-07），视差地形单独配套，4K 全量需 8GB+ 显存。
aliases: [Skyrim 202X, Skyrim 2020, Skyrim 2020 Parallax, 2020视差]
---

# Skyrim 202X（Pfuscher）

- **作者**：Pfuscher（一手源：Nexus 2347）
- **Nexus**：skyrimspecialedition/mods/**2347**；2016-11 上传，当前 **v10.5.2**
  （2025-07-30/31 更新）
- **规模**：约 2200 个文件；下载量 2200 万+（一手源：files 页）

## ⚠️ 页面改名史（排错高频）

中文教程常写"**Skyrim 2020 Parallax**"——那是 **LE** 时代与 SE 旧页（2777）的名字。
**SE 现行页面是 "Skyrim 202X by Pfuscher"（2347）**，旧页已被取代。
找不着"2020 Parallax SE"不是被下架，是改名了。详见
[过时与改名页面](../10-sources/outdated-pages-and-renames.md)。

## 结构（一手源：files 页）

- **三部分**：Part I Landscape（约 4.3GB）/ Part II Architecture（约 9.2GB）/
  Part III Other（约 10.8GB）——4K/8K 拆分控制体积，**必须按作者顺序装**。
- **Skyrim 2018**：主文件前置依赖（作者强烈建议）。
- **Bugfixes 1.5 + 1.6**：同页安装。
- **Parallax Meshes - Whiterun / - Riften Ground**：complex parallax 网格
  （Whiterun 的视差**必须**装网格；其它区域用各自的 mesh mod）。
- 可选：Whiterun Street/City Wall Alternative、Snow alternative、
  Blended Roads Retexture、7 Mountain Textures（无 parallax）。

## 视差依赖（一手源：发布页）

"To see the parallax effect, download the latest ENB version for Skyrim SE
**Or Community Shaders**"——没这两者视差不显示。地形视差另有
"Skyrim 2020 Terrain Parallax / Complex Terrain Parallax"配套。

## 兼容性与坑（均一手源：发布页/files 页）

- **SMIM 视为扩展，直接覆盖**。
- **Blended Roads 是"life like roads"必备**。
- ELFX：让 202X 覆盖 ELFX；与 Lux 兼容。
- **不兼容 Better Dynamic Snow 3.x**（文件页注明）。
- **白块贴图 glitch = 雪着色器冲突，用 Simplicity of Snow 修**（作者原话）。
- 早期需要 "SSE Parallax Shader Fix"，有 ENB 后不再需要。
- 崩溃/卡顿/低帧先查 "enbsettings, vram and allocation"（LE 页原话）。
- 支持 1.6.1170 / 1.6.640 / 1.5.97 与 VR（二手转述：mythiq，以 Nexus 页为准）。

## 显存（社区经验 + 二手源）

全 4K 建议 **8GB+ 显存**；作者提供 2K 降级版（202X Downscale Mod）。
显存不足症状是 stutter 而非警告——见[VRAM 预算](../01-principles/vram-and-enboost.md)。

## 相关

- [视差原理](../01-principles/parallax-and-complex-material.md)
- [材质包选型](../02-textures/texture-pack-selection.md)
