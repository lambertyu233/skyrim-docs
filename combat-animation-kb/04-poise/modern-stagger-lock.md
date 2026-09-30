---
id: modern-stagger-lock
title: Modern Stagger Lock（MSLF）——踉跄动画框架
category: 04-poise
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [Modern Stagger Lock, MSLF, 踉跄动画, 框架, Maxsu]
aliases: [stagger lock, 踉跄框架, 硬直动画]
source: https://github.com/max-su-2019/ModernStaggerLock
summary: Maxsu 的踉跄动画框架：管踉跄动画的衔接与限制；触发逻辑交给 MaxsuPoise 等触发型 mod——两者是配套关系。
---

# Modern Stagger Lock（MSLF）——踉跄动画框架

## 一句话

它是一个**踉跄动画框架**而非触发逻辑 mod——让角色踉跄中能进入新的踉跄动画（可被注释限制），**踉跄的触发机制要由另一个 mod（如 MaxsuPoise）重新设计**。

## 关键定位（fkmods 说明，社区转述但准确）【社区经验】

> "MSLF 使得角色处于交错动画时，能够进入新的交错动画，但可以通过添加注释的方式对其进行限制……MSLF 本身只是一个交错动画框架，它需要另一个模组来重新设计《天际》的交错触发机制！"

**作者归属勘误：MSLF 的作者是 Maxsu（max-su-2019），不是 Dtry**【一手源，GitHub】。

## 基本事实【一手源】

- GitHub：[max-su-2019/ModernStaggerLock](https://github.com/max-su-2019/ModernStaggerLock)，SKSE 插件（SE/AE）。
- 代码更新至 **v1.1.7（2024-03-17，"Updated for new Precision API"）**。
- 是 [MaxsuPoise](./maxsu-poise.md) 的**硬性前置**（GitHub Release 原文 "Hard Requirements"）。
- Elden Rim 新版社区反馈也硬性要求它【一手源，ER Katana 页面回帖】。
