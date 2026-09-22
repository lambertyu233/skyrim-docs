---
id: cbbe-3ba
title: CBBE 3BA（3BBB Advanced）—— 当代事实标准
category: 03-body
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [身形, 3BA, 3BBB, CBBE, 物理身形]
aliases: [cbbe 3ba, 三乳骨, acro, 事实标准身形, amazing body]
source: https://www.nexusmods.com/skyrimspecialedition/mods/30174
summary: 3BA 的命名、作者、它为什么成为当代女性身形事实标准，以及它与 CBBE 的关系（同基底网格，不是替代品）。
---

# CBBE 3BA（3BBB Advanced）

## 术语先分清

| 缩写 | 含义 |
|---|---|
| **3BBB** | **3 Breast Bones Body** —— 带 3 根乳房骨的身体（术语，不是文件名） |
| **3BA** | **CBBE 3BBB Advanced**，也常被称作 "Amazing Body" |

**3BA 是 CBBE 的扩展，使用与 CBBE 相同的基底网格** —— 这一点很重要：
它意味着**任何为 CBBE 设计的皮肤与服装都与 3BA 兼容**。

## 作者与来源

- 作者 **Acro**（LoversLab ID `Acro748`）。
- 历史：先有 **CBBE 3BBB Advanced**（Acro 制作，经 **Ousnius 授权**），
  后并入 CBBE 3BBB 页，并以 **CBBE 3BA** 名义上传 Nexus。
- Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/30174`
- LoversLab 官方文件页：`https://www.loverslab.com/files/file/11063-cbbe-3bbb-advanced`

## 它增加了什么

在 CBBE 基底上新增：

- **受物理控制的骨骼**：3 根乳房骨，以及腹部 / 大腿 / 小腿等；
- **大量额外 morph**（因此 RaceMenu 里会多出一批滑杆）。
- 提供 **RaceMenu Morphs 组件**（如 `RaceMenuMorphsCBBE.esp`）—— 它决定捏脸菜单里
  「身形那一栏」**有哪些滑块、叫什么名字**。真正的变形数据仍来自你自己构建的 `.tri`。
  这三层来源的对应关系见 [`morph-runtime-vs-bake.md`](morph-runtime-vs-bake.md)。

技术上：装了 3BA 不一定要再装基础 CBBE，但**基础 CBBE 自带所有原版服装转换**，
所以通常两者都装（3BA 覆盖身体，CBBE 提供服装基础）。

## 为什么它成了事实标准

1. **同时支持 CBPC 与 HDT-SMP**，可自由切换，甚至能在游戏内切；
2. 对 CPU 友好（相对纯 SMP 方案）；
3. **morph 与预设生态庞大** —— 绝大多数新服装、预设都写明 for CBBE 3BA；
4. 有 **3BAv2** 迭代。

> **3BAv2 的重要后果**：2021 年底之后为 3BAv2 制作的服装才与 3BAv2 兼容，
> 更老的 CBBE/3BBB 服装需要转换。这是"跟随从/穿某件衣服时穿模"的一个隐蔽成因。

## 依赖

| 依赖 | 说明 |
|---|---|
| CBBE | 基底网格（3BA 是扩展，不是替代） |
| **XPMSSE 4.61+** | 骨骼节点 |
| **CBPC 1.5.1+** | 碰撞物理 |
| BodySlide | 构建身形与服装 |
| HDT-SMP / **FSMP** | 可选（SE 下可选 SMP；AE 下可选 FSMP） |
| PapyrusUtil | 部分版本的分发描述里被列为依赖 |

## 版本

- Nolvus 指南使用的文件名对应 **2.45** 左右（2022）。
- 存在 **3BAv2** 迭代。
- **当前最新版本：未确认** —— 请以 Nexus Files 页为准。

## 来源

- 作者 Acro、与 CBBE 同基底、物理支持、3BAv2：LoversLab 官方文件页 + Nolvus 指南 —— **一手 + 社区指南（一致）**
- "3BBB = 3 Breast Bones Body"：LoversLab 术语表 —— **社区经验**
- "成为事实标准"的原因：**社区共识 + 机制归纳**（不是某个官方声明）
- 依赖清单（XPMSSE 4.61+ / CBPC 1.5.1+）：描述正文经转述 —— **一手（经转述）**
- 当前最新版本：**未确认**
