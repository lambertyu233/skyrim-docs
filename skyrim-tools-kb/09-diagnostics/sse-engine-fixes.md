---
id: sse-engine-fixes
title: SSE Engine Fixes
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [稳定性, 引擎修复, 必备, 内存, 崩溃]
aliases: [SSE Engine Fixes, Engine Fixes, 17230, 内存补丁, preloader, 减少崩溃]
source: https://www.nexusmods.com/skyrimspecialedition/mods/17230
summary: 修 SSE 引擎自身缺陷的必备插件（aers）：内存分配、文件处理、随机崩溃等；分两部分安装，Part 2 必须手动放进游戏根目录。
---

# SSE Engine Fixes

Nexus：`skyrimspecialedition/mods/17230`，作者 **aers**（来源：整合包清单的权威标注）。
社区口径里它是**最有价值的一个稳定化 mod**——修的是**引擎自身**的问题，
而非某个玩法系统的 bug。

## 两部分，装法不同（这是最容易出错的地方）

| 部分 | 内容 | 装到哪 |
|---|---|---|
| **Part 1** | `(Part 1) SSE Engine Fixes for 1.#.###` | **用 mod 管理器安装**（含 skse 插件与配置） |
| **Part 2** | `Engine Fixes - skse64 Preloader and TBB Lib` | **手动解压到游戏 EXE 所在目录**（不是 `Data\`） |

> Part 2 必须在**游戏根目录**；只装 Part 1 会出现"配置项不生效/部分功能缺失"。
> 这与 SKSE64 的装法类似（loader/DLL 放根目录），是本库反复出现的同一个坑。

## 与 DLL Plugin Loader / .NET Script Framework 的冲突

社区流传的老配方是"装 .NET Script Framework 还要配 DLL Plugin Loader"。
**SSE Engine Fixes 自身包含 DLL Preloader 的替代实现**，
**两者同时装会出问题**——只保留一个。（社区经验，来自多份整合指南的安装说明）

## 版本匹配

- 必须选**与游戏运行时版本对应**的文件（下载页会按版本分栏）。
- 与 SKSE64、Address Library 一样，属于"版本错 = 症状诡异"的一类。

## 与其它稳定化工具的分工

| 工具 | 层次 |
|---|---|
| **SSE Engine Fixes** | 引擎级：内存、文件、崩溃 |
| **Scrambled Bugs** | 玩法/机制层的引擎 bug 与补丁 |
| **Bug Fixes SSE** | 一批具体的引擎函数 bug |
| **Papyrus Tweaks NG** | 脚本引擎调度 |
| **Powerofthree's Tweaks** | 其它未被覆盖的修复与可选调整 |

**它们不互相替代**，多数整合包会同时带上好几个。

## 相关

- [Scrambled Bugs](../09-diagnostics/scrambled-bugs.md)、[Bug Fixes SSE](../09-diagnostics/bug-fixes-sse.md)
- [Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md)、[powerofthree's Tweaks（引擎修复与调整）](../09-diagnostics/po3-tweaks.md)
- [Crash Logger SSE](../09-diagnostics/crash-logger-sse.md)（修不掉的崩溃才去读日志）
- [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)（同样的"根目录 vs Data"坑）
