---
id: cbbe
title: CBBE（Caliente's Beautiful Bodies Enhancer）
category: 03-body
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [身形, CBBE, 女性身形, 体模]
aliases: [caliente, beautiful bodies, beautiful bodies enhancer, cbbe 身形, 女性体模]
source: https://www.nexusmods.com/skyrimspecialedition/mods/198
summary: CBBE 的作者、构成、UV 与体型选项，以及它与 BodySlide 的绑定关系与"不能与其他女性身形共存"这条硬约束。
---

# CBBE（Caliente's Beautiful Bodies Enhancer）

## 作者与命名

| 角色 | 人 |
|---|---|
| 原作者 | **Caliente**（CBBE 鼻祖，软件工程师） |
| 共同开发者 / SE 维护 | **Ousnius** |
| 重要贡献者 | **Jeir**（BodySlide 使用教程与社区支持） |

> **命名**：LE 时代叫 *Edition*，SE 页改叫 *Enhancer*。搜索时两种写法都会遇到。

- Nexus SE：`https://www.nexusmods.com/skyrimspecialedition/mods/198`（该页在成人内容墙后，需登录）
- 作者访谈（官方）：`https://www.nexusmods.com/skyrim/news/12985`

## 它是什么

女性身体网格 + 配套原版服装转换。官方描述称网格规模约 **13,554 顶点**，
约为原版的 20 倍、老版 CBBE 的 6 倍。

**必须靠 BodySlide 构建形状** —— CBBE 本体只提供"基础网格 + 滑块定义"，
你实际在游戏里看到的体型是 BodySlide 构建出来的。

## 体型选项（Shape Options）

```
Slim / Curvy / Vanilla
以上各带 NeverNude 版本
+ Underwear（黑 / 紫 / 红 / 浅蓝 / 灰 五色）
```

所有原版与 DLC 服装已转换为这三种基础体型，并能吃滑块与预设。

## UV：一条必须记住的约束

> **CBBE 有独立的 UV 映射。为 CBBE 做的皮肤贴图不能直接用在 UNP 系，反之亦然。**

错配的表现是手 / 颈 / 脚接缝、纹理错位。这不是"皮肤 mod 不好"，而是**两套 UV 本来就不兼容**。
所以选身形 = 同时选定了皮肤的可用范围。

## 硬约束：互斥

> **CBBE 不能与任何其他女性身形替换 mod 共存。**

想同时拥有"女性 CBBE"和"男性身形"是可以的（那是两条独立的链），
但**女性身形只能有一个**。

## 版本

- SE 版本号在不同二手来源里出现过 **1.6.1** 与 **1.6.2**（Nolvus 指南下载的文件名为
  `...v1.6.2-198-1-6-2-1628020768.7z`）。
- **当前最新版本：未确认** —— Nexus 页在成人内容墙后，本轮未能读取 Files 页。
  **请以 Nexus 页面为准。**

## 依赖

| 依赖 | 是否必须 |
|---|---|
| BodySlide and Outfit Studio | **是**（构建形状） |
| SKSE64 | 否（CBBE 本身是纯网格/纹理） |
| 物理（CBPC / FSMP） | 否（但 **3BA** 的物理扩展需要） |
| XPMSE | 否（但物理需要它提供骨骼节点） |

## 来源

- 作者与 SE 维护者：Nexus 采访页（`/news/12985`）+ FO4 版 BodySlide 页署名 "Created by Ousnius and Caliente" —— **一手**
- 顶点数、体型选项、需 BodySlide 构建、原版服装已转换：CBBE 描述正文（经转述引用）—— **一手（描述正文）**
- UV 独立、与 UNP 互斥：描述正文 + 社区一致确认 —— **一手 + 社区经验（一致）**
- 版本 1.6.1 / 1.6.2：**二手来源不一致，已标注未确认**
- 适用游戏版本（SE/AE 通用，1.6.1170 可用）：社区实践一致 —— **社区经验**
