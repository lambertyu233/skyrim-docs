---
id: facelight
title: 脸部补光（Facelight）
category: 02-face
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [捏脸, 补光, 照明, Facelight]
aliases: [面部补光, 脸光, 打光, 脸黑看不见, Face Light, tktk, 捏脸补光, 暗处看不清脸, RaceMenu light, Facelight Plus, 补光 mod, 脸部照明, NPC 补光, facelight 是什么]
source: https://www.nexusmods.com/skyrimspecialedition/mods/5965
summary: 脸部补光的三条路线——RaceMenu 内置补光（Light On/Off，只在捏脸界面内有效）、独立补光 mod Face Light 原版（作者 tktk，SE 5965 / LE 13457，法术常驻、可挂 NPC 上限 20）与社区增强版 Facelight Plus——各自的安装与使用，以及相关但未确认的项。
---

# 脸部补光（Facelight）

**要解决的问题**：捏得再好的脸，在暗处或逆光下也看不清。补光类 mod 在角色（或 NPC）
脸前挂一个光源，让脸在室内/夜晚也保持可读。

> **一句话**：补光分两族——**RaceMenu 内置**（只在捏脸界面内有效，出菜单就没了）与
> **独立的补光 mod**（常驻游戏世界，可挂到 NPC）。只想捏脸时看清脸，前者就够；
> 要让脸在游戏里也亮，才需要后者。

## 速览

| 项 | RaceMenu 内置补光 | Face Light（原版） | Facelight Plus（社区增强） |
|---|---|---|---|
| 作者 | expired6978（随 RaceMenu） | **tktk** | 社区站收录，标注作者 **Freya**（**Nexus 发布状态未确认**） |
| 首发 | 随 RaceMenu（SE 页 2018-08-06 建立） | **LE 2012-03-22**（Nexus 13457）；**SE 2016-12-10**（Nexus 5965） | **未确认**（社区站页面标注 2023-12） |
| 当前版本 | 随 RaceMenu（0.4.20.0） | **SE v2.0**（2018-01-21 末更）；LE 末版同为 v2.0（2016-08-25） | **未确认** |
| 许可证 | RaceMenu 作者权限栏：不得再分发 | 不得上传到其它站点；可为随从/NPC 使用其数据但须署名 | **未确认** |
| 前置 | 无（RaceMenu 自带） | **SKSE + SkyUI**（MCM 需要） | **SkyUI + SKSE**（社区站明示） |
| 生效范围 | **仅捏脸界面内** | **常驻游戏世界**；玩家 + NPC（**上限 20**） | 常驻；NPC 上限 **15**（社区站自述） |
| 维护状态 | 随 RaceMenu 维护中 | **停止更新**（SE 末更 2018-01） | **未确认**（作者建议用回原版，见下） |
| 可信层级 | 一手（RaceMenu 发布页） | **一手（Nexus 发布页 + changelog）** | **社区经验（非官方站）** |

要点：

- **两族补光互不替代**：RaceMenu 的 Light On/Off 是捏脸时的临时手段；
  Face Light 是游戏内的常驻光源。**"捏脸亮着、出菜单就黑"是设计如此，不是 bug。**
- **原版 Face Light 已停止更新**（SE 末版 2018-01），但作者 tktk 明确建议
  **从 Facelight Plus 切回原版**："it is not stable, but my facelight mod is stable"（LE 页作者原话，一手）。
- **法术常驻、可挂 NPC**：`Facelight Target` 可挂到 NPC，**上限 20 个**；
  光源太多有性能代价（作者文档原话式提醒）。
- **切换区域光源会被禁用**，需要在 MCM 里重新管理——这是最常见的"咦怎么不亮了"。
- **潜行时 Facelight 会自动降低 NPC 侦测**（补光亮多少、侦测降多少，v2.0 changelog）。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 2012-03-22 | **Face Light LE 版首发**（Nexus 13457，作者 tktk） | 捏脸补光从"调视角"变成"挂光源" |
| 2013-02-19 | v1.3：修"切换 cell 后 Target 光源消失"；光源位置固定；与 candlelight 联动开关 | 切区域管理光源的机制从这时就有 |
| 2013（v1.2） | **`Facelight Target` 加入**（可挂 NPC） | 补光第一次能用在别人身上 |
| 2014-04-06 | v1.8：可显示光源上限设为 11、Facelight 上限设为 **10** | 上限问题第一次显式化 |
| 2016-08-25 | **v2.0（LE）大改**：上限 10→**20**；MCM 列表管理；光色改暖；降低光源导致的 NPC 侦测；潜行不必手动关；读档自动获得法术；**需要 SKSE** | 作者自述"I revamp the facelight in version 2.0" |
| 2016-12-10 | **SE 页建立**（Nexus 5965），12-11 发布 SE 版 v2.0 | 进入 SE 生态 |
| 2018-01-20/21 | SE 末版 v2.0：MCM 支持意大利语；优化 esp 与 nif | **此后停止更新** |
| 2023-12（页面标注） | Facelight Plus 出现在社区指南站 | 社区增强版；上限回到 15（基于旧版基数），说明它并非原版的直接续作 |

