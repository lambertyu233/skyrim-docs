---
id: morph-runtime-vs-bake
title: 运行时 morph 与离线烘焙——为什么拖滑块衣服跟着变，换预设就穿模
category: 03-body
kind: concept
version: 1.0.0
updated: 2026-09-22
tags: [身形, morph, 烘焙, Zeroed Sliders, 原理, RaceMenu, BodySlide]
aliases: [运行时变形, 离线烘焙, 换预设穿模, 拖滑块衣服跟着变, 归零构建, 两套预设不通用, 3ba 那一栏, 裸体调好了穿衣服又变样]
source: https://forums.nexusmods.com/topic/12433428-cant-use-my-own-character-preset/
summary: 用"运行时 morph vs 离线烘焙"两条路径解释身形的全部行为：捏脸菜单里那一栏的三层来源、为什么拖滑块衣服会跟着变、为什么换 BodySlide 预设就穿模，以及 Zeroed Sliders + Build Morphs + Batch Build 这条正解工作流。
---

# 运行时 morph 与离线烘焙

这一页回答四个连在一起的问题，它们是同一个机制的不同侧面：

1. 捏脸菜单里「CBBE 3BA」那一栏是谁给的？
2. 为什么在菜单里拖滑块，身上衣服会**一起跟着变**？
3. 为什么在 BodySlide 里换个预设，衣服就**不匹配**了？
4. 有没有一劳永逸的装法？

**答案的关键是把"变形"拆成两条完全不同的路径**：一条在运行时算，一条在构建时烘焙。

---

## 一、身型的第一性事实

> **Skyrim 里"穿衣服"不是给身体套一层布，而是用装备网格直接替换裸体网格。**

装备本身就是"一具穿好衣服的身体"。所以身型问题的本质**只有一个**：

> **所有网格（裸体 + 每一件衣服护甲）的顶点形状必须一致。谁不一致，谁穿模。**

后面所有现象都是这一句的推论。

---

## 二、那一栏是谁给的：三层叠加

| 层 | 贡献 | 缺了会怎样 |
|---|---|---|
| **RaceMenu** | 菜单框架 + NiOverride 的**运行时施加 morph** 能力 | 没有捏脸界面，也就没有那一栏 |
| **身形的 RaceMenu Morphs 组件**（如 `RaceMenuMorphsCBBE.esp` / `RaceMenuMorphsUUNP.esp`） | 决定这一栏**有哪些滑块、叫什么名字** | 滑块不出现 |
| **你自己用 BodySlide 勾 `Build Morphs` 构建出的 `.tri`** | 真正的**变形数据**（并在 NIF 里写入 `BODYTRI` 指向它） | 那一栏是空的，或拖了没反应 |

> 一句话：**栏目的"名字"来自身形 mod，"能变形的数据"来自你自己的构建。**

3BA 另带的物理骨骼与顶点权重（负责抖动）**与滑块变形是两回事**，别混：
前者是物理模拟，后者是 morph 位移。

对应到本资料库：
[`cbbe-3ba.md`](cbbe-3ba.md)（谁定义滑块）、
[`../02-face/racemenu.md`](../02-face/racemenu.md)（谁提供能力）、
[`bodyslide-outfit-studio.md`](bodyslide-outfit-studio.md)（谁产生数据）。

---

## 三、两条变形路径（本页核心）

| | **运行时 morph** | **离线烘焙（BodySlide Build）** |
|---|---|---|
| 何时算 | 游戏运行中，每一帧 | 你在 BodySlide 里点 Build 的那一刻 |
| 算在哪 | 内存里的网格顶点 | **写进 `.nif` 的顶点坐标**（落盘，成静态模型） |
| 输入 | RaceMenu 界面的滑块值 | BodySlide 预设（一组数值） |
| 结果 | 临时形变，**不改任何文件** | 生成一个新网格文件 |
| 谁能享受 | **只影响玩家**（以及被显式分配过的 NPC） | **所有用这个网格的人**（含全部 NPC） |
| 作用对象 | 身上**所有带同名 morph 的网格** | 你构建的那一个项目 |

**这两条路径互不替代，而且是叠加的**：先在构建时烘出一个"起点形状"，
再在运行时往它上面叠加 morph。**起点不一致，叠加就必然错位 —— 这就是穿模的来源。**

---

## 四、conform：衣服为什么"拥有同一套 morph 名字"

3BA 的衣服在 **Outfit Studio** 里做过 **conform** —— 把身体的滑块形变数据**复制到衣服的顶点上**。
于是衣服和身体**拥有同一套 morph 名字**（`Breasts`、`AppleCheeks`…）。

这就是"拖滑块衣服跟着变"的机制：

