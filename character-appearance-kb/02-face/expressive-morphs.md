---
id: expressive-morphs
title: Expressive Facegen Morphs 与 Expressive Facial Animation（EFM / EFA）
category: 02-face
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [捏脸, EFM, EFA, 表情, morph]
aliases: [expressive facegen morphs, expressive facial animation, 表情包, 面部表情, 表情 morph, 脸部动画, 表情滑块, 捏脸表情, niroku, EFM 历史, 怎么装 EFM, 表情不生效, 嘴部 morph, 吸血鬼牙齿, NPC 没表情]
source: https://www.nexusmods.com/skyrimspecialedition/mods/35785
summary: 作者 Niroku 的面部 morph 系列——EFM 换掉原版 chargen/race morph 并给 RaceMenu 加滑块，EFA 换掉表情 morph；写清两者的分工、覆盖种族、主文件与可选插件的区别、自带网格的冲突，以及"只影响玩家、不影响 NPC"这条最关键的限制。
---

# Expressive Facegen Morphs 与 Expressive Facial Animation

> **一句话分工**：**EFM 管"你捏出来的这张静态脸长什么样"，EFA 管"这张脸动起来什么样"。**
> 两个 mod 是同一作者、面向同一套原版头部网格做的，一起装是官方推荐组合，
> 但**作用层不同、影响范围也不同**，混着理解就会得出错误预期。

---

## 速览

| 项目 | EFM（Expressive Facegen Morphs） | EFA（Expressive Facial Animation） |
|---|---|---|
| 作者 | **Niroku**（Nexus 用户 35150865） | **Niroku** |
| Nexus（SE / LE） | **35785** / **102796** | 女 **19181** / 男 **19532**（LE 92897 / 93258） |
| 当前版本 | **1.0** | 女 **1.7**、男 **1.21** |
| 首发 | LE **2020-05-10**；SE **2020-07** 前后（**一手，归档文件名时间戳**） | SE 女版 **2018-08-08**；男版日期**未确认** |
| 前置 | **RaceMenu**（硬前置，不用则须禁用 esp/esl） | EFM 主文件为推荐；可选嘴部文件需 **Fair Skin Complexion** |
| 作用层 | chargen + race morph（**捏脸**） | 表情 morph：phoneme / modifier / mood（**动画**） |
| 影响范围 | **仅玩家** | 发布页原文写"players and NPCs"（影响**表情动画**，不改脸型） |
| 许可证 | 严格：禁止转载 / 修改 / 转平台 / 取用资产 | 同左 |
| 维护状态 | 停在 1.0，作者未宣布后续计划 | 停在女 1.7 / 男 1.21 |

要点：

- **EFM 覆盖 9 个种族**：Nord、Imperial、Breton、Redguard、Elder、High Elf、Dark Elf、Wood Elf、Dremora。
- **新增滑块用连字符命名**（如 `Lip-Height`），在 RaceMenu 的 FILTER 里搜 **`EFM`** 就能全部筛出来。
- **两个文件必须二选一**：主文件面向**新预设**、不兼容旧脸；可选 `EFM - Racemenu Plugin` 只有滑块、可保留旧脸。
- ⚠️ **EFM morph 不适用于 High Poly Head / Citrus Heads**，作者明确表示**暂无计划支持**不同网格。
- ⚠️ **装主文件时不要同时装** Enhanced Female Head Mesh / Eyes AO Clipping Fix。

---

## 前世今生

### 时间线

