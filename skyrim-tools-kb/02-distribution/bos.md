---
id: bos
title: Base Object Swapper (BOS)
category: 02-distribution
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [分发, SKSE, 免冲突, 替换, base form, powerofthree]
aliases: [Base Object Swapper, 替换模型, 运行时替换, 换模型不建补丁]
source: https://github.com/powerof3/BaseObjectSwapper
summary: 在运行时把某个 base form 换成另一个的框架——改外观、换变体而不编辑记录，从而不必与原 mod 打补丁。
---

# Base Object Swapper (BOS)

## 官方定位（仓库 README）

> **"SKSE/SKSEVR plugin and framework that allows swapping base forms at runtime"**

它做的事：把场景里引用某个 base form（如"某张桌子""某棵树的某变体"）
的引用，在**运行时**替换成另一个 base form。于是：

- 你改了外观/模型，却**没有编辑任何记录** → 与原 mod 零冲突；
- 多个 BOS 配置可以**叠加**（这依赖其配置的匹配机制，见下）。

## 版本与能力（官方 Releases）

- 最新 Release 为 **v3.4.1（2025-07-16）**，License **MIT**。
- 版本演进中新增的能力包括：
  - 支持 **多个 base form + 随机分配**（v3.2.0）；
  - 支持 `baseFormID1,baseFormID2|swapFormID|...` 形式的常规替换（v3.3.0）；
  - v3.4.1 修复了「引用未保存原始文件」的问题（`Workaround for references not storing original file`）。
- **支持 VR**（README 里列出 SSE/AE 与 VR 两套 Address Library 要求）。

> 引用具体版本号时**请核对 Releases 页**——本文数字取自 2025-07 的官方 Releases 列表。

## 典型用途

- 替换场景物件的模型/材质（桌椅、路牌、容器）而不做补丁；
- 给随机生成的物件加变体（配合随机分配）；
- 让某个 mod 的替换效果与"改同一物件"的其他 mod 共存。

## 常见误解

- **"BOS 和 SPID 是一回事。"** 不是。SPID 面向 **NPC** 分发内容，BOS 面向 **base form** 做替换。
- **"用了 BOS 就完全不会冲突。"** 它消除的是**记录级**冲突；
  若两个 BOS 配置命中同一引用，仍会按匹配规则决出结果，需要看 log。

## 相关

- [Spell Perk Item Distributor (SPID)](../02-distribution/spid.md)、[Keyword Item Distributor (KID)](../02-distribution/kid.md)
- [Address Library for SKSE Plugins](../01-frameworks/address-library.md)
- [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)（确认某个物件原本来自哪个插件）
