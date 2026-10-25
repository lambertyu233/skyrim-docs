---
id: racemenu-bodygen
title: RaceMenu BodyGen（内置身形随机化）
category: 05-distribution
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [分配, BodyGen, RaceMenu, morph, NPC 身形]
aliases: [racemenu morphs, 随机身形, npc 身形随机, morphs.ini, templates.ini, bodygen 是什么, bodygen 怎么配, bodygendata, All|Female, jbs2bg, bodygen 迁移, bEnableBodyGen, bodygen 失效, bodygen 历史, bodygen 前提]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: BodyGen 的配置目录与两份 ini 的语法（templates.ini 定义模板、morphs.ini 映射 Actor）、硬前提（BodySlide 必须勾 Build Morphs）、morph 状态写 co-save 的后果，以及向 OBody NG 迁移的建议。
---

# RaceMenu BodyGen

> **一句话**：BodyGen **不是独立 mod** —— 它是 [RaceMenu](../02-face/racemenu.md) 内置的
> 身形随机化功能（作者就是 RaceMenu 的 **expired6978**），把 **morph 组合**分发给
> NPC 与玩家，让每个 NPC 的身材不完全一样。

## 速览

| 项 | 内容 |
|---|---|
| 性质 | RaceMenu 内置功能，**无需安装额外 mod** |
| 开关 | `Data\SKSE\Plugins\skee64.ini` 的 `bEnableBodyGen`（默认 `0`，要用置 `1`） |
| 数据目录 | `meshes\actors\character\BodyGenData\<插件名含扩展名>\` |
| 两份配置 | `templates.ini`（定义模板：一组 morph 取值）· `morphs.ini`（把 ActorBase 映射到模板） |
| 硬前提 | BodySlide 必须勾 **`Build Morphs`**（否则没有 `.tri`，无从应用 morph） |
| 施加者 | RaceMenu 的 **NiOverride（`skee64.dll`）** 运行时施加 |
| 状态存储 | morph 状态写入 **SKSE co-save**（后果见专节） |
| 现状 | 仍是零依赖备选；社区主流已转向 [OBody NG](obody-ng.md) |

要点：

- **它是"零依赖"选项**：只要 RaceMenu 本身，不加任何 mod 就能让 NPC 身材多样。
- **配置是纯 ini，没有 GUI**：语法原始，改错没有报错提示——**ini 末尾必须留空行**。
- **分配状态进 co-save**：中途增删 mod、改配置，旧档的 NPC **可能不刷新**。
- **与 OBody 类工具互斥**：用后者时把 `bEnableBodyGen` 置 0，别同时开。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 未确认 | BodyGen 随 RaceMenu（LE 时代）内置发布 | morph 数据第一次被分发给 NPC |
| LE 中期 | **JBS2BG**（Nexus LE `mods/88707`）出现 | 把 BodySlide 预设转成 BodyGen 配置的 patcher 生态形成——"要跑 patcher"的由来 |
| 2018-08-06 | **RaceMenu SE 首发**（Nexus 19080） | BodyGen 进入 SE 生态 |
| 未确认 | `skee64.ini` 的 `bEnableBodyGen` 配置项 | 从"默认开"变成可开关（与 OBody 生态共存后） |
| 2021 前后 | OBody 作者称 BodyGen 为 "semi-obscure" 并将其**完全重写** | 社区重心转移的明确信号（一手：作者 Patreon 帖） |
| 2026 年 | RaceMenu 停在 0.4.20.0（面向 1.6.1170）；OBody NG 5.0 支持 1.7.x | BodyGen 仍可用，但新手指引多直通 OBody NG |

### 它从哪来

BodyGen 要解决的是"**morph 只作用于玩家**"这个缺口：RaceMenu 滑块改的是运行时状态，
NPC 不吃。BodyGen 的思路是**预定义 morph 组合（模板），再按 ActorBase 映射下去**，
让 NiOverride 在 NPC 加载时施加对应 morph——分发形态从此诞生。

### 中间经历了什么

它的短板催生了整个"分配工具"世代：**配置靠 patcher 生成**（JBS2BG）、
**只支持预设的 '100' 体重档**、**没有界面**。OBody（Sairion350）正是针对这三点
做了完全重写——读 BodySlide 预设文件夹、支持权重、后来加上 MCM。
BodyGen 本身则基本停在初始形态。

### 现状

功能仍在（RaceMenu 内置），仍是**唯一零依赖**的分配方案；但在"少折腾、有界面"的
维度上，社区默认答案已经是 [OBody NG](obody-ng.md) 或 [AutoBody](autobody.md)。

## 它解决什么问题

| 没有它 | 后果 |
|---|---|
| 只有 RaceMenu 滑块 |  morph 是**运行时状态，只作用于玩家**；NPC 身材恒定 |
| 只有 BodySlide 烘焙 | 全世界 NPC 同一个形状（按体重插值，仍无多样性） |
| **BodyGen** | 按模板把 morph 组合分发给 NPC/玩家，**零额外 mod** 获得多样性 |

机制上与 morph 两条路径的关系见
[`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)：
BodyGen 分发的仍是运行时 morph 数据，**前提依然是有 `.tri`**。

