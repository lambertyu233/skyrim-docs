---
id: bodyslide-presets
title: 身形预设（SliderPresets）
category: 03-body
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [身形, 预设, BodySlide, 分享]
aliases: [bodyslide 预设, sliderpreset, 身形预设, 预设 xml, 体型预设]
source: https://github.com/ousnius/BodySlide-and-Outfit-Studio/wiki/Creating-a-BodySlide-project
summary: 身形预设的文件形态与存放位置、自带预设与社区生态、它如何被 OBody NG 与 RaceMenu BodyGen 二次引用。
---

# 身形预设（SliderPresets）

## 形态与位置

预设就是 `SliderPresets/` 下的 **`.xml`** 文件，保存一组命名过的滑块值
（完整路径 `Data\CalienteTools\BodySlide\SliderPresets\`）；
另有 `SliderGroups/*.xml` 定义分组。

**XML 的结构要点**：每个滑块**存两个值** —— 体重 0 一个、体重 100 一个。
所以 BodySlide 预设天然描述「同一个体型在不同体重下的样子」；
游戏里一个体重 50 的 NPC，拿的就是这两个值**线性插值**的结果。

> ⚠️ **BodySlide 预设（`.xml`）与 RaceMenu 预设（`.jslot`）是完全不同的两种文件**：
> 刻度不同（0~100 vs 浮点）、生效方式不同（烘焙 vs 运行时），**不能互相导入**。
> 对照见 [`morph-runtime-vs-bake.md`](morph-runtime-vs-bake.md)。

制作方式：在 BodySlide 里调好滑块 → **Save As** → 存到 `SliderPresets/` →
立刻出现在预设下拉框里。

## 自带预设

| 来源 | 自带内容 |
|---|---|
| CBBE | Slim / Curvy / Vanilla，及对应的 outfit 变体 |
| CBBE 3BA / 3BBB | 随包附带大量预设 |
| BHUNP | 随包附带，数量略少于 3BBB（社区共识） |

## 社区生态

- 通过 Nexus 的 *BodySlide Preset* 分类或 LoversLab 分享；
- 可举证被引用的个人作者例子：**Mousebell**（3BA 玩家预设）；
- **"最流行的预设作者"会随时期变化，不宜写死**，引用时请附日期与来源链接。

## 预设如何被"再引用"

这是本条目最实用的部分：**预设名是上游配置的键**。

| 消费方 | 配置文件 | 引用方式 |
|---|---|---|
| **OBody NG** | `SKSE/Plugins/OBody_presetDistributionConfig.json` | 按 `raceFemale` / `raceMale` / 黑名单等规则指定可用预设 |
| **RaceMenu BodyGen** | `meshes/actors/character/BodyGenData/<插件名>/templates.ini` | `模板名=morph@值 \| morph@区间` |
| **AutoBody** | `morphs.ini` | 用 EditorID 匹配（如 `All\|Female\|TownWhiterunFaction`） |

所以"给 NPC 分配不同身材"**本质上就是引用你的 BodySlide 预设名**。
预设命名杂乱会让 L4 分配层很难配置 —— 建议**统一命名规范**。

详见 [`../05-distribution/obody-ng.md`](../05-distribution/obody-ng.md) 与
[`../05-distribution/racemenu-bodygen.md`](../05-distribution/racemenu-bodygen.md)。

## 一条实践纪律

> **裸身与服装必须用同一个预设构建。**
> 裸身用 Curvy、服装用 Slim，结果是穿模 —— 这是穿模问题最常见的自伤原因。

排查详见 [`../06-troubleshooting/clipping.md`](../06-troubleshooting/clipping.md)。

## 来源

- 预设文件位置与"Save As 即出现"：BodySlide 官方 wiki —— **一手**
- 自带预设与社区生态、Mousebell："**社区经验**，随时期变化"
- 预设被 OBody NG / BodyGen / AutoBody 引用：各工具官方配置说明 —— **一手**
