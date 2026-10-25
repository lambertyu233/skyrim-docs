---
id: cbbe
title: CBBE（Caliente's Beautiful Bodies Enhancer）
category: 03-body
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [身形, CBBE, 女性身形, 体模]
aliases: [caliente, beautiful bodies, beautiful bodies enhancer, cbbe 身形, 女性体模, cbbe 是什么, cbbe 历史, 怎么装 cbbe, cbbe uv, caliente body, Big Bottom Edition, cbbe 皮肤, cbbe 版本, 衣服身形]
source: https://www.nexusmods.com/skyrimspecialedition/mods/198
summary: CBBE 完整百科：从 Oblivion 的 HGEC 到 LE 群雄并起、Caliente"本想做衣服却先做出身体"的起源、衣服生态压倒性支持如何把它推上市占率冠军，以及 Shape Options、独立 UV、身形互斥、依赖链、安装构建流程与排错。
---

# CBBE（Caliente's Beautiful Bodies Enhancer）

> **一句话**：CBBE 是 Skyrim 女性身形的"人台"与生态中心——绝大多数护甲/衣服 mod 以它为第一支持对象；
> 而你游戏里看到的体型不是它自带的，是你用 BodySlide 构建出来的。

## 速览

| 项 | 内容 |
|---|---|
| 原作者 | **Caliente**（软件工程师，BodySlide 共同作者） |
| 现任维护 | **Ousnius** 与 **Jeir**（作者原话："they still maintain the mod"） |
| 命名沿革 | Caliente's **Big Bottom Edition** → Caliente's **Beautiful Bodies Edition**（LE）→ Caliente's **Beautiful Bodies Enhancer**（SE） |
| 当前版本 | SE **2.0.3**（2025-03，两个独立第三方页交叉确认；Nexus 页在成人墙后，以官方 Files 页为准） |
| 前置 | **BodySlide and Outfit Studio**（构建形状，硬性前置） |
| 影响范围 | 女性裸体网格 + 原版/DLC 服装转换 + RaceMenu morph 滑块组 |
| 维护状态 | 低频更新、仍在维护（2025 年仍有发布） |
| 硬约束 | **不能与其他女性身形替换共存**；UV 自成一族 |

要点：

- **衣服生态压倒性支持**是 CBBE 市占率冠军的真正原因——2011-12-04 之后它就不再只是"一个身体 mod"。
- CBBE 本体只提供**基础网格 + 滑块定义**；你看到的 Slim/Curvy 体型是 BodySlide 离线烘焙出来的。
- **CBBE 有独立的 UV 映射**：CBBE 皮肤贴图不能用到 UNP 系身上，反之亦然。
- 女性身形**只能有一个**赢家；男性身形（如 [HIMBO](himbo.md)）是另一条独立的链，可以并存。
- 物理不在本体里：要抖动就加 [3BA](cbbe-3ba.md)（3BBB 骨骼 + CBPC/SMP），或直接配 [CBPC](../04-physics/cbpc.md)。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| Oblivion 时代 | **HGEC**（Hour Glass Expanded Curve）比例流行 | CBBE 比例审美的前身（社区经验） |
| 2011 年前后 | LE 早期身形圈群雄并起：**TNT / DMRA / CHSBHC / EyeCandy** | CBBE 诞生时的竞争格局（社区经验，多源一致） |
| 2011 | Caliente 发布初版，原名 **Caliente's Big Bottom Edition** | 初始比例夸张到作者亲自拿它命名；随后改名 **Beautiful Bodies**（作者访谈） |
| **2011-12-04** | 发布第一个"配得上该身体"的服装 mod | 作者本想做衣服，结果先做出了身体——CBBE 从此走上"身体 + 服装生态"路线（作者访谈） |
| LE 后期 | 更名 **Caliente's Beautiful Bodies Edition** | *Edition* 时代的正式名 |
| SE 时期 | 以 **Caliente's Beautiful Bodies Enhancer** 重新发布 | *Enhancer* 命名沿用至今；作者栏变为 Ousnius / Caliente / Jeir |
| 2021 | SE 版 1.6.x 世代（Nolvus 清单文件名为 1.6.2） | 二手来源；早年"1.6.1 / 1.6.2"的版本分歧说的就是这个世代 |
| 2025-03 | SE 版 **2.0.3** | 两个独立第三方页交叉确认；Nexus 页本体在墙后未能直读 |

