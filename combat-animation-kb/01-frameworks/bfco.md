---
id: bfco
title: BFCO——Attack Behavior Framework（第三代，现役）
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [BFCO, BF001, 烽火, 攻击框架, 现役, 3.100]
aliases: [Attack Behavior Framework, BFCO 要求, BFCO 方向重击, bfco 版本, BFCO NG]
source: https://www.nexusmods.com/skyrimspecialedition/mods/117052
summary: BF001 的第三代攻击框架：MCO 全部能力之上新增方向重击/跳跃攻击/游泳攻击/弓弩 bash/强力重击热键/MCM，3.100.x 持续更新。
---

# BFCO——Attack Behavior Framework（第三代，现役）

## 一句话

**MCO 的扩展与再迭代，功能最全、仍在活跃更新**（最新 3.100.8，2026-09-03 上传）——新装动作框架的默认答案。

## 基本事实【一手源】

- Nexus 页：[mods/117052](https://www.nexusmods.com/skyrimspecialedition/mods/117052)（"BFCO - Attack Behavior Framework (SSE AE VR)"），作者 **BF001**，2024-05 首发。
- **不是 MCO 官方续作**，而是定位相同的新一代框架。官方 FAQ 原文："Q: How is it different from MCO? — BFCO supports vanilla attack speed and direction heavy attack…"
- **DLL 开源**：官方 Credits 给出 [vinymayan/BFCO](https://github.com/vinymayan/BFCO/tree/og) 与 [sky199411/BFCO_Functions](https://github.com/sky199411/BFCO_Functions)。

## 官方 description 核实过的功能（逐条对照原文）【一手源】

- ✅ **方向重击**：WASD + 攻击键 → `BFCO_PowerAttackA/B/L/R.hkx`
- ✅ **跳跃攻击**：jump + LMB → `BFCO_JumpAttack.hkx`
- ✅ **游泳攻击**：`BFCO_SwimAttack1~3.hkx` 等
- ✅ **弓弩 bash**：`BFCO_BowBash.hkx` / `BFCO_BowPowerBash.hkx`
- ✅ **强力重击热键**（PowerAttack-Comb：热键 或 轻击+ActionKey）
- ✅ **MCM 菜单**细调操作手感、自定义蓄力攻击、自定义派生注释
- ✅ NPC 连招支持；原生兼容原版攻速/技能树；与 DMCO 任意版本兼容
- 原版手感党可以整套不装：想保留原版战斗只换动作动画，BFCO 不是必需品。

## 版本线【一手源】

3.3.11（2025-03）→ 3.6.1（2026-02）→ **3.100**（2026-04-16）→ 3.100.8（2026-09-03）。作者置顶帖："Version 3.100+ has almost done with my idea, enjoy :)"；要更灵活的热键分配作者推荐 "BFCO NG"（细节未在可访问页面核实【未核实】）。

## 依赖

- FAQ 原文提到"伪方向重击"需要 **dTry's Key Utilities**【一手源】。
- **Directional Movement Keys（DMK）**：BFCO Requirements 页面列为方向重击前置（详见 [Key Utils 与 DMK](../02-foundations/key-utils-and-dmk.md)）；但"真方向重击"是行为层原生实现，DMK 主要服务于伪方向/热键派生玩法——两层说法并存，以 Nexus 正文为准。
- 社区同步的前置清单（3DM 3.100 帖）【社区经验】：SKSE、AMR、OAR、PapyrusUtil、MCM Helper 必需；Payload Interpreter 可选。

## 下一站

不兼容清单与迁移注意事项 → [BFCO 官方不兼容清单](../08-compatibility/bfco-incompatibilities.md)。