| 时间 | 事件 | 意义 |
|---|---|---|
| 原版 | Bethesda 自带一套 chargen / race morph（`.tri`）与表情 morph | 滑块少、变形生硬，复杂组合容易破坏网格 |
| **2018-08-08** | **EFA 女版（SE 19181）**首发 | Niroku 先做表情：替换 phoneme / modifier / mood |
| 2018-08 起 | EFA 男版（SE 19532）跟上；两个版本各自迭代 | 表情 morph 覆盖面补齐 |
| **2019-12** | EFA 女版 **1.7**（2019-12-07）、男版 **1.21**（整合包记录同一批次）定版 | 现行版本，此后未见更新 |
| **2020-05-10** | **EFM（LE 102796）**首发 | 从"表情"推进到"捏脸"，替换 chargen + race morph |
| **2020-07** 前后 | **EFM SE（35785）**上线；版本 1.0 的 changelog 只有一句 **"Added male version"** | 说明 1.0 之前只有女版（LE 页标签至今仍是 *Only for Female Characters*） |
| 此后 | EFM 停在 1.0；HPH 成为现代预设事实标准，EFM 未跟进 | 见下"为什么 HPH 用户用不上" |

### 原版的局限 → Niroku 的两步

原版那套 morph 的问题不是"不够多"，而是**变形质量**：顶点位移设计粗糙，多个滑块叠加时
容易把网格拉坏（嘴角撕裂、眼皮穿模、眉部错位）。Niroku 的做法分两步：

1. **先做 EFA（表情）**——把嘴唇、眉毛、眼球运动的表情 morph 全部重做，
   作者自己在 changelog 里反复处理的就是"穿模"：`1.1 Improvement of tongue clipping`、
   `1.2 LookUp / Down and mouth clipping countermeasure`。
2. **再做 EFM（捏脸）**——把 chargen 与 race morph 也重做，并额外加一批 RaceMenu 滑块。
   官方承诺是"**designed to be deformed smoothly and will not break the mesh structure
   even in complex combinations**"，并且**保证与 EFA 兼容**（这解释了为什么两者常被一起装）。

### 现状：停在 1.0，与 HPH 路线分道

EFM 最后停在 **1.0**，没有跟进 High Poly Head。作者的原话是：

> The morphs in this mod are for vanilla head mesh, they don't work with different meshes
> like Citrus Heads or High Poly Heads. **Currently there are no plans to support different meshes.**

**这不是 bug，是路线选择**：EFM 依附于原版头的顶点数与顶点顺序；HPH 换掉了头部网格，
两者对不上。所以社区现在的现实是——**现代预设绝大多数按 HPH 做，EFM 在这些预设上用不了**，
EFM 主要留在"原版头 + 原版系预设"这条线上。

---

## 它解决什么问题

### 没有它之前

- 原版 chargen 滑块少且粗，捏不出细节，多滑块叠加会破坏网格；
- 表情 morph 呆板，说话时口型与情绪对不上（社区俗称"木头脸"）；
- 吸血鬼变脸靠替换整张脸型 morph，容易和其他改动打架。

### 它怎么解决的

| 问题 | EFM 的做法 | EFA 的做法 |
|---|---|---|
| 捏脸变形质量 | 重做 chargen + race morph，保证平滑变形 | — |
| 滑块不够 | 额外加一批 RaceMenu 滑块（连字符命名） | — |
| 表情呆板 | — | 重做全部 phoneme / modifier / mood |
| 吸血鬼 | **移除脸型 morph**，改为**牙齿 morph** + 一个独立的 RaceMenu 吸血鬼滑块 | — |

---

## 工作原理

morph 文件（`.tri`）记录的是"每个顶点往哪移动多少"，同一套机制被用在两个层面：

| 层 | 谁用 | 何时算 |
|---|---|---|
| **chargen / race morph**（EFM） | 角色创建时的脸型构造 | 捏脸时 + 玩家角色加载时 |
| **表情 morph**（EFA） | 对话、情绪、喊叫时的面部运动 | 运行时按事件触发 |

> **为什么 EFM 只影响玩家而 EFA 能影响 NPC**：玩家的脸是**实时按 morph 生成**的，
> NPC 的脸是 **FaceGen 预生成好的静态网格**（原理见 [`facegen-pipeline.md`](facegen-pipeline.md)）。
> 所以 EFM 改的"脸型构造过程"对 NPC 根本不会发生；而 EFA 改的"表情位移"是运行时叠加的，
> 发布页因此写的是 *used by players and NPCs*。
> ⚠️ 但 EFA **不会改变 NPC 的脸型**——那仍是它自己那张预生成网格（**一手 + 推断**）。

