---
id: skse-plugin-dev
title: SKSE 插件开发
category: 05-tools
version: 1.0.0
updated: 2026-09-20
tags: [skse, cpp, plugin, plugin-abi, engine]
source: https://ck.uesp.net/wiki/SKSE_Plugin_Development/What_Is_SKSE
summary: SKSE（Skyrim Script Extender）用 C++ 扩展引擎能力；插件开发涉及 ABI、调用 Papyrus 函数与跨版本兼容。
status: stable
kind: reference
---

# SKSE 插件开发

**SKSE（Skyrim Script Extender）** 是一个在官方 Creation Kit 之外，用 **C++** 扩展《天际》引擎能力的框架。它让 MOD 能读写引擎内部数据、新增原生函数、与 Papyrus 双向通信。

## 什么是 SKSE

- 一个注入式扩展层，随游戏启动加载。
- 为 Papyrus 提供大量额外函数（如 `SKSE` 相关的存储、输入、UI 接口）。
- 允许开发者编写**插件（Plugin）**，以 C++ 实现复杂逻辑。

## 为什么需要它

- CK 与 Papyrus 的能力有边界；涉及内存、文件、底层对象操作时必须借助 SKSE。
- 很多流行 MOD（装备/库存/界面增强）依赖 SKSE 插件。

## 插件开发要点

| 主题 | 说明 |
| --- | --- |
| **Plugin ABI** | 插件须遵循 SKSE 的 ABI 约定，错误版本会导致崩溃。 |
| **Calling Papyrus Functions** | 插件可反向调用 Papyrus 函数，实现 C++ ↔ 脚本通信。 |
| **Creating New Methods for Forms** | 为 Form 类型挂载新的原生方法。 |
| **Getting Specific Forms** | 从插件侧按 Form ID 取回游戏对象。 |
| **Iterating all Actors/NPCs** | 遍历世界中全部 Actor 做批量处理。 |
| **Resources / Why Game Updates Break Everything** | 游戏更新会改变内存布局，导致插件失效——需随 SKSE 更新重新编译。 |

> SKSE 插件的稳定性高度依赖游戏版本；游戏大更新后插件常需等待 SKSE 团队更新 ABI。

## 入门路径

1. [What Is SKSE](https://ck.uesp.net/wiki/SKSE_Plugin_Development/What_Is_SKSE) → 2. [Getting Started](https://ck.uesp.net/wiki/Getting_Started_with_SKSE_Plugin_Development) → 3. 阅读 Plugin ABI 与各专题页。

## 相关条目

- [Papyrus 脚本概览](04-scripting/papyrus-overview.md)
- [Archive.exe 打包](02-features/archive-exe.md)

> 来源：[UESP SKSE Plugin Development](https://ck.uesp.net/wiki/SKSE_Plugin_Development)
