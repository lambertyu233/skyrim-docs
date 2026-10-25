---
id: obody-ng
title: OBody NG（Next Generation）
category: 05-distribution
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [分配, OBody, 预设分发, NPC 身形, JSON]
aliases: [obody ng, 身形分发, preset distribution, 随机分配身形, aietos, obody 是什么, obody 历史, orefit, 穿衣重算, obody 安装, obody 热键, obody mcm, obody 5.0, obody 1.7, sairion350, obody 依赖]
source: https://www.nexusmods.com/skyrimspecialedition/mods/77016
summary: OBody 谱系（Sairion350 的 BodyGen 完全重写 → Aietos 的 CommonLibSSE NG 版单 DLL 通吃）、启动扫描 SliderPresets 建库、随机分配、按种族/NPC/faction 规则、ORefit 穿衣重算、O 键热键指派，以及与 BodyGen、AutoBody 的对比。
---

# OBody NG（Next Generation）

> **一句话**：把你 `Data\CalienteTools\BodySlide\SliderPresets` 里的所有预设
> **随机分发给玩家与 NPC**，并按规则细调；它本质上是 **RaceMenu BodyGen 的完全重写**，
> 解决了 BodyGen"要 patcher、只认 100 体重、没有界面"的三个老问题。

## 速览

| 项 | 内容 |
|---|---|
| 谱系 | **OBody**（原版，**Sairion350**，OStim 生态，Nexus SE 51084）→ **OBody NG**（**Aietos**，Nexus 77016） |
| 编译方式 | **CommonLibSSE NG**：**单个 DLL 通吃所有 Skyrim 版本（含 AE/1.7.x）**，不用追着游戏版本找 DLL |
| 许可证 | **GPL-3**（作者：可随意使用，遵守许可证即可） |
| 形态 | SKSE 插件（C++）+ Papyrus 脚本 + `OBody.esp`（**flagged ESL**）+ MCM |
| 核心机制 | 启动扫描 `SliderPresets` 建库 → NPC 首次遭遇时随机分配并记住 → **ORefit** 穿衣重算 → **O 键**热键手动指派 |
| 依赖 | SKSE64 + Address Library + UIExtensions + PapyrusUtil（版本匹配）+ MCM Helper + SkyUI；**不需要 OStim** |
| 维护状态 | 活跃；2026-10 仓库提交 "Support OBody **5.0** and Skyrim version **1.7.x**" |
| 硬前提 | 必须先做 **Zeroed Sliders + `Build Morphs`** 基础构建（见下） |

要点：

- **它读的是你磁盘上现成的 `.xml` 预设**：装完预设进 MO2 即用，
  **不需要跑任何 patcher**，也不用重开游戏（作者原话：just go ingame and they're ready to use）。
- **支持权重滑块**：NPC weight 15 就用该预设的 weight-15 变体——这是它对 BodyGen 的
  关键改进之一（BodyGen 只分发 '100' 那一档）。
- **ORefit**：穿衣状态下重算体型，保证衣服贴身；可黑名单特定 outfit
  （topless 类的刚需）。
- **默认热键是 `O`**（MCM 里可改）：准星对准 NPC 弹预设列表，点一下实时换体型。
- **与 RaceMenu BodyGen、AutoBody 二选一**，不要都装（会争同一批 actor 的 morph）。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 未确认 | RaceMenu 内置 **BodyGen** 发布（expired6978） | morph 分发的鼻祖；难用、要 patcher、只支持 '100' 体重（作者后来的评价："semi-obscure"） |
| 未确认（Nexus SE 51084） | **OBody 原版**由 **Sairion350** 发布，属 OStim 生态（原版需要 OStim） | 作者自述是 "a total rewrite of Racemenu's semi-obscure bodygen feature" |
| 2021-11 | **OBody Standalone NG**：脱离 OStim 的编辑版（Nechigawara 首创、**Aietos** 续维护；credits expired6978 的 UIExtensions 与 Parapets 的 MCM Helper） | 第一次用 CommonLibSSE NG 做到"单 DLL 通吃所有版本" |
| 2022-11 | Standalone NG 首个 Papyrus 发布（2022-11-06） | 形态成熟 |
| 2022 前后 | Aietos 的 **OBody NG** 成为主线：自带 MCM、JSON 配置、种族/NPC/faction 规则、黑名单 | 从"OStim 附属"变成独立工具 |
| 2026-02 | 社区文档引用 OBody NG **4.4.3**；配套 Settings Loader 1.0.2（2026-02-03） | 社区评价 4.0.0 起"very stable" |
| 2026-10-03 | 仓库提交 "Support OBody 5.0 and Skyrim version 1.7.x" | **少数宣布支持 1.7.x 的捏脸链组件** |
| 2026-10-15 | `Aietos/OBody` 仓库退役，Papyrus 与 C++ 源码并入 `Aietos/OBody-NG` 单仓库 | 工程收拢 |

