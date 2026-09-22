---
id: address-library
title: Address Library for SKSE Plugins
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [前置, SKSE, 依赖库, 版本无关, meh321]
aliases: [Address Library, 地址库, 地址映射, 32444, versionlibdb, 插件依赖]
source: https://www.nexusmods.com/skyrimspecialedition/mods/32444
summary: 把「绝对内存地址」换成「稳定 ID」的映射库，让 SKSE 插件不必在每次游戏更新后重编译——数百个现代插件的隐形前置。
---

# Address Library for SKSE Plugins

## 解决的问题

SKSE 插件要调用游戏内部函数，就得知道函数在 `SkyrimSE.exe` 里的地址。
Bethesda 一发更新，二进制重排，**硬编码地址全部失效**，所有插件在各自作者重编译前一律罢工。

Address Library 引入一层间接：插件申请"函数 #12345"，库负责在当前版本的
`versionlibdb` 里解析出真实地址。于是：

- 更新后**只需等库更新**，大量插件无需作者重编译即继续可用；
- 老插件能跨越多个游戏版本存活数年。

（来源：Nexus 发布页 + 社区整理；机制描述与 `CommonLibSSE-NG` 的官方说明一致）

## 安装要点

- **两份文件，二选一，不能混装**：
  - `All in one` → Skyrim SE **1.5.97**
  - `Anniversary Edition` → Skyrim **1.6+**
- 本质是 SKSE 插件（`.bin` + `Data/SKSE/Plugins/` 下的数据），**不占插件位次**，
  放在左列表哪里都行。
- 无 UI、无 INI、无输出。**装完看不到任何变化是正常的**。

## VR 与开发侧

- **Skyrim VR 用 `VR Address Library for SKSEVR`**，是另一份数据库，不是这个。
- `CommonLibSSE-NG`（现代插件的编译框架）**默认依赖它**——所以用新版框架写的插件
  等于间接要求 Address Library。

## 常见故障

| 现象 | 原因 |
|---|---|
| SKSE 日志出现 "address library not found" | 未安装，或装成了 VR 版本 |
| 插件加载了但功能无效 / 崩溃 | 装错分支（SE 版装在 1.6.x 上） |
| 更新游戏后一批插件同时失效 | 游戏更新了但库还没跟上（等作者更新） |

## 未确认 / 需核实

- 具体 `versionlibdb` 的版本号与游戏运行时的对应关系随更新变动，
  请以 Nexus 发布页 Files 标签的实际文件名与说明为准，**不要照抄任何旧表格**。

## 相关

- [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)：必须先用它启动游戏。
- [CommonLibSSE-NG（插件开发框架）](../01-frameworks/commonlibsse-ng.md)：开发侧框架。