### 它从哪来

补光的需求和捏脸改造本身一样老：原版角色创建界面的光照不可控，
逆光、室内、夜晚三种场景下脸直接糊掉。第一代解法是**调相机角度**（治标），
Face Light 的思路是**在脸前挂一盏常驻法术光源**——用照明法术的机制，
而不是改游戏的光照系统。这也是它"兼容性基本没问题"（作者原话）的原因：
它不碰任何原版资源。

### 中间经历了什么

一条主线是**上限的反复**：10（v1.8）→ 20（v2.0）→ Facelight Plus 又回到 15。
Plus 的上限数字本身就是线索：它基于 v2.0 之前的旧版做增强，
所以作者 tktk 的建议是"I recommend switch this mod from facelight plus"
（建议从 Plus 切回原版）——**稳定性是作者亲自背书过的判据**。

另一条线是**MCM 化**：v2.0 起需要 SKSE + SkyUI，换来目标列表管理、
批量 Reset、名称显示。没有 SKSE 的环境用不了完整功能。

### 现状

原版停在 SE v2.0（2018-01），LE 停在 v2.0（2016-08）。功能上仍是社区默认推荐
（作者自己说原版更稳），**停更但未过时**——它依赖的只是 SKSE + SkyUI，
不碰 morph、不碰网格，版本敏感度在本库所有 mod 里几乎最低。

## 它解决什么问题

**没有它之前**：暗处/逆光下的脸只有剪影。原版能用的只有 candlelight 一类
照明法术——有持续时间、颜色不对、且**脸并不是常亮**。

**它的解法**：一个**常驻、可开关、色温接近日光**的脸前光源：

| 需求 | 原版 / 无 mod | Face Light |
|---|---|---|
| 捏脸时看清脸 | 调角度，收效有限 | RaceMenu 的 Light On/Off 或 Face Light 都行 |
| 游戏里脸也亮（含截图） | candlelight（有时限、色偏） | **常驻白光**，`Facelight` 法术开关 |
| NPC 的脸也亮 | 无 | **`Facelight Target`** 挂到 NPC，上限 20 |
| 更暗的场景 | —— | **`FaceLightDark`**（正常亮度一半） |

> 原版发布页原话：**"Does not interfere with visibility"（不影响实际可见度）**——
> 它是**给脸补光让你看得清**，不是**让角色在黑暗中无所遁形**的作弊光源。

## 工作原理：它包含什么

### 三种补光的分层

```
RaceMenu 内置 Light On/Off   → 捏脸界面内生成一盏白光（临时）
Face Light 原版               → 常驻法术光源：玩家一盏 + NPC 至多 20 盏
Facelight Plus                → 原版 + MCM 管理 / 潜行联动 / 对话联动 / 快捷键（社区增强）
```

### 法术清单（原版 v2.0，首次读档自动获得，共 5 个）

| 法术 | 作用 |
|---|---|
| `Facelight` | 玩家脸前常驻白光；用同名法术开关 |
| `Facelight Target` | 挂到 NPC（上限 **20**；Plus 为 15） |
| `FaceLightDark` | 正常亮度**一半** |
| `FacelightDark Target` | 一半亮度的 NPC 版 |
| `Facelight Reset` | 释放全部 Target（"Reset all list" 一键清空） |

### 关键机制细节

- **常驻**：效果持续存在，不是有持续时间的光。
- **切换区域（cell）光源被禁用**：需要在 MCM 列表里重新管理——
  这是设计行为（v1.3 就在修与之相关的 bug），不是故障。
- **潜行**：v2.0 起 Facelight **自动按补光量降低 NPC 侦测**，
  所以潜行不必手动关灯（作者 changelog 原话）。
- **性能**：光源多了有代价（作者文档原话式提醒："Too many light source is performance hit"）。

## 安装

### A. RaceMenu 内置补光（无需安装）

1. 装好 [RaceMenu](../02-face/racemenu.md)（捏脸界面本来就带）。
2. 进捏脸界面，相机操作区附近即有 **Light On/Off**。
3. **验证点**：开关后角色正前方出现/消失一盏白光；**退出菜单后灯消失**——
   这正是它"只在捏脸界面内有效"的判据。需要在游戏里也亮 → 装下面的独立 mod。

### B. Face Light 原版（tktk）

