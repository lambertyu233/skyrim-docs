---
id: mo2-override-rules
title: MO2 覆盖规则（左栏 vs 右栏）
category: 07-workflow
kind: concept
version: 1.0.0
updated: 2026-09-22
tags: [安装, MO2, 覆盖, 优先级, 冲突, VFS]
aliases: [左栏 右栏, 覆盖顺序, mod organizer, 虚拟文件系统]
source: https://forums.nexusmods.com/topic/5755942-the-dark-faces-bug-how-to-fix-it/
summary: MO2 的左栏（资产优先级）与右栏（插件顺序）是两件独立的事，以及"两者不一致"为什么会造成黑脸这类"找不到原因"的故障。
---

# MO2 覆盖规则

> 本工作区另有专门讲 MO2 与 USVFS 机制的资料库（`mo2-usvfs-kb`）。
> 本条目只讲**与捏脸/身形直接相关**的那部分。

## 两个面板是两件事

| | 左栏（Mods） | 右栏（Plugins） |
|---|---|---|
| 控制什么 | **资产覆盖**：`.nif` / `.dds` / `.hkx` 等文件谁覆盖谁 | **插件加载顺序**：`.esp` / `.esm` / `.esl` 的记录谁赢 |
| 机制 | 虚拟文件系统（VFS）把文件投影进游戏 | 记录级的"后加载者胜" |
| 由谁决定 | 你手动拖 | 常由 LOOT 决定 |

**它们互不影响。** 左栏放得很好的 mod，右栏仍可能在记录层面输掉。

## 为什么这条值得单独写一条

因为**黑脸、脖缝、穿模这三类"查不出原因"的故障，根源常常就在这条不一致上**。

以黑脸为例：

1. 修改 NPC 记录的 mod（假设是 A）在**右栏赢了** → 引擎按 A 的 head parts 去找 FaceGen；
2. 但 A 的 FaceGen 文件在**左栏输了**，被另一个 mod B 的同 FormID 文件覆盖；
3. 于是 head parts 与头网格对不上 → **脸变黑**。

**只看一个面板永远查不出来。**

## 实用的排查动作

1. 打开 MO2 的 **Conflicts** 面板：
   - **红色 = 这个 mod 覆盖了别人**；
   - **绿色 = 这个 mod 被别人覆盖**；
2. 定位到相关 FormID 的 `.nif` / `.dds`，看是谁覆盖了谁；
3. **必要时用 `hide` 隐藏冲突文件**（保留 mod，只排除那一个文件）；
4. 用 **SSEEdit** 看记录层面谁赢了，与资产层面是否一致。

## 与身形/皮肤的覆盖关系

| 资源 | 谁应该覆盖谁 |
|---|---|
| 身形网格 | 你的身形 mod 应**覆盖**原版与其他身形（但只能启用一个身形 mod） |
| 皮肤贴图 | 皮肤 mod 应在身形**之后**（覆盖） |
| BodySlide 输出 | 应在最终 Data 中**胜出**，否则 `BODYTRI` 丢失 |
| FaceGen | NPC 美化 mod 的 FaceGen 应在其他 FaceGen 之前（覆盖） |

**BodySlide 输出要放进 MO2 的 Overwrite 或一个专门的 mod 文件夹**，
不要直接写进游戏目录 —— 否则它会绕开 VFS 的覆盖关系。

## Wabbajack 列表的特殊纪律

Wabbajack 装出来的列表是一个**封闭的 MO2 实例**：
**不要把自己的 mod 叠上去** —— 列表更新会清掉额外添加的 mod。
详见 [`wabbajack.md`](wabbajack.md)。

## 来源

- 左栏 = 资产优先级、右栏 = 加载顺序，二者独立：MO2 机制说明与社区 cheatbook —— **一手（工具机制）+ 社区经验**
- "左栏右栏不一致 → 黑脸"：Nexus 论坛 Black-Face 讨论 —— **社区经验（多帖一致）**
- Conflicts 面板红/绿含义、用 hide 排除单文件：
  Nexus Black-Face Fix Guide（`mods/77338`）—— **社区经验**
- Wabbajack 列表隔离、更新会清掉额外 mod：Wabbajack 官方文档 —— **一手**
  `https://wiki.wabbajack.org/user_documentation/Installing%20a%20Modlist.html`
