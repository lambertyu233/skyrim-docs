---
id: ube
title: UBE 2.0（新世代身形 base）与"三套并行"局面
category: 03-body
kind: concept
version: 1.0.0
updated: 2026-09-30
tags: [身形, UBE, 生态, 新一代, bodybase]
aliases: [ultimate body enhancer, 新身形, 身形标准, 三套并行, 新一代身形]
source: https://www.nexusmods.com/skyrimspecialedition/mods/143045
summary: UBE（Ultimate Body Enhancer）2.0 是继 CBBE/3BA 之后的新一代身形 base；当前真实局面是新 mod 同时提供 3BA / HIMBO / UBE 三套 BodySlide 文件，而不是谁取代了谁。
---

# UBE 2.0 与"三套并行"局面

## UBE 是什么

**UBE = Ultimate Body Enhancer**，当前主线版本 **2.0**（Nexus 上的完整名常写作
**"UBE 2.0 -- Ultimate Body Enhancer 2.0"**）。

它是一个**身形 base（bodybase）**，与 CBBE / UNP 是同一层级的概念 ——
不是某个预设，也不是某个物理方案。Nexus 的 mod 标签体系里直接有 **`UBE Bodybase`** 这一标签，
与 `CBBE Bodybase`、`UNP Bodybase`、`UNPB Bodybase`、`TBD Bodybase` 并列。

## ⭐ 重点：不是"取代"，而是"并行"

社区里容易听到的说法是"UBE 取代了 3BA"。**本轮取证不支持这个说法。**

实际观察到的现象是：**新出的盔甲/衣服 mod 会同时提供三套 BodySlide 文件**：

```
Additional Bodyslide files for 3BA, HIMBO and UBE
```

且发布页把三者都列为**可选前置（OPTIONAL）**，互相不覆盖：

| 身形 | 性别侧 | 性质 |
|---|---|---|
| **CBBE 3BA (3BBB)** | 女性 | 当前主流，带物理 |
| **HIMBO** | 男性 | 当前主流（见 [`himbo.md`](himbo.md)） |
| **UBE 2.0** | 女性 | 新世代 base，逐步被新 mod 支持 |

**推论**：选型时按"我要给哪个身形穿这套甲"来挑，**不要为了"追新"把 3BA 换掉**。
三套文件的存在恰恰说明作者们不做取舍。

## 怎么判断该用哪个

1. **看你已有的身形。** 身形 base 决定裸体网格与 UV；盔甲必须匹配你选的 base。
2. **看 mod 提供了哪套。** 只提供 3BA 的甲，装在 UBE 身上会穿模或贴图错位。
3. **不要混装多个 base 的裸体网格。** 裸体网格只能有一个赢家（覆盖规则见
   [`../../mo2-usvfs-kb/`](../../mo2-usvfs-kb/) 相关条目）。

## 已知未确认项

| 事项 | 状态 |
|---|---|
| **UBE 2.0 的作者** | **未确认**（发布页在内容墙后，本轮未取得署名） |
| **UBE 2.0 的 Nexus mod ID 与版本号** | **未确认** |
| UBE 是否自带物理、与 3BA 的物理方案是否兼容 | **未确认** |
| UBE 与 CBBE 纹理能否互换 | **未确认** |

> 这几项**不要凭印象补**。需要时在 Nexus 站内按 **"Ultimate Body Enhancer"**
> 或标签 **`UBE Bodybase`** 检索。

## 为什么把"未确认"写这么满

因为身形领域最容易发生的事，就是**把某个新 base 的传闻当成现状**，然后照着装、装完穿模。
本库 [`../08-sources/unreliable-and-unconfirmed.md`](../08-sources/unreliable-and-unconfirmed.md)
里已经收录了一批这类误传。在拿到一手来源之前，**"未确认"比"猜一个"有用得多**。

## 来源

- UBE 全称 **UBE 2.0 -- Ultimate Body Enhancer 2.0**、与 3BA/HIMBO 并列为可选前置：
  Iron Rose Armor 发布页 Requirements 段 —— **一手**
- Nexus 存在 `UBE Bodybase` 标签，与 `CBBE Bodybase` / `UNP Bodybase` / `TBD Bodybase` 并列：
  Nexus 标签体系 —— **一手**
- "3BA / HIMBO / UBE 三套 Bodyslide 文件同时提供"：Iron Rose Armor 发布页正文 —— **一手**
