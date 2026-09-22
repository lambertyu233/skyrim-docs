---
id: scrambled-bugs
title: Scrambled Bugs
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [稳定性, bug 修复, 玩法机制, 可选补丁, SKSE]
aliases: [Scrambled Bugs, 43532, 引擎 bug, 修附魔, 修药水, ScrambledBugs.json, KernalsEgg]
source: https://www.nexusmods.com/skyrimspecialedition/mods/43532
summary: 一批「玩法机制层」引擎 bug 的修复 + 一批默认关闭的可选 patch；每项都能在 ScrambledBugs.json 里单独开关，日志会报告启用了哪些。
---

# Scrambled Bugs

Nexus：`skyrimspecialedition/mods/43532`。
**作者署名在资料源之间有出入**：Nexus 发布页显示 `Created by Magicockerel`，
而 STEP wiki 记作 **KernalsEgg, meh321**，整合包清单多写作 **KernalsEgg**。
（同一作者改过名的可能性最大，但**引用时请以你看到的 Nexus 页面为准**。）

## 两类内容，默认状态不同（重要）

- **Fixes（修复）**：**默认全部开启**。
- **Patches（可选补丁）**：**大多默认关闭**。

所以"装了没感觉"是正常的——绝大多数 patch 需要你手动在设置里打开。

## 配置与日志

| 文件 | 路径 | 作用 |
|---|---|---|
| 设置 | `Data/SKSE/Plugins/ScrambledBugs.json` | 逐项开关每个 fix / patch |
| 日志 | `Data/SKSE/Plugins/ScrambledBugs.log` | 报告**哪些已启用**，以及**被静默处理的警告与错误**（含与其它 mod 的冲突） |

> **日志里"被静默处理的冲突"这一项很有价值**：这类问题平时不报错，
> 但会让某个修复悄悄失效。排错时值得一看。

## 前置（发布页 Requirements）

- SKSE64
- **Address Library for SKSE Plugins**
- Microsoft Visual C++ Redistributable for **Visual Studio 2022 x64**

## 它替代了哪些 mod（有助于理解覆盖面）

发布页明确列出了一批"这些 fix/patch 是下列 mod 的替代品"，例如
附魔消耗类修复、Enchantment Reload Fix、采集标记（Harvested Flags）类修复、
Quick Shot 的弓术 perk bug、最佳弹药自动装备（Equip Best Ammo）等。
**含义**：如果你的 modlist 里同时装了"被替代"的那个 mod，功能会重复——
通常无害，但值得知道该留哪个。

## 版本现状与一个已知的划分变化

- 发布页显示 **Version 21，最后更新 2023-03-14**——**更新节奏已经放缓**。
- 官方 Q&A 里有一条重要的历史变更：
  **"魔法效果条件修复"已被移除并移入 Bug Fixes SSE**（见 [Bug Fixes SSE](../09-diagnostics/bug-fixes-sse.md)）。
  这是查老教程时最容易对不上的地方。
- 作者的评论串里还有一条社区线索：**VR 用户的对应实现是 Poached Bugs VR**（属社区经验）。

## 引用数值的纪律

本文提到的版本号与更新日期取自 Nexus 发布页快照，**可能已过期**。
需要准确信息请核对发布页 Files / Changelogs。

## 相关

- [Bug Fixes SSE](../09-diagnostics/bug-fixes-sse.md)、[SSE Engine Fixes](../09-diagnostics/sse-engine-fixes.md)
- [powerofthree's Tweaks（引擎修复与调整）](../09-diagnostics/po3-tweaks.md)、[Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md)
- [Address Library for SKSE Plugins](../01-frameworks/address-library.md)
