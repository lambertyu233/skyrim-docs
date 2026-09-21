---
id: requirements
title: 前置需求与支持的版本
category: 01-installation
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 前置, 需求, 版本支持]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: OAR 需要 SKSE + Address Library；未开启"跳过预加载动画"实验开关时还需要 Animation Queue Fix，配对动画注释要靠 Paired Animation Improvements。
---

# 前置需求与支持的版本

## 用户侧前置（官方清单）

| 前置 | 说明 |
| --- | --- |
| **SKSE** | Skyrim Script Extender，必须与你的游戏版本匹配 |
| **Address Library for SKSE Plugins** | SSE/AE 必需（按游戏版本提供地址映射） |
| **VR Address Library for SKSEVR** | **仅 VR** 需要 |
| **Animation Queue Fix** | **仅当你没有启用**"跳过预加载动画"这一实验性设置时才需要 |
| **Paired Animation Improvements** | 让**配对动画（paired animations）**内部的注释（annotations）正常工作 |
| 最新 **Visual C++ 可再发行组件** | 官方需求区列出的站外需求 |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（Requirements）

## 支持的游戏版本

- 与**任何非远古的** Skyrim 版本兼容，包括 **1.5.97、1.6+ 与 VR**。
- 官方 FAQ 里对 SE/AE/VR 的回答是简单的 **"Yes."**

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（Compatibility / FAQ）

## 传奇版（LE）——不支持，且作者不打算支持

官方 FAQ 原文大意：

> 抱歉，不行。SE 的引擎稳定得多，像 CommonLibSSE 这样的框架让实现高级插件容易太多。**真的、真的**是时候往前走了。不过如果你愿意挑战，欢迎自己把它移植到 LE——我更愿意把时间花在别的事情上，而不是支持一个糟糕得多、而且到现在已经离谱过时的游戏版本。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（FAQ）

## 依赖的传递关系

```
SKSE ──> Address Library ──> OAR
                       └──> Detection Plugin / Math Plugin / IED Conditions …
Animation Queue Fix ──────> OAR（仅在关闭"跳过预加载"时）
Paired Animation Improvements ──> OAR（配对动画注释）
Immersive Equipment Displays / Simple Dual Sheath ──> IED Conditions
```

## 配套插件的前置差异

| 插件 | 额外前置 |
| --- | --- |
| **Detection Plugin** | 无（只要 OAR 本体） |
| **Math Plugin** | 无（只要 OAR 本体） |
| **IED Conditions** | **Immersive Equipment Displays ≥ 1.7.1** 或 **Simple Dual Sheath ≥ 1.5.3**（按你用的动画替换器要求）；技术上不强制依赖，但**找不到对应插件时它那批条件就不会提供给 OAR** |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/104806>、<https://www.nexusmods.com/skyrimspecialedition/mods/98308>

## 相关

- [安装与 ini 配置](install-and-config.md)
- [兼容性 FAQ](compatibility-faq.md)
- [插件生态](../06-plugins/plugin-api.md)
