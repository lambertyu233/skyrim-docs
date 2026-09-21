---
id: unreliable-sources
title: 不可信来源警示：AI 生成站会编造版本号与功能
category: 07-sources
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [警示, 谣言, AI生成, 核实, 来源可信度]
aliases: [AI 编造版本号, 假教程, 不可信来源, unreliable sources, AI 生成的假文档, 被 AI 骗]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki
summary: 实测发现部分内容农场/AI 生成站会编造不存在的版本号与功能，本文列出已知错误说法与核实方法。
---

# 不可信来源警示：AI 生成站会编造版本号与功能

## 结论先行

整理本领域资料时，**CSDN、toolify 一类内容农场/AI 聚合站不可信**——实测它们会**编造不存在的版本号和功能**（例如凭空造出 "OAR v5.0"、"State Override" 等根本不存在的东西）。请以官方页面为准。

## 已知的错误 / 可疑说法

| 说法 | 问题 | 正确口径 |
| --- | --- | --- |
| "Pandora 是 Nemesis 的 **fork/分支**" | 错误 | Pandora 是**独立实现**的新引擎，仅**兼容** Nemesis/FNIS 补丁格式（官方 wiki） |
| "OAR v5.0"、"State Override" 等 | 疑似**编造** | 官方仓库无此版本/功能；勿采信 |
| "Nemesis 完全不支持生物" | 不准确 | 官方对比表写的是 **Humans & some creatures（部分生物）** |
| "FNIS 与 Nemesis 可以一起用" | 错误 | Nemesis 官方明列 FNIS、FNIS PCEA 为**不兼容** |
| 各站给出的"最新版本号" | 常过期/杜撰 | 一律以 Nexus 页面「File information」与 GitHub releases 为准 |

## 核实方法（三步）

1. **回官方**：原理 → Pandora 官方 Wiki / README；版本 → Nexus 页面与 GitHub releases。
2. **看一手**：能追到作者本人（fore、Shikyo Kira、Pandora 团队）或官方仓库的，优先。
3. **交叉验证**：中文/俄文聚合站的说法，与官方页面对照；不一致时**信官方**。

## 本库的来源纪律

- 所有**原理性定义**均标注官方出处（页内 "> 来源" 引用块）；
- 所有**版本号/日期**均来自官方页面或仓库；
- 社区说法一律标注"（社区）"，并说明其非官方性质；
- 不引用内容农场的数字与功能名。

## 相关

- [官方来源清单](official-sources.md)
- [社区与讨论来源](community-sources.md)
