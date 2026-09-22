---
id: po3-papyrus-extender
title: powerofthree's Papyrus Extender
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [前置, 脚本, 函数扩展, powerofthree, 依赖库]
aliases: [Papyrus Extender, po3 Papyrus Extender, 22854, 扩展函数, PO3PE]
source: https://www.nexusmods.com/skyrimspecialedition/mods/22854
summary: 给 Papyrus 追加两百多个原生函数的 SKSE 插件——现代脚本 mod 的常用依赖，把"游戏做不到的事"变成一行脚本调用。
---

# powerofthree's Papyrus Extender

## 是什么

在 Papyrus 里新增**数百个原生函数与若干事件**（社区常见描述为 "over 200 / 275 additional functions"，
数字随版本增长，**以发布页为准**）。它本身不产生游戏内容，
但大量现代脚本 mod 声明依赖它——因为它们想要的功能（更细的检测、更直接的对象操作）
原生 Papyrus 给不了。

> 作者 powerofthree 的另一件作品 **powerofthree's Tweaks** 是引擎修复类，
> 与本文不是同一个 mod：Tweaks 见 [powerofthree's Tweaks（引擎修复与调整）](../09-diagnostics/po3-tweaks.md)。
> **两者名字相似、用途完全不同，且常被同时安装。**

## 安装

- SKSE 插件（`Data/SKSE/Plugins/`），**有 AE 专用文件**——按运行时版本选。
- 需要 Address Library。
- 无 UI；装了没变化是正常的。

## 属于"生态黏合剂"这一层

这一类工具（Papyrus Extender、PapyrusUtil、JContainers、ConsoleUtil、SPID）
共同构成 modlist 的**依赖底座**：它们自己不提供内容，却是别人能工作的前提。
管理它们的办法只有一个：**看每个 mod 页面的 Requirements 段**，
不要凭"我已经装了类似的"来省略。

## 常见症状

| 症状 | 原因 |
|---|---|
| 某 mod 报找不到函数 / 静默失效 | Papyrus Extender 未装或版本过老 |
| 装了 AE 版却仍报错 | 游戏是 1.5.97 降级版，应装 SE 版文件 |
| 与其他 po3 插件冲突 | 通常不是冲突，而是**配置 INI 在 Overwrite 里**没归位 → 见 [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md) |

## 相关

- [powerofthree's Tweaks（引擎修复与调整）](../09-diagnostics/po3-tweaks.md)（同名作者，不同用途）
- [Spell Perk Item Distributor (SPID)](../02-distribution/spid.md)（作者同一位，分发类）
- [PapyrusUtil SE](../01-frameworks/papyrusutil.md)、[JContainers SE](../01-frameworks/jcontainers.md)、[ConsoleUtilSSE](../01-frameworks/consoleutil.md)
