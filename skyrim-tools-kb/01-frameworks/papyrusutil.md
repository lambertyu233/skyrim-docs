---
id: papyrusutil
title: PapyrusUtil SE
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [前置, 脚本, 数据存储, JSON, 依赖库]
aliases: [StorageUtil, JsonUtil, 13048, 脚本工具函数]
source: https://www.nexusmods.com/skyrimspecialedition/mods/13048
summary: 给 Papyrus 补上"存数据"能力的 SKSE 插件：StorageUtil 把变量挂在 form 上，JsonUtil 存到外部 JSON，另有 MiscUtil / ActorUtil。
---

# PapyrusUtil SE

## 提供的四个脚本

| 脚本 | 作用 |
|---|---|
| `PapyrusUtil.psc` | 版本检查、初始化数组等基础工具 |
| `StorageUtil.psc` | 把 int/float/form/string 或其列表，**以 form + 变量名为键**挂在任意 form 或全局 |
| `JsonUtil.psc` | 同上的数据模型，但写到**外部 `.json` 文件**，可脱离存档独立保存与手工编辑 |
| `MiscUtil.psc` | 杂项命令 |
| `ActorUtil.psc` | Actor 的 package 覆盖 |

（来源：Nexus 发布页描述正文；`.psc` 内含文档注释）

## 为什么它是前置

Papyrus 原生**没有可靠的持久化容器**。任何"跨存档记住状态""把配置写在外部文件里"
的 mod，几乎都通过 PapyrusUtil 实现。于是它成了**整个 modlist 里被引用次数最高的依赖之一**，
很多 mod 会把它列在 Requirements 的第一行。

## 安装

- 需要 **SKSE SE/AE 2.2.6+** 与 **Address Library**。
- 包内 `Data/SKSE/Plugins/PapyrusUtil.dll` + `Data/Scripts/*.pex`。
- 用 mod 管理器正常装即可；更新时**直接覆盖**。

## 版本匹配（易错点）

发布页明确：面向 **1.6.1170** 构建，其它版本需下对应的旧版文件。
**GOG 版 1.6.1179 要装 GOG 专用文件**。装错的典型症状不是崩溃，
而是依赖它的 mod 报"函数不存在"或行为诡异。

日志位置：`文档\My Games\Skyrim Special Edition\SKSE\PapyrusUtilDev.log`。

## 相关

- [JContainers SE](../01-frameworks/jcontainers.md)：另一套（更重、支持 JSON 结构）的持久化方案。
- [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)、[Address Library for SKSE Plugins](../01-frameworks/address-library.md)：两个硬前置。
- [FallrimTools / ReSaver（存档清理）](../09-diagnostics/fallrimtools-resaver.md)：注意 JSON 数据**不在** `.ess` 里，
  ReSaver 也动不到它——这是"清了存档但数据还在"的原因之一。
