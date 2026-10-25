---
id: neck-seam
title: 脖子接缝 / 手脚接缝
category: 06-troubleshooting
kind: tutorial
version: 2.0.0
updated: 2026-10-25
tags: [排错, 接缝, 脖缝, 皮肤, UV]
aliases: [neck seam, 脖子接缝, 手脚接缝, 皮肤接缝, 颈部色差, 手腕接缝, 脚踝接缝, 脖子一圈色差, 头身不同源, 皮肤不同族, 脖缝修补, seam, 脖子分界线]
source: https://forums.nexusmods.com/topic/13527930-i-cant-get-rid-of-the-neck-seams-in-bhunp-body/
summary: 脖子/手脚接缝按频率排序的六类成因（皮肤不同套不同档、皮肤与身形不同族、自定义头网格未配套、BodySlide 未构建、FaceGen tint 不一致、loose 文件覆盖）、有序排查法，以及"多数情况是皮肤与身形不同族、不是 bug"与"脖缝修补 mod 是创可贴"两条认知。
---

# 脖子接缝 / 手脚接缝

> **一句话**：脖子（或手腕、脚踝）那一圈色差或错位线，**多数情况不是 bug**，
> 而是皮肤与身形不同族 / 不同档——两套 UV 在交界处对不上。

## 速览

| 项 | 内容 |
|---|---|
| 症状 | 头像"套"在身体上，颈部（或手腕、脚踝）有一圈**色差**或**纹理错位**线 |
| 高频成因 | 皮肤与身形家族不匹配（UV 不同族）；头/手/身来自不同皮肤或不同档 |
| 首选判据 | 看接缝是**色差**（贴图问题）还是**几何缺口**（网格问题）——两者排查路径不同 |
| 最短修复路径 | 确认身形家族 → 整套皮肤换同族同档；换过头模的确认配套 |

要点：

- **第一性事实**：皮肤贴图靠 **UV 展开**贴到网格上；CBBE 与 UNP 是两套 UV，
  同一张贴图贴上去落到不同位置（见 [身体皮肤材质](../03-body/body-textures.md)）。
- **脖缝发生在两套 UV 的交界处**：脸用原版头部 UV，身体那半才分家族——
  所以"同族了还有缝"的困惑来自这里（见 [脸部皮肤与纹理](../02-face/face-textures.md)）。
- **"脖子接缝修补 mod"是创可贴**：根因（不同源 / UV 错配）还在，换一套资源接缝就重现。
- **色差型与缺口型是两回事**：前者查皮肤，后者查身形构建（BodySlide）。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 原版时代 | Bethesda 自带头/身共用一套原版 UV 的皮肤 | 没有接缝问题——一切皮肤 mod 的基线 |
| 2011-2012 | **CBBE 与 UNP 分家**，各自建立 UV 体系 | **皮肤从此分族**，这是后续所有接缝问题的结构性源头（见 [身体皮肤材质](../03-body/body-textures.md) 时间线） |
| LE 中期（具体年份未确认） | 皮肤 mod 普遍按**部件分档**打包（头/身/手/脚 × 风格 × 分辨率） | "混档"成为新的高频自伤方式 |
| SE 早期（2018 前后） | **Fair Skin Complexion**（Nexus 798）等同时提供 CBBE / UNP 两选项 | 约束从"找不到同族皮肤"变成"**别选错档**" |
| 2019-2021（具体年份未确认） | **HPH / CITRUS** 等自定义头网格普及 | 头部拓扑变化连带动脖子附近的 UV 与衔接 |
| 2023 起 | **UBE 2.0** 带来第四条 UV 线 | 与任何现存身形都不通用，接缝/错位是必然 |

### 它从哪来

接缝问题的"前世"就是**身形分家的历史**。原版时代一套贴图走天下；
CBBE / UNP 各自重做 UV 之后，皮肤 mod 被迫二选一——这条规则至今没变
（UNP 全系共用原版 UV，所以 vanilla 皮肤可直接用；CBBE 必须 CBBE 系）。

### 中间经历了什么

分水岭是**头身分包 + FOMOD 分档**的普及：一个皮肤包动辄十几个选项，
只要有一项选得不一样，接缝就出现。这也是为什么本条的排查顺序把
"同一套同一档"放在最前面——它是**最常见也最容易被忽略**的自伤。

### 现状

选型层面已无争议：**先定身形，再挑皮肤**。剩下的接缝几乎都来自
执行层面（选错档、混装两套、旧文件残留）。修补类 mod 作为应急手段存在，
但社区共识明确：不解决根因。

