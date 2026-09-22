---
id: obody-ng
title: OBody NG（Next Generation）
category: 05-distribution
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [分配, OBody, 预设分发, NPC 身形, JSON]
aliases: [obody ng, 身形分发, preset distribution, 随机分配身形, aietos]
source: https://www.nexusmods.com/skyrimspecialedition/mods/77016
summary: OBody 与 OBody NG 的作者沿革、ORefit 算法与 JSON 配置、依赖清单（并澄清它不直接依赖 SPID/JContainers），以及它相对 BodyGen 的优势。
---

# OBody NG

## 作者沿革

| 版本 | 作者 |
|---|---|
| **OBody**（原始） | **Sairion350** |
| **OBody NG**（Next Generation） | **Aietos** |
| **OBody Standalone NG** | 脱离 OStim 依赖的版本 |

- Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/77016`
- GitHub（SKSE/C++ 侧）：`https://github.com/Aietos/OBody-NG`
- GitHub（Papyrus 侧）：`https://github.com/Aietos/OBody`

## 它做什么

把**你已安装的所有 BodySlide 预设**随机/按规则分发给玩家与 NPC。
核心是用 **ORefit 算法**把某套预设的滑块值"拟合"到目标 actor 上。

它基于一个 **Zeroed Sliders 参考体**——这不是可选项，而是**前提条件**：

> **必须先用 `Zeroed Sliders` 预设 + 勾 `Build Morphs`，把所有身体与服装 Batch Build 一遍。**
> OBody NG 会**读取你 `SliderPresets` 文件夹里的 `.xml` 预设**，在此基础上分配给 NPC。

所以「OBody 装了没效果 / NPC 身材没变化」的第一检查点是：
**你有没有做过那次 Zeroed Sliders 的基础构建。**

步骤见 [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

## 配置：JSON

```
SKSE/Plugins/OBody_presetDistributionConfig.json
```

支持按 `raceFemale` / `raceMale` / `blacklistedRaces` 等维度指定可用预设。
带 **MCM** 管理界面。

## 依赖

```
RaceMenu（提供 skee64 的 morph API）
MCM Helper
UIExtensions
SKSE
Address Library for SKSE Plugins
```

> **澄清两点**：
> 1. OBody NG 的配置是 **JSON**，因此**不直接依赖 JContainers**；
> 2. 它也**不依赖 SPID** —— SPID 的 Outfit Distribution 分的是"服装"，不是"身形"。

## 与 RaceMenu BodyGen 的对比

| | BodyGen | OBody NG |
|---|---|---|
| 来源 | RaceMenu 内置 | 独立 mod |
| 配置 | `.ini` | `.json` |
| 界面 | 无 | **有 MCM** |
| 配置粒度 | 模板 + 映射 | 按种族/黑名单，规则更直观 |
| 依赖 | 只需 RaceMenu | RaceMenu + MCM Helper + UIExtensions |

**给新手的建议**：如果你想"少折腾、有界面"，用 OBody NG；如果你已经在用 RaceMenu 且不想加 mod，BodyGen 够用。

## 与 AutoBody 的关系

两者都是"把预设分发给 NPC"，但：

- **配置语言不同**（OBody NG 用 `.json`，AutoBody 用 `.ini` 且语法仿 BodyGen）；
- 社区里有"OBody NG 是 AutoBody 的继任者"的说法 ——
  **这个先后关系未确认**，两者作者不同、也都在维护。

选一个用即可，**不要都装**（会争同一批 actor 的 morph）。

## 来源

- 作者沿革、ORefit 算法、Zeroed Sliders、JSON 配置路径、依赖、MCM：
  Nexus 发布页（`mods/77016`、`mods/167286`）与 GitHub README —— **一手**
- "不直接依赖 SPID/JContainers"：**本资料库对依赖链的辨析结论**
  （依据：配置格式为 JSON 而非 JContainers 容器；SPID 的 outfit 分发是另一回事）
- OBody NG 与 AutoBody 的先后关系：**社区说法不一致，未确认**
