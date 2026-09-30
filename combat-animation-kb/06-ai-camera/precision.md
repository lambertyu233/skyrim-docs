---
id: precision
title: Precision——Accurate Melee Collisions（武器精确碰撞）
category: 06-ai-camera
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [Precision, 碰撞, 命中判定, Ersh, hitstop]
aliases: [武器碰撞, 碰撞mod, accurate melee, 卡肉]
source: https://www.nexusmods.com/skyrimspecialedition/mods/72347
summary: Ersh 的基于 Havok 的真实武器碰撞：贴合挥砍轨迹判定、程序化受击、卡肉、镜头震动；支持 SE/AE，v2.0.4。
---

# Precision——Accurate Melee Collisions（武器精确碰撞）

## 一句话

官方描述原文："Physically accurate, true Havok collisions for melee. Procedural, physics-based hit reactions. Weapon trails. Hitstop and camera shake. Recoils…"——武器碰撞**贴合挥砍轨迹**判定，不再按"挥到哪都算"的距离盒判定。

## 基本事实【一手源】

- 全称 **Precision - Accurate Melee Collisions**；作者 **Ersh**（Nexus 上传名 Ershin）。
- [mods/72347](https://www.nexusmods.com/skyrimspecialedition/mods/72347)，**v2.0.4（2023-01-22）**；官方明确 "Supports SE/AE"（未见"要求 1.6.640+"的表述）。
- 要求 SKSE64、Address Library；可选：Nemesis（"very strongly recommended"）、SkyUI + MCM Helper、AMR（自定义后坐力位移）、SSE Display Tweaks。
- 支持第一/第三人称、NPC 与生物；为新 moveset 提供**自定义碰撞**（动作包通过注释接入）。

## 两个易混点

- **箭矢精确碰撞不是 Precision 本体功能**——那是衍生 mod **Accurate Projectile Collision**（Ersh & Seb263，[mods/188551](https://www.nexusmods.com/skyrimspecialedition/mods/188551)，2026-08 首发，依赖 Precision，不支持 VR）【一手源】。
- Precision 是底层碰撞系统，与 MCO/BFCO **都兼容**；部分动作包（如 Anchor 系）的动画使用 Precision 事件，属"强烈推荐"而非硬前置【社区经验】。
