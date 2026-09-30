---
id: elden-parry
title: Elden Parry——盾击变弹反（dTry，停更）
category: 05-block-parry
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [Elden Parry, 弹反, parry, dTry, 格挡]
aliases: [盾反, parry mod, 弹箭, projectile parry, 轻盾击]
source: https://www.nexusmods.com/skyrimspecialedition/mods/70240
summary: dTry 的 SKSE 插件：轻盾击改成精确时机弹反，可把箭矢/法术弹回去；不要求 MCO/BFCO，AE 需社区补丁。
---

# Elden Parry——盾击变弹反（dTry，停更）

## 一句话

官方描述原文："Light bash is now turned into 'parry'"——**轻盾击改成精确时机弹反**，成功弹反不耗精力，且可把箭矢/法术**弹回去**（hook 投射物碰撞函数实现，非特权/假弹补偿）。

## 作者勘误

**作者是 dTry（D7ry），不是 Maxsu**。GitHub：[D7ry/EldenParry](https://github.com/D7ry/EldenParry)【一手源】。

## 基本事实【一手源】

- [mods/70240](https://www.nexusmods.com/skyrimspecialedition/mods/70240)，v1.3（2022-08-04）后停更。
- 要求 SKSE + Address Library；**不要求 MCO/BFCO**，官方称 "Compatible with every single combat mods/behavior mods"。
- 官方注明：与 Better God Modes 不兼容；Ersh 的 Precision beta 需 ≥0.4。

## AE 用户注意【社区经验】

原版**不支持 AE 1.6.1170**。Nexus 讨论区置顶经验（2025-08 回帖）：需另装 dTry 系列 AE 补丁（mods/85740）与 Precision 下盾击修复（mods/188223）。

## 相关条目

[Valhalla Combat](../04-poise/valhalla-combat.md)（联动眩晕）· [Elden Counter](./elden-counter.md)（格挡后的防御反击）· [MaxsuBlockOverhaul](./maxsu-block-overhaul.md)（格挡受击动画重做）
