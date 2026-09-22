---
id: skse64
title: SKSE64 与 Address Library
category: 01-prerequisites
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [前置, SKSE, Address Library, 版本]
aliases: [脚本扩展, 版本库, 地址库]
source: https://www.nexusmods.com/skyrimspecialedition/mods/30379
summary: SKSE64 的版本对应关系与安装方式，以及 Address Library（地址库）为什么能解耦 SKSE 插件的版本依赖，和两者错误配置的症状。
---

# SKSE64 与 Address Library

## SKSE64

**Skyrim Script Extender** —— 扩展脚本与原生能力的加载器，作者 **ianpatt**（Ian Patterson）
与 **behippo**（Stephen Abel）。捏脸/身形生态里几乎所有"能动的功能"都靠它。

- Nexus 页：`https://www.nexusmods.com/skyrimspecialedition/mods/30379`
- **仅支持 Steam 与 GOG 版本**，不支持 Epic / Game Pass
- 版本必须与游戏可执行文件版本**精确对应**（见 [`../00-overview/version-matrix.md`](../00-overview/version-matrix.md)）
- **1.6.1170 → SKSE64 2.2.6**

### 安装要点

1. 把 SKSE 的文件解压到**游戏根目录**（与 `SkyrimSE.exe` 同级），不是 Data 目录。
2. 通过 `skse64_loader.exe` 启动游戏（MO2 里把它设为可执行项）。
3. `Data/SKSE/Plugins/` 是各 DLL 插件与配置的落脚点 —— 排错时先看这里有没有对应文件。

### 错误配置的症状

| 症状 | 含义 |
|---|---|
| SkyUI 弹 "SKSE is not functioning properly" | SKSE 脚本没装好或版本不符 |
| 游戏能启动但所有插件功能消失 | SKSE 版本与游戏不匹配（DLL 拒绝加载） |
| 启动即崩 | 某个 DLL 插件的游戏版本档选错了 |

## Address Library for SKSE Plugins

作者 **meh321**。Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/32444`。

**它解决的问题**：原生插件需要知道"引擎内部某个函数的地址"。
游戏每更新一个小版本，地址就变，插件就得重编译 —— 这曾导致"游戏一更新，全生态瘫痪"。

Address Library 提供一份**地址映射数据库**，插件通过"库编号（ID）"间接寻址，
于是**跨 1.6.x 小版本通用**。多数现代插件（FSMP、MCM Helper、PapyrusUtil 4.1+、Engine Fixes 等）都依赖它。

### 关键坑

> **SE 版（1.5.x）与 AE 版（1.6.x）是两套独立数据库，地址不通用。**

装错了的表现是：**依赖 Address Library 的插件全部静默失效**，而游戏本身照常运行。
排查时不要盯着某个 mod 找原因，先确认 ADL 装的是不是 AE 版。

## 最小前置链（1.6.1170）

```
SkyrimSE.exe 1.6.1170
├─ SKSE64 2.2.6
├─ Address Library for SKSE Plugins（AE 版）
├─ SkyUI
└─ 之后才是 RaceMenu / 物理 / 分配工具
```

## 来源

- SKSE64 Nexus 页与官方文档：`https://www.nexusmods.com/skyrimspecialedition/mods/30379` —— **一手**
- Nexus wiki「Skyrim 1.6.117x Notes」：SKSE 2.2.6 对应 1.6.1170 —— **一手（Nexus 官方文档）**
- Address Library：`https://www.nexusmods.com/skyrimspecialedition/mods/32444` —— **一手**
- SE / AE 地址库不通用、依赖清单：Nexus 页说明与插件 README 一致 —— **一手**
