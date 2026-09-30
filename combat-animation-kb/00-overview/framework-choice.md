---
id: framework-choice
title: 攻击框架选型：SkySA/ABR → MCO → BFCO
category: 00-overview
kind: concept
version: 1.0.0
updated: 2026-09-30
tags: [选型, BFCO, MCO, SkySA, ABR, 对比]
aliases: [攻击框架, combat framework, 用MCO还是BFCO, 三代框架, 战斗框架怎么选, SkySA 还能装吗]
source: https://www.nexusmods.com/skyrimspecialedition/mods/117052
summary: 攻击框架三代演进——SkySA/ABR 已淘汰、MCO 停止演进、BFCO 现役且功能最全；新装一律选 BFCO。
---

# 攻击框架选型：SkySA/ABR → MCO → BFCO

## 一句话

**新装一律选 BFCO。** MCO 官方 Nexus 页已由作者 Distar 以告别口吻重新上传（1.6.0.6 为终版），SkySA/ABR 停更多年。

## 三代演进（均有官方页面佐证）

| 代 | 框架 | 现状 | 证据 |
|---|---|---|---|
| 一 | SkySA | Nexus 文件区**全部 Archived**（作者不再支持）；同系作者 DuffB 原话 "Switch to MCO please as SkySA is deprecated and wont get anymore updates" | 【一手源】 |
| 一 | ABR（Attack Behavior Revamp，非 "Replacer"） | Nexus 版停在 2021-04（v5.0），后续版本走 Patreon 后也停摆 | 【一手源】 |
| 二 | MCO（ADXP\|MCO，Distar） | 现行页 [mods/175044](https://www.nexusmods.com/skyrimspecialedition/mods/175044)（2026-03 重新上传，1.6.0.6）；作者留言 "It was such a fun run… Bye!"——框架本体停止演进 | 【一手源】 |
| 三 | BFCO（BF001） | 2024-05 首发，3.100.x 持续更新中（最新 3.100.8，2026-09-03） | 【一手源】 |

## BFCO 比 MCO 多什么（全部出自 BFCO 官方 description）【一手源】

- 方向重击（WASD + 攻击键触发 `BFCO_PowerAttackA/B/L/R.hkx`）
- 跳跃攻击、游泳攻击、自定义蓄力攻击
- 弓弩 bash（`BFCO_BowBash.hkx`）
- 强力重击热键（MCM 内置，不必再装重击热键 mod）
- NPC 连招支持、MCM 细调、原生兼容原版攻速与技能树
- 与 DMCO 任意版本兼容（官方原文 "Fully compatible with DMCO (any version)"）

详细功能与依赖见 [BFCO 条目](../01-frameworks/bfco.md)；与 MCO 的冲突与迁移见 [BFCO 不兼容清单](../08-compatibility/bfco-incompatibilities.md)。

## 什么时候还选 MCO

- 你想用的**特定动作包只有 MCO 版**且转换后体验不佳（MCO 注释转换后方向重击只能变成"伪方向重击"，见 [Converter 条目](../01-frameworks/mco-to-bfco-converter.md)）。
- 注意 MCO 的官方页面状态很乱：原页 mods/124806 已 **Removed by staff**，引用一律以 mods/175044 为准【一手源】。

## 老框架还在的理由（仅存档价值）

老整合包（SkySA 时代的 ERC/Leviathan 系等）里会绑死 SkySA/ABR，这类整合要么整体保持原样，要么弃用——SkySA/ABR 与 MCO/BFCO **不能共存**。
