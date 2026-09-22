---
id: privateprofile-redirector
title: PrivateProfileRedirector SE（INI 读取加速）
category: 11-config
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [配置, INI, 性能, 启动加速, SKSE]
aliases: [PrivateProfileRedirector, PPR, 18860, ini 缓存, 启动慢, 加载加速]
source: https://www.nexusmods.com/skyrimspecialedition/mods/18860
summary: 缓存游戏对 INI 文件的读取，修正一处 INI 加载缺陷；效果是「装了几百个 mod 之后启动变快」，本身没有可见功能。
---

# PrivateProfileRedirector SE

Nexus：`skyrimspecialedition/mods/18860`，作者 **Karandra**
（来源：整合包清单的权威标注）。

## 它做什么

游戏在运行中会**反复读取 INI 文件**，这在 mod 很多时成为可观的启动/加载开销。
本工具对这类读取做缓存（社区描述为 "INI file cacher"），
并修正一处与 INI 配置加载相关的引擎问题。

**特征**：属"装了看不出变化，但启动更快"的一类——
不产生 UI、不产生日志噪音。

## 什么时候值得装

- modlist 规模大（几百个 mod）、体感**启动明显变慢**；
- 想减少磁盘上的重复小文件读取（放在机械盘或网络盘上时收益更明显）。

单装几个 mod 的用户通常感受不到差别。

## 与其它 INI 相关工具的边界

| 工具 | 层面 |
|---|---|
| **BethINI** | INI 的**内容**（整理、纠错、预设）→ [BethINI（INI 配置优化）](../11-config/bethini.md) |
| **PrivateProfileRedirector** | INI 的**读取性能**（本条目） |
| **各 mod 的 ini** | 独立配置，落点在 `Data/SKSE/Plugins/` 或 Overwrite → [配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md) |

三者互不冲突，可以同时存在。

## 相关

- [BethINI（INI 配置优化）](../11-config/bethini.md)、[配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md)
- [SSE Engine Fixes](../09-diagnostics/sse-engine-fixes.md)（另一类"减少无谓开销"的修复）
- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)（Overwrite 与 ini 归位）
