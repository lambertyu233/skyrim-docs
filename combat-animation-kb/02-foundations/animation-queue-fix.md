---
id: animation-queue-fix
title: Animation Queue Fix——动画队列过载修复
category: 02-foundations
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [Animation Queue Fix, 队列, T-Pose, Ersh, 修复]
aliases: [AQF, 动画队列, 进图加载慢, tpose 修复, 动画加载慢]
source: https://github.com/ersh1/AnimationQueueFix
summary: Ersh 的修复插件：解决 DAR/OAR 大量动画同时入队导致的加载慢与 T-Pose——OAR 官方 Requirements 之一。
---

# Animation Queue Fix——动画队列过载修复

## 一句话

Nexus 描述原文："Fixes the queue getting overloaded when a lot of animations are queued for loading at the same time."——游戏同一时刻只允许一个动画"排队"加载且两个负责函数不同步；本插件让第二个函数紧跟第一个执行。

## 为什么装动作包要装它（作者原话）【一手源】

> "The issue isn't normally visible in the vanilla game… This slow loading issue only starts to show up when you have a lot of animations added by plugins like Dynamic Animation Replacer or Open Animation Replacer."

即：原版看不出来，装了 DAR/OAR 后大量动画突然进队列才暴露——表现为**进图动画加载慢、偶发 T-Pose**。OAR 的 Nexus Requirements 直接要求它（除非启用"跳过动画预加载"实验性设置）。

## 基本事实【一手源】

- 作者 Ersh（ersh1），GitHub：[ersh1/AnimationQueueFix](https://github.com/ersh1/AnimationQueueFix)，Nexus [mods/82395](https://www.nexusmods.com/skyrimspecialedition/mods/82395)，v1.0.1（2023-01-10）。
- 要求 SKSE + Address Library；作者原话 "compatible with any non-ancient Skyrim version, including **1.5.97, 1.6+ and VR**"；无 LE 版（作者："It's really time to move on."）。

## 相关条目

[OAR 生态定位](./behaviour-engine-choice.md) · [装完动作包的刷新流程](../08-compatibility/install-workflow.md)
