---
id: hdt-smp
title: HDT-SMP（Skinned Mesh Physics）
category: 04-physics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [物理, HDT-SMP, SMP, Bullet, XML]
aliases: [hdt smp, skinned mesh physics, hdt, 物理引擎, hdtSkinnedMeshConfigs]
source: https://github.com/HydrogensaysHDT/hdt-skyrimse-mods
summary: HDT-SMP 的原作者、技术原理、XML 配置方式、前置与许可，以及它与旧方案 HDT-PE 的本质区别。
---

# HDT-SMP（Skinned Mesh Physics）

## 是什么

**HDT = hydrogensaysHDT（氫姐）**，作者，已退休。

- **SMP = Skinned Mesh Physics** —— 基于 **Bullet** 物理库的**逐顶点蒙皮网格物理**。
- 与旧的 **HDT-PE** 的差别：PE 是**骨骼级**碰撞（用游戏内建 Havok），
  SMP 是**网格顶点级**（自己带物理引擎）。这是"精度跃升"的关键。
- 源码以 **MIT** 许可开源。
- **原始仓库**：`https://github.com/HydrogensaysHDT/hdt-skyrimse-mods`

> ⚠️ 常见的一个错误仓库名是 `hydrogensaysHDT/hdt-skyrim-smp`（实测 404）。
> 正确仓库名为 **`hdt-skyrimse-mods`**。

## 配置方式：XML

配置文件目录：**`Data/SKSE/Plugins/hdtSkinnedMeshConfigs/`**，每个使用物理的 mod 放一个 XML。

XML 的作用是**把碰撞体（sphere / capsule / triangle）挂到骨骼上**，
默认身体配置通常叫 `defaultBBPs.xml`（或 `configs.xml`）。

因此"某个衣服没物理"往往不是引擎问题，而是**它没带或没加载 XML**。

## 前置

- **SKSE64**（SE）。
- 早期需要 **OpenCL 2.0**（用 GPU 计算）；也可以改 CPU 模拟 ——
  注意所谓"关闭 OpenCL"实际上是**切到 CPU**，不是完全关掉物理计算。

## 支持的游戏版本

原版主要支持 **LE 与 SE 1.5.97**。
**AE（1.6.x）支持由社区 fork 承接** —— 现代用户实际应该装 **Faster HDT-SMP（FSMP）**，
它已经**完全取代**原版（作者原话的意思是：不要同时安装原版）。

见 [`faster-hdt-smp.md`](faster-hdt-smp.md)。

## 与骨骼的关系

SMP **只把网格附加到 XPMSE 的 human skeleton**。
这条设计的好处是修掉了"Lurker 等非人骨架被物理破坏"的老问题；
代价是**你必须装 XPMSE**。

## 与 CBPC 的关系

两者都想要 body 插槽。共存需要显式配置：
见 [`physics-overview.md`](physics-overview.md)。

## 来源

- 作者、MIT、Bullet、逐顶点蒙皮网格与原版/PE 的区别、XML 目录与 `defaultBBPs.xml`、
  只附加 XPMSE human skeleton：**Nexus 页描述与 GitHub 仓库** —— **一手**
  （HDT-SMP 落地页：`https://www.nexusmods.com/skyrimspecialedition/mods/30872`）
- "正确仓库名是 `hdt-skyrimse-mods`，`hdt-skyrim-smp` 返回 404"：**本工作区实测（2026-09-22）**
- OpenCL 2.0 与"关 OpenCL 实为切 CPU"：Nexus 描述与社区指南 —— **一手 + 社区经验**
- 支持 1.5.97、AE 靠 fork：**社区经验（多源一致）**
