---
id: maxsu-block-overhaul
title: MaxuBlockOverhaul——格挡受击动画重做
category: 05-block-parry
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [MaxsuBlockOverhaul, 格挡, block, 破防, Nemesis]
aliases: [格挡大修, block overhaul, guard break, 破防动画]
source: https://github.com/max-su-2019/MaxuBlockOverhaul
summary: Maxsu 重做原版格挡受击行为与动画，向现代动作游戏看齐；提供 guard break 破防动画；与改格挡行为的 mod 潜在冲突。
---

# MaxuBlockOverhaul——格挡受击动画重做

## 一句话

GitHub Release 原文："Reworked the Skyrim BlockHit behavior & animations to make it perform similar to the way in modern action games"——把格挡受击的反馈重做得像现代动作游戏。

## 基本事实【一手源】

- GitHub：[max-su-2019/MaxuBlockOverhaul](https://github.com/max-su-2019/MaxuBlockOverhaul)，作者 Maxsu。
- 主要是行为/动画文件（仓库含 behaviors、animationdatasinglefile，无 SKSE DLL 声明）——**装完必须在 Nemesis/Pandora 里勾补丁刷新行为**。
- v0.21a 起为其他战斗 mod 提供 **guard break（破防）** 动画供调用。
- v0.24a（2025-02-17）："Convert the block hit DAR animations folder into OAR folder struct"——动画目录已支持 OAR 结构。

## 冲突清单（Release 原文）【一手源】

> "Incompatible with: Impactful Blocking、Dual Wield Blocking and Attack Cancelling（用其 SKSE 版代替）、any other mod that modify the block behavior."

即与一切改格挡行为的 mod 潜在冲突。