### 它从哪来

上游是 **RaceMenu BodyGen**：功能早在 RaceMenu 里就有，但要把预设转成它的配置得靠
外部 patcher（JBS2BG 一类），且只认预设的 '100' 体重档。OBody 原版（Sairion350）把它
**完全重写**：直接读 BodySlide 的预设文件夹、支持全部体重档、穿衣也合身。
但原版挂在 OStim 生态上，需要 OStim。

### 中间经历了什么

分叉点是"**要不要 OStim**"：先有 Nechigawara/Aietos 一系的 **Standalone NG** 编辑版
（脱离 OStim，并用 CommonLibSSE NG 编译成单 DLL）；随后 Aietos 的 **OBody NG** 成为
事实主线，加入 MCM 界面、JSON 配置（按种族 / 单个 NPC / 插件 / faction 分配，黑名单预设与 NPC）、
"查看当前 NPC 应用的是哪套预设"等功能。

### 现状

活跃维护，语义化版本号（仓库明示），GPL-3。2026-10 的提交显示 **5.0 起支持 Skyrim 1.7.x** ——
这在"RaceMenu 缺席 1.7.x"的当下是个例外（它的 morph 施加路径是否仍依赖 RaceMenu，见
"兼容与冲突"）。Nexus 页：`https://www.nexusmods.com/skyrimspecialedition/mods/77016`。

## 它解决什么问题

**没有它之前**：NPC 身材是死的——BodySlide 烘出什么就是什么；想让 NPC 多样，
要么给每个 NPC 单独建 ArmorAddon（工作量大），要么用 BodyGen（要 patcher、只认 100 体重、
没有界面）。

**它的解法**（作者原话归纳）：

| BodyGen 的老问题 | OBody 的解法 |
|---|---|
| 增改预设要跑 patcher | **启动直接扫 `SliderPresets` 文件夹**，装完即用，中途加预设也认 |
| 只支持预设的 '100' 体重 | **完整支持权重滑块**，按 NPC 自身 weight 取变体（可再随机 weight） |
| 配置原始、无界面 | NG 自带 **MCM** + JSON 配置 |
| 穿了衣服就不合身 | **ORefit**：穿衣状态下重算体型 |
| 想指定某个 NPC 的体型很麻烦 | **O 键**准星一指，实时换预设并记住 |
| 身形与生殖器形态绑死 | 可选生殖器/乳头的 procedural 随机（原版功能） |

## 工作原理

```
启动：扫描 Data\CalienteTools\BodySlide\SliderPresets 下的 XML 预设 → 建库
  ↓
NPC 首次加载 → 按规则（随机 / 种族偏好 / faction / 单个 NPC 指定）分配一套预设 → 记住
  ↓
施加：morph 位移 + ORefit（穿衣重算，保证贴身）
  ↓
游戏中：O 键（可改）→ 弹出已安装预设列表 → 点一下实时更换
```

两个机制细节值得知道：

- **分配是持久的**：OBody 记住每个 NPC 的分配结果；你中途安装新预设，
  新遭遇的 NPC 会用到它们，**不需要重跑 BodySlide、不需要新档**。
- **权重是真实生效的**：NPC 拿到预设后按自身 weight 取对应变体，所以"同一个预设
  在不同体重 NPC 身上不同形"。

## 安装

