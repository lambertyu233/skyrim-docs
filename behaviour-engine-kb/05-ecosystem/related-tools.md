---
id: related-tools
title: 相关工具链：hkx 查看/编辑、行为编辑器与战斗框架
category: 05-ecosystem
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [hkxcmd, HKX2, Haviour, BehaviorTool, MCO, SCAR, 工具链]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki
summary: 整理与动作引擎配套的 hkx 解包/编辑工具、行为编辑器、位移注释工具与常见战斗框架，标注各自用途与出处。
---

# 相关工具链：hkx 查看/编辑、行为编辑器与战斗框架

## hkx 解包 / 序列化工具

| 工具 | 用途 | 备注 |
| --- | --- | --- |
| **hkxcmd** | Havok 官方命令行工具，解包/打包 hkx | **32 位（LE）** 用；FNIS 与 Nemesis 的 Export 工具 |
| **hkxconv** | 64 位 hkx 解包 | **64 位（SE/AE）** 用（ret2end） |
| **HKX2** | .NET 编写的 hkx 读写库 | Pandora 使用其改版替代 hkxcmd 做(反)序列化，Export 记为 **HKX2E** |

> Pandora 官方 wiki 提到：hkx 包文件"可用 hkxcmd 和 hkx2 解包"。

## 行为文件编辑工具（作者向）

| 工具 | 用途 |
| --- | --- |
| **Zartar's Behaviour Tool** | 编辑行为包文件（"最突出的"工具之一，官方 wiki 点名） |
| **Haviour**（Pentalimbed） | 另一款行为编辑工具（官方 wiki 点名） |
| **Skyrim Behavior Tool** | 编辑行为修饰符（如开启 `bAnimationDriven`），AMR 章节提到 |

## 动画注释工具

| 工具 | 用途 |
| --- | --- |
| **hkanno64** | 往动画里加注释（AMR 的位移/旋转数据即由此写入） |

## 动作引擎本体

| 引擎 | 一句话 |
| --- | --- |
| **FNIS** | 第一代，闭源、停更，LE 用户的选择 |
| **Nemesis** | 第二代，开源、模板化，文档缺失 |
| **Pandora** | 第三代，开源、快、全生物支持、有官方 Wiki |

## 替换器（Replacer）

| 工具 | 用途 |
| --- | --- |
| **DAR** | Dynamic Animation Replacer（旧） |
| **OAR** | Open Animation Replacer（新，兼容 DAR，开源） |

## 常见战斗 / 动作框架（通常需要动作引擎）

| 框架 | 说明 |
| --- | --- |
| **MCO**（Modern Combat Overhaul） | 基于 AMR 的现代战斗框架，需行为补丁 |
| **SCAR**（Skyrim Combos AI Revolution） | 让 NPC 智能使用攻击动画 |
| **BFCO** | 现代动作框架（中文社区指南中提及；自 2.0 起曾不兼容 FNIS） |
| **True Directional Movement** | 全向移动/锁定类框架（中文指南提示：勾选 **Procedural** 项，核心功能在此） |

## 说明

- 上表中"官方 wiki 点名"的工具，出处为 Pandora 官方 Wiki 的「What is Havok Behavior™?」一节。
- 战斗框架的具体前置与勾选方式随版本变化，**以各 mod 当前页面为准**；本表只做定位，不给死版本号。

> 来源：Pandora 官方 Wiki https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki

## 相关

- [OAR / DAR](oar-dar.md)
- [AMR](amr.md)
- [hkx 其实有两种](../01-principles/hkx-two-kinds.md)
