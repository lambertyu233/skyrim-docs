---
id: crash-logger-sse
title: Crash Logger SSE
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [诊断, 崩溃日志, SKSE, 排错, 必备]
aliases: [Crash Logger, Crash Logger SSE, crash log, 59818, 崩溃记录, 抓日志]
source: https://github.com/alandtse/CrashLoggerSSE
summary: 现行最通用的崩溃日志器（AE/VR）：在游戏崩溃时写出可读日志，配合 PDB 能把地址还原成函数与 mod 归属，是排错的第一块砖。
---

# Crash Logger SSE

## 官方定位（仓库 README）

> **"SKSE/SKSEVR plugin that generates crash logs when the game Just Works™."**

即：一个 SKSE 插件，崩溃时把可读信息写到日志。它支持 **AE 与 VR**
（README 里的 "AE Version / VR Version" 两栏）。

## 前置（官方 Requirements）

- **Address Library for SKSE**（AE 用）
- **VR Address Library for SKSEVR**（VR 用）

## 日志在哪

Phostwood 的分析器页面给出的路径是：

```
[我的文档]\My Games\Skyrim Special Edition\SKSE
```

文件名带时间戳，形如 `crash-2026-01-21-10-20-23.log`。
**注意**：Crash Logger SSE 的日志比 Trainwreck 的**上一层目录**——
找不到日志时这是第一个要核对的地方。

## 关于 PDB（为什么它的日志更好读）

仓库把 **PDB 打包成单独的 FOMOD 归档**分发，并有专门的
`diaprobe` 工具做符号解析检查。带符号时，日志里的地址能被还原成**函数名**，
进而指向具体是哪个插件/mod 出的问题——这是"能读"与"只能看地址"的分界。

## 纪律：**只能装一个崩溃日志器**

官方分析器页面明确：

> **"Only one crash logging mod may be used, so be sure to remove or disable
> all other crash logging mods."**

也就是说 **Crash Logger SSE / Trainwreck / .NET Script Framework 三者不能共存**。
同时装的典型症状是"没有日志""日志残缺"或干脆更早崩溃。

## 版本兼容

- 仓库的活动分支持续跟进游戏运行时（release note 里可见
  "support Skyrim AE 1.7.99" 一类条目，以及 `__fastfail` / fail-fast 异常的 VEH 记录等改进）。
- **引用版本号请以 Releases 页为准**——它在持续更新。

## 配套工具

- [Crash Log Analyzer（崩溃日志解读）](../09-diagnostics/crash-log-analyzer.md)：把日志翻成人话（强烈建议配合使用）。
- [SSE Engine Fixes](../09-diagnostics/sse-engine-fixes.md)：修掉一批"根本不进日志器"的崩溃。
- [More Informative Console](../09-diagnostics/more-informative-console.md)：游戏内反查物品/对象来源。

## 相关

- [Address Library for SKSE Plugins](../01-frameworks/address-library.md)、[CommonLibSSE-NG（插件开发框架）](../01-frameworks/commonlibsse-ng.md)
- [常见错误认知](../12-sources/common-misconceptions.md) 第 4 条
