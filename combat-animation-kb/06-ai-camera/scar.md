---
id: scar
title: SCAR——Skyrim Combos AI Revolution（NPC 连招 AI）
category: 06-ai-camera
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [SCAR, AI, 连招, NPC, Maxsu]
aliases: [combos ai, NPC 连招, 敌人 AI, Skyrim Combos AI Revolution, scar 补丁]
source: https://www.nexusmods.com/skyrimspecialedition/mods/72014
summary: Maxsu 的 SKSE 连招 AI：NPC 按距离/角度选攻击动作打连段；本体锁 1.5.97，AE 用 doodlum 移植版；BFCO 下 NPC 出招由 BFCO 默认 AI 接管。
---

# SCAR——Skyrim Combos AI Revolution（NPC 连招 AI）

## 一句话

官方描述原文："SCAR introduces a dynamic and highly customizable AI attack system... One Moveset, One Attack AI Setup"——**NPC 每次出招前检查距离、角度等条件**，选取符合条件的攻击动作，实现连招 AI。**全称是 Skyrim Combos AI Revolution**（不是 "Skyrims Combat AI Reborn"）。

## 基本事实【一手源】

- 作者 **Maxsu**（原版概念来自 Monitor144hz/221hz，Maxsu 重制为 SKSE 插件）。Nexus [mods/72014](https://www.nexusmods.com/skyrimspecialedition/mods/72014)，GitHub [max-su-2019/SCAR](https://github.com/max-su-2019/SCAR)。
- 要求：SKSE、Address Library、VC++ 2015-2022、**Nemesis**。
- 兼容 **ADXP|MCO v1.3.2+**；Skysa/ABR 需打补丁。**页面未提及 BFCO**（停更早于 BFCO 发布）。

## 版本地雷【一手源】

- **v1.06 起作者移除 1.6 runtime 支持，仅支持 1.5.97**（changelog 原文 "Remove supporting of v1.6 runtime, from now on all of my plugin supports only 1.5.97"）。
- **AE 用户装 doodlum 的 SCAR AE Support**（[mods/77285](https://www.nexusmods.com/skyrimspecialedition/mods/77285)，v1.06.1，2026-08-24 更新）。
- GitHub 另有 SCAR v2.01 pre-release（仅 1.5.97，改要求 OAR + BDI + Nemesis）。

## 与 BFCO 的分工【一手源，BFCO 作者站点】

NPC 使用带 SCAR 注释的动作时完全由 SCAR 管理；无 SCAR 注释时 BFCO 启用默认 AI 出招。**moveset 必须预先打好 SCAR patch 才对 NPC 生效**（所以很多动作包文件名里带 "SCAR"）。
