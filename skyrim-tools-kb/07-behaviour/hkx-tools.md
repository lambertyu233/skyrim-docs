---
id: hkx-tools
title: hkx 文件工具（动画与行为文件）
category: 07-behaviour
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [动画, hkx, 文件格式, 转换, 工具]
aliases: [hkxcmd, HKX 转换, 动画文件, 行为文件, 打包 hkx, havok]
source: https://dyndolod.info/DynDOLOD-Reference
summary: 处理 Havok 打包格式（.hkx）的几个工具入口：LE↔SE 转换、打包/解包，以及为什么绝大多数改造只需要「改名」而不需要动内容。
---

# hkx 文件工具

## 先建立心智模型

`.hkx` 是 **Havok 的打包格式**，Skyrim 用它承载两类东西：

- **动画文件**：单个动作的骨骼曲线（`meshes\actors\...\animations\*.hkx`）
- **行为文件**：状态机与事件图（`meshes\actors\character\behaviors\*.hkx`）

**它们是同一个容器格式，但语义完全不同**——一个改动作，一个改逻辑。
判断属于哪类，看它在目录树里的位置。

## 三条可复用的事实

1. **hkx 标签 `hk_2010.2.0-r1` LE/SE 共用**——所以**不能靠标签判断版本**，
   必须与一个已知可用的 SSE 动画逐字节对比，或看它能否被游戏加载。
2. **LE 的动画直接拿到 SE 通常不可用**，需要转换（见下）。
3. **改造现成动画包时，99% 的情况不需要动内容**：
   把文件**改名成目标状态请求的原始文件名**、放到对应目录即可。
   内容是给引擎读的，文件名才是"钥匙"。

## 工具入口

| 需求 | 用什么 |
|---|---|
| **LE → SE 转换** anim/hkx | **Cathedral Assets Optimizer**（它的 Animation 页专做 `.hkx` 转换）→ [Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md) |
| 打包/解包 hkx | 社区命令行工具（如 `hkxcmd` 一类），用于把 xml ↔ hkx 互转以查看/编辑 |
| 改行为（新增动画事件） | **不要手改 hkx**——用 FNIS / Nemesis / Pandora，见 `behaviour-engine-kb` |
| 换动画（同一事件换文件） | **OAR / DAR**，见 `oar-kb` |
| 从 bsa 里取 hkx | BSA 工具 → [BSA / BA2 归档工具](../05-assets/archive-tools.md) |

> ⚠️ 本条目**刻意不给出具体命令行参数**：这类工具由社区接力维护、命令片段版本差异大，
> 二手转述极易出错。需要命令行时请去工具自身的发布页/仓库看 README。

## 排错提示

- **改了没效果**：先核对**文件名**是否是游戏在该状态下请求的那个（最常见原因），
  再查 OAR 的**条件**是否命中。
- **双份生效**：旧的 DAR 目录还在 `meshes\` 下 → 必须移出。
- **动画不动/摆大字**：多半是行为引擎没跑（FNIS/Nemesis/Pandora），或新增动画未注册。

## 相关

- [原理](../../behaviour-engine-kb/01-principles/)（Havok Behavior = 非确定性有限状态机）
- [实战](../../oar-kb/08-practices/)（改造方法论）
- [Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md)（LE→SE 资产转换）
