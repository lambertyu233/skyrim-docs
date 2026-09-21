---
id: pandora-architecture
title: Pandora 架构与性能设计：为什么它"更快"
category: 04-pandora
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [Pandora, 性能, 架构, 增量序列化, 预加载]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki/Performance-Notes
summary: 官方 Performance Notes 全文要点：预加载、浅映射、增量(反)序列化、不调用 hkxcmd、克制的并行——解释了 Pandora 为何比前辈快。
---

# Pandora 架构与性能设计：为什么它"更快"

Pandora 官方 Wiki 专设 **Performance Notes** 页，开篇即澄清："用户说它快，是因为一系列设计因素，不是魔法，也没有为了速度牺牲输出质量的捷径。"以下为该页核心内容。

## 1. 预加载（Preloading）：把终点线往前移

> Pandora preloads all the behaviour project data that it needs in the background, as soon as the program is opened.
> （Pandora 一打开就在后台预加载所需的全部行为工程数据。）

理由：程序既然打开，用户大概率会在改完 mod 列表后运行引擎。于是在**用户勾选补丁的时间里**完成预加载，可省下数秒到半分钟。若在预加载完成前就点了 Launch，引擎会等待预加载结束。

## 2. 映射（Mapping）：只做"浅层"映射

> Behavior trees are huge finite state automata that can't be fully mapped without a large processing overhead.
> （行为树是庞大的有限状态自动机，完整映射开销极大。）

因此预加载阶段只做 **shallow map（浅映射）**：只保留**所有节点的名字**和对节点的**引用**。当某个节点真需要被改动时，才按名字查到它，再"弹"到 xml 层映射其参数。

## 3. 增量(反)序列化（Incremental (De)serialization）—— 2.0.0-alpha 起的核心

引擎有**两个逻辑层**：

- **native 层**：内存中的一等公民对象，强类型、操作廉价；
- **xml 层**：仅是补丁表达编辑的通用媒介，没有 native 层的安全保证。

流程：

1. 打开行为文件时，全部 xml **反序列化**为 native 对象树；
2. 某个对象需要被补丁修改时，**只把该对象**序列化到 xml 层（映射成类似 XPath 的局部路径）；
3. xml 编辑完成后，再**反序列化回 native 层**替换原对象；
4. 若反序列化因**非法编辑**失败，则**不替换**，保留未修改的原对象 → 这就是**强容错的来源**；
5. 最后把整棵 native 对象树**直接序列化为二进制包文件**。

> 对比：**旧版** Pandora 会把整棵树做 `XML → Native → XML → Binary` 的多次翻译；新版只处理"被改到的那部分"。

## 4. 不做数据编组 / 不包裹外部进程

- 最初版本会**并行启动多个 hkxcmd 进程**，短加载时快，但 modlist 一变大就呈指数级变慢。
- Pandora+ **不再调用 hkxcmd 或 Havok SDK**，改用 ret2end 的 **HKX2**（.NET 编写）的改版。
- **同语言库**使"编组（marshalling）"开销降到最低。

## 5. 并行化：克制使用

- 引擎**只对最重的组件**并行化。
- 教训来自初版：过度并行导致多线程能力较弱的 CPU 上**卡死**。
- 做法：**每个 mod 补丁在各自线程解析、并行应用**，并保证数据线程安全；**IO 密集或轻量操作一律不并行**。

## 实践含义

- **别在预加载没完成时就急着点 Launch**（会等）；
- **日志（`Engine.log`）是第一排错入口**，它记录了哪些补丁编辑失败；
- 性能瓶颈通常在**动画数量**而非引擎本身：社区报告 4.4 万+ 动画时 Pandora 跑一轮约 **25 秒**（首轮约 1.5 分钟）。

> 来源：Pandora 官方 Wiki「Performance Notes」
> https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki/Performance-Notes

## 相关

- [Pandora 概览](pandora-overview.md)
- [行为补丁器原理](../01-principles/behaviour-patcher.md)
