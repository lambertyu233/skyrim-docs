---
id: unp-bhunp
title: UNP 家族与 BHUNP
category: 03-body
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [身形, UNP, BHUNP, UUNP, 女性身形]
aliases: [unpb, dimon99, bakafactory]
source: https://www.nexusmods.com/skyrimspecialedition/mods/31126
summary: UNP 家族的演变（UNP → UUNP → Legacy UUNP → BHUNP）、BHUNP 的物理能力与硬依赖，以及它与 CBBE 不兼容的原因。
---

# UNP 家族与 BHUNP

## 家族演变

| 名称 | 说明 |
|---|---|
| **Dimonized UNP** | 作者 **dimon99**。最初只是"原版的替代身形"，**并非**为"让装甲贴合某体型"设计 —— 那是 BodySlide / CBBE 时代的产物 |
| **UUNP（Unified UNP）** | 把各种 UNP 变体统一进 BodySlide，用于 LE |
| **Legacy UUNP** | SE 下 UUNP 官方不再支持后的过渡方案（SE `mods/43773`），用于 LE→SE 转换 |
| **UNP Female Body Renewal** | 原始 UNP 的 SE 直移植（SE `mods/1699`）。**不支持 BodySlide**，已过时 |
| **UNPB** | UNP Blessed Body，丰胸丰臀重制版，仍属 UNP 家族 |
| **BHUNP** | 见下 |

## BHUNP

- **全称**：BHUNP (UUNP Next Generation) SSE
- **作者**：**Bakafactory 与 Haeun**（在 LoversLab 亦以 "Baka Haeun" / "factoryclose" 出现）
- Nexus SE：`https://www.nexusmods.com/skyrimspecialedition/mods/31126`（LE：`mods/100306`）
- LoversLab 官方文件页：`https://www.loverslab.com/files/file/10630-bhunp-3bbb-body-for-le`

### 特点

- 基于 HDT 的自然运动的大幅改进 UNP 身形；
- **3 根乳房骨**；
- 支持 Breasts / Butt / Thighs / Calves / Vagina / Belly 的**物理与碰撞**；
- 基础身形分 **BHUNP 3BBB / TBBP / BBP** 三档；
- 另有仅供 modder 使用的 **Ref 体**（Vagina / Breasts Ref，明确标注"不可用于游玩"）。

### 硬依赖

```
BodySlide and Outfit Studio
CBPC
HDT-SMP
SKSE64
XPMSSE 4.67+
```

**注意**：BHUNP 同时要求 CBPC **和** HDT-SMP —— 而这两个默认都想要 body 插槽。
BHUNP 的分档与配置正是为了让它们各管一部分，装完务必按说明配置，
否则会出现"物理打架"（详见 [`../04-physics/physics-overview.md`](../04-physics/physics-overview.md)）。

### 与 CBBE 的关系

> **不兼容。** 不同 UV、不同皮肤体系。BHUNP 与 **UUNP 系**完全兼容。

## 关于"BHUNP"这个缩写

社区普遍读作 **"UNP Bearer"** 或 **"Baka Haeun UNP"**，
但**官方未给出正式展开式** —— 引用时请标注为"社区惯例，未确认"。

## 版本与维护状态

LE 官方文件可见 **1.41V**；**SE 侧的最新版本与维护状态本轮未确认**（Nexus 页未能直读）。
请以 Nexus / LoversLab 文件页为准。

## 选择判据

选 UNP 系（而非 CBBE 系）的典型理由：

- 你已经在用 UNP 系的皮肤或预设；
- 你要装的服装包写明 for UNP / BHUNP；
- 你偏好 BHUNP 的物理分档方式。

**不要为了"对比一下"同时装 CBBE 与 BHUNP。**

## 来源

- BHUNP 作者、3 乳房骨、物理部位、依赖、不兼容 CBBE：LoversLab 官方文件页 + Nexus 发布页 —— **一手**
- UNP → UUNP → Legacy UUNP → UNP Renewal 的演变：Nexus 论坛 UNP 专题帖（资深用户/版主）—— **社区经验（多源一致）**
- "UUNP 在 SE 官方不再支持、Legacy UUNP 为过渡"：Nexus 页面与指南 —— **社区经验**
- "BHUNP" 缩写含义：**社区惯例，未确认官方展开式**
- BHUNP SE 最新版本 / 维护状态：**未确认**
