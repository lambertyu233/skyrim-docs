---
id: poise-family
title: POISE 与 Chocolate Poise——两代韧性重做
category: 04-poise
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [POISE, Chocolate Poise, 韧性, stagger, doodlum, Loki]
aliases: [Loki poise, 格斗游戏硬直, POISE NG, poise 对比]
source: https://www.nexusmods.com/skyrimspecialedition/mods/72653
summary: POISE（Loki）用行为层重做硬直但已停更；Chocolate Poise（doodlum）是 SKSE 数值韧性条、当前活跃替代品——别混淆。
---

# POISE 与 Chocolate Poise——两代韧性重做

## 一句话

**POISE**（作者 Loki）近乎彻底移除原版随机硬直、改格斗游戏式机制，但已停更；**Chocolate Poise**（doodlum）是当前活跃维护的替代品——两者**别混淆**。

## POISE（原版）

- [mods/72653](https://www.nexusmods.com/skyrimspecialedition/mods/72653)，官方描述原文："A near complete gutting of the vanilla stagger system for something more inspired by traditional fighting games"——踉跄由攻击属性决定而非 RNG，作者声明绝不加"硬直冷却"；实现方式是移除人形角色进原版踉跄动画的能力、全部换成自己的行为【一手源】。
- 硬性要求：SKSE、**Nemesis、DAR、AMR**【一手源】。
- **NG 版 [mods/72692](https://www.nexusmods.com/skyrimspecialedition/mods/72692) 已于 2026-08-22 被 doodlum 设为隐藏**（"not supported by the author(s) and/or has issue(s) they are unable to fix yet"）【一手源】。
- 原版 v1.0.2（2022-08-21）后无更新。配套 addon：Poisebreaker（ConnerRia/Linnsanity）。

## Chocolate Poise（doodlum，活跃替代品）

- [mods/70478](https://www.nexusmods.com/skyrimspecialedition/mods/70478)：SKSE 纯数值韧性条，风格类似 Elden Ring，v30F（2026-08-25）仍在更新【一手源】。

## 选型提示

- 新装且要"韧条显示"的现代组合 → Chocolate Poise，或 [MaxsuPoise](./maxsu-poise.md)（配 TrueHUD 条）。
- 老整合绑死 POISE 的照原样保留，但要接受 Nemesis/DAR/AMR 老生态。

**注意**：常被说的"韧性显示需要 TrueHUD"更多见于 MaxsuPoise / Loki 系用法；POISE 原版页面正文并无 TrueHUD 要求【一手源核对】。
