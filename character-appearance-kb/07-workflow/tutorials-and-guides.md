---
id: tutorials-and-guides
title: 教程与指南资源评估
category: 07-workflow
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [安装, 教程, 指南, 来源评估]
aliases: [看哪个教程, 学习资源, guide, 视频教程]
source: https://stepmodifications.org/wiki/SkyrimSE:0.1.0
summary: 外部教程的分级与两个常见的走错路（modding.wiki 不托管 STEP、内容农场的"2026 完整指南"），以及每条资源的适用场景。
---

# 教程与指南资源评估

## 推荐（按可信度）

| 资源 | 性质 | 适用 |
|---|---|---|
| **STEP Guide**（`stepmodifications.org/wiki/SkyrimSE:0.1.0`） | 社区标杆级"从零到稳定"指南 | 想系统建一套稳定环境 |
| **Wabbajack 官方文档**（`wiki.wabbajack.org`） | 自动安装与排错 | 想跳过装配 |
| **GamerPoets**（`gamerpoets.com`） | MO2 / BodySlide / RaceMenu 的实操演示 | 需要"看别人点一遍" |
| 各 mod 的 Nexus 描述页 | **最权威的一手材料** | 任何具体问题 |

## 两个常见的走错路

### ① `modding.wiki` 不托管 STEP 的 Skyrim SE 指南

实测该域名下的 `Skyrim_Special_Edition`、`Guide:Mod_Organizer`、`SkyrimSE:0.1.0`
三个页面**都返回 Page Not Found**。

**STEP 的官方 wiki 是 `stepmodifications.org`。** 这是一个容易走错的路 ——
`modding.wiki` 这个名字听起来太像"modding 的官方 wiki"了。

（本工作区另有基于 `modding.wiki` 的资料库，说明该域名确实有内容，
但**它不承载 STEP 的 SE 指南**。）

### ② 内容农场的"完整指南"

搜索"Skyrim 2026 完整指南"之类时，会大量命中一类页面：
域名陌生、标题夸张（"16K 视差""全光追""终极方案"）、
正文结构工整但**没有任何具体版本号与文件路径**。

这类站点包括但不限于：`tsight.io`、`gifpow.com`、`2023game.com`、
`maoxu.com`、`bajiujiu.com`、`233leyuan.com`，以及部分门户的转载号。

**判据**：真正的 mod 文档**一定会有版本号、文件路径、Nexus 链接**。
一个说不清"你该装哪个版本的 BodySlide"的教程，不是教程。

见 [`../08-sources/unreliable-and-unconfirmed.md`](../08-sources/unreliable-and-unconfirmed.md)。

## 一条实用建议

> **遇到冲突的说法时，去读 Nexus 描述正文或 GitHub README。**
>
> 教程会过期、会转述失真、会夹杂作者个人偏好；
> mod 发布页与仓库 README 是**发版者本人在维护**的，且随版本更新。
> 本资料库所有条目的"一手"标记，指向的都是后者。

## 来源

- STEP 官方 wiki 与页面可达性：**本工作区实测（2026-09-22）**
  `https://stepmodifications.org/wiki/SkyrimSE:0.1.0`
- Wabbajack 文档：`https://wiki.wabbajack.org/` —— **一手**
- GamerPoets：`https://www.gamerpoets.com/` —— **社区资源**
- 内容农场域名清单：**本工作区检索过程中识别并排除的域名**