1. **确认前置**：**SKSE + SkyUI**（MCM 功能需要两者；v2.0 起的硬性要求，
   依据 LE 页 Requirement 原文 Skyrim 1.9.32 / SKSE 1.7.3 / SkyUI 3.1+）。
   SE 版对 SKSE 版本的要求以 Nexus Files 页当期说明为准（**具体最低版本号未确认**）。
2. **用 mod 管理器安装**（Nexus SE 5965 / LE 13457），启用 `Facelight.esp`。
   ⚠️ 作者权限栏：**不得上传到其它站点**；可为随从/NPC 使用其数据但须在描述中署名。
3. **首次读档自动获得 5 个法术**（官方描述原文）。
4. **验证点**：法术栏（→ 其它）出现 `Facelight` 等 5 个法术；
   施放后脸前出现白光；对一个 NPC 施放 `Facelight Target` 成功。
5. **若没拿到法术**：用 AddItem Menu 一类工具取（官方描述指定的补救途径）。

### C. Facelight Plus（社区增强，来源为社区站）

1. **来源与可信层级**：仅见社区指南站 `https://www.skyrimodding.com/facelight-plus/`
   （**非 Nexus**），页面标注作者 **Freya**；**Nexus 发布状态与作者归属未确认**。
2. 前置：**SkyUI + SKSE**（社区站明示 Important）。
3. 该站给出的安装说明是 NMM 一键或**手动解压进 `Data`** 再激活 `FacelightPlus.esp`——
   ⚠️ 这是**陈旧教程**（NMM 时代做法）。**建议改用 mod 管理器安装**，
   不要直接往游戏目录写文件（理由见 [`mo2-override-rules.md`](../07-workflow/mo2-override-rules.md)）。
4. **验证点**：MCM 出现 Facelight Plus 菜单；潜行时灯自动熄灭；
   对 NPC 按激活键能循环切换补光状态（Edit Mode）。
5. ⚠️ **稳定性**：原版作者明确建议从 Plus 切回原版（"it is not stable"）——
   这是**一手来源对 Plus 的负面评价**，引用时请一并转述。

## 使用与配置

### MCM（原版 v2.0 起需要 SkyUI）

- **目标列表**：显示当前带 Facelight 的 NPC 列表，可逐个移除；
- **Reset all list**：一键释放全部 Target；
- **切区域后**：光源被禁用，回 MCM 重新管理；
- 目标开关时**显示 NPC 名字**（v2.0 加入）。

### 常见使用路径

```
只想玩家亮        → Facelight 法术常驻
想给随从/ NPC 亮  → Facelight Target（逐个挂，上限 20）
场景太亮           → FaceLightDark / FaceLightDark Target
全部收掉           → Facelight Reset（或 MCM 的 Reset all list）
```

### 性能管理

- 光源越多代价越大——NPC 补光**按需挂、用完 Reset**，不要全场乱挂。
- 潜行场景：v2.0 起不必手动关灯（自动降侦测）。

## 兼容与冲突

| 关系 | 结论 |
|---|---|
| 原版 Face Light vs Facelight Plus | **二选一**（同改一套光源机制；作者建议留原版） |
| 与 RaceMenu 内置补光 | 不冲突但**互不替代**：内置的只作用于捏脸界面 |
| 与原版资源 | **零改动**——纯加法术，作者自述"compatible with other mod basically" |
| 与 ENB / 大型光照 mod | **未确认**（本轮未检索到明确的冲突记录；理论上是叠加关系，以实测为准） |
| 与潜行 / 侦测系统 | v2.0 起自动按补光量降侦测，不需要额外补丁 |
| SKSE / SkyUI | 硬性前置（MCM 功能）；无 SKSE 的环境功能残缺 |

### 已核实的简单替代

**Shining face - Face light and Ambient Light**（Nexus SE **10190**）：
作者 Askinnn_80，2017-06-01 首发，v1.1 更新至 2023-10-20。
思路与 Face Light 同族（常驻照明法术），额外附带环境光；
v1.1 起书本自动获得（v1.0 需在 Dragonsreach 找 Farengar 购买或 AddItemMenu）。
**作为 Face Light 停更期间的一个仍在维护的平替可考虑**——机制与复杂度相近，
本库未做逐项对比（**未确认项：与原版的详细差异**）。

## 相关但未确认的项

- **Better Lighting for Face Light / Facelight Plus**：常被作为配套光照 mod 提及，
  Facelight Plus 的社区站页面也把它列为"Highly recommended"；
  **本轮未确认其 Nexus ID 与作者**。引用时标注"来源为社区站，未确认"。
- **Facelight Plus 的 Nexus 发布状态与作者归属**：仅见社区指南站描述（页面标注作者 Freya），
  **未能确认其 Nexus 发布状态**——引用时请标注"来源为社区站，未确认"。
- **原版 Face Light SE 版对 SKSE 的最低版本要求**：LE 页 Requirement 写了 SKSE 1.7.3（LE 时代），
  SE 页未见等效明确数字，**未确认**。