## 工作原理

```
templates.ini：模板名 = 一组 morph 取值（含随机区间）
        ↓
morphs.ini：插件|FormID（或 All|Female） = 模板名
        ↓
游戏内：NiOverride（skee64.dll）在该 actor 加载时施加模板 morph
        ↓
状态写入 SKSE co-save（持久、随存档）
```

## 安装与放置

1. **确认前置**：RaceMenu 正常（`showracemenu` 界面正常）+ BodySlide 侧已完成
   **`Build Morphs`** 构建。验证点：RaceMenu 里身形那一栏有滑块且拖了有反应。
2. **开开关**：`Data\SKSE\Plugins\skee64.ini` 里 `bEnableBodyGen=1`。验证点：进游戏不报错。
3. **放置数据**。目录名必须是**插件文件名含扩展名**（例如 `MyMod.esp`）：

```
meshes/actors/character/BodyGenData/<插件名含扩展名>/
├── templates.ini     定义"模板"（一组 morph 取值）
└── morphs.ini        把 ActorBase 映射到模板
```

   放法三选一：自己做进一个 esp 的目录 / 丢进任意现有 mod 的 meshes 路径 /
   在 MO2 里建一个只含这些文件的小 mod。验证点：目录名带扩展名、两份 ini 齐全。
4. **验证生效**：进游戏找该目录覆盖到的 NPC（先用 `All|Female` 这类批量写法最容易观察）。
   验证点：NPC 身材出现差异；改 ini 后**新遭遇的** NPC 反映变化。

> ⚠️ **改了配置，已经遇到过存档里的 NPC 可能不刷新**——状态在 co-save 里，见下节。

## 使用与配置

### `templates.ini`：定义模板

```
模板名=morph@值 | morph@区间
```

- **逗号 = AND**（同时应用）；
- **`|` = OR**（随机取一个）；
- `@` 后可以是固定值，也可以是 `a:b` 的随机区间。

例：

```
Breasts=Breast@1.0 | BreastCleavage@0.1:1.0
```

### `morphs.ini`：映射 Actor

```
Skyrim.esm|F62F0=模板名
All|Female=模板名
```

- 左边是 **插件名 | FormID**，或 **`All|Female`** 这类批量写法；
- 多个模板可用逗号组合（如 `Sevenbase,Random` 之类的用法）。

> **AutoBody 的 README 称其 EditorID 匹配"just like Bodygen"** —— BodyGen 本身是否
> 同样支持 EditorID 键，本库**未逐字确认**；社区文档以 `插件|FormID` 为准。
> EditorID/faction 匹配的扩展语法见 [autobody.md](autobody.md)。

### 两条必须记住的规则

1. **ini 末尾需留一个空行**（社区经验）。判据：不加空行时整份配置可能被解析器
   忽略——症状是"明明写好了却完全不生效"。
2. **其他 mod 的显式覆盖按加载顺序覆盖**：两个 mod 对同一个 actor 给了不同模板时，
   **后加载者胜**（MO2 里调整 mod 优先级即可控制）。

## 硬前提与"第 3 条的后果"

硬前提三条：

1. **BodySlide 必须勾 `Build Morphs`** —— 否则没有 `.tri`，RaceMenu 无从应用 morph；
2. 运行时由 RaceMenu 的 **NiOverride（`skee64.dll`）** 应用；
3. **morph 状态会写入 SKSE co-save**。

**第 3 条的后果（重要）**——因为状态在 co-save 里：

- 中途增删身形/皮肤/预设类 mod，**旧档可能对不上**（脸/身材回到默认，或出现异常）；
- 调整 BodyGen 配置后，**已有 NPC 的状态可能不会自动刷新**（需要新档或让游戏重新生成）。

这与"预设不生效"类问题高度相关，见
[`../06-troubleshooting/preset-not-applied.md`](../06-troubleshooting/preset-not-applied.md)。