```
你在菜单里拖 Breasts
  → NiOverride 遍历身上所有含名为 Breasts 的 morph 的网格
  → 对它们同时施加顶点位移（运行时实时，不改文件）
  → 身体与衣服按同一规则一起变 ⇒ 始终贴合
```

**反之**：某件衣服没被 3BA 化、不带这套 morph，它就**纹丝不动**。
这就是最常见的抱怨 —— **"裸体调好了，穿上衣服又变样"**。

---

## 五、于是两个现象都解释得通了

### 为什么拖滑块是安全的

因为它是运行时叠加，**不改变起点**。身体和衣服的起点本来就一致，叠加规则也一致。

### 为什么换预设就穿模

因为 BodySlide 的 Build 是**离线烘焙**：预设是一组滑块数值，Build 把这些数值
**永久写进 `.nif` 的顶点坐标**，生成一个静态模型。

> 你换预设只重新烘焙了**身体**，衣服的 nif 还停在**上一个预设的形状** ——
> 顶点对不上 ⇒ 破皮、穿模、塌陷。

三个常见自伤原因（详见 [`../06-troubleshooting/clipping.md`](../06-troubleshooting/clipping.md)）：

1. 只 Build 了身体，**没 Batch Build 把同一预设刷给所有衣服**；
2. 衣服**压根不支持 3BA**（是给 CBBE 或 UNP 做的，滑块组和骨骼都对不上）；
3. **预设用错**，例如把 CBBE 预设套在 3BA 项目上。

---

## 六、正解工作流：Zeroed Sliders + Build Morphs + Batch Build

思路是**把"起点"统一到零，把"形状"全部交给运行时**。这样所有网格起点一致，
之后实时 morph 对谁都生效，随便调都不会穿模。

### 六个步骤

1. **打开 `skee64` 配置**（RaceMenu 安装目录下 `SKSE\Plugins\skee64`），确认：
   - `bEnableBodyMorph=1`（启用 BodySlide 辅助变形）
   - `bEnableBodyGen=0`（按需；这是随机化，与本节无关）
2. **BodySlide 的 Group Filter** 里勾选你的身体与所有服装所在的组。
   ⚠️ **很多服装在 `Unassigned` 组**（下拉列表最后一个），**别忘了勾它**。
3. **Outfit/Body 选你的主身体**：
   - CBBE 3BA → `CBBE 3BBB Body Amazing`
   - BHUNP → `BHUNP 3BBB Advanced Ver 3` 或 `Ver 4`
4. **Preset 选 `Zeroed Sliders`**（滑块归零），然后**勾上 `Build Morphs`**，点 **Batch Build**。
5. 在构建列表里**确认每一件服装都在**。缺了 → 回 Group Filter 找漏勾的组。
6. 出现**冲突解决列表**时（装了多个身体版本时必然出现），**统一选你第 3 步选的那个身体**。

### 两个容易踩的细节

- ⚠️ **Zeroed Sliders 里有滑块是 100% 是正常的，不要改。**
  BHUNP 与 CBBE 3BA 的官方 Zeroed Sliders 预设都可能带 100% 的项，这是**有意设计**。
  优先用你的身体 mod 自带的 Zeroed Sliders；确实没有才自己做一份。
- **代价**：带 morph 的 `.tri` 文件很大。社区实测过某大型身体包因此让网格体积
  从 1GB 涨到 4GB。这是"所有衣服都能实时调"的价格。

做完之后：进游戏，用 RaceMenu 那一栏调形状 —— 会即时作用到身体和所有衣服上。

---

## 七、两套预设体系不通用（重要）

**BodySlide 预设和 RaceMenu 预设不是同一种东西，也不能互相导入。**

