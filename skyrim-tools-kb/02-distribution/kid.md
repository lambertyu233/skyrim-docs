---
id: kid
title: Keyword Item Distributor (KID)
category: 02-distribution
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [分发, SKSE, 免冲突, 关键词, powerofthree]
aliases: [Keyword Item Distributor, 关键词分发, 给装备加keyword, 物品关键词]
source: https://github.com/powerof3/Keyword-Item-Distributor
summary: SPID 的「物品版」：用配置文件给护甲/武器/弹药批量挂关键词，让依赖关键词的 mod 能作用于新装备，而无需编辑任何记录。
---

# Keyword Item Distributor (KID)

## 官方定位

仓库 README 原文只有一句：**"Distributes keywords to items (armor/weapons/ammo)"**。

覆盖面比 SPID 窄，但解决的是同一个结构性问题：
一大批 mod 靠**关键词**判定"这件装备属于什么"（轻甲类、可附魔、属于某套装…）。
新装备 mod 如果没被挂上对应关键词，那些 mod 就**看不见它**——
表现为"新盔甲不吃某某系统的效果"。

传统解法是做一个补丁插件，把关键词加进装备记录 → **又是一次记录级冲突**。
KID 改成运行时分发，配置写在 `Data/` 下的 `_KID.ini` 一类文件里。

## 与 SPID 的分工

| | SPID | KID |
|---|---|---|
| 分发对象 | **NPC**（法术/技能/物品/服装/派系…） | **物品**（护甲/武器/弹药） |
| 配置后缀 | `_DISTR.ini` | KID 自己的配置文件 |
| 共同点 | 不编辑记录、纯文本配置、加载时应用 | 同左 |

两者是**互补**关系，常同时出现：KID 给装备挂关键词，SPID 把装备发给 NPC。

## 细节（来自官方仓库）

- License：**MIT**。
- 官方 Requirements：`Address Library for SKSE`（SSE）/ `VR Address Library for SKSEVR`（VR）。
- 构建使用 CommonLibSSE（作者的 `powerof3/dev` 分支），是**现代 CommonLibSSE-NG** 的前身实践。
- 仓库里含 verbose logging 相关的配置项——排查"某条配置没生效"时可开详细日志。

## 常见症状

| 症状 | 排查 |
|---|---|
| 新装备不吃某系统的效果 | 是该系统靠关键词判定 → 用 KID 挂上关键词 |
| 配置文件改了没反应 | 与 SPID 一样需要**重新加载存档** |
| 某条配置报错 | 开启详细日志，看具体是哪一行没解析 |

## 相关

- [Spell Perk Item Distributor (SPID)](../02-distribution/spid.md)、[Base Object Swapper (BOS)](../02-distribution/bos.md)
- [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)、[Address Library for SKSE Plugins](../01-frameworks/address-library.md)
