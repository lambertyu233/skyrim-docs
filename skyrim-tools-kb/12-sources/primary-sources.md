---
id: primary-sources
title: 一手来源清单
category: 12-sources
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [来源, 一手, 权威, 出处]
aliases: [官方来源, 权威站点, 可信来源, official sources, 去哪查, 官方文档]
source: https://www.nexusmods.com/skyrimspecialedition/
summary: 本资料库采信的一手来源白名单：按「工具 → 该工具的权威出处」列出，并写明为什么它是权威。
---

# 一手来源清单

结论要能追溯到**工具作者或平台自己发布的内容**。下表是本库采信的白名单，
按"权威性等级"排列。写条目时优先引用上一级，不得引用下两级来推翻上一级。

## L1：官方文档站 / 官方 wiki

| 工具 | 出处 | 为什么权威 |
|---|---|---|
| LOOT | `loot.github.io/docs/` | 作者自建文档站，含 Introduction To Load Orders 等概念页 |
| xEdit | `tes5edit.github.io/docs/` | 官方文档站，含 cleaning 与 conflict 章节 |
| Wrye Bash | `wrye-bash.github.io/docs/` | 官方 General / Advanced / Technical Readme 全文 |
| DynDOLOD | `dyndolod.info` | 作者 elwaps 的官方站点，含 Reference 与 FAQ |
| Wabbajack | `wiki.wabbajack.org` | 官方 wiki，含安装与 list 创作文档 |
| SKSE | `skse.silverlock.org` | 唯一官方分发点，含 archived builds |
| Nexus Mods | `wiki.nexusmods.com` | 平台官方 wiki（SKSE64 安装、Vortex 使用） |
| NifSkope | `github.com/niftools/nifskope/wiki` | 官方仓库 wiki |
| Creation Kit | `ck.uesp.net` | 社区维护但被官方引用的 CK 文档（本库仅作交叉引用） |
| UESP | `en.uesp.net` | 文件格式与游戏数据的事实标准参考 |

## L2：官方代码仓库（README / CHANGELOG / 源码）

- `github.com/loot/loot`
- `github.com/TES5Edit/TES5Edit`（xEdit）
- `github.com/wrye-bash/wrye-bash`
- `github.com/Mutagen-Modding/Synthesis` 与 `Mutagen-Modding/Mutagen`
- `github.com/z-edit/zedit`
- `github.com/niftools/nifskope`、`github.com/fo76utils/nifskope`
- `github.com/Guekka/Cathedral-Assets-Optimizer`
- `github.com/alandtse/CrashLoggerSSE`
- `github.com/Nukem9/FaceFXWrapper`
- `github.com/DanRuta/xVA-Synth`、`github.com/DanRuta/xva-trainer`
- `github.com/powerof3/Spell-Perk-Item-Distributor`
- `github.com/wabbajack-tools/wabbajack`
- `github.com/expired6978/SKSE64Plugins`（RaceMenu 等）

> 仓库 README 的价值在于：作者会写**已知限制**与**版本要求**，
> 而这些恰恰是发布页常常省略的部分。

## L3：Nexus 发布页描述正文与官方论坛回帖

Nexus 发布页的 `Description` 由作者撰写，属一手；但同页的 `Posts`（用户回帖）属**社区经验**，
引用时必须标注。**例外**：作者本人在回帖里的答复可视为 L2。

## L4：作者本人渠道

- 作者 Patreon / Discord 公告（如 ElminsterAU 的 xEdit 更新说明、po3 的 Patreon）。
- 官方 Discord 的 `#wip-builds`（Wrye Bash 等）。

## 本库明确不采信

见 [不可信来源警示](../12-sources/unreliable-sources.md)：CSDN、toolify、AI 聚合站、
以及"重新托管他人 mod 并自写介绍"的镜像站（其描述常被二次创作出错误参数）。
