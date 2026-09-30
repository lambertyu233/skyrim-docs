---
id: tk-dodge-family
title: TK Dodge 家族——SE/RE/NG/Redux 四个分支
category: 03-dodge
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [TK Dodge, 闪避, dodge, RE, Redux]
aliases: [tk dodge 哪个版本, TKD, 闪避mod, tk dodge pandora, 按键闪避]
source: https://www.nexusmods.com/skyrimspecialedition/mods/56956
summary: TK Dodge 有四个分支；Pandora 用户选 RE（Standalone），要持续更新选 Redux（v3.6.2）。
---

# TK Dodge 家族——SE/RE/NG/Redux 四个分支

## 一句话

原版 tktk 的经典按键闪避（翻滚/快步），现在装**RE 或 Redux**，不要装老 SE 版。**"TK Dodge Ultimate" 这个名字查无此 mod**——那是把 TK Dodge 与 Ultimate Combat（另一个战斗 mod，mods/17196）套装混称了【一手源，官方渠道无此独立 mod】。

## 四个分支

| 分支 | 作者 | 状态 | 适用 |
|---|---|---|---|
| TK Dodge SE（原版） | tktk1 | 老脚本版 | 仅老整合【一手源】 |
| **TK Dodge RE** | Maxsu、FBplus、Loop、Xing | 停更（v0.55-rc3，2023-07） | **Pandora 用户选它**（Standalone 文件 + Pandora 勾 "Tk Dodge standalone"）【一手源】 |
| TK Dodge NG | moshikle（Maxsu 版 AE 适配） | AE 适配 | 1.6.x 老方案【一手源】 |
| **TK Dodge Redux** | PaulMix | **活跃**（v3.6.2，2026-06-26） | 要 NPC 闪避/闪避攻击/8 向闪避等新功能；3.1.9+ 官方兼容 MCO 闪避攻击，并注明 "BFCO Movesets must have BFCO format Animation annotations"【一手源】 |

## 硬性要求（RE 版）【一手源】

SKSE、Address Library、TK Dodge SE（仅需 meshes）、Nemesis/Pandora 打补丁；**IFrame Generator RE 可选**（只要闪避无敌帧时装）。

## 与框架的配合

- 行为层闪避，可与 MCO/BFCO 共存；改动 1hm_behavior 的 mod 装完都要重跑 Pandora（BFCO 作者置顶帖原话提示 tkDodge 兼容问题需跑 Nemesis & Pandora）【一手源】。
- Pandora 3.0+ 下按补丁作者 jiuzhoucanglan 回帖（2025-07）："pandora 3.0+ 使所有额外补丁失效/不再需要"，勾 standalone 即可【社区经验】。
- 与 DMCO **互斥**（同类功能）。BFCO 官方推荐的闪避搭档是 DMCO——见 [DMCO 条目](./dmco.md)。
