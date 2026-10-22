---
id: ini-and-display-settings
title: 游戏 INI 显示设置（STEP 口径）
category: 08-practices
version: 1.0.0
updated: 2026-10-22
tags: [INI, 显示, STEP, BethINI, View Distance]
kind: tutorial
source: https://stepmodifications.org/wiki/SkyrimSE:2.0.0
summary: STEP 推荐的显示/视野距离/贴图细节值：Grass Fade 18000、Light Fade 50000、Flickering Light 8192、uGridsToLoad 永不动、水 SSR 0.5。
aliases: [显示设置, skyrim.ini, 视野距离, uGrids, grass fade]
---

# 游戏 INI 显示设置（STEP 口径）

> 均为**社区经验级**（STEP 指南推荐值），非引擎硬限；配合 BethINI 使用。

## View Distance（一手源：STEP wiki）

- **Grass Fade = 18000**（最大）
- **Light Fade = 50000**（最大）
- **Flickering Light = 8192**
- **`uGridsToLoad` 永远保持原版 5**——STEP 原话 "should never been changed
  from vanilla's default of 5"（改它=崩溃与脚本错乱的经典来源）。
- 其余 Fade 值看机器。

## Detail / Visuals（一手源：STEP wiki）

- 水面反射：全选**除了 Sky**（反射天空会加重 LOD 水缝）。
- Particles = 4500（约两倍原版）。
- Depth of Field 开；Lens Flare / Anamorphic Lens Flare 可关。
- **Improved Shader 关掉**（MM 自带自定义 INI 改 Sparkles 与 Improved Snow Shader）。
- Project UV Diffuse Normal 开。
- 用 Cathedral Landscapes 时 Grass 项无需再调（其 ini 已含默认）。

## Custom（一手源：STEP wiki）

- `fWaterSSRIntensity=0.5`（修 SSR 在水面的一道线）。
- `uMaxSkinDecals` / `uMaxSkinDecalsPerActor` = 100；
  `iMaxDecalsPerFrame` / `iMaxSkinDecalsPerFrame` = 200。
- `fBookOpenTime=500`（翻书加速，可选）。

## 草地（一手源：各草 mod 页）

- `[GRASS] iMaxGrassTypesPerTexure` 与 `iMinGrassSize` 见
  [草地 INI 设置](../04-flora/grass-ini-settings.md)——**以草 mod 作者值为准**。

## 风（社区经验：sinitar 指南）

- `[Display] fWindGrassMultiplier`：3.5/7/11 实验，加大草摆。

## 纪律（社区经验）

- 改 ini **一次改一段，进游戏测一次**——出问题能回滚定位。
- MO2 用户的 ini 在 profile 里，别直接改 Documents 下的。

## 相关

- [草地 INI 设置](../04-flora/grass-ini-settings.md)
- [VRAM 与 ENBoost](../01-principles/vram-and-enboost.md)
- ENB 的 ini 体系另见 [ENB 预设与 CS 衔接](enb-presets-and-cs-bridge.md)