## 成因（按发生频率排序）

### ① 头 / 手 / 身体用了不同套或不同档的皮肤 ⭐ 最高频

皮肤 mod 的 FOMOD 里常有多个部件选项（例如 12 个文件）。
**只要有一项选得不一样，就会出现接缝。**

→ **检查**：同一套皮肤、同一档，全部部件一致。

### ② 皮肤与身形家族不匹配 ⭐ 最常见根因

**CBBE 与 UNP 用不同的 UV 映射**，贴图不能互换。
给 CBBE 做的皮肤贴到 BHUNP 身上，接缝是必然的。

→ **检查**：CBBE 皮肤配 CBBE 系身形；UNP 皮肤配 UNP / BHUNP。
家族规则见 [body-textures.md](../03-body/body-textures.md)，
两族身形的对照见 [cbbe.md](../03-body/cbbe.md) / [unp-bhunp.md](../03-body/unp-bhunp.md)。

### ③ 自定义头网格与身体皮肤不配套

装了 **CITRUS**、**High Poly Head** 之类的自定义头网格，
却没有把头部纹理/法线与身体对齐。

→ **检查**：HPH 兼容"基于原版头部的纹理"，但如果你同时换了皮肤，
要确认皮肤提供了 HPH 适配。CotR / UBE 这类拓扑 UV 全变的，
需要各自专门的版本（见 [high-poly-head.md](../02-face/high-poly-head.md)、[ube.md](../03-body/ube.md)）。

### ④ 身形未构建 / 构建产物被覆盖（几何缺口型）

身体网格没按当前身形构建，或构建产物被后装的 mod 覆盖。

**为什么也会表现为"接缝"**：脖子周围的顶点位置与头 / 手的预期对不上，
出现的是**凹陷或嵌入**式的缺口，而不是色差。

→ **判据**：接缝是几何缺口 → 查 [BodySlide 构建](../03-body/bodyslide-outfit-studio.md)
与覆盖关系；是色差 → 回成因①②。构建与 morph 机制见
[morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)。

### ⑤ FaceGen 的 tint 与 NPC 记录不一致

改了肤色之后没有同步：

- RaceMenu 里记下肤色 **RGB**；
- 导出头后把 tint mask 放到正确位置、让头网格指过去；
- 在 CK 的 NPC 记录里把 **Face Tinting Color** 设为**相同 RGB**，**Interpolation = 1**；
- 然后 `Ctrl+F4` 重导该 NPC 的 FaceGen。

→ 这条管"脸黑 / 脸花"；管不了理想接缝。若脸变黑，转
[dark-face.md](../06-troubleshooting/dark-face.md)。

### ⑥ 旧 mod 残留的 loose 文件覆盖

装了新皮肤，但旧皮肤的松散文件还在覆盖。

→ **检查**：MO2 的 Conflicts 面板（跨库操作方法见
[conflict-resolution](../../mo2-usvfs-kb/05-usage/conflict-resolution.md)）。

## 排查顺序（照着走）

```
1. 接缝是"色差/错位"还是"几何缺口"？
   色差 → 查皮肤链（第 2 步起）
   缺口 → 查身形构建与覆盖（成因④）

2. 头/手/身体是否同一套皮肤同一档？
3. 皮肤与身形是否同族？
4. 是否装了自定义头网格而没做配套？
5. 身体是否按当前身形构建过、构建产物是否被覆盖？
6. FaceGen tint 与 CK 的 Face Tinting Color 是否一致？
7. 是否有旧 mod 的 loose 文件覆盖？
```

> 每一步都能单独排除一类根因，**按顺序走完再考虑补丁**。

## 修法

### ① 皮肤不同套 / 不同档 → 整套换同档

- 在 MO2 里打开皮肤 mod 的 FOMOD 记录（或重装），**头 / 身 / 手 / 脚
  全部选同一档**（风格一致、分辨率一致）；
- 验证点：进游戏新建角色，看脖子一圈、手腕、脚踝是否还有色差。

### ② 皮肤与身形不同族 → 换同族皮肤

- 先确认身形家族：CBBE / 3BA → CBBE 系皮肤；UNP / BHUNP → UNP 系皮肤
  （vanilla 皮肤可直接用）；UBE → UBE 专用皮肤；
- 没有"两族通吃"的转换补丁，只能换皮肤文件本身；
- 验证点：换肤后颈 / 手 / 脚接缝消失；不错位即同族。

