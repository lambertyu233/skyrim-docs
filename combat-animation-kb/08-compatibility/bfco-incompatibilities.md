---
id: bfco-incompatibilities
title: BFCO 官方不兼容清单
category: 08-compatibility
kind: reference
version: 1.0.0
updated: 2026-09-30
tags: [BFCO, 不兼容, 冲突, 清单]
aliases: [BFCO 冲突, 哪些mod和BFCO冲突, 飞行mod 冲突, incompatible]
source: https://www.nexusmods.com/skyrimspecialedition/mods/117052
summary: 逐条对照 BFCO Nexus description 的 "Incompatible with" 原文——含功能性冲突（SkySA/ABR/MCO/CGO 等）与"可兼容但需注意"两类。
---

# BFCO 官方不兼容清单

全部引自 BFCO Nexus description 的 **"Incompatible with"** 原文【一手源】；"可兼容但需注意"类也在同页。

## 功能性冲突（别同装）

| 对象 | 官方原文要点 |
|---|---|
| **SkySA / ABR / MCO** | 功能重复（"Repetitive functions"）；官方并指出可用 MCO To BFCO Converter 迁移 |
| **重击热键类**（One Click Power Attack NG、Elden Power Attack、For Honor Power Attack） | 同类功能 MCM>BFCO 已内置 |
| **Dual Wield Parrying** | 功能重复 |
| **UCBO**（Unarmed Combat Behavior Overhaul）、**One Handed Crossbow Framework** | 功能重复 |
| **CGO** | 功能重复，且**跳攻会卡在坠落状态**（"Whenever player jumps to attack, it will cause stuck in a falling"） |
| **Dragon Clutch** | 会卡坠落 |
| **FNIS** | "FNIS is outdated, please use Pandora" |
| **Kaputt**（Melee Killmove Manager） | 破坏强力重击衔接 |

## 飞行类 mod——是"条件兼容"不是绝对不兼容

官方原文：flying mod beta **"may cause the jump attack to fail, user can disable jump attack in MCM>BFCO"**——飞 mod 可能破坏跳跃攻击，但可以在 MCM 里**关掉 BFCO 的跳攻**来共存【一手源】。

## 可兼容但需注意

- **Elden Counter**：勿勾其 Vanilla Behavior Patch（BFCO 下用社区 [BFCO MCO Fix](../05-block-parry/elden-counter.md)）。
- **Campfire**：勿让其他 mod 覆盖 PapyrusUtil.dll。
- **VioLens**、**TK Dodge 系**：装完改动 1hm_behavior 的 mod 后要重跑 Pandora/Nemesis 刷新。
- **SmoothCam 1.7**：冲刺攻击 FOV 跳变 bug（作者推荐 1.5）→ [SmoothCam](../06-ai-camera/smoothcam.md)。
