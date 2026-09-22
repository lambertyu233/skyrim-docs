---
id: crash-log-analyzer
title: Crash Log Analyzer（崩溃日志解读）
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [诊断, 崩溃日志, 在线工具, 排错, 解读]
aliases: [Crash Log Analyzer, CLA, 崩溃日志分析, crash analyzer, 读日志, Phostwood, QLP]
source: https://phostwood.github.io/crash-analyzer/skyrim.html
summary: 把崩溃日志喂进去、输出「可能原因 + 排查步骤」的在线分析器；支持三种日志格式，并会给出该修哪个 mod 的建议。
---

# Crash Log Analyzer

> 作者 Phostwood 的官方站：`phostwood.github.io/crash-analyzer/skyrim.html`。
> 用**浏览器打开、上传日志、读报告**，不需要安装。

## 支持的三种日志（官方页面）

| 日志来源 | 适用 |
|---|---|
| **Crash Logger SSE** | Skyrim SE / AE（**官方推荐的首选项**） |
| **.NET Script Framework** | Skyrim SE |
| **Trainwreck** | SE / AE（**备选**，见下） |

页面明确：**同时只能装一个日志器**，要把其它的移除或禁用。

## 它能给出什么（作者自述要点）

- 立刻识别多种崩溃原因，并为其中很多给出**经过调研的排查步骤与链接**；
- 当日志里有多个可能原因时，**排优先级**；
- 对不兼容 AE 的旧版 mod，**推荐替代 mod**；
- 对 Wabbajack / Nexus Collections 这类**整合包用户**有专门提示；
- 给出降低随机崩溃的通用建议；
- 列出日志里各文件的来源注释；
- 建议你把"缺的 mod"补上（参考 J3w3ls 的 Essential Mod List）；
- 生成**摘要版崩溃日志**，便于在社区里分享与比较。

## 诚实边界（官方页面原话意思）

> **"Not all crash issues can be detected with this tool."**
> 它是**公式化**的分析，可能漏掉人眼能看出的细微线索。

所以当它给不出方向时，正确动作是：带着**原始完整日志**去社区求助，
而不是反复重跑分析器。

## 日志找不到怎么办（官方排错清单）

1. **路径**：Crash Logger SSE 的日志落点比 Trainwreck **高一层目录**，先核对路径。
2. **杀毒软件**可能在隔离/锁住日志文件 → 把日志目录加入白名单。
3. **OneDrive** 同步会锁住文档目录里的文件 → 调整同步设置或排除目录。
4. **权限**：以管理员运行游戏与 mod 管理器，确认游戏/Mod 目录不是只读。
5. **磁盘空间**：空间不足时游戏/日志会写失败，留出余量。
6. **备选**：必要时临时换成 **Trainwreck**——它通常缺少关键线索，
   但有时能在其它日志器写不出东西的场景下产出日志。
7. **连日志都没有的冻结**：作者提到可用 ProcMon 一类工具看"崩溃前最后加载了什么"。

## 相关的便捷入口

作者维护了 **Quick Link Plugins（QLP）**（MO2 / Vortex 各一版）：
零点击检测新生成的崩溃日志并直接打开分析器，还能生成可分享链接。

## 相关

- [Crash Logger SSE](../09-diagnostics/crash-logger-sse.md)（日志来源）
- [Trainwreck（备选崩溃日志器）](../09-diagnostics/trainwreck.md)
- [Wabbajack（整合包一键安装）](../03-managers/wabbajack.md)（整合包用户的特别提示）