### ③ 自定义头网格未配套 → 补齐适配

- HPH：官方称兼容基于原版头部的纹理，一般不需要专门脸部皮肤；
  但同时换了皮肤时，确认皮肤提供 HPH 适配；
- CotR / UBE：需要各自的基础 mod 与专门版本，别混。

### ④ 几何缺口型 → 重新构建

- 在 BodySlide 里用当前身形预设重新 Batch Build 身体（含手 / 脚）；
- 检查构建产物是否被后装 mod 覆盖（`BODYTRI` 丢失同样会让形状回退）；
- 流程见 [morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)；
  滑块类症状转 [racemenu-sliders-missing.md](../06-troubleshooting/racemenu-sliders-missing.md)。

### ⑤ tint 不一致 → 同步 RGB 后重导

- RaceMenu 记下肤色 RGB → 导出头并放好 tint mask →
  CK 的 **Face Tinting Color** 填相同 RGB、**Interpolation = 1** → `Ctrl+F4`；
- 若伴随脸黑，按 [dark-face.md](../06-troubleshooting/dark-face.md) 的成因链处理。

### ⑥ loose 文件残留 → 清理覆盖

- MO2 Conflicts 面板定位覆盖者，hide 掉旧皮肤的残留文件；
- 只保留一个皮肤 mod 生效（同时装两个皮肤 = 看覆盖关系谁赢，结果不稳定）。

> ⚠️ **一条重要认知**
>
> **多数接缝是"皮肤与身形不同族 / 不同档"，不是 bug。**
>
> 有一种常见做法是用 **Caliente's Texture Blender** 混合头颈纹理，
> 或用"接缝修补"类 mod 遮盖。这些在"实在找不到根因"时可以应急，
> 但只要根因（不同源 / UV 错配）还在，换一套资源接缝就会重新出现。

## 判断分叉点（别误诊）

| 看起来像 | 其实 |
|---|---|
| "皮肤 mod 有 bug" | 九成是不同族 / 不同档；皮肤包本身没坏 |
| "只有脖子一圈分界" | 头 / 身来自不同选项或不同 mod——FOMOD 全选同一档 |
| "手 / 脚也有一圈" | 手 / 脚贴图与身体不同源；同一个包的同一档一起装 |
| "穿上衣服脖子处破皮" | 这不是皮肤问题是衣服没构建——转 [clipping.md](../06-troubleshooting/clipping.md) |
| "整张脸发黑" | 与接缝无关，是 FaceGen 数据缺失——转 [dark-face.md](../06-troubleshooting/dark-face.md) |
| "只有一个 NPC 有缝" | 查该 NPC 的 FaceGen / tint（成因⑤），不是皮肤全局问题 |

## 取舍与建议

- **先定身形再挑皮肤**，顺序反了必然返工；换身形 = 换全套皮肤。
- **FOMOD 一次选全**：头 / 身 / 手 / 脚同档，是性价比最高的防接缝动作。
- **别急着装脖缝补丁**：它掩盖症状，且换资源后复发。
- **男性角色是另一条链**：HIMBO / SOS 系 UV 独立，皮肤要下 SOS-Lite / SOS 版
  （见 [himbo.md](../03-body/himbo.md)）。

## 来源

- **"头/手/身体必须同源同档"、"必须同族"、"`Ctrl+F4` 重导"**：
  Nexus 论坛脖子接缝帖（BHUNP）与 LoversLab 帖 —— **社区经验（多帖一致）**
  `https://forums.nexusmods.com/topic/13527930-i-cant-get-rid-of-the-neck-seams-in-bhunp-body/`
- **CBBE / UNP UV 不通用、UNP 全系共用原版 UV**：Nexus 发布页描述 + 社区一致确认
  —— **一手 + 社区经验**（本库整理见 [body-textures.md](../03-body/body-textures.md)）
- **"脸用原版头 UV、分家的是身体那一半"**：由 HPH 官方"兼容基于原版头纹理"
  与皮肤包普遍头身分开打包两点交叉推出 —— **本工作区辨析（推断，未取得直接一手表述）**
- **CITRUS 头网格导致接缝**：LoversLab 帖 —— **社区经验**
- **CK 的 Face Tinting Color / Interpolation**：Creation Kit wiki（NPC 记录）—— **一手**
- **"脖缝修补是创可贴"**：**机制推论 + 社区共识**
- **男性皮肤下 SOS-Lite 版**：Return to Skyrim 指南与社区一致经验 —— **社区经验**