## 与其他分配工具的关系

| 工具 | 配置形态 | 说明 |
|---|---|---|
| **BodyGen**（本篇） | `.ini`（含在 RaceMenu 里） | 语法最原始，无 GUI；**零依赖** |
| **OBody NG** | `.json` | 有 MCM，直读 `SliderPresets`，支持权重与 ORefit |
| **AutoBody** | `.ini`（**仿 BodyGen 语法**） | 额外支持 faction / 男性 / 权重随机 |

**注意**：AutoBody 的 `morphs.ini` 语法是**有意仿照 BodyGen** 的，见过 BodyGen 写法的人
能直接上手——但两者是**不同的 mod**，不要混装。

### 迁移到 OBody NG 的建议

1. **关掉 BodyGen**：`bEnableBodyGen=0`（避免两个分配系统争同一批 actor）。
2. **不要试图翻译 ini**：OBody NG 直读 `SliderPresets` 里的 `.xml` 预设，
   旧 `templates.ini` / `morphs.ini` 没有一键转换路径——**丢弃旧 ini、改配 JSON** 更省事。
3. **种族/NPC 级意图**（"让兽人偏好大胸"这类）在 OBody NG 的 JSON 里按种族表达。
4. **旧档处理**：co-save 里的 BodyGen 状态不会自动消失；遇到异常按
   [`../06-troubleshooting/preset-not-applied.md`](../06-troubleshooting/preset-not-applied.md)
   的思路排查，必要时干净存档。

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| NPC 身材毫无变化 | 没勾 `Build Morphs`，没有 `.tri` | BodySlide 勾 `Build Morphs` 重构建 |
| 同上 | `bEnableBodyGen` 仍是 0 | 置 1 并重启游戏 |
| 配置"完全不生效" | ini 末尾没留空行（社区经验） | 补一个空行 |
| 只有部分 NPC 生效 | morphs.ini 只映射了特定 actor；或别的 mod 覆盖了同一 actor | 用 `All|Female` 验证；查加载顺序 |
| 想要的模板被别人覆盖 | 显式覆盖按**加载顺序**，后加载者胜 | 调整 mod 优先级 |
| 改了配置旧 NPC 不刷新 | co-save 里状态已定型 | 新档测试；或让游戏重新生成该 NPC |
| 与 OBody NG 同装后行为混乱 | 两个分配系统争同一批 actor | 二选一；BodyGen 侧置 0 |
| 脸/身材突然回默认 | 中途增删了 morph 相关 mod，co-save 对不上 | 见 preset-not-applied 的排查链 |

## 取舍与建议

- **只用 RaceMenu、不想加 mod**：BodyGen 是唯一选择，接受 ini 语法与"改配置旧档不刷新"。
- **愿意加一个 mod 换界面和规则**：直接上 [OBody NG](obody-ng.md)——这是当前社区默认答案。
- **只想分发、依赖链洁癖**：看 [AutoBody](autobody.md)（仅 Address Library，但维护基本停滞）。
- **无论选谁**：先确认 `.tri` 构建这条地基（[morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)），
  分配工具全都建立在它上面。
- **别混装两个分配工具**——这是本类问题里最常见的自伤。

## 来源

- **BodyGen 配置目录、两份 ini、语法、co-save 存储**：LoversLab 的非官方 BodyGen 文档
  （基于 expired6978 原话整理）—— **社区文档，引作者原话**
  `https://www.loverslab.com/topic/53531-unofficial-bodygen-docs`
- **硬前提需 BodySlide `Build Morphs` + NiOverride 应用**：BodySlide 机制 + BodyGen 文档
  —— **一手（机制）+ 社区**
- **"ini 末尾需空行"**：**社区经验**
- **`bEnableBodyGen` 配置项与默认值**：RaceMenu `skee64.ini` 字段（见
  [`../02-face/racemenu.md`](../02-face/racemenu.md)）—— **一手（作者文档）**
- **JBS2BG（Nexus LE 88707）为 BodyGen 配置的 patcher 来源**：AutoBody README 引用
  —— **一手（相邻证据）**
- **"semi-obscure" 与完全重写**：OBody 作者 Patreon 帖 —— **一手（作者本人）**
- **AutoBody 语法仿 BodyGen、EditorID 匹配**：AutoBody 官方仓库 README —— **一手**
- **未确认**：BodyGen 的首次发布版本与日期；BodyGen 是否支持 EditorID 键
  （AutoBody README 的表述未逐字核对）
