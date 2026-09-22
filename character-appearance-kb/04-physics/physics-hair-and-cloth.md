---
id: physics-hair-and-cloth
title: 物理头发与衣物
category: 04-physics
kind: concept
version: 1.0.0
updated: 2026-09-22
tags: [物理, 头发, 衣服, SMP, 斗篷]
aliases: [物理头发, 物理衣服, hdt 头发, 假发, cloth physics, 斗篷物理]
source: https://github.com/DaymareOn/hdtSMP64
summary: 头发与衣物物理为什么"只能靠 SMP"、它们靠什么文件工作、以及常见的失败表现与排查手段。
---

# 物理头发与衣物

## 核心事实

> **CBPC 不能管理头发和衣服的物理，必须用 HDT-SMP（实际是 FSMP）。**

原因是机制性的：CBPC 用"骨骼上的球/胶囊"近似，而头发与衣物的形变
本质是**网格顶点级别的摆动**，需要 SMP 的逐顶点蒙皮模拟。

所以"我装了 CBPC 但头发不动"不是配置问题，是**方案选错了**。

## 它们靠什么文件工作

SMP 通过 **`Data/SKSE/Plugins/hdtSkinnedMeshConfigs/`** 下的 XML
为 hair / cloth 网格定义碰撞体并挂到骨骼上。

典型情况：

- 每个物理发型/衣物 mod **自带** XML（如物理版 KS Hairdos 之类）；
- **没有 XML 就没有物理** —— 这是"某件斗篷死活不飘"的第一嫌疑；
- 遵循 SMP Modder Guide 的 XSD/Schematron schema。

## 挂点

通常挂到头部骨骼（`Head`）及额外发骨；XPMSE 提供相关节点（见
[`xpmse-skeleton.md`](xpmse-skeleton.md)）。

> 已知限制：FaceGen 相关的 HDT 头骨有约束（NPC head parts 方向），
> 所以"给 NPC 换物理发型"比给玩家换更容易出问题 —— **社区经验**。

## 排查手段

FSMP 提供了一个直接的工具：

```
smp report [warnings] [gear]
```

它会**校验整个 load order 的物理 XML 与 `.nif`** 并给出警告。
出问题时先跑它，而不是逐个 mod 试。

## 常见失败表现

| 表现 | 可能原因 |
|---|---|
| 头发完全不动 | 只装了 CBPC；或该发型没有 XML；或 SMP/FSMP 未生效 |
| 头发穿过身体 | 碰撞体没定义或不匹配身形 |
| 头发抽搐/抖动异常 | XML 参数问题（可用 `smp report` 找） |
| 衣服飘但头发不飘 | 只有衣服带了 XML |
| 开局 CTD | SMP/FSMP 版本档选错 |

## 来源

- "CBPC 不能管头发或衣服，必须有 SMP"：LoversLab 帖 —— **社区经验（多帖一致）**
- XML 目录、schema、`smp report` 命令：FSMP 官方仓库 README / wiki —— **一手**
  `https://github.com/DaymareOn/hdtSMP64`
- 挂到 Head 及额外发骨、FaceGen HDT 头骨限制：Karonar1 的 hdtSMP64 README —— **社区技术文档**
- 失败表现与成因：综合社区帖归纳 —— **社区经验**
