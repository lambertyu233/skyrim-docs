---
id: consoleutil
title: ConsoleUtilSSE
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [前置, 脚本, 控制台, 依赖库]
aliases: [ConsoleUtilSSE, 24858, 脚本执行控制台, console command 脚本]
source: https://www.nexusmods.com/skyrimspecialedition/mods/24858
summary: 允许 Papyrus 脚本执行控制台命令的小型前置库，被一批需要"以脚本调用控制台"的 mod 依赖。
---

# ConsoleUtilSSE

## 是什么

Papyrus 原本**无法**执行控制台命令。ConsoleUtilSSE 暴露了这个能力，
于是脚本可以像玩家一样提交控制台指令——用于自动化调试、批量操作、
或实现那些只能在控制台达成的效果。

## 取舍

- **极小、无 UI、无配置**，属"装了就不管"的类型。
- 反过来，**依赖它的 mod 会因此获得"脚本注入控制台"的能力**——
  这在原则上是强能力，安装来源不明的 mod 时值得留意。
- 有 AE 支持，安装时按运行时版本选文件。

## 典型依赖者

社区指南里常见的组合安装清单（如 B.C.M. 一类整合教程）会把它与
PapyrusUtil、JContainers、po3 系插件、SPID 并列列为核心前置。
**它是否必需取决于你的 modlist 里有没有 mod 声明依赖它**——不必盲装，但很常见。

## 相关

- [powerofthree's Papyrus Extender](../01-frameworks/po3-papyrus-extender.md)
- [PapyrusUtil SE](../01-frameworks/papyrusutil.md)
- [More Informative Console](../09-diagnostics/more-informative-console.md)（同样是控制台相关，但用途是排错）
