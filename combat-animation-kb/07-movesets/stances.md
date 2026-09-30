---
id: stances
title: Stances——架式系统（DAR/OAR 层工具）
category: 07-movesets
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [Stances, 架式, DAR, OAR, OmecaOne]
aliases: [架式系统, stances mod, 换架势, Stances NG]
source: https://www.nexusmods.com/skyrimspecialedition/mods/40484
summary: OmecaOne 的架式系统：每武器 4 套架式，本体不带动画需自填 hkx；NG 版（aljo/styyx）SKSE 重写并内置 OAR 结构。
---

# Stances——架式系统（DAR/OAR 层工具）

## 一句话

官方机制：通过脚本切换 perk + DAR 条件实现**每武器 4 套架式**（含中立）——**本体不带动画**，架式里放什么招式由你自己填 hkx。它是 **DAR/OAR 层工具，不绑定 MCO/BFCO**。

## 两个版本【一手源】

| 版本 | 作者 | 形态 | 状态 |
|---|---|---|---|
| Stances - Dynamic Animation Sets（[SE mods/40484](https://www.nexusmods.com/skyrimspecialedition/mods/40484)） | OmecaOne | 脚本 + perk + DAR 条件 | 老版，依赖 DAR + MCM |
| **Stances NG**（[mods/117986](https://www.nexusmods.com/skyrimspecialedition/mods/117986)） | aljo/styyx | SKSE DLL 重写，内置 OAR 文件夹 | **v2.0.1（2026-06-15 更新）**，依赖 OAR + Address Library，不依赖 Key Utils |

另有数值 Add-On（mods/41251）。

## 定位提醒

Stances 解决"**同一把武器多种打法**"的组织问题；招式内容仍要靠 [动作包](./moveset-ecosystem.md) 或自备 hkx 提供。
