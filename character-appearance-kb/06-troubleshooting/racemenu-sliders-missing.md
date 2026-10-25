---
id: racemenu-sliders-missing
title: RaceMenu 里没有滑块 / 滑块不能动
category: 06-troubleshooting
kind: tutorial
version: 2.0.0
updated: 2026-10-25
tags: [排错, RaceMenu, 滑块, morph, SKSE]
aliases: [没有滑块, 滑块缺失, 滑块不见, 滑块不能动, 滑块是空的, sliders missing, racemenu 没反应, 身形滑块没有, 身形栏空白, morph 未构建, build morphs, tri 被覆盖, esp 未启用, 那一栏没有]
source: https://www.loverslab.com/topic/202366-racemenu-problem-sliders-absent-or-not-working
summary: 滑块缺失的分流表（哪一栏没有滑块）+ 十一条检查清单（SKSE/RaceMenu 版本、Build Morphs、RaceMenuMorphs*.esp 启用、.tri 被覆盖、HPH/EFM 不兼容 morph、skee64.ini 开关、1.7.x 未适配），以及 RaceMenu"给能力不给数据"这条总认知。
---

# RaceMenu 里没有滑块 / 滑块不能动

> **一句话**：RaceMenu **提供能力，不提供数据**——你能拖哪些滑块由身形 mod 决定，
> 拖了有没有反应取决于你自己有没有构建出 `.tri`。"没滑块"八成不是 RaceMenu 的错。

## 速览

| 项 | 内容 |
|---|---|
| 症状 | 捏脸界面里身形那一栏没有滑块 / 滑块是空的 / 拖动无效果 |
| 高频成因 | morph 未在 BodySlide 里构建（没勾 `Build Morphs`）；SKSE 版本不匹配 |
| 首选判据 | 界面像原版（无搜索框无数值）⇒ SKSE/RaceMenu 层；只有身形栏缺 ⇒ morph 数据层 |
| 最短修复路径 | BodySlide 勾 `Build Morphs` + 确认 `RaceMenuMorphs*.esp` 已启用 + 重构建 |

要点：

- **三层来源**：RaceMenu 框架（能力）+ 身形的 RaceMenu Morphs 组件 esp（有哪些滑块）
  + 你构建的 `.tri`（真正的变形数据）——缺任何一层都出问题
  （完整机制见 [morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)）。
- **最常见的根因是 SKSE 版本不匹配**：所有 SKSE 插件静默失效，
  界面可能直接退回原版。
- **1.7.x 下"没有滑块"不是故障**：RaceMenu 尚无 1.7.x 正式版，
  这是未适配（见 [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)）。
- **HPH / EFM 会改脸**：它们改变 morph 基础，"预设失效 / 滑块奇怪"要连着看。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 2012-03-15 | **ECE**（Enhanced Character Edit）在 Nexus 发布 | slot morph 时代：数据绑槽位、脚本层施加，槽位有限 |
| 2013-01-08 | **RaceMenu LE 首发**（Nexus 29624） | 捏脸框架与 ECE 并列；morph 路线转向 SKSE 插件 |
| 2018-08-06 | **RaceMenu SE 首发**（Nexus 19080，`skee64.dll` 内含 NiOverride 与 CharGen） | SE  morph 管线定型：BodySlide 产数据、skee64 施加数据 |
| 2018-08-21 | 发布 **Modders Package**（脚本源码与模板） | 第三方身形滑块生态（`RaceMenuMorphs*.esp`）的起点 |
| 2019-11 | BodySlide "记住 `Build Morphs` 勾选状态" | `Build Morphs` 从临时选项变成常规工作流 |
| 2020 前后 | **OBody / RaceMenu BodyGen** 普及；0.4.19.11 加 `bEnableEarlyRegistration`（changelog 原文 "use this for OBODY"） | 分配工具与 morph 体系合流 |
| 2026-04-20/21 | **0.4.20.0**（部件标签 + GOG 版 untested） | 当前最新正式版 |
| 2026-08-23 | 作者帖：1.7.99 完成但被 SKSE Papyrus bug 卡住；**1.7.104 未做**；转向 CommonLibSSE-NG 重写 | **1.7.x 下整套滑块消失成为新成因** |

### 它从哪来

"滑块"这个概念随 morph 技术演进了三代：ECE 的 slot（绑槽位）→
BodySlide 的离线构建（写顶点）→ skee64/NiOverride 的运行时施加。
每一代换轨都淘汰一批老教程——今天的"没滑块"排查必须建立在
**能力 / 名称 / 数据三层分离**的模型上。

