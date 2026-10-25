---
id: bodyslide-presets
title: 身形预设（SliderPresets）——形态、生态与"被引用"的预设名
category: 03-body
kind: reference
version: 2.0.0
updated: 2026-10-25
tags: [身形, 预设, BodySlide, 分享]
aliases: [bodyslide 预设, sliderpreset, 身形预设, 预设 xml, 体型预设, zeroed sliders, 预设分享, 怎么分享预设, 预设怎么用, obody 预设, 预设不生效, sliderpresets 目录, 预设安装]
source: https://github.com/ousnius/BodySlide-and-Outfit-Studio/wiki/Creating-a-BodySlide-project
summary: 身形预设的完整百科：.xml 形态与 Data\CalienteTools\BodySlide\SliderPresets 位置、每个滑块存体重 0/100 两值的结构、各身形自带预设清单（含 HIMBO 全家桶）、社区分享生态、预设名如何被 OBody NG / BodyGen / AutoBody 当配置键引用，以及"裸身与服装必须用同一预设"的实践纪律。
---

# 身形预设（SliderPresets）

> **一句话**：预设就是 `SliderPresets/` 下的一组命名过的滑块值——
> 它既是"一键复刻别人体型"的分享单位，也是 **OBody NG / BodyGen / AutoBody
> 分配给 NPC 时的配置键**。预设命名杂乱，下游分配层就很难配。

## 速览

