---
id: trainwreck
title: Trainwreck（备选崩溃日志器）
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [诊断, 崩溃日志, 备选, 排错]
aliases: [崩溃日志备选, 备选日志器, 日志器二选一]
source: https://phostwood.github.io/crash-analyzer/skyrim.html
summary: 另一个崩溃日志器：通常线索不如 Crash Logger SSE 丰富，但在其它日志器写不出日志的场景下有时能出结果——三者只能装一个。
---

# Trainwreck

## 它在工具链里的角色

**备选崩溃日志器**。Crash Log Analyzer 的官方页面把它列为
**"backup option for Skyrim SE or AE"**，并直接给出它的定位：

> 它**通常缺少重要线索**，但**有时**能在别的日志器无法产出日志的情况下写出日志。

所以它的用法很明确：**平时不用它，卡住时临时换它**。

## 三个日志器只能留一个（硬规则）

| 日志器 | 适用 | 说明 |
|---|---|---|
| **Crash Logger SSE** | SE / AE / VR | 首选，PDB 支持使地址可读 |
| **.NET Script Framework** | SE 生态（AE 不兼容） | 老配方，日志格式仍被分析器支持 |
| **Trainwreck** | SE / AE | 备选 |

> 官方页面原话意思：**"Only one crash logging mod may be used"**——
> 同时装多个，症状是**没有日志或日志不全**，而不是报错。

## 路径差异（一个容易白找的坑）

Phostwood 页面的排错清单特别指出：
**Crash Logger SSE 的日志落点比 Trainwreck 的落点高一层目录**——
按某个教程去找却找不到时，先换一层目录看看。

## 与本库其它条目

- [Crash Logger SSE](../09-diagnostics/crash-logger-sse.md)（首选）
- [Crash Log Analyzer（崩溃日志解读）](../09-diagnostics/crash-log-analyzer.md)（解读工具，两种格式都支持）
- [常见错误认知](../12-sources/common-misconceptions.md) 第 4 条