**前置中的前置**：先完成 **Zeroed Sliders + `Build Morphs` + Batch Build** 基础构建。
OBody 分配的是预设数据，没有 `.tri` 就无从施加——「装了没效果」的第一检查点就是这里。
六步流程见 [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

有序步骤（每步附验证点）：

1. **SKSE64 + Address Library**。验证点：`getskseversion` 有输出；版本对照见
   [`../00-overview/version-matrix.md`](../00-overview/version-matrix.md)。
2. **UIExtensions**（Nexus 17561）。验证点：`UIExtensions.esp` **已启用**
   （MO2/Vortex 有时不自动启用）。
3. **PapyrusUtil**，版本与游戏匹配（社区排错文档口径：1.5.97→3.9、1.6.353→4.3、
   1.6.640→4.4、GOG 用 GOG 版）。验证点：`PapyrusUtilDev.log` 存在。
4. **MCM Helper + SkyUI**。验证点：其他带 MCM 的 mod 菜单能正常弹出。
5. **OBody NG 本体**（`OBody.esp` 为 flagged ESL，不占常规插件位）。
   验证点：MCM 列表里出现 OBody NG（**要等几分钟**，见排错）。
6. **（可选）OBody NG - Settings Loader**（Nexus 171188）：跨档沿用 MCM 设置，
   用户设置位于 `MCM\Settings\OBody NG.ini`。验证点：设置在新档仍在。
7. **skee64.ini 两处**（`Data\SKSE\Plugins\skee64.ini`）：
   - `bEnableBodyGen=0`（RaceMenu 内置 BodyGen 与 OBody 互斥，见
     [`../02-face/racemenu.md`](../02-face/racemenu.md)）；
   - `bEnableEarlyRegistration=1` —— RaceMenu **0.4.19.11** 新增的兼容模式，
     changelog 原文 **"use this for OBODY"**。

## 使用与配置

### 游戏内

| 操作 | 效果 |
|---|---|
| **按 `O`**（默认，MCM 可改），准星对准 NPC | 弹出**已安装预设列表**，点选实时换体型并记住 |
| 按 `O` 且**准星无 NPC** | 更换**玩家角色**自己的预设 |
| MCM → OBody NG | 热键改绑、查看当前 NPC 应用哪套预设、分配规则总览 |

> **MCM 注册慢是设计如此**：进游戏不暂停跑几分钟才出现，别据此判断没装上
> （社区排错文档同样强调）。

### JSON 配置

配置文件支持以下维度（作者描述归纳）：

- **按种族**分配/指定预设（如让兽人偏好大胸预设——原版即支持）；
- **按单个 NPC** 预先指定（进游戏前就定好）；
- **按插件、按 faction** 分配；
- **黑名单**：把预设移出随机池；把 NPC 设为不被 OBody 触碰；
- **ORefit 黑名单**：把特定 outfit 排除出穿衣重算（**topless 类的刚需**）——
  作者推荐配套使用社区的 **OBody NG ORefit JSON Master List**（一份预置的大名单）。

### 一个已知的显示怪现象

预设列表对**你在这个存档里早就见过的 NPC** 会显示 **"Unknown Preset"** ——
作者明说无法知道旧版本分配的记录，手动换一次或等新 NPC 才正常。**不是 bug。**

## 兼容与冲突

| 对象 | 结论 |
|---|---|
| **RaceMenu BodyGen** | **互斥**：用 OBody 时把 `bEnableBodyGen` 置 0 |
| **AutoBody** | **二选一**，不要都装——两者争同一批 actor 的 morph；继任关系说法**未确认** |
| **OStim** | **NG 不需要**（原版需要；Standalone/NG 已移除该依赖） |
| **RaceMenu** | 历史上列为依赖（提供 skee64 的 morph API），0.4.19.11 的 `bEnableEarlyRegistration` 就是为它开的兼容模式；**5.0 起支持 1.7.x 而 RaceMenu 无 1.7.x 版 —— 当前是否仍硬性依赖 RaceMenu，未确认**，以 Nexus Requirements 为准 |
| **SPID / JContainers** | **不直接依赖**：OBody NG 配置是 JSON 文件而非 JContainers 容器；SPID 分的是"服装"不是"身形" |
| **1.7.x** | 5.0（2026-10）起有支持提交；RaceMenu 侧现状见 [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md) |
| **其他分配工具** | 与任何"改 NPC morph"的工具都存在争抢，一律单装 |

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 按 O 无反应 / 游戏卡住 | ① UIExtensions 没装或 `.esp` 未启用；② PapyrusUtil 版本错或被别的 mod 覆盖；③ 热键被改绑 | 逐一核对（UIExtensions esp / PapyrusUtil 版本映射 / MCM 里看热键） |
| MCM 不出现 | 注册慢（等几分钟）；或 MCM Helper 版本与游戏不匹配 | 不暂停跑 5 分钟再看；核对 MCM Helper 档位 |
| NPC 身材没变化 | **没做 Zeroed Sliders + `Build Morphs` 基础构建** | 按 [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md) 重做 |
| 预设列表显示 Unknown Preset | 旧档正常现象（作者明说无历史记录） | 手动换一次；新档正常 |
| 衣服不贴身 / 穿了模 | 该 outfit 被 ORefit 黑名单排除，或未参与构建 | 检查 JSON 黑名单与构建覆盖 |
| 装了完全没效果 | 本体未初始化（缺 UIExtensions/PapyrusUtil） | 上 Crash Logger 看堆栈；先核前置 |
| 换新档后设置全丢 | MCM 设置存在存档侧 | 装 Settings Loader（`MCM\Settings\OBody NG.ini`） |

## 取舍与建议

三方对比（选型看这张表就够）：

| | **RaceMenu BodyGen** | **OBody NG** | **AutoBody** |
|---|---|---|---|
| 性质 | RaceMenu 内置功能 | 独立 mod | 独立 mod |
| 配置 | `.ini`（templates + morphs） | **`.json`**（规则更直观） | `.ini`（仿 BodyGen） |
| 界面 | 无 | **MCM** | 游戏内菜单 + 法术 |
| 预设来源 | 需 patcher 预处理 | **直读 `SliderPresets`** | 直读（两处可选） |
| 权重支持 | 仅 '100' 档 | **完整** | 完整（三模式） |
| 男性身形 | 有限 | 支持（有受支持男性身形清单） | **HIMBO** |
| 依赖 | 只要 RaceMenu | RaceMenu/skee 生态 + MCM Helper + UIExtensions + PapyrusUtil | **仅 Address Library** |
| 版本适应 | 随 RaceMenu | **单 DLL 通吃，5.0 支持 1.7.x** | 按游戏版本分档；2022-09 后基本停滞 |

- **想少折腾、要界面、要规则细调**：选 **OBody NG**——它是当前社区默认答案。
- **已经在用 RaceMenu 且不想加 mod**：BodyGen 够用，接受它的原始语法与 patcher。
- **依赖链洁癖 / 只肯装一个 DLL**：可考虑 AutoBody（仅 Address Library），
  但接受其维护停滞（详见 [autobody.md](autobody.md)）。
- **从 BodyGen 迁移**：ini 数据没有一键转换路径；OBody NG 直读预设库，
  一般**丢弃旧 ini、改配 JSON** 更省事。旧档的 morph 状态清理思路见
  [`../06-troubleshooting/preset-not-applied.md`](../06-troubleshooting/preset-not-applied.md)。

## 来源

**一手**

- **OBody NG Nexus 发布页与描述**（CommonLibSSE NG 单 DLL 通吃 SE/AE、MCM、种族/NPC/插件/faction
  规则、黑名单、ORefit 黑名单、O 键热键、OStim 依赖移除、ESP flagged ESL、GPL-3、credits：
  Aietos / Sairion350（原版）/ VersuchDrei 与 Kannonfodder（测试与 C++ 帮助）/ Sswaye（测试与预览））：
  `https://www.nexusmods.com/skyrimspecialedition/mods/77016`（描述经其翻译页全文转引核对）
- **GitHub `Aietos/OBody-NG`**（C++ 源码、语义化版本、GPL-3、构建链）与
  **`Aietos/OBody`**（Papyrus 侧；2026-10-03 "Support OBody 5.0 and Skyrim version 1.7.x"、
  2026-10-15 退役并入主仓库）
- **GitHub `Aietos/OBody-Standalone-NG`**（脱离 OStim 的编辑版、基于 Nechigawara/OBody-Standalone、
  credits expired6978 / Parapets）
- **OBody 作者 Patreon 帖**（`patreon.com/posts/52599023`）："a total rewrite of Racemenu's
  semi-obscure bodygen feature"、扫 `SliderPresets` 建库、权重滑块（BodyGen 只支持 '100'）、
  ORefit、生殖器/乳头随机、种族手动指定、热键、脚本 API —— **一手（作者本人）**
- **OBody NG Settings Loader**（Nexus 171188；MCM Helper + OBody NG 依赖；
  设置落点 `MCM\Settings\OBody NG.ini`；1.0.2 / 2026-02-03）
- **RaceMenu 0.4.19.11 changelog**（`bEnableEarlyRegistration`，"use this for OBODY"）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/19080?tab=files` —— **一手**

**社区经验 / 社区文档**

- "O 键无反应"的三大原因（UIExtensions 未装/未启用、PapyrusUtil 版本错或被覆盖、热键被改）、
  MCM 需数分钟注册、PapyrusUtil 的版本映射（3.9/4.3/4.4/GOG）：
  OBody NG 排错指南（第三方整理）—— **社区文档**
- Zeroed Sliders + `Build Morphs` 是 OBody 的前提：第三方安装指南类文档 —— **社区文档**
- 与 AutoBody 的"继任者"说法：**社区说法不一致，未确认**

**未确认**

- OBody 原版的确切首发日期（Nexus SE 51084 的 original upload 未逐条核实）
- OBody NG 当前 Nexus Files 页的确切版本号（社区文档引用 4.4.3；仓库提交提及 5.0）
- OBody NG 5.x 是否仍硬性依赖 RaceMenu（1.7.x 已支持而 RaceMenu 无 1.7.x 版，逻辑上应有变化，
  但官方 Requirements 未逐字核对）