### 它从哪来

Caliente 的动机很朴素：嫌原版女身 **bulky、肩膀宽、胯窄**，想先做一具好看的"人台"，
方便自己做衣服（作者访谈原述）。这个"人台"思路决定了 CBBE 后来的全部形态——
它不追求"一件衣服配一个体型"，而是追求"所有衣服共用一具身体"。

比例审美上，CBBE 承袭 Oblivion 时代的 **HGEC** 传统。在 LE 早期，
它与 **TNT / DMRA / CHSBHC / EyeCandy** 等身形同场竞争，最终胜出。

### 中间经历了什么

初版夸张的比例给了它 **Big Bottom Edition** 的戏名，作者随后改名 **Beautiful Bodies**。
真正的转折点是 **2011-12-04**：Caliente 发布了第一个"配得上该身体"的服装 mod。
在此之前它是"一个身体替换"；在此之后它成了**一个服装生态的中心**——
mod 作者开始默认按 CBBE 的顶点与 morph 规则做衣服，雪球越滚越大。

进入 SE 后，Caliente 逐步退居，维护由 **Jeir 与 Ousnius** 接手
（作者原话：they still maintain the mod）。Ousnius 同时是 BodySlide 的作者，
这条人物交叉也是"CBBE 与 BodySlide 深度绑定"的原因之一。

### 为什么它是市占率冠军

不是因为它技术最好，而是因为**衣服生态压倒性支持**：

1. 绝大多数新护甲/衣服 mod 写明 for CBBE（或 for CBBE 3BA）；
2. 双支持（如 "3BA - BHUNP - CBBE"）的 mod 也总是把 CBBE 系列排在第一档；
3. 整合包（Nolvus 等）默认选 CBBE 系，新手入口进一步强化了生态。

后来者（UNP 系、UBE）在衣服数量上始终是追赶者。这就是选型时
"跟着生态走"通常比"追新"稳妥的原因。

### 现状

低频更新、仍在维护：SE 版 2025 年 3 月仍有 **2.0.3**（第三方页交叉确认）。
它没有被取代，而是被**扩展**——带物理的现代主力是 [CBBE 3BA](cbbe-3ba.md)，
与 CBBE 共用同一基底网格。

## 它解决什么问题

**没有它之前**：原版女身 bulky；衣服 mod 各自为政，一个 mod 一个体型，
装三个衣服 mod 可能得到三具互不兼容的身体，捏脸菜单里也没有身形滑块。

**它的解法**是三件套：

1. 一具高模"人台"基础网格（官方描述约 **13,554 顶点**，约为原版 20 倍、
   老版 CBBE 6 倍）；
2. 一套**滑块定义**（SliderSets），让 BodySlide 能在此基础上变形；
3. 一条**构建管线**：所有衣服按同一套顶点/morph 规则转换（conform），
   于是身体与衣服共享同一套 morph 名字，拖滑块时一起变。

> 这就是"为什么拖滑块衣服跟着变"的根源，完整机制见
> [运行时 morph 与离线烘焙](morph-runtime-vs-bake.md)。

## 它包含什么

| 组件 | 说明 |
|---|---|
| 女性身体网格 | 裸体 + 手 + 脚；官方描述约 13,554 顶点 |
| Shape Options | **Slim / Curvy / Vanilla** 三种基础体型，各带 NeverNude 版本 |
| Underwear | 黑 / 紫 / 红 / 浅蓝 / 灰 五色内衣网格 |
| 原版服装转换 | 所有原版与 DLC 服装已转换为上述体型，可吃滑块与预设 |
| BodySlide 资产 | 组（Group）与滑块定义，供 BodySlide 读取构建 |
| 基础皮肤纹理 | 自带；但多数玩家会另装皮肤包（见 [身体纹理](body-textures.md)） |

⚠️ 它**不包含**：物理骨骼与顶点权重（那在 [3BA](cbbe-3ba.md) 里）、
RaceMenu 框架本身（见 [RaceMenu](../02-face/racemenu.md)）。

## 安装

### 步骤

