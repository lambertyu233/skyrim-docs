---
id: nemesis-complexity-tiers
title: Nemesis 复杂度分级（Basic → Master）
category: 03-nemesis
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [Nemesis, 复杂度, 分级, 文档, 用户责任]
aliases: [Nemesis 分级, Nemesis basic master, nemesis tier, 复杂度等级, Nemesis 选项怎么选]
source: https://www.nexusmods.com/skyrimspecialedition/mods/60033
summary: Nemesis 官方描述页给出的四档复杂度清单（Basic/Intermediate/Expert/Master）及对应的用户责任，是理解框架设计意图的官方文本。
---

# Nemesis 复杂度分级（Basic → Master）

Nemesis 官方描述页把使用者按能力分为四档，并为每档列出"能做什么"与"要承担什么责任"。这是理解该框架设计意图的第一手材料。

## COMPLEXITY TIER LIST（能做什么）

| 档位 | 内容 |
| --- | --- |
| **Basic** | 安装 mod 并打补丁 |
| **Intermediate** | 生成行为补丁；用动画模板创建新动画；用行为模板创建新行为 |
| **Expert** | 为中级用户制作行为模板；为中级用户制作动画模板；把新行为**注册进 Nemesis 框架**（以使用框架提供的功能） |
| **Master** | 改进本框架的代码；为本框架添加新功能；修复系统级 bug（Nemesis 内部） |

## USER'S RESPONSIBILITY（要承担什么）

| 档位 | 责任 |
| --- | --- |
| **Basic** | 自行研究学习；提问前先在公共场合发帖；**读错误信息**并先自行在互联网/文档找解决方案；知道该联系谁再私信 |
| **Intermediate** | 必要时**更新自己的补丁**（可能因版本不兼容）；更新动画查询以修复问题（可能因底层模板被专家级用户更新） |
| **Expert** | 维护/排错/修复自己创建的行为模板与动画模板；**模板必须采用开放免费许可证**以保证社区长期支持；不要给各级用户制造额外困惑 |
| **Master** | 尊重 GPLv3、描述清晰易懂、尊重社区意愿、遵循框架设计原则 |

> 来源：Nemesis Nexus 描述页 https://www.nexusmods.com/skyrimspecialedition/mods/60033

## 这套分级说明了两件事

1. **"模板"是本框架扩展性的核心**：Expert 档的核心工作就是"做模板并注册进框架"。这正是 Nemesis 相比 FNIS 能支持任意动画类型的机制来源。
2. **官方对文档的态度很明确**：Basic 档被要求"先读错误信息、先自己找答案"。这与后文 [Nemesis 的局限](nemesis-limitations.md) 中"中级以上无公开文档"直接相关。

## 框架设计原则（官方原文要点）

- 在保护所有者版权的同时，**允许用户自由修改和分发补丁**；
- 对普通用户快速易用；
- 足够强大以实现复杂功能；
- **采用分层复杂度系统**以服务不同类型用户。

## 相关

- [Nemesis 概览](nemesis-overview.md)
- [Nemesis 的局限](nemesis-limitations.md)