- **与 ENB 的具体交互**：未检索到可靠记录，**未确认**。

> 以上未确认项与全库其它"未确认事项"集中记录在
> [`../08-sources/unreliable-and-unconfirmed.md`](../08-sources/unreliable-and-unconfirmed.md)，
> 转述本条目时请保持同样的标注口径。

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 捏脸时能亮、出菜单就黑 | **正常**——那是 RaceMenu 内置补光 | 需要常驻就装 Face Light |
| 首次读档没拿到法术 | 自动授予失败（官方描述预留的兜底情形） | 用 AddItem Menu 一类工具取（官方指定途径） |
| 挂到 NPC 的灯突然不亮 | **切换了区域**（cell 变化时光源被禁用） | 回 MCM 重新管理/重新挂 |
| MCM 打不开或功能缺失 | 缺 SKSE 或 SkyUI（v2.0 起硬性要求） | 补装两者（[`../01-prerequisites/skse64.md`](../01-prerequisites/skse64.md)） |
| 挂 NPC 时提示到上限 | 已达 **20** 个 Target（Plus 为 15） | `Facelight Reset` 清一批再挂 |
| 潜行时还是会被发现 | 灯没起效（非 Plus 的 Edit Mode 路径） | v2.0 起自动降侦测；确认法术生效 |
| 用了 Plus 出现各种不稳 | 作者本人就说 Plus "not stable" | **切回原版**（一手来源的建议） |
| 帧数下降明显 | 光源数量过多 | 减少 Target 数量；用完 Reset |

## 取舍与建议

- **只想捏脸时看清脸**：**不用装 Facelight** —— RaceMenu 自带的 Light On/Off 就够
  （这是原条目就有的结论，仍然成立；RaceMenu 本身见 [`../02-face/racemenu.md`](../02-face/racemenu.md)）。
  它在学习路径里属于阶段 2 的可选项，见
  [`../00-overview/learning-path.md`](../00-overview/learning-path.md)。
- **要游戏内常驻补光 / 截图**：装 **Face Light 原版**——停更但稳定，
  作者亲自背书，依赖面最窄。
- **要 MCM 管理 / 潜行联动 / 快捷键**：可以考虑 Facelight Plus，
  但先接受"作者说它不稳"这个一手评价；出问题先切回原版做对照。
- **给 NPC 补光要节制**：上限 20 是性能护栏，不是目标。
- **停更是停更，不是报废**：它不碰网格与 morph，1.6.1170 / 1.7.x 的版本浪潮
  对它基本无影响（**具体兼容性本库未在 1.7.x 实测 → 未确认**）。

## 来源

**一手**

- Face Light SE 发布页（作者 tktk、original upload **2016-12-10**、
  last updated **2018-01-21**、v2.0、5 个法术首次读档自动获得、Target 上限 20、
  Dark 版亮度一半、`Facelight Reset`、权限栏原文、翻译列表）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/5965`
- Face Light LE 发布页（作者 tktk / 上传 tktk1、original upload **2012-03-22**、
  Requirement Skyrim 1.9.32 + SKSE 1.7.3 + SkyUI 3.1+、**v0.1→v2.0 完整 changelog**、
  **"I recommend switch this mod from facelight plus. Because it is not stable"**）：
  `https://www.nexusmods.com/skyrim/mods/13457`
- RaceMenu 发布页（**Light On/Off 只在捏脸界面内有效**）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/19080`
- Shining face - Face light and Ambient Light（作者 Askinnn_80、2017-06-01 首发、
  v1.1 更新 2023-10-20、v1.0 需找 Farengar 购买、v1.1 书本自动获得）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/10190`

**社区经验（非官方站）**

- Facelight Plus（作者标注 Freya、前置 SkyUI+SKSE、上限 10→15、Edit Mode、
  潜行自动开关、对话补光、快捷键、安装说明含 NMM/手动路径、
  推荐 Better lighting for Face Light and Facelight Plus）：
  `https://www.skyrimodding.com/facelight-plus/` —— **Nexus 发布状态未确认**
- "切区域光源被禁需 MCM 重新管理""Reset all list""光源多的性能代价"
  "潜行自动降侦测""与原版 mod 基本兼容"：社区站对作者文档的转述页
  `https://www.skyrimodding.com/face-light/` —— **社区站转述（与 Nexus changelog 互相印证）**

**未确认**

- **Facelight Plus 的 Nexus 发布状态与作者归属**（仅见社区指南站）
- **Better Lighting for Face Light / Facelight Plus 的 Nexus ID**
- **SE 版对 SKSE 的最低版本要求**（LE 页的 1.7.3 是 LE 时代数字）
- **与 ENB 的具体交互**、**在 1.7.x 下的实测表现**
