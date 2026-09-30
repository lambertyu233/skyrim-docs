---
id: dual-wield-parrying
title: Dual Wield Parrying SKSE——双持格挡
category: 05-block-parry
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [Dual Wield Parrying, 双持, 格挡, parry]
aliases: [双持格挡, 双持弹反, DWP, 双手武器格挡]
source: https://www.nexusmods.com/skyrimspecialedition/mods/85505
summary: 双持（及武器+法术等组合）按独立键格挡的老牌 mod 的 SKSE 化新版；被 BFCO 官方列为不兼容（功能重复）。
---

# Dual Wield Parrying SKSE——双持格挡

## 一句话

老牌 mod 的 SKSE 化新版：双持（及武器+法术等组合）时按独立键（默认 V）格挡/招架。

## 基本事实【一手源】

- 现行 Nexus 页 [Dual Wield Parrying SKSE](https://www.nexusmods.com/skyrimspecialedition/mods/85505)；插件源码 [DennisSoemers/DualWieldParryingSKSE](https://github.com/DennisSoemers/DualWieldParryingSKSE)。
- 老原版（LE mods/9247）与 SSE SKSE 移植：DennisSoemers / Borgut1337；**支持 1.6.1130+（含 1.6.1170）的 v2.0.1（2024-03-26）代码由 moshikle 编写**（文件页原文 "Code written by moshikle"）。
- **注意：alandtse 不是本 mod 维护者**——他只是编译所用 CommonLibSSE-NG 库的作者之一（GitHub 另有 clayne/DualWieldParryingNG 等镜像仓）【一手源】。
- GitHub README：SE 1.5.97 测试、兼容 1.6.353+；SKSE + Address Library；自称 "Safe to install / update / uninstall mid-game"。

## 与 BFCO 冲突【一手源】

BFCO 官方不兼容清单明列 **"Dual Wield Parrying (Repetitive functions)"**——BFCO MCM 已内置同类功能。**BFCO 用户不装**。老 MCO/SkySA 时代它是标配双持弹反方案。
