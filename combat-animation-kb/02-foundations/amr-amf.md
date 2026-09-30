---
id: amr-amf
title: AMR 与 AMF——动画位移修正（两个不同的 mod）
category: 02-foundations
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [AMR, AMF, 位移, 根运动, motion]
aliases: [Animation Motion Revolution, Animation Motion Fix, 位移修正, 攻击位移, 根运动修复]
source: https://www.nexusmods.com/skyrimspecialedition/mods/145100
summary: AMR（alexsylex，2022 停更）按注释注入真实位移；AMF（Maxsu，活跃）修引擎根运动缺陷——互补而非替代，常同时装。
---

# AMR 与 AMF——动画位移修正（两个不同的 mod）

## 一句话

**AMR 和 AMF 不是同一个东西，也不是同一人写的**。AMR 提供"按注释注入位移"的机制，AMF 修引擎根运动系统本身的缺陷；现代战斗包常两者同时要求。

## AMR = Animation Motion Revolution

- Nexus [mods/50258](https://www.nexusmods.com/skyrimspecialedition/mods/50258)，GitHub [alexsylex/AnimationMotionRevolution](https://github.com/alexsylex/AnimationMotionRevolution)；**作者是 alexsylex**（Maxsu 仅在致谢中）【一手源】。
- 作用：读取动画注释 `animmotion [x][y][z]` / `animrotation [deg]`，把真实位移/旋转注入引擎——"removes the mismatch between displacement and custom animations"（MCO 的动画位移就建在它上面，官方原话 "MCO is built around this mod"）。
- v1.5.3（2022-09-29）后停更；依赖 DAR（原话 "this mod would make little sense without Dynamic Animation Replacer"）、SKSE、Address Library【一手源】。
- 功能正被 AMF 与 OAR 系生态部分取代（社区共识【社区经验】），但 **BFCO 3.100 系前置清单仍列 AMR 为必需**【社区经验，3DM 同步帖】。

## AMF = Animation Motion Fix

- Nexus [mods/145100](https://www.nexusmods.com/skyrimspecialedition/mods/145100)，GitHub [max-su-2019/AnimationMotionFix](https://github.com/max-su-2019/AnimationMotionFix)；作者 **Maxsu**，AE/VR 移植 SkyHorizon3【一手源】。
- 作用：修复战斗中根运动动画**位移缩减/卡住**的问题；含 NPC 俯仰角位移修正、可禁用玩家旋转磁吸与攻击移动磁吸（ini 开关），兼容 TDM 等【一手源】。
- v1.2.0（2026-08-30）明确支持 "1.5.97, 1.6.640, 1.6.1170, 1.6.1179, 1.7.104, VR"【一手源】。

## 怎么记

- 动作包位移**不生效/漂移** → 查 AMR 是否装了、注释是否被转换工具改坏。
- 攻击动画**被吸回去/卡住** → 查 AMF 的磁吸开关。
