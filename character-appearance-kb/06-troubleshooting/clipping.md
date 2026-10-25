---
id: clipping
title: 穿模 / 破皮（身形与衣服不匹配）
category: 06-troubleshooting
kind: tutorial
version: 2.0.0
updated: 2026-10-25
tags: [排错, 穿模, 破皮, BodySlide, 预设]
aliases: [衣服穿模, 身体穿模, 护甲穿模, 身形不符, 跟随从穿模, 随从穿模, 衣服撑破, 衣服不贴身, 裸体调好穿衣服又变样, zeroed sliders, batch build, 3bav2 兼容, 衣服变形]
source: https://forums.nexusmods.com/topic/13536754-body-clips-through-clothes-but-only-on-followers/
summary: 穿模的根因（"构建是烘焙、滑块是运行时"，起点不一致）、按频率排序的六类成因、"为什么只有随从穿模"的三层解释、有序排查与 Zeroed Sliders + Build Morphs + Batch Build 正解，以及 3BAv2 断代与判断分叉点。
---

# 穿模 / 破皮

> **一句话**：穿模的本质永远是同一句话——**某些网格的起点形状与你的身体不一致**。
> 而"起点"由离线烘焙决定，"微调"由运行时 morph 决定，两条路径起点不一致就必错位。

## 速览

| 项 | 内容 |
|---|---|
| 症状 | 身体从衣服里穿出来，或衣服像纸片一样被撑破 |
| 高频成因 | 服装没在 BodySlide 里构建；身形家族不匹配；预设不一致 |
| 首选判据 | 拖滑块时衣服**纹丝不动** ⇒ 那件衣服没有同源 morph（未 conform / 别族） |
| 最短修复路径 | Zeroed Sliders + `Build Morphs` + **Batch Build** 全部网格 |

要点：

- **根因模型**：BodySlide 的 Build 是**离线烘焙**（数值写进 `.nif` 顶点），
  RaceMenu 滑块是**运行时 morph**（临时叠加）。**起点不一致，叠加就必然错位。**
- **换预设只重烘了身体**，衣服的 nif 还停在上一个预设的形状——顶点对不上，
  于是破皮、穿模、塌陷。
- **"只有随从穿模"多数不是 bug**：随从的身体来自离线烘焙 + 分配工具的预设，
  与你在 RaceMenu 里调的玩家身体走的是两条路径。
- **正解是把起点统一到零**：Zeroed Sliders + `Build Morphs` + Batch Build，
  之后运行时 morph 对谁都生效，随便调都不穿模。
- **NPC 不吃运行时 morph**：你调好的身材只作用于玩家，这是设计（见
  [morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)）。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 2011-2013（具体日期未确认） | **BodySlide** 随 CBBE 滑块体系出现 | 第一次把"变形数据"变成可离线构建、可分享的资产（首发日期未确认，见 [bodyslide-outfit-studio.md](../03-body/bodyslide-outfit-studio.md)） |
| 2012 前后 | **ECE** 的 slot morph 在 LE 发布 | 运行时 morph 的雏形，但槽位有限、只在脚本层 |
| 2018-08-06 | **RaceMenu SE 首发**（`skee64.dll`：NiOverride + CharGen） | SE  morph 管线定型：BodySlide 产数据、skee64 施加数据 |
| 2019-11 | BodySlide 提交 "Remember 'Build Morphs' selection in config" | `Build Morphs` 成为工具的一等选项并被默认记住 |
| 2020 前后 | **OBody / RaceMenu BodyGen** 普及 | morph 数据第一次被分发给 NPC：直接读 `SliderPresets` 目录的 `.xml` |
| 2021 底 | **3BAv2** 迭代 | 之后为 3BAv2 制作的服装才与其原生兼容；更老的衣服需转换（见 [cbbe-3ba.md](../03-body/cbbe-3ba.md)） |
| 2023-2026 | UBE / 新护甲普遍以"预构建 zero-slider 网格 + 预设"分发 | 零化起点成为分发标准形态（社区经验，见 [bodyslide-presets.md](../03-body/bodyslide-presets.md)） |

### 它从哪来

穿模问题比大多数 mod 都老：**从"装备网格直接替换裸体网格"这个引擎设计起，
它就存在**。BodySlide 出现前，衣服 mod 各自为政，一个 mod 一个体型，
装三个衣服 mod 可能得到三具互不兼容的身体——穿模是默认状态。

