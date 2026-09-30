---
id: tdm
title: True Directional Movement（TDM）——第三人称锁定与八向移动
category: 06-ai-camera
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [TDM, True Directional Movement, 锁定, 八向移动, Ersh]
aliases: [锁定mod, 第三人称锁定, 八向攻击, TrueHUD, target lock]
source: https://www.nexusmods.com/skyrimspecialedition/mods/51614
summary: Ersh 的现代动作游戏式第三人称大修：任意方向移动攻击+目标锁定；要求 TrueHUD；v2.3.1 已适配 BFCO 攻击事件。
---

# True Directional Movement（TDM）——第三人称锁定与八向移动

## 一句话

官方描述原文："Overhauls the third person gameplay similarly to modern action RPGs, entirely through SKSE. Move and attack in any direction. Includes a custom target lock component…"——现代动作游戏式第三人称：**八向移动/攻击 + 自定义锁定**（动画准星 widget）。

## 基本事实【一手源】

- 作者 **Ersh**（ersh1），GitHub：[ersh1/TrueDirectionalMovement](https://github.com/ersh1/TrueDirectionalMovement)（贡献者含 max-su-2019）。
- [mods/51614](https://www.nexusmods.com/skyrimspecialedition/mods/51614)，要求：SKSE、Address Library、SkyUI + MCM Helper、**TrueHUD**（锁定准星 widget 必需）；Nemesis 可选但强烈推荐（修复头跟）。
- **v2.3.1（2026-09-02 更新）**——页面已恢复更新；v2.2.6 更新日志明确 "**Added BFCO attack events** to the attack phase recognition logic"，另有 Dodge Framework 兼容说明【一手源】。

## 配套与易混

- 相机搭档：[SmoothCam](./smoothcam.md)（v1.6 起内置 TDM 十字准星补偿）。
- **"DM-IIO" 查无此物**：未能找到任何以此为名的 TDM 附属 mod，TDM 相关知名附属是 **TrueHUD**（Ersh 同作者）与 Dodge Framework【未核实，疑为记忆混淆】。
- 与 [DMK（Directional Movement Keys）](../02-foundations/key-utils-and-dmk.md) 是不同作者的**不同 mod**，别混淆。
