---
id: havok-behavior
title: Havok Behavior 是什么：FSM 与 hkx 包文件
category: 01-principles
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [Havok, FSM, hkx, 中间件, 原理]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki
summary: Havok Behavior 是一套用非确定性有限状态机控制动画逻辑的专有中间件，状态机序列化进 .hkx 包文件——这是所有动作引擎的底层对象。
---

# Havok Behavior 是什么：FSM 与 hkx 包文件

## 官方定义

Pandora 官方 wiki 的「What is Havok Behavior™?」一节给出的是一手定义：

> Havok Behavior is a proprietary middleware software for controlling animation logic in video games through non-deterministic finite state automata. These automata are serialized in pack files with the `hkx` extension using a custom binary format, which hkxcmd and hkx2 can unpack.
> （Havok Behavior 是一套专有中间件，用**非确定性有限状态自动机**控制游戏中的动画逻辑。这些自动机以自定义二进制格式序列化进扩展名为 `hkx` 的包文件，可用 hkxcmd 与 hkx2 解包。）

同页还列出了社区用来编辑这些包文件的代表性工具：**Zartar's Behaviour Tool** 与 **Haviour**。

> 来源：Pandora 官方 Wiki https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki

## 拆开看几个关键词

- **中间件（middleware）**：不是游戏本体，而是被游戏调用的第三方组件。Skyrim 用它决定"什么时候播哪段动画、怎么过渡、什么条件下允许被打断"。
- **非确定性有限状态机（FSM）**：行为文件本质是一张巨大的状态图，节点 = 状态/事件/过渡，边 = 转移条件。所谓"非确定性"指同一输入下可能有多种转移分支，由引擎按规则裁决。
- **序列化（serialize）**：内存中的对象树 ↔ 二进制包文件的相互转换。Havok 的原始创作格式是 **xml**，最终被转成"打包"的二进制 `.hkx`。
- **`.hkx` 扩展名**：见 [hkx 其实有两种](hkx-two-kinds.md)。

## README 层面的技术描述

Pandora 仓库 README 给出了更接近实现的一段：

> Havok Behavior (`hkb`) and Havok Animation (`hka`) consist of multiple non-deterministic finite state machines, serialized in xml before being converted to "packed" binary files (`.hkx`). This program parses changes to nodes in xml, serializes them into the FSMs using native DTOs, validates nodes, and then outputs the files in a game-ready binary format.
> （Havok Behavior（`hkb`）与 Havok Animation（`hka`）由多个非确定性有限状态机组成，先序列化为 xml，再转成"打包"二进制文件（`.hkx`）。本程序解析 xml 中的节点变更，用原生 DTO 将其序列化进 FSM，校验节点，最后输出游戏可用的二进制格式。）

> 来源：Pandora 仓库 README https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/blob/main/README.md

这段话其实就是**补丁器的工作原理**：`xml 节点变更 → 序列化进 FSM → 校验 → 输出二进制`。详见 [行为补丁器原理](behaviour-patcher.md)。

## 为什么必须"补丁"而不能"覆盖"

Skyrim 的行为文件对 mod 极不友好：它是一棵互相引用的巨大对象树，**两个 mod 同时改同一个行为文件几乎必然冲突**（谁后加载谁整个覆盖前者）。fore 在 2012 年就点破了这个结构性难题——这正是"补丁器"范式诞生的原因。

## 相关

- [hkx 其实有两种：行为文件 vs 动画文件](hkx-two-kinds.md)
- [行为补丁器原理](behaviour-patcher.md)
- [动画数据库与事件名机制](animation-database.md)