### 中间经历了什么

两条线索：**构建侧**从"烘一个固定体型"演进到 Zeroed Sliders 零化起点；
**分发侧**从"玩家自己构建"演进到"作者预构建 + 分配工具分发"。
每条线索都在降低穿模概率，但也带来新的断代方式（3BAv2、预设体系分裂）。

### 现状

管线稳定：BodySlide 产 `.tri` → NIF 写 `BODYTRI` → skee64/NiOverride 施加。
**装新护甲 → 重跑 Batch Build** 仍是标准动作，没有一劳永逸的装法。

## 成因（按发生频率排序）

### ① 服装没有在 BodySlide 里构建 ⭐ 最常见

装了服装 mod 但没跑 Batch Build → 服装还是那个服装的原始形状，
和你的身形对不上。

→ **修**：在 BodySlide 里用**与身形相同的预设**对全部服装做 Batch Build。

### ② 身形家族不匹配

CBBE 身形穿 BHUNP 服装（或反之）。两族网格结构不同，必然穿模。

→ **修**：确认服装写明 for CBBE 3BA 还是 for BHUNP，只装同族
（[cbbe.md](../03-body/cbbe.md) / [unp-bhunp.md](../03-body/unp-bhunp.md) / [ube.md](../03-body/ube.md)）。

### ③ 预设不一致

裸身用 Curvy、衣服用 Slim → 穿模。

→ **修**：裸身与服装用**同一个预设**构建。

### ④ 3BAv2 的版本断代（隐蔽但重要）

**3BAv2（2021 年底）之后**为 3BAv2 制作的服装才与 3BAv2 兼容。
更老的 CBBE / 3BBB 服装需要转换。

→ **修**：用 **Outfit Studio** 把老服装 Conform / 转换到你的身形
（Outfit Studio 职责见 [bodyslide-outfit-studio.md](../03-body/bodyslide-outfit-studio.md)）。

### ⑤ 只有手/脚/内衣穿模

slot 32（身体）被替换了，但手（33）/ 脚（37）/ 内衣没有同步构建。

→ **修**：Batch Build 时把全套部件都包含进去。

### ⑥ 构建产物被覆盖（`.tri` / `BODYTRI` 丢失）

后装的 mod 用同名 nif 覆盖了你的构建产物，`BODYTRI` 一起丢失。

**为什么也表现为穿模**：身体回到"起点形状"而衣服还带着 morph（或反之），
两条路径的起点再次错开。

→ **判据**：身形滑块突然消失 + 穿模同时出现，优先查覆盖（转
[racemenu-sliders-missing.md](../06-troubleshooting/racemenu-sliders-missing.md)）。

## ⭐ 为什么"只有随从穿模"

这是社区里反复出现的问题，成因有三层，从常见到隐蔽：

1. **随从用了不同的身形预设**：分配工具按预设分发身形
   （[OBody NG](../05-distribution/obody-ng.md) / [RaceMenu BodyGen](../05-distribution/racemenu-bodygen.md)），
   如果随从拿到的预设与你为服装构建的预设不同，就会穿模；
2. **3BAv2 兼容性问题**：随从身上的服装来自更老的包；
3. **NPC 不吃运行时 morph**：你在 RaceMenu 里拖滑块只作用于玩家；
   随从的身体完全来自离线烘焙——**你们俩看到的"形状"本来就出自两条路径**。

所以遇到"只有随从穿模"，先查**分配工具给它的预设**，再查服装年代，
最后才是"是不是随从 mod 本身有问题"。

## 排查顺序

```
1. 这件服装构建过吗？（Batch Build）
2. 服装的身形家族 == 身形的家族吗？
3. 构建用的预设 == 裸身用的预设吗？
4. 服装是 3BAv2 前还是后？
5. 是随从专属问题吗？（→ 查分配工具的预设）
6. 手/脚/内衣是否同步构建？
7. 构建产物是否被覆盖？（身形滑块是否也突然消失）
```

## 修法

### 正解：Zeroed Sliders + Build Morphs + Batch Build

与其「每换一次预设就把所有衣服重刷一遍」，更省心的做法是**把起点统一到零**：

