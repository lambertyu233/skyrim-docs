---
id: cgo
title: CGO——Combat Gameplay Overhaul
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [CGO, Combat Gameplay Overhaul, 冲突, 翻滚]
aliases: [dTry CGO, cgo 和 BFCO 冲突, 战斗玩法大修, cgо]
source: https://www.nexusmods.com/skyrimspecialedition/mods/33766
summary: CGO 给原版战斗加翻滚/握姿/空中攻击等，与 BFCO/MCO 功能重叠互斥——BFCO 官方明确列为不兼容。
---

# CGO——Combat Gameplay Overhaul

## 一句话

给**原版**战斗加"动作补丁式"功能（翻滚闪避、程序性倾斜、握姿切换、空中攻击、双持双手武器），并重做攻击动画混合——不做连招派生框架。

## 基本事实

- SE 页 [mods/33766](https://www.nexusmods.com/skyrimspecialedition/mods/33766)，页面署名 Dservant；社区认为后期由 dTry 接手维护【社区说法，未在官方页面正文核实】。

## 与 BFCO 冲突（官方原文）【一手源】

BFCO description "Incompatible with" 清单明列：

> "CGO (Repetitive functions \*Whenever player jumps to attack, it will cause stuck in a falling)"

即跳攻会**卡在坠落状态**。原因：两者都改 1hm（单手武器）攻击行为且功能重叠。社区共识 "you cannot use MCO, CGO and BFCO together"【社区经验】。

## 定位选择

- 要现代动作游戏的连招/方向重击体系 → 用 BFCO，**别装 CGO**。
- 只想在原版手感上补几个小动作（翻滚、握姿）→ CGO 仍是独立可行路线（此时别装 MCO/BFCO）。
- ABR 曾官方提供 CGO 兼容版本，说明一代框架时代两者共存是常见组合【一手源】。