| | BodySlide 预设 | RaceMenu 预设 |
|---|---|---|
| 文件 | `.xml` | `.jslot` |
| 位置 | `Data\CalienteTools\BodySlide\SliderPresets\` | `Data\SKSE\Plugins\CharGen\Presets\` |
| 存储内容 | **每个滑块在体重 0 与体重 100 各一个值** | `bodyMorphs` 段里的**浮点数** |
| 数值刻度 | **0 ~ 100** | **浮点**（实测样例是 `0.50000` 这种 0~1 量级） |
| 生效方式 | Build 时**烘焙进 nif** | 游戏内**运行时施加** |

RaceMenu 预设里的条目长这样（注意 `keys[].key` 指向**提供 morph 的那个 esp**）：

```json
{ "keys": [ { "key": "RaceMenuMorphsCBBE.esp", "value": 0.50000 } ], "name": "Breasts" }
```

BodySlide 预设里的对应内容则是"体重 0 一个值、体重 100 一个值"，
所以它天然支持"同一个体型在不同体重下呈现不同效果"。

> **推论**：想"把 BodySlide 预设搬进 RaceMenu"，**没有直接办法**，只能逐滑块换算
> （社区给出的做法：以体重 100 的 BodySlide 值为准换算到 RaceMenu 的浮点刻度，
> 手工改 `.jslot` 里对应条目的 `value`）。**别指望两边的文件能互相导入。**

另外两个数值体系的细节：

- BodySlide 的滑块可以**手输负数或大于 100**（官方说"不推荐"，但不是硬限制）。
- RaceMenu 滑块的可拖范围由 `RaceMenuMorphs*.psc` 里 `OnSliderRequest` 的
  `Float factor` 决定（社区记录默认 `2.0`，改它需要把 `.psc` 重编译成 `.pex`）。
  ⚠️ **常见说法"RaceMenu 滑块是 -1 到 +1"并不准确** —— 以你实际界面为准。

---

## 八、玩家 vs NPC

| | 手动拖 RaceMenu 滑块 | BodySlide 烘焙 |
|---|---|---|
| 玩家 | ✅ 直接生效 | ✅ 生效 |
| NPC | ❌ **不生效** | ✅ 生效（按 NPC 自己的体重在 0/100 两值间线性插值） |

**所以"我调好了身材，NPC 却还是老样子"是正常的**，不是 bug。

要让 NPC 有不同身材，有两条路：

1. **分配工具**（推荐）：[`racemenu-bodygen.md`](../05-distribution/racemenu-bodygen.md) /
   [`obody-ng.md`](../05-distribution/obody-ng.md) / [`autobody.md`](../05-distribution/autobody.md)。
   OBody NG 的做法正是**读取你 `SliderPresets` 文件夹里的 `.xml` 预设**，
   把它分配给 NPC —— 这也解释了为什么它要求你先做第 6 节的 Zeroed Sliders 基础构建。
2. **给单个 NPC 专属身体**（社区经验，工作量大但精确）：
   以目标预设本地构建裸体/手/脚 → 把网格复制到该 NPC 的专属文件夹 →
   在 CK 里建指向这些 nif 的 ArmorAddon → 建一个含这些 Addon 的 Armor →
   把它设为该 NPC 的"裸体皮肤"。

---

## 来源

- **两条路径的机制与对比、conform 与"同一套 morph 名字"、Zeroed Sliders 优于固定预设**：
  LoversLab 关于"RaceMenu BodySlide 插件该以什么基准构建网格"的讨论
  （Pauduan 的解答，指出"按某预设构建后，游戏内 morph 会作用在那个形状上而非基准形状"）
  —— **社区经验（机制解释清楚，与官方机制一致）**
  `https://www.loverslab.com/topic/83189-skyrim-special-edition-male-dick-mod`
- **Zeroed Sliders + Build Morphs + Batch Build 六步流程、`bEnableBodyMorph` / `bEnableBodyGen`、
  "Zeroed Sliders 里有 100% 是正常的不要改"、冲突列表选同一身体、必勾 `Unassigned` 组**：
  OBody NG 安装指南（第三方整理的步骤文档）—— **社区文档**
- **`.xml` 预设位于 `Data\CalienteTools\BodySlide\SliderPresets`、每个滑块存体重 0/100 两个值、
  `.jslot` 的 `bodyMorphs` 存浮点、两套体系不通用的换算步骤、给单个 NPC 专属身体的 ArmorAddon 做法**：
  Nexus 论坛 scorrp10 的详细解答（附实际文件片段）—— **社区经验（引用了实际文件内容）**
  `https://forums.nexusmods.com/topic/12433428-cant-use-my-own-character-preset/`
- **RaceMenu 只作用于玩家；NPC 用 BodySlide 构建的网格并按体重线性插值**：
  LoversLab 帖（同一段解释里给出体重 0/100 线性外推的例子）—— **社区经验**
- **RaceMenu 滑块上限由 `OnSliderRequest` 的 `factor` 决定（默认 2.0）、改它需重编译 `.pex`**：
  LoversLab 帖 —— **社区经验（仅见于 UUNP 脚本的讨论，标注"未完全确认"）**
- **`.tri` 文件体积代价**：LoversLab 帖（某身体包网格自 1GB 涨至 4GB）—— **社区经验**
- **`Build Morphs` → `.tri` + `BODYTRI` → NiOverride 运行时施加**：
  BodySlide 官方仓库提交记录与 wiki、RaceMenu 发布页 —— **一手（机制）**
- **Outfit Studio 负责"在身形之间转换服装、创建滑块"（含 conform）**：
  BodySlide 官方 wiki —— **一手**
- **NiOverride / CharGen 属于 `skee64.dll`**：RaceMenu 发布页与源码仓库 —— **一手**
"""