1. **Outfit/Body** 选你的主身体（CBBE 3BA → `CBBE 3BBB Body Amazing`；
   BHUNP → `BHUNP 3BBB Advanced Ver 3` / `Ver 4`）；
2. **Preset** 选 **`Zeroed Sliders`**（用身体 mod 自带的那份；
   里面有滑块是 100% 属正常设计，**不要改**）；
3. 勾上 **`Build Morphs`**；
4. **Batch Build** 所有服装（记得在 Group Filter 里勾上 `Unassigned` 组，
   很多服装在那儿）；
5. 出现冲突列表时**统一选第 1 步的那个身体**。

这样所有网格起点一致，之后在游戏里用 RaceMenu 那一栏调什么都生效、不穿模。

> 六步详细版（含 `skee64` 配置 `bEnableBodyMorph=1`）见
> [morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)。

### 老服装（3BAv2 前）→ Outfit Studio 转换

- 用 Outfit Studio 的 Conform 把老服装转换到当前身形；
- 转换不了就找作者更新版或换一件；
- 不要强行混装两个 SMP 身体 addon（`CBBE SMP (3BBB)` 与 3BA 不是同一个文件）。

### 随从专属问题 → 查分配预设

- 用 `skee preset-load` 或分配工具把与服装构建一致的预设给随从；
- 或把随从穿的衣服一并纳入你的 Batch Build。

## 判断分叉点（别误诊）

| 看起来像 | 其实 |
|---|---|
| "裸体调好了，穿上衣服又变样" | 那件衣服**没有同源 morph**（未 conform / 别族）——不是身形坏了，是衣服没被 3BA 化 |
| "拖滑块时衣服纹丝不动" | 同上：没有同名 morph 的网格不会被 NiOverride 施加位移 |
| "只有随从穿模" | 分配预设 / 服装年代 / NPC 不吃运行时 morph，三层解释见上 |
| "所有 NPC 都穿模" | 全局问题：你的构建没覆盖到 NPC 穿的衣服，重跑 Batch Build |
| "身体破皮但衣服正常" | 身体构建与衣服不是同一预设；重烘全部 |
| "滑块没了而且开始穿模" | 构建产物被覆盖（`BODYTRI` 丢失）——转 [racemenu-sliders-missing.md](../06-troubleshooting/racemenu-sliders-missing.md) |
| "脸变黑" | 与穿模无关，是 FaceGen——转 [dark-face.md](../06-troubleshooting/dark-face.md) |

## 取舍与建议

- **装新护甲 = 重跑 Batch Build**，这是标准动作，没有一劳永逸；
- **优先 Zeroed Sliders 起构建**：把起点统一到零，是唯一能长期避开
  "换预设就穿模"的做法（代价是 `.tri` 体积变大，社区实测过 1GB→4GB 的量级）；
- **性能敏感**时在"全部衣服可调"与"磁盘/内存"之间自选；
- **只给自己捏体型**：随便拖滑块——运行时路径零成本、零风险。

## 来源

- **成因与修法（未构建 / 家族不匹配 / 预设不一致 / slot 未同步）**：
  LoversLab 与 Nexus 论坛穿模帖 —— **社区经验（多帖一致）**
- **"只有随从穿模"与分配工具的关系**：Nexus 论坛随从穿模帖 + **机制推论** —— **社区经验**
  `https://forums.nexusmods.com/topic/13536754-body-clips-through-clothes-but-only-on-followers/`
- **3BAv2 兼容断代**：Nexus 73324（KS Hairdos SMP 碰撞 bodyslides）描述
  "setup to support 3BA v2" + 社区一致 —— **一手（依赖页）+ 社区经验**（本库整理见 [cbbe-3ba.md](../03-body/cbbe-3ba.md)）
- **Conform / 用 Outfit Studio 转换**：BodySlide 官方 wiki（Outfit Studio 职责）—— **一手**
- **Zeroed Sliders + Build Morphs + Batch Build 流程、`Unassigned` 组必勾、
  冲突列表选同一身体、"Zeroed Sliders 里有 100% 是正常的"**：
  OBody NG 安装指南（第三方整理的步骤文档）—— **社区文档**（本库整理见 [morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)）
- **NPC 不吃运行时 morph、OBody NG 读 `SliderPresets` 的 `.xml` 分配**：
  OBody 作者文档（经社区整理）—— **一手（转述）**