1. **前置**：装好 MO2（或 Vortex）、SKSE64、[BodySlide and Outfit Studio](bodyslide-outfit-studio.md)。
   - 验证点：MO2 工具里能跑起 BodySlide，且 Groups 里出现 CBBE 组。
2. **装 CBBE 主文件**，FOMOD 按需选择（见下表）。
   - 验证点：`Data\meshes\actors\character\character assets\female\` 下出现 CBBE 网格。
3. **装衣服的 CBBE 版本**（每个衣服 mod 都要有 for CBBE 的文件）。
   - 验证点：BodySlide 的 Outfit 下拉里出现该衣服，且属于 CBBE 组。
4. **构建**：BodySlide 里选 Outfit/Body = `CBBE Body`，Preset 选预设，点 Build；
   再 **Batch Build** 把同一预设刷给所有衣服。
   - 验证点：构建列表里每件衣服都在；缺的回到 Group Filter 找漏勾的组
     （**`Unassigned` 组必勾**）。
5. **（可选）物理**：加 [3BA](cbbe-3ba.md)，或按 [CBPC](../04-physics/cbpc.md) 说明配置。
6. **（可选）morph**：构建时勾 `Build Morphs`，RaceMenu 里才有一栏可拖的滑块
   （完整工作流见 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md)）。

### FOMOD 选项

| 选项 | 选什么 | 备注 |
|---|---|---|
| Body | Slim / Curvy / Vanilla | 只是**构建起点**，之后可被滑块与预设覆盖 |
| NeverNude | 按需 | 各体型都带 NeverNude 变体 |
| Underwear | 五色选一或不装 | 仅影响内衣网格 |
| Textures | 按需 | 自带基础皮肤；要换皮肤包见 [body-textures.md](body-textures.md) |

## 使用与配置

### BodySlide：形状从这里来

CBBE 本体**没有形状**，你在游戏里看到的体型完全来自 BodySlide 构建：

```
Data\CalienteTools\BodySlide\SliderPresets\   ← .xml 预设放这里
Data\CalienteTools\BodySlide\SliderSets\      ← CBBE 的滑块定义
```

推荐工作流（Zeroed Sliders 基准 + 运行时 morph）见
[morph-runtime-vs-bake.md](morph-runtime-vs-bake.md) 第六节，核心是：

> **先把身体与所有衣服按 `Zeroed Sliders` 统一构建一遍（勾 Build Morphs），
> 再把形状交给 RaceMenu 实时调。**

### RaceMenu：那一栏滑块

三层来源：RaceMenu 框架 + CBBE 的 `RaceMenuMorphsCBBE.esp`（决定有哪些滑块）
+ 你构建的 `.tri`（真正的变形数据）。滑块不出现时按
[racemenu-sliders-missing.md](../06-troubleshooting/racemenu-sliders-missing.md) 排。

`skee64` 配置（RaceMenu 安装目录下 `SKSE\Plugins\skee64`）确认：

```ini
bEnableBodyMorph=1
bEnableBodyGen=0    ; 随机分配身材，按需
```

### NPC 身材分配

RaceMenu 滑块**只作用于玩家**；NPC 要用分配工具：
[RaceMenu BodyGen](../05-distribution/racemenu-bodygen.md)、
[OBody NG](../05-distribution/obody-ng.md)、[AutoBody](../05-distribution/autobody.md)。

## 兼容与冲突

### 互斥表（女性身形只能有一个）

| 组合 | 结果 |
|---|---|
| CBBE + CBBE 3BA | 同基底，3BA 覆盖身体，生态互通 |
| CBBE + UNP / UUNP / BHUNP | **互斥**（不同 UV、不同滑块组、裸体网格只能有一个赢家） |
| CBBE + UBE | 可并存（UBE 是独立种族），但 CBBE 皮肤**不通用** |
| CBBE + HIMBO（男性） | 两条独立链，互不干扰 |

裸体网格"只能有一个赢家"的覆盖规则见
[mo2-override-rules.md](../07-workflow/mo2-override-rules.md)。

### 皮肤与 UV

> **CBBE 的 UV 自成一族。** 错配的表现是手 / 颈 / 脚接缝、纹理错位——
> 这不是皮肤 mod 不好，是两套 UV 本来就不兼容。

选身形 = 同时选定皮肤的可用范围。UNP 全系（含 BHUNP）**共用原版 UV**，
所以 vanilla 皮肤可直接用于 UNP 系，但不能用于 CBBE（见
[unp-bhunp.md](unp-bhunp.md)）。

### 物理搭配

| 方案 | 说明 |
|---|---|
| CBBE + 3BA | 现代主流：3BBB 骨骼 + CBPC/SMP 可切换 |
| CBBE + CBPC | 轻量：只需骨骼节点（XPMSSE 安装时选 Physics Extensions） |
| CBBE + HDT-SMP / FSMP | 需 3BA 化的身体；纯 CBBE 本体不带 SMP 配置 |

物理不动的排错见 [physics-not-working.md](../06-troubleshooting/physics-not-working.md)，
两代物理引擎的区别见 [hdt-smp.md](../04-physics/hdt-smp.md)。

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 手 / 颈 / 脚接缝、纹理错位 | 皮肤是 UNP 系做的 | 换 CBBE 系皮肤（见 [body-textures.md](body-textures.md)） |
| 角色变回原版体型 | 该衣服没有 CBBE 化版本，或没参与构建 | 找 for CBBE 的衣服；Batch Build 覆盖全部 |
| RaceMenu 身形栏空白 / 拖了没反应 | 没勾 `Build Morphs`，或 Group Filter 漏勾 `Unassigned` | 按 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md) 第六步重做 |
| NPC 身材不随你调 | RaceMenu morph 只作用于玩家 | 用 OBody NG / BodyGen 分配 |
| 穿模、破皮 | 身体与衣服预设不一致 | 同一预设 Batch Build；衣服不支持就转换（[clipping.md](../06-troubleshooting/clipping.md)） |
| 进游戏黑脸 | 与 CBBE 无关，是 facegen / 覆盖问题 | [dark-face.md](../06-troubleshooting/dark-face.md) |

## 取舍与建议

**该选 CBBE（+3BA）当你**：

- 你想装的衣服 mod 大多 for CBBE / 3BA（绝大多数情况）；
- 你在跟随主流整合包（Nolvus 等默认 CBBE 系）；
- 你已经攒了一批 CBBE 预设 / 皮肤。

**不该选当你**：

- 你的皮肤、预设、衣服资产都在 UNP 系（见 [unp-bhunp.md](unp-bhunp.md)）；
- 你追求 UBE 的高模画质并接受其补丁成本（见 [ube.md](ube.md)）；
- 你只是想"对比一下"——**不要同时装两个女性身形**，那是自伤。

**版本敏感性**：本条版本结论（2.0.3，2025-03）来自第三方页交叉确认，
Nexus 页在成人墙后未能直读。装前请以 Nexus Files 页为准；
游戏 **1.7.x** 下的兼容性本轮**未确认**（相关背景见
[game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)）。

## 来源

- **一手（描述正文）**：顶点数（约 13,554）、Shape Options、原版服装已转换、
  需 BodySlide 构建、UV 独立与互斥——CBBE Nexus SE 198 描述正文（经转述引用）
  `https://www.nexusmods.com/skyrimspecialedition/mods/198`
- **一手（作者访谈）**：Caliente 的动机（嫌原版 bulky、想做"人台"）、
  本想做衣服却先做出身体、**2011-12-04** 第一个配套服装 mod、原名 Big Bottom Edition
  后改名 Beautiful Bodies、Jeir 与 Ousnius 接手维护（"they still maintain the mod"）——
  Nexus 官方新闻转载的作者访谈（原载 skyrimromance.com）
  `https://www.nexusmods.com/skyrim/news/12985`
- **一手（当前署名）**：SE 页作者栏 "Ousnius - Caliente - Jeir"——多个第三方页
  （翻译页、整合清单）引用一致
- **一手（依赖链）**：3BA 的前置表述见 Nexus 30174 描述（经 3DMGAME 转载）
- **社区经验**：HGEC 比例前身、TNT / DMRA / CHSBHC / EyeCandy 同期竞争（多源一致）；
  SE 版 1.6.x（2021）与 2.0.3（2025-03）由 Nolvus 清单文件名与独立翻译页交叉确认
- **未确认**：Nexus 页当前版本号（墙后未能直读）、许可证条款、LE 初版具体首发月份
