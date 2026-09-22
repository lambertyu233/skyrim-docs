---
id: sse-display-tweaks
title: SSE Display Tweaks
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [性能, 显示, 帧率, 垂直同步, 高刷新率]
aliases: [SSE Display Tweaks, Display Tweaks, 高刷, 解锁帧率, 34705, 卡顿]
source: https://www.nexusmods.com/skyrimspecialedition/mods/34705
summary: 接管「OS ↔ 显示」这一层：帧率上限、垂直同步、刷新率、无边框窗口等；高刷屏与手持设备上体感差异最大的一个性能向插件。
---

# SSE Display Tweaks

Nexus：`skyrimspecialedition/mods/34705`。
官方描述口径：**修正并改进操作系统与显示之间的交互**。

## 它解决什么

原版启动器对**帧率上限、垂直同步、刷新率**的控制极其粗糙，
导致两类问题：

- **高刷屏**：无法真正跑满，或帧生成节奏不稳 → 微卡顿；
- **掌机 / 低功耗设备**：做不到"锁定 40/45 FPS 这种比波动 60 更顺"的策略。

SSE Display Tweaks 把这些控制交给 ini，可精确设定帧率上限、
垂直同步行为、无边框全屏等。

## 为什么常与物理 mod 一起提

Skyrim 的**物理与部分引擎逻辑依赖帧率**。因此：

- 解锁帧率前要确认物理方案能不能适配（HDT-SMP / CBPC 这类）
  → [骨骼与物理](../../character-appearance-kb/04-physics/)；
- 出现"解锁帧率后物理乱飞 / 卡顿"时，先怀疑帧率相关设置，而不是物理 mod 本身。

## 装法与注意

- 属 SKSE 插件；**安装前先阅读发布页的 ini 说明**——
  这类显示设置高度依赖你的显示器与硬件，没有通用最佳值。
- 与游戏内/启动器的显示设置可能**互相覆盖**：改完一处要确认另一处没被写回。
- 属"装了看得到效果"的性能向插件，不需要额外前置（除 SKSE 系）。

## 与其它性能向工具的边界

| 工具 | 管什么 |
|---|---|
| **SSE Display Tweaks** | 帧率/同步/刷新率（OS ↔ 显示） |
| **SSE Engine Fixes** | 引擎崩溃与内存 |
| **Papyrus Tweaks NG** | 脚本调度（[Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md)） |
| **xLODGen / DynDOLOD 档位** | 远景渲染负担（`06-lod/`） |

## 相关

- [SSE Engine Fixes](../09-diagnostics/sse-engine-fixes.md)、[Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md)
- `community-shaders-kb/`（画质与着色器侧的性能话题）
- [骨骼与物理](../../character-appearance-kb/04-physics/)（帧率与物理的耦合）
