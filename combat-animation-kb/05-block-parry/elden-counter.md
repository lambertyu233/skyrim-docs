---
id: elden-counter
title: Elden Counter——环学防御反击（dTry）
category: 05-block-parry
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [Elden Counter, 防御反击, guard counter, dTry, BFCO]
aliases: [格挡反击, 弹反后反击, BFCO 补丁]
source: https://www.nexusmods.com/skyrimspecialedition/mods/65579
summary: dTry 的无脚本"防御反击"：格挡成功后短时间内按重击触发；依赖 DAR+AMR+Payload Interpreter；BFCO 用户需第三方 Fix。
---

# Elden Counter——环学防御反击（dTry）

## 一句话

官方描述原文："Perform an Elden Ring style 'guard counter' against your enemy shortly after blocking their attack"——**格挡成功后短时间内按重击**触发防御反击；每类原版武器有专属反击动画，可选无敌帧。

## 基本事实【一手源】

- 作者 dTry（D7ry），GitHub：[D7ry/EldenCounter](https://github.com/D7ry/EldenCounter)。
- Nexus Requirements：Address Library、**Animation Motion Revolution、Dynamic Animation Replacer、Payload Interpreter**（注意依赖的是 DAR 不是 OAR）。
- v1.6（ESLified AE version）；原版发布 2022-03-27。

## 框架适配【一手源】

- MCO/ADXP：官方提供可选 MCO 兼容补丁；Skysa/ABR：无需补丁。
- **BFCO 无官方补丁**——社区方案 **Elden Counter - BFCO MCO Fix**（[mods/174642](https://www.nexusmods.com/skyrimspecialedition/mods/174642)，作者 VX09，v1.1，2026-05-09）。
- BFCO 官方另提示：可兼容但**勿勾 Elden Counter 的 Vanilla Behavior Patch**【一手源，BFCO description】。

## 注意

- 官方称与 Wildcat、Blade&Blunt、Inpa Sekiro、Ultimate Combat 等兼容。
- FAQ：无敌帧若与改 `setGhost` 的 mod 冲突会**武器隐身**【一手源】。
