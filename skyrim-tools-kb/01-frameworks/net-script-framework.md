---
id: net-script-framework
title: .NET Script Framework
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [前置, .NET, 脚本框架, 崩溃日志, 遗留]
aliases: [NET Script Framework, dotnet script framework, .net sf, 21294, 崩溃日志旧格式]
source: https://www.nexusmods.com/skyrimspecialedition/mods/21294
summary: 用 C# 给游戏挂载运行时逻辑的框架，同时提供了 SE 时代最可读的一代崩溃日志；对 AE 的兼容性已断裂，新环境请优先用 Crash Logger SSE。
---

# .NET Script Framework

## 两个身份

1. **运行时框架**：让 C# 程序在游戏进程里跑，提供事件钩子与对象访问。
   历史上不少功能型 mod 依赖它。
2. **崩溃日志器**：它生成的 log 是 SE 时代**可读性最好**的一代（带托管调用栈与 mod 归属），
   至今仍是 Crash Log Analyzer 支持的三种日志格式之一。

## 兼容性现状（关键）

- 面向 **Skyrim SE 1.5.97** 生态设计；**在 AE（1.6+）上不可用/不兼容**是社区共识。
  （Nexus Mods 上的常见表述为 "mentioned as incompatible with AE"）
- 因此现代 AE 环境的标准组合是：
  **Crash Logger SSE**（日志器）+ **CommonLibSSE-NG**（开发框架），而不是 .NET SF。

## 什么时候还会遇到它

- 你在看一份**老教程**，它让你装 `.NET Script Framework` 来获得崩溃日志 →
  在 AE 上应改为 **Crash Logger SSE**（见 [Crash Logger SSE](../09-diagnostics/crash-logger-sse.md)）。
- 你在看一份 **SE 1.5.97 降级版 modlist**（很多中文整合包仍是 1.5.97），
  此时 .NET SF 仍是可用的，且它的日志格式被 Crash Log Analyzer 原生支持。
- 你的 modlist 里有明确声明依赖它的老 mod。

## 与 DLL Plugin Loader 的关系（易错点）

社区流传的"装了 .NET SF 还要装 DLL Plugin Loader"是**老配方**。
**SSE Engine Fixes 已包含 DLL Preloader 的替代实现，两者同时装会出问题**——
只保留一个。（来源：B.C.M. 等整合指南的安装说明，属社区经验）

## 相关

- [Crash Logger SSE](../09-diagnostics/crash-logger-sse.md)：AE 时代替代方案
- [Crash Log Analyzer（崩溃日志解读）](../09-diagnostics/crash-log-analyzer.md)：支持三种日志格式（含 .NET SF）
- [SSE Engine Fixes](../09-diagnostics/sse-engine-fixes.md)：DLL Preloader 的归属问题