### 中间经历了什么

最大的变化是**分发形态**：早年滑块数据靠玩家自己构建；后来身形 mod
直接带 `RaceMenuMorphs*.esp` 与预构建资产；OBody 类工具再进一步
直接读 `SliderPresets` 的 `.xml` 分发给 NPC。每层新增一个依赖，
就新增一类"滑块不出现"的失败模式。

### 现状

1.6.x 上管线稳定；1.7.x 上 RaceMenu 缺位——**升级前先想清楚要不要放弃整套捏脸**。

## 先分流：哪一栏没有滑块

| 现象 | 主要嫌疑 |
|---|---|
| **所有滑块都没有**，界面像原版（无搜索框、无数值、一堆 `$`） | SKSE / RaceMenu 版本或安装问题；**1.7.x 也归这类** |
| **界面正常但没有身形滑块**（那一栏不存在或空白） | morph 未构建 / `RaceMenuMorphs*.esp` 未启用 / `.tri` 被覆盖 |
| **界面正常但头部没变成高模** | HPH 未在 Head 页的 Face Part 切换 |
| **滑块在但拖动无效果** | morph 数据缺失或被覆盖；`bEnableBodyMorph=0` |
| **只有某几个滑块没有** | 提供那组 morph 的 esp 未启用（如 EFM - Racemenu Plugin） |
| **没有武器样式 / SOS 滑块** | XPMSE 的 FOMOD 没选 RaceMenu，或 RaceMenu 低于 0.4.2 |
| **不是没滑块而是启动/捏脸就崩** | 转 [overlay-nif-ctd.md](../06-troubleshooting/overlay-nif-ctd.md) |

## 完整检查清单

### 1. SKSE 版本与游戏版本是否匹配 ⭐ 最常见

**这是最常见的原因。** 1.5.97 误用 AE 版 SKSE（或反之）
→ 所有 SKSE 插件 DLL 失效 → 滑块缺失或不动。

判断捷径：装 SkyUI，如果它弹 **"SKSE is not functioning properly"**，
就是这一层的问题。版本对照见
[version-matrix.md](../00-overview/version-matrix.md)。

### 2. RaceMenu 版本是否匹配（含 1.7.x）

AE 环境用旧版 RaceMenu → 没有（或只有部分）滑块。
**1.7.x 目前没有官方正式版**——1.7.99 版被 SKSE 的 Papyrus 函数 bug 卡住，
1.7.104 未做，作者转向 CommonLibSSE-NG 重写（截至 2026-10-25 核实）。
决策见 [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)。

### 3. 散装旧 `.pex` 是否还在

RaceMenu 官方描述明确要求：见到"版本不匹配"警告时，删除 Data 下的
这些松散文件：

```
CharGen.pex
NiOverride.pex
RaceMenu.pex
RaceMenuBase.pex
RaceMenuLoad.pex
RaceMenuPlugin.pex
```

### 4. morph 是否在 BodySlide 里构建了 ⭐（身形滑块）

**必须勾 `Build Morphs`**，否则不生成 `.tri` 与 NIF 里的 `BODYTRI`，
RaceMenu 无从显示身形滑块。机制见
[morph-and-nif-basics.md](../00-overview/morph-and-nif-basics.md)。

### 5. morph 提供者 esp 是否启用

`RaceMenuMorphs*.esp`（如 `RaceMenuMorphsCBBE.esp`）需要启用。
它决定这一栏**有哪些滑块、叫什么名字**；损坏也会导致对应滑块消失。

### 6. 构建产物是否被覆盖

BodySlide 构建出的 NIF 若被别的 mod 覆盖，`BODYTRI` 一起丢失 →
**身形滑块突然消失**。查 MO2 的 Conflicts（覆盖规则见
[mo2-override-rules.md](../07-workflow/mo2-override-rules.md)）。

### 7. High Poly Head 是否真的被选中（头部）

**HPH 不是自动生效的。** 要到 RaceMenu 的 **Head 页 / Face Part 滑杆**
把头部部件切换为高模头。社区常写"把 Face Part 拉到 3"
（社区经验，官方未给编号）。

### 8. 是否装了 EFM 之类不兼容 morph

- **EFM morph 不适用于 High Poly Head**（EFM 作者明确暂无支持计划）；
- **EFM 主文件不兼容现有预设**（会改脸）——想保留现有脸用可选的
  *EFM - Racemenu Plugin*（只有滑块）；
- EFM 不兼容 ECE；ECE / RaceMenu / EFM 用不同种族 morph，预设不能简单互通。

