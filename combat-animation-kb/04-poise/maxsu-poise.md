---
id: maxsu-poise
title: MaxsuPoise——韧性条与踉跄触发
category: 04-poise
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [MaxsuPoise, 韧性, poise, 踉跄, stagger]
aliases: [poise mod, 韧性条, 硬直mod, Maxsu 韧性, MaxsuPoiseRevise]
source: https://github.com/max-su-2019/MaxsuPoise
summary: Maxsu 的韧性系统：踉跄由双方体型/护甲/武器/动画计算，带防无限锁踉跄保护；硬前置 BDI + DMenu + Modern Stagger Lock。
---

# MaxsuPoise——韧性条与踉跄触发

## 一句话

官方 Release 原文："A poise mod that intends to introduce a stagger trigger mechanics that fitting the modern action combat environment"——用**韧性值**决定何时踉跄，替代原版的随机硬直。

## 机制要点【一手源】

- 攻击造成的 poise damage 超过阈值才触发踉跄；韧性伤害与踉跄等级基于**双方的 mass、scale、护甲、武器、攻击动画**计算。
- 内置 **staggerProtectTime** 机制防"无限锁踉跄"。
- 2025-02 加入 **TrueHUD 集成**（配 special bar 显示韧性条）。

## 硬性要求（GitHub Release 原文）【一手源】

- **Behavior Data Injector / BDI Universal Support**
- **DMenu**
- **Modern Stagger Lock Framework**（见 [Modern Stagger Lock](./modern-stagger-lock.md)）

推荐搭配 Shield Of Stamina 或 Valhalla Combat（开 Block Stamina + Guard Break）；否则把 BlockedModel 设为 PercentBlocked。

## 版本与衍生

- 仓库最新 **v0.34 AE**（pre-release；修复 mass 读取与魔法踉跄问题），2025 年仍接受 PR【一手源】。
- Nexus 有第三方修订版 **MaxsuPoiseRevise（影天硬直修改）**：[mods/117988](https://www.nexusmods.com/skyrimspecialedition/mods/117988)【一手源】。

## 同类对比

- **POISE（Loki）**：格斗游戏式重做，改行为层，要求 Nemesis+DAR+AMR → [POISE/Chocolate Poise](./poise-family.md)
- **Valhalla Combat**：精力+计时格挡大修，韧性只是"计划中"未实装 → [Valhalla Combat](./valhalla-combat.md)
