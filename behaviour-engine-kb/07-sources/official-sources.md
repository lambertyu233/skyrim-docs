---
id: official-sources
title: 官方来源清单（按阅读优先级）
category: 07-sources
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [来源, 官方, 文档, Pandora, Nemesis, FNIS]
aliases: [官方文档在哪, 动作引擎官方源, official sources, wiki 链接]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki
summary: 本领域最值得先读的官方/半官方文档清单，按"讲原理→官方页面→安装排错"三类排序，附地址与看点。
---

# 官方来源清单（按阅读优先级）

> 若时间有限：**先读 Pandora 官方 Wiki 首页**，二十分钟能把 FNIS → Nemesis → Pandora 的脉络一次理顺。

## 一、讲原理（最该先看）

| 来源 | 地址 | 看点 |
| --- | --- | --- |
| ⭐ **Pandora 官方 GitHub Wiki** | https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki | 首页两节「What is Havok Behavior™?」「What is a Behaviour Patcher?」直接回答原理问题；**三引擎对比表**在此 |
| **Pandora 仓库 README** | https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/blob/main/README.md | "parses changes to nodes in xml, serializes them into the FSMs"——最准确的技术描述；含安装、启动参数、作者向补丁格式 |
| **Pandora Wiki：Performance Notes** | https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki/Performance-Notes | 预加载/浅映射/增量序列化——"为什么更快"的官方解释 |
| **Pandora Wiki：Graph Injection** | https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki/Graph-Injection | 图注入（实验性） |
| **fore 本人 2012 年原帖** | https://forums.nexusmods.com/topic/747532-dawnguard-dlc-crossbow-questions/ | **一手**："behavior 目录下的 hkx 不是动画文件；hkx 只是包格式，连骨骼也压在里面"——"hkx 有两种"说法的源头 |

## 二、官方页面与作者文档

| 来源 | 地址 | 看点 |
| --- | --- | --- |
| **FNIS** | https://www.nexusmods.com/skyrim/mods/11811 | — Files → Miscellaneous →「**FNIS for Modders Documentation 6.2**」⭐ 是 fore 写的最一手文档（AnimList 语法、动画注册）；— Docs 讲 FNIS Spells（72 个 idle 位、FNISSPc001.hkx 命名）；— 讲为何与所有改 behavior 的 mod 不兼容；— 7.6 版，2020 停更 |
| **Nemesis** | https://www.nexusmods.com/skyrimspecialedition/mods/60033 | 描述页有 **COMPLEXITY TIER LIST**（Basic→Master）；**但中级以上无公开文档**，需 Discord 联系作者 |
| **Pandora** | https://www.nexusmods.com/skyrimspecialedition/mods/133232 | 描述页 + 官方安装指南；页面写明"Check the wiki if you'd like to contribute or write plugins" |

## 三、安装与排错教程

| 来源 | 地址 | 看点 |
| --- | --- | --- |
| **STEP Modifications · Pandora** | https://stepmodifications.org/wiki/SkyrimSE:Pandora_Bahavior_Engine | MO2 下 Pandora 的 STEP 标准做法 |
| **Nexus Article #12319**「Extremely Detailed Pandora Install Guide」 | https://www.nexusmods.com/skyrimspecialedition/articles/12319 | Vortex / MO2 两套完整步骤 |
| **The Phoenix Flavour · Nemesis** | https://thephoenixflavour.com/tpf/finalisation/nemesis | MO2 输出文件夹设置讲得很细 |
| **Gate to Sovngarde Wiki · Nemesis** | https://gatetosovngarde.wiki.gg/wiki/Nemesis | 附"该勾选哪些补丁"的完整清单 |
| **GamerPoets 视频（YouTube）** | — | Nemesis 的 MO2 / Vortex 安装，公认入门参考 |

> 注：STEP 页面的 URL 拼写为 `Pandora_Bahavior_Engine`（官网原样，非笔误）。

## 相关

- [社区与讨论来源](community-sources.md)
- [不可信来源警示](unreliable-sources.md)