底层概念（`.tri` / `BODYTRI` / morph 与网格的关系）见
[`../00-overview/morph-and-nif-basics.md`](../00-overview/morph-and-nif-basics.md) 与
[`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

---

## 安装

1. **先装好 RaceMenu**（硬前置），确认捏脸界面正常。见 [`racemenu.md`](racemenu.md)。
   验证点：`Data/SKSE/Plugins/` 下有 skee64 相关文件，捏脸界面能打开。
2. **决定用哪个文件**（这是最容易装错的一步，见下表）。
3. **用 mod 管理器安装**。作者明确：*"Please use mod manager to install this mod.
   Manual installation is not recommended."*
4. **启用插件**：SE 下是 `Expressive Facegen Morphs.esl`，LE 下是 `.esp`。
   它是**空插件**，不用管加载顺序，但**必须启用**；不打算用时请禁用它。
   验证点：MO2 右侧插件列表里该 esl 处于启用状态。
5. **装 EFA（可选但推荐）**：女版 19181 + 男版 19532 可同时装（分别作用于各自性别）。
6. **进游戏验证**：打开 RaceMenu → 在 FILTER 里输入 `EFM` → 应筛出一批连字符命名的滑块。
   一个都没有 = 第 4 步的插件没启用，或装成了不含滑块的组合。

### 两个文件怎么选（关键）

| 文件 | 适用 | 内容 | 对既有预设 |
|---|---|---|---|
| 主文件 `Expressive Facegen Morphs` | **新预设** | chargen + race morphs、额外 RaceMenu 滑块、**自带网格** | ❌ **不兼容，装前务必备份脸数据（存档 / 预设 / 网格）** |
| 可选 `EFM - Racemenu Plugin` | **既有预设** | **只有**额外的 RaceMenu 滑块 | ✅ 保留当前脸，只是多一批滑块 |

> 选错会得到两种**相反**的结果：用主文件 → "我的预设全乱了"；
> 用可选插件想要完整效果 → "滑块不够 / 脸没变"。

**卸载**：直接禁用或删除即可，脸会用安装前的 morph 重建；装前备份过预设就重新载入。

---

## 使用与配置

### 找滑块：用 FILTER 而不是翻列表

作者在原帖 Q&A 里专门回答了"我懒得找滑块"：RaceMenu 的 **FILTER** 支持搜索，
可搜 **`EFM`**、**`EFM_Eye`**、**`Upper`** 等关键词。

搜索命中的其实是**翻译文件里带 `$` 的名字**（如 `$EFM_Lip_Height`），
所以 EFM 的全部语言文件都统一用英文词，不会因为语言切换而搜不到：

```
Data\Interface\Translations\Expressive Facegen Morphs_xxx.txt
```

### 滑块范围

滑块的可调范围由 RaceMenu 的 ini 决定（作者给出的示例值）：

```
Data\SKSE\Plugins\Charagen.ini
fSliderMultiplier=3.0
```

> ⚠️ 该 ini 的**确切文件名以你本机的 RaceMenu 为准**（不同版本写作 `CharGen.ini` 等）；
> 上面是 EFM 作者原文写法。

### 重置雕塑

在 Sculpt 界面按 **`Z`** 键——重置的是**头部部件面板最右端复选框里被选中的那一项**。

### 自定义种族看不到 EFM 滑块

需要在 EFM 的 `races.ini` 里登记你的种族：

```
Data\meshes\actors\character\facegenmorphs\Expressive Facegen Morphs.esp\races.ini
```

基础 morph 替换对自定义种族**可能不兼容**；若该种族用的是原版脸网格，RaceMenu 那部分滑块仍可用。

### 想预览表情

> **RaceMenu 的表情滑块不受 EFA 影响**（它们不引用 EFA 的文件）。
> 想在角色创建时预览表情，只能用**控制台命令**设表情，这需要
> **opparco mfg Command for SSE** 或 **Mfg Fix**。

另外：**用 RaceMenu 的 Facegen 导入功能时，务必先把表情控制台命令重置**，否则脸是歪的。

---

## 兼容与冲突

| 对象 | 关系 |
|---|---|
| **RaceMenu** | 硬前置。EFM 是给 RaceMenu 做的 |
| **ECE** | ❌ **不兼容**（*"does not work with ECE"*） |
| **High Poly Head / Citrus Heads** | ❌ morph **不适用**，作者**暂无计划支持**。HPH 的 FOMOD 里有 EFM 配套项（07），但那是打包便利，不等于 morph 生效。见 [`high-poly-head.md`](high-poly-head.md) |
| **Enhanced Female Head Mesh**（LE 94545）/ **Eyes AO Clipping Fix**（LE 97707） | ❌ **用 EFM 主文件时不要装**，同类 mod 同理 |
| **EEO 一类替换 chargen / race morph 的 mod** | ⚠️ 改用 `EFM - Racemenu Plugin`；用主文件覆盖且对方自带 morph 文件时会穿模 |
| **其它 morph 文件覆盖 EFM 的 `.tri`** | ❌ **文件冲突会导致穿模**（作者原话） |
| **细线类化妆（thin line makeup）** | ⚠️ 头部 UV 被修过，**可能破图**——这是为减少变形拉伸的取舍 |
| **Female Facial Animation** | ❌ EFA 与之冲突（改同一批文件），二选一 |
| **眉毛 / 胡须 mod** | ⚠️ 若其引用了**独特的 morph**，变形对不上就会穿模 |
| **加载顺序** | 社区（预设包作者）经验：**HPH 排在 EFM 之前**。插件本身是空 esl，顺序影响很小 |

### 自带网格到底改了什么（重要）

EFM 主文件带的网格是**调整过 UV 与 shader flag 的原版网格**：

| 文件 | 改动 |
|---|---|
| `femalehead.nif` | UV map（修眼睛与鼻子） |
| `eyesfemale.nif` 等 | UV map（修睫毛）、**Shader Flags（双面）**、Eye Reflection（位置与大小） |
| `mouthhuman(f).nif` | EFA 嘴部的升级版，为 **Fair Skin（HHaleyy）嘴部纹理**适配过的原版网格 |

> 主文件含嘴部网格与纹理。**想用别的嘴部 mod**，必须删掉/禁用 EFM 的对应文件，
> 或用别的 mod 覆盖它——EFM 的嘴部 UV 是为了匹配自带纹理改过的，**配别的纹理会对不上**。

### 许可限制（作者原文）

禁止转载到其它站点、禁止修改（含修 bug）、禁止转换到其它游戏、禁止取用其资产；
作者补充：**不要把 EFM 的 `.tri` 打包进你的 mod**；NPC / 随从类 mod **不需要**内含 EFM morph 文件。

---

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 装完**预设全乱了** | 用了主文件 | 主文件本就不兼容旧预设：载入备份，或改用 `EFM - Racemenu Plugin` |
| **搜不到 EFM 滑块** | FILTER 输入 `EFM` 一条都没有 | 检查 `Expressive Facegen Morphs.esl` 是否已启用；换语言试试（翻译文件用英文名） |
| 自定义种族**看不到滑块** | 只有该种族缺 | 在 `races.ini` 里登记该种族 |
| **NPC 脸没变化** | 玩家变了、NPC 没变 | **这是设计，不是 bug**——NPC 脸是预生成网格 |
| **眉毛 / 胡须穿模** | 只在装了眉/须 mod 后出现 | 多为**文件冲突**（对方引用了自己的 morph）或雕塑导致顶点错位 |
| **细线妆容断裂** | 换上 EFM 主文件后出现 | UV 被修过的已知副作用，换妆容贴图 |
| 嘴部**纹理对不上 / 发白** | 装了别的嘴部 mod | 禁用或覆盖 EFM 的 `mouthhuman(f).nif` |
| 滑块**能拖但幅度太小** | — | 调 RaceMenu ini 的 `fSliderMultiplier` |
| EFA 装了但**表情没变化** | 说话时嘴不动 | 确认没和 Female Facial Animation 并存；确认头部是原版网格 |
| 更泛的"滑块不出现" | — | 见 [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md)、[`../06-troubleshooting/preset-not-applied.md`](../06-troubleshooting/preset-not-applied.md) |

---

## 取舍与建议

- **用原版头 / 原版系预设 → 值得装**。EFM 是这条线上几乎唯一把 chargen morph 整体重做的方案，
  和 EFA 是官方推荐的配套组合。
- **用 High Poly Head → EFM 用不上**。别指望它，morph 对不上就是没有。
  这条线上的替代是 HPH 自带的 morph + 预设作者自己的雕塑。
- **想保住现有脸 → 只装 `EFM - Racemenu Plugin`**。它只加滑块、不动既有 morph，
  也是"和 EEO 一类 mod 并存"时的正确选择。
- **装主文件前必须备份**（存档、`.jslot` 预设、网格）。这不是谨慎，是必需步骤。
- **别用 ECE**。两者不在同一套体系上，预设也不互通。
- **别把它当"NPC 美化"**。它改变的是玩家的脸型构造过程；想改 NPC 的脸要走 FaceGen 重导那条路
  （见 [`facegen-pipeline.md`](facegen-pipeline.md)）。

---

## 来源

**一手（Nexus 发布页 / 作者原帖）**

- EFM（LE 102796 / SE 35785）发布页：覆盖种族、连字符命名与 `EFM` 搜索、只影响玩家、
  主文件 vs `EFM - Racemenu Plugin`、自带网格改动清单、HPH/Citrus 不支持且无计划、
  Enhanced Female Head Mesh / Eyes AO Clipping Fix 不要装、吸血鬼 morph 处理、
  ECE 不兼容、`races.ini` 路径、`fSliderMultiplier`、卸载方式、许可条款
  `https://www.nexusmods.com/skyrim/mods/102796`、`https://www.nexusmods.com/skyrimspecialedition/mods/35785`
- EFM SE 的 changelog「Version 1.0 Added male version」：Nexus SE 35785 页 —— 一手
- EFA 女版（SE 19181 / LE 92897）发布页与 Files 页：版本 1.7、上传与更新日期、
  与 Female Facial Animation 不兼容、仅适用原版头网格、RaceMenu 表情滑块不受影响、
  需 opparco mfg Command / Mfg Fix、牙齿位置说明、完整 changelog（1.1~1.7）
  `https://www.nexusmods.com/skyrimspecialedition/mods/19181`
- EFA 男版（SE 19532）与 `EFA Mouth SSE` 可选文件说明 —— 一手
- EFM 嘴部纹理来自 **Fair Skin Complexion（HHaleyy）**：EFM 页 credits —— 一手

**社区经验**

- EFM SE 归档文件名 `Expressive Facegen Morphs SE-35785-1-0-1595174141.7z`
  （时间戳 1595174141 ≈ 2020-07-19）：Nolvus 整合包安装指南 —— 一手（Nexus 文件名），日期为换算推断
- 加载顺序「HPH 在 EFM 之前」：预设包作者说明 —— 社区经验
- EFA 男版 v1.21 / 女版 v1.7 的打包版本与日期：Nolvus 指南记录 —— 社区文档

**未确认**

- **EFA 男版（SE 19532）的首发与最后更新日期**
- **EFM SE 35785 页面上的精确 original upload / last updated 日期**（本轮直接抓取被 Cloudflare 拦截）
- **EFM 与 EFA 是否有 1.0 / 1.7 / 1.21 之后的更新计划**
- 某些整合包给 HPH 打的 "EFM patch" 究竟改了什么、是否让 morph 真正生效