| 项 | 内容 |
|---|---|
| 文件形态 | `SliderPresets\*.xml`（纯文本 XML，一组命名过的滑块值） |
| 位置 | `Data\CalienteTools\BodySlide\SliderPresets\`（分组定义在 `SliderGroups\`） |
| 数据结构 | 每个滑块存**两个值**：体重 0 一个、体重 100 一个 |
| 生效方式 | BodySlide 构建时**烘焙进 nif**（离线，非运行时） |
| 与 RaceMenu 预设 | **完全不同的两种文件**（`.xml` vs `.jslot`），不能互相导入 |
| 下游消费者 | OBody NG（直接扫这个目录建库）、RaceMenu BodyGen、AutoBody |
| 维护纪律 | 裸身与服装**必须用同一个预设**构建 |

要点：

- 预设让"体型"变成可分享、可版本化、可被程序引用的**命名资产**；
- **Zeroed Sliders** 是现代事实标准——把起点统一到零，形状交给运行时
  （见 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md)）；
- **HIMBO Zero for OBody** 是作者为零化场景专门准备的预设（见 [himbo.md](himbo.md)）；
- 预设名是 OBody NG / BodyGen / AutoBody 的**键**——改名 = 改配置。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 早期 | BodySlide 与 CBBE 的滑块体系同时诞生 | 预设从第一天就是工具的一等公民（具体日期未确认，见 [bodyslide-outfit-studio.md](bodyslide-outfit-studio.md)） |
| CBBE 各代 | 自带 **Slim / Curvy / Vanilla** 三档 | "官方预设"成为身形的默认交付物 |
| 3BBB / 3BA 世代 | 随包附带大量预设（社区共识：数量远多于其他身形） | 预设开始作为"增值内容"竞争 |
| 2020 前后 | **Zeroed Sliders** 随 OBody / BodyGen 工作流普及 | 社区从"烘一个固定体型"转向"零起点 + 运行时 morph" |
| 2021 | HIMBO 发布，自带 **HIMBO Zero for OBody** 等 13 个预设 | 身形作者开始主动照顾分配工具的需求 |
| 2023-2026 | UBE / 新护甲转换普遍以"预构建 zero-slider 网格 + 预设"分发 | 零化预设成为分发标准形态（社区经验） |

### 它从哪来

预设与 BodySlide 同岁：工具一旦支持"存一组滑块值再复现"，
分享体型就不再依赖截图和文字描述。早期预设只是方便（Slim/Curvy 一键切换），
后来 OBody 出现——它要求基础形状零化、再由它按种族随机分配预设——
**预设从此从"方便"升级为"基础设施"**。

### 中间经历了什么

分水岭是 **Zeroed Sliders 工作流的普及**：玩家发现"烘一个固定体型"会让
BodySlide 预设与 RaceMenu 预设两套体系互相打架（详见
[morph-runtime-vs-bake.md](morph-runtime-vs-bake.md) 第七节），
于是社区统一到"零起点构建 + 运行时调"，OBody NG 更是把这个作为安装前提。

### 现状

形态稳定：`.xml` + 两值结构十年未变；生态上，新身形（HIMBO、UBE）
都自带 zero 预设，新护甲转换普遍预构建零化网格。
预设的"消费者"从玩家扩展到三个自动分配工具——这是它与普通配置文件的本质区别。

## 它解决什么问题

**没有它之前**：换个体型要在 BodySlide 里重拖几十个滑块；
分享体型只能发截图 + 一串数字；NPC 身材分配更是无从谈起
（RaceMenu  morph 只作用于玩家）。

**它的解法**：

1. **一键复现**：存成 `.xml`，任何装了同一身形的人都能用；
2. **程序可读**：OBody NG 启动时扫描 `SliderPresets` 目录建库，
   BodyGen / AutoBody 按名引用——**预设名就是 API**；
3. **跨体重描述**：两值结构让"瘦体型在高体重下变 dadbod"成为可能。

## 形态与位置

预设就是 `SliderPresets/` 下的 **`.xml`** 文件
（完整路径 `Data\CalienteTools\BodySlide\SliderPresets\`）；
另有 `SliderGroups/*.xml` 定义分组。

**XML 的结构要点**：每个滑块**存两个值**——体重 0 一个、体重 100 一个。
所以 BodySlide 预设天然描述「同一个体型在不同体重下的样子」；
游戏里一个体重 50 的 NPC，拿的就是这两个值**线性插值**的结果。

> ⚠️ **BodySlide 预设（`.xml`）与 RaceMenu 预设（`.jslot`）是完全不同的两种文件**：
> 刻度不同（0~100 vs 浮点）、生效方式不同（烘焙 vs 运行时），**不能互相导入**。
> 对照与换算见 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md) 第七节。

**制作方式**：在 BodySlide 里调好滑块 → **Save As** → 存到 `SliderPresets/` →
立刻出现在预设下拉框里（官方 wiki，一手）。

## 使用与配置

玩家侧完整流程（拿到一个预设之后）：

1. **下载**：Nexus 的 *BodySlide Preset* 分类或 LoversLab；
   注意作者是否同时给了项目文件（`.osp`/`.osd`/`.nif`，见"制作与分享"）；
2. **放置**：把 `.xml` 放进 `Data\CalienteTools\BodySlide\SliderPresets\`
   （分组文件进 `SliderGroups\`）；
3. **重启 BodySlide**：预设下拉框里即出现（"Save As 即出现"同理）；
4. **选择并构建**：Outfit/Body 选身体 → Preset 选它 → **Batch Build**
   把同一预设刷给身体与所有衣服（缺一就穿模，见"实践纪律"）；
5. **（可选）交给分配工具**：确认预设名已被
   [OBody NG](../05-distribution/obody-ng.md) 的
   `OBody_presetDistributionConfig.json` 引用，进游戏看 NPC 效果。

> 预设只是"一组数值"，**不装对应身形 mod 就没有滑块可调**——
> 拿到 CBBE 预设的前提是装了 CBBE（或 3BA）。

## 自带预设

| 来源 | 自带内容 |
|---|---|
| CBBE | Slim / Curvy / Vanilla，及对应的 outfit 变体 |
| CBBE 3BA / 3BBB | 随包附带大量预设（社区共识：数量最多的一档） |
| BHUNP | 随包附带，数量略少于 3BBB（社区共识） |
| **HIMBO** | **13 个**：Daddy（低重均称/高重 dadbod）、Jack（低重瘦/高重 dadbod）、Mike（壮）、Simple（低重瘦/高重肌肉）、Sultry（bara 风）、Chonky（全体重胖）、Hassan / Hugh / Hideo（三个全身滑块的单展）、**Zero for OBody**（零化基础，高重带少量调整保持真实）、Urbon、Joseb、Sebastian |

HIMBO 的 **Zero for OBody** 值得单独说：作者原述它"meant to use with mods
like OBody or Bodygen that requires your base shape to be at zeroed sliders"，
并对高体重做了最小调整以免失真——**这是分配工具友好的预设范本**。

## 社区生态

- 通过 Nexus 的 *BodySlide Preset* 分类或 LoversLab 分享；
- 可举证被引用的个人作者例子：**Mousebell**（3BA 玩家预设）；
- **"最流行的预设作者"会随时期变化，不宜写死**，引用时请附日期与来源链接；
- 常见的分发形态不是裸预设，而是"**预构建 zero-slider 网格 + 预设 +
  patch plugin**"一整套（配合 OBody NG 使用，社区经验）。

## 预设如何被"再引用"

这是本条目最实用的部分：**预设名是上游配置的键**。

| 消费方 | 配置文件 | 引用方式 |
|---|---|---|
| **OBody NG** | `SKSE/Plugins/OBody_presetDistributionConfig.json` | 按 `raceFemale` / `raceMale` / 黑名单等规则指定可用预设；**启动时直接扫描 `Data\CalienteTools\BodySlide\SliderPresets` 下的 XML 建库** |
| **RaceMenu BodyGen** | `meshes/actors/character/BodyGenData/<插件名>/templates.ini` | `模板名=morph@值 \| morph@区间` |
| **AutoBody** | `morphs.ini` | 用 EditorID 匹配（如 `All\|Female\|TownWhiterunFaction`） |

所以"给 NPC 分配不同身材"**本质上就是引用你的 BodySlide 预设名**。
预设命名杂乱会让分配层很难配置——建议**统一命名规范**
（如 `<身形>-<风格>-<体重倾向>`，别用"最终版2""test1"）：

```
<身形>-<风格>-<用途>      例：CBBE-Zeroed-Base / HIMBO-Zero-for-OBody / 3BA-Curvy-NPC
```

- **带身形前缀**：OBody NG 按名引用时一眼看出适配对象；
- **带 `Zeroed` 字样**：标明这是零化基础，不是最终体型；
- **别用"最终版2""test1"**：分配工具的配置里全是这种名时，排查生不如死。

详见 [obody-ng.md](../05-distribution/obody-ng.md) 与
[racemenu-bodygen.md](../05-distribution/racemenu-bodygen.md)。

## 制作与分享（作者向）

玩家侧"Save As 存预设"只是半成品；**完整可分享的单位是 BodySlide 项目**。
官方 wiki 给出的打包清单（保存项目后应产生的文件）：

```
SliderSets\*.osp            ← 项目定义（一个 .osp 可含多个项目）
ShapeData\<项目名>\*.osd    ← 滑块数据（二进制）
ShapeData\<项目名>\*.nif    ← 网格本体
SliderGroups\*.xml          ← 分组定义（可选）
```

配套两个易漏的动作（官方 wiki，一手）：

- **分组**：用 BodySlide 右上角的 **Group Manager** 把项目加进身形主组
  （如 `CBBE`），否则预设下拉里看不到它；
  ⚠️ 给项目建了 solo 组时，**别忘了同时加进主组**（官方 wiki 原注）。
- **conform 与骨骼权重**：Outfit Studio 里 `Slider -> Conform All` +
  复制骨骼权重，是项目能跟着滑块变的前提
  （机制见 [bodyslide-outfit-studio.md](bodyslide-outfit-studio.md)）。

> ⚠️ **权重变体陷阱**（官方 wiki 明示）：Skyrim 系网格常用 `_0` / `_1`
> 后缀区分低/高体重文件，**要分别为两个变体做项目**，只做一个会另一半没形状。

## 一条实践纪律

> **裸身与服装必须用同一个预设构建。**
> 裸身用 Curvy、服装用 Slim，结果是穿模——这是穿模问题最常见的自伤原因。

现代工作流把这条纪律升级为：**先用身形自带的 Zeroed Sliders 勾
`Build Morphs` 全量 Batch Build，再在游戏里用 RaceMenu 实时调**
（六步见 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md)）。
固定预设没有消失，只是从"最终形状"退位成"分配工具的素材"。

⚠️ **Zeroed Sliders 里有滑块是 100% 是正常的，不要改**——
BHUNP 与 CBBE 3BA 的官方预设都可能带 100% 的项，这是有意设计；
优先用身形自带的 Zeroed Sliders，确实没有才自己做一份。

排查详见 [clipping.md](../06-troubleshooting/clipping.md) 与
[preset-not-applied.md](../06-troubleshooting/preset-not-applied.md)。

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 预设下拉里没有我的 xml | 放错目录 / 文件损坏 / 工具没重启 | 放 `Data\CalienteTools\BodySlide\SliderPresets\`；重启 BodySlide |
| 构建后穿模、破皮 | 裸身与衣服用了不同预设 | 同一预设重新 Batch Build；不会用就上 Zeroed Sliders 工作流 |
| OBody NG 不分配我的预设 | 预设不在 `SliderPresets` 目录 / 名字没被 json 引用 | 把 xml 放进该目录；检查 `OBody_presetDistributionConfig.json` 的规则 |
| 想"把 BodySlide 预设搬进 RaceMenu" | 两套体系格式、刻度、生效方式都不同 | 没有直接办法；只能逐滑块手工换算（见 morph 条目第七节） |
| Zeroed 预设里有 100% 想"修正" | 官方设计如此 | 别改；用身形自带的 Zeroed Sliders |
| NPC 身材不生效 / 不随机 | RaceMenu morph 只作用于玩家 | 这是设计而非 bug；用 OBody NG / BodyGen 分配 |
| 换了预设游戏里没变化 | 构建输出被覆盖 / 没 Batch Build 到衣服 | 查覆盖关系（[mo2-override-rules.md](../07-workflow/mo2-override-rules.md)）与冲突列表 |
| 别人分享的预设在我这下拉里没有 | 只发了 `.xml`，没发项目文件（`.osp`/`.osd`/`.nif`） | 要对方补打包项目文件（见"制作与分享"） |
| 项目建好了但预设选不了 | 没加进身形主组（solo 组忘了挂主组） | Group Manager 补挂主组 |

## 取舍与建议

- **只想换个体型**：用身形自带预设 + Batch Build，别从零拖滑块；
- **想给 NPC 分配身材**：预设 + [OBody NG](../05-distribution/obody-ng.md)，
  基础构建用 Zeroed Sliders（或 HIMBO Zero for OBody）；
- **想分享自己的体型**：导出 `.xml` 时**命名带身形与风格**
  （如 `CBBE-Zeroed-Base`），别人好引用，OBody 也好配；
- **不要攒上百个预设**：分配工具按名引用，池子越大配置越难维护；
  留 3~5 个常用的足够。

**版本敏感性**：预设格式（两值 XML）与目录路径多年稳定，
但各身形**自带预设清单随版本增减**（本条 HIMBO 清单来自其描述页，
对应版本未精确到小版本）；引用时以对应身形当前发布页为准。

## 来源

- **一手（官方 wiki）**：预设文件位置（`SliderPresets/`）、"Save As 即出现"、
  项目分享文件清单（`.osp` / `.osd` / `.nif` / SliderGroups xml）、
  Group Manager 与"solo 组别忘挂主组"、`Slider -> Conform All` 与复制骨骼权重、
  Skyrim `_0` / `_1` 权重变体需分别做项目
  `https://github.com/ousnius/BodySlide-and-Outfit-Studio/wiki/Creating-a-BodySlide-project`
- **一手（Nexus 页，经转载）**：HIMBO 13 个自带预设及其说明
  （Daddy/Jack/Mike/Simple/Sultry/Chonky/Hassan/Hugh/Hideo/Zero for OBody/
  Urbon/Joseb/Sebastian；Zero for OBody 的设计意图）
  `https://www.nexusmods.com/skyrimspecialedition/mods/46311`
- **一手（作者文档）**：OBody 启动时扫描 `Data\CalienteTools\BodySlide\SliderPresets`
  下的 XML 预设并建库、按种族分配——OBody 作者 Patreon/文档（经社区整理）
- **一手（各工具配置说明）**：OBody NG 的
  `OBody_presetDistributionConfig.json`、BodyGen 的 `templates.ini` 语法、
  AutoBody 的 `morphs.ini` EditorID 匹配
- **社区经验**：自带预设数量对比（3BBB > BHUNP）、"预构建 zero-slider 网格 +
  预设 + patch plugin"分发形态、Mousebell 预设、"最流行预设作者随时期变化"、
  命名规范建议
- **未确认**：CBBE/BHUNP 自带预设的逐版本清单、社区预设的 Nexus 分类现状