见 [expressive-morphs.md](../02-face/expressive-morphs.md) 与
[high-poly-head.md](../02-face/high-poly-head.md)。

### 9. `skee64.ini` 开关

路径 `Data\SKSE\Plugins\skee64.ini`：

| 字段 | 默认 | 说明 |
|---|---|---|
| `bEnableBodyMorph` | `1` | 身形 morph 的总开关；**置 0 = 滑块拖了没反应** |
| `bEnableBodyGen` | `0` | 内置随机身形；与 OBody 类工具互斥 |

### 10. 是否需要重开捏脸界面

有时需要先建好角色，再 `showracemenu` 重开一次才加载。
SKSE 输入故障（zoom / light 不响应）也常常重开即解。

### 11. 其他入口自查

- 从 `skee64_loader.exe` 启动（不是原版启动器）；
- 界面一堆 `$` = SKSE 未正确加载（社区经验）；
- RaceMenu 本体对加载顺序不敏感，但**依赖它的东西**敏感
  （HPH 与 EFM 的相对顺序，见 [install-order.md](../07-workflow/install-order.md)）。

## 判断分叉点（别误诊）

| 看起来像 | 其实 |
|---|---|
| "RaceMenu 坏了" | 八成是 `.tri` 没构建、esp 没启用、或被覆盖——**先查数据再查工具** |
| "滑块拖了没反应" | `bEnableBodyMorph=0` 或 morph 数据与当前身体不是同一套 |
| "拖滑块身体变了衣服没变" | 衣服没有同源 morph——转 [clipping.md](../06-troubleshooting/clipping.md) |
| "预设导进去脸不对" | 依赖资源缺失 / HPH 未切——转 [preset-not-applied.md](../06-troubleshooting/preset-not-applied.md) |
| "1.7.x 下没滑块" | 未适配，不是故障；升级前读决策树 |
| "没有武器/SOS 滑块" | XPMSE FOMOD 的 Character Creation 没选 RaceMenu |
| "进 Sculpt 页就崩" | 网格不是 BSDynamicTriShape（0.4.10 已修此类崩溃） |

## 取舍与建议

- **先分流再动手**：界面像不像原版，决定你查 SKSE 层还是 morph 数据层。
- **"调不动就先查有没有数据"**：这是本类问题回报率最高的习惯。
- **别为"多几个滑块"去开 `bAllowAnyRacePart` / `bAlloyAnyGenderPart`**，
  官方自己标了 "not recommended"。
- **1.7.x 用户**：要么留在 1.6.1170，要么接受捏脸功能缺失——
  决策树见 [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)。

## 来源

- **SKSE 版本不匹配为最常见原因、`RaceMenuMorphs*.esp` 损坏、morph 未构建、
  HPH 需手动选 Face part、重开 `showracemenu`、SkyUI 的 "SKSE is not functioning
  properly" 提示**：LoversLab 与 Nexus 论坛的 RaceMenu 滑块帖 —— **社区经验（多帖一致）**
  `https://www.loverslab.com/topic/202366-racemenu-problem-sliders-absent-or-not-working`
- **`Build Morphs` → `.tri` + `BODYTRI` → RaceMenu 应用**：
  BodySlide 官方仓库提交记录 + wiki —— **一手（机制）**
- **"构建被覆盖导致滑块消失"**：**机制推论 + 社区经验**
- **1.7.x 无官方版（1.7.99 被 SKSE 卡住、1.7.104 未做、CommonLibSSE-NG 重写）**：
  RaceMenu 作者 2026-08-23 帖 —— **一手（作者本人）**
  （本库整理见 [racemenu.md](../02-face/racemenu.md)、[game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)）
- **需删除的 6 个 `.pex`、`bEnableBodyMorph` / `bEnableBodyGen` 字段、
  0.4.19.11 `bEnableEarlyRegistration` "use this for OBODY"**：
  RaceMenu 发布页与 changelog —— **一手**
- **EFM 不适用 HPH、EFM 主文件不兼容现有预设、可选 Racemenu Plugin**：
  EFM 发布页描述 —— **一手**（本库整理见 [expressive-morphs.md](../02-face/expressive-morphs.md)）
- **XPMSE RaceMenu 插件提供武器/SOS 滑块、要求 RaceMenu 0.4.2+**：
  XPMSSE 发布页 —— **一手（经转载）**（见 [xpmse-skeleton.md](../04-physics/xpmse-skeleton.md)）
- **"把 Face Part 拉到 3"的具体档位**：中文社区帖 —— **未确认（官方未给编号）**
