---
id: glossary
title: 术语表
category: 00-overview
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [总览, 术语, 速查, 缩写]
aliases: [名词解释, 3BA 是什么, SMP 是什么, 什么叫 morph]
source: https://www.loverslab.com/blogs/entry/16040-glossary
summary: 捏脸与身形领域的缩写、俗称与易混词逐条对齐，每条给出"它到底指什么"以及易混对象。
---

# 术语表

## 身形（body）

| 词 | 指什么 | 易混点 |
|---|---|---|
| **CBBE** | Caliente's Beautiful Bodies Enhancer，女性身形网格，有独立 UV | 不是软件，是网格+贴图资源 |
| **UNP / UUNP** | Dimonized UNP 及其统一版；UUNP 在 SE 官方已不再支持，靠 **Legacy UUNP** 过渡 | UNP 系与 CBBE 系**互斥** |
| **UNPB** | UNP Blessed Body，UNP 的丰胸丰臀重制变体 | 属 UNP 家族，不是独立家族 |
| **BHUNP** | "UUNP Next Generation" 的 SE 版，作者 Bakafactory 与 Haeun | 属 UNP 家族；**与 CBBE 不兼容** |
| **3BBB** | 3 Breast Bones Body，带 3 根乳房骨的身体 | 这是**术语**，不是文件名 |
| **3BA** | CBBE 3BBB Advanced，作者 Acro；CBBE 的扩展，基底网格同 CBBE | 常被误当成"CBBE 的替代"，其实**同基底** |
| **HIMBO** | 男性身形（对应 CBBE 生态的男性版） | 与女性身形分属不同家族 |

## 物理（physics）

| 词 | 指什么 | 易混点 |
|---|---|---|
| **HDT-PE** | 旧方案，用游戏内建 Havok 做**骨骼级**碰撞 | 已被 SMP 取代 |
| **HDT-SMP** | Skinned Mesh Physics，用 Bullet 做**逐顶点蒙皮网格**物理 | "SMP" 单说时多指它 |
| **FSMP** | Faster HDT-SMP，SMP 的现代 fork，性能大幅提升 | **取代**原版 SMP，不要两个都装 |
| **CBPC** | CBP Physics with Collisions，用**球体/胶囊近似**做碰撞物理 | 轻量、对 CPU 友好；**管不了头发和衣服** |
| **CBP** | 旧的基础版物理（无碰撞），CBPC 的前身 | 名字像但不是同一个 |

## 机制（mechanics）

| 词 | 指什么 |
|---|---|
| **morph** | 顶点位移数据。滑块的本质就是"按权重把 morph 加到基础网格上" |
| **`.tri`** | morph 目标文件。BodySlide 勾 `Build Morphs` 后生成，RaceMenu 靠它出滑块 |
| **BODYTRI** | NIF 里的 extra data，指向对应的 `.tri` 文件 |
| **NiOverride** | RaceMenu 的运行时叠加机制（在 `skee64.dll` 内），负责在游戏内应用 morph / tint |
| **CharGen** | RaceMenu 的角色创建模块（`skee64.dll`）。**2.7+ 起 CharGen Extension 已完全并入本体** |
| **FaceGen** | 引擎的"头部预生成数据"：头网格 `.nif` + 色调 `.dds`，由 CK 的 `Ctrl+F4` 导出 |
| **tint mask** | 脸部的着色遮罩（唇色/腮红/眼线/肤色…），RACE 与 NPC 记录里逐层定义 |
| **head part / HDPT** | 面部部件数据对象（头发、眼、胡须、疤痕…） |
| **`.jslot`** | RaceMenu 的预设文件，**JSON 文本**格式；旧的二进制 `.slot` 仍可读但不再被写出 |
| **`.osp` / `.osd`** | Outfit Studio 的项目文件（`.osp` 是**纯文本 XML**）与滑块数据（`.osd` 是**二进制**） |
| **`.xml`（SliderPresets）** | BodySlide 的预设文件，存命名过的一组滑块值 |

## 前置（frameworks）

| 词 | 指什么 |
|---|---|
| **SKSE64** | Script Extender，版本必须与游戏版本精确对应 |
| **Address Library** | 让 SKSE DLL 插件跨 1.6.x 小版本通用；**SE(1.5.x) 与 AE(1.6.x) 两套地址不通用** |
| **XPMSE / XPMSSE** | XP32 Maximum Skeleton (Special) Extended，骨骼扩展，物理与身形的事实标准前置 |
| **PAPYRUS 相关** | PapyrusUtil（StorageUtil/JsonUtil）、JContainers（JSON 容器）、MCM Helper（配置菜单） |

## 来源

- LoversLab 术语表（社区整理）：`https://www.loverslab.com/blogs/entry/16040-glossary` —— **社区经验**
- 各词条的"指什么"以 Nexus 发布页描述与 GitHub README 为准 —— **一手**
- `NiOverride` / `CharGen` / `.jslot` 的定义出自 RaceMenu 发布页与 changelog —— **一手**
- `3BA` 为 CBBE 扩展、同基底网格：LoversLab 官方文件页 + 指南一致 —— **社区经验（多源一致）**
