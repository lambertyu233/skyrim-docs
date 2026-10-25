---
id: ecosystem-map
title: 捏脸与身形生态地图——五层链与它的来历
category: 00-overview
kind: concept
version: 2.0.0
updated: 2026-10-25
tags: [总览, 生态, 路线图, 选型]
aliases: [ecosystem, 该装什么, body mod 有哪些, 捏脸需要什么, 五层结构, 依赖链, 先装哪个, 分层模型, appearance mods, 身形生态, 物理属于哪层, NPC 身材怎么给, 不装骨骼会怎样, 皮肤 UV 不匹配]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: 把"人物外貌"拆成五层（前置框架 / 脸 / 身形 / 骨骼物理 / 分配），逐层讲清它在改什么、典型 mod、不装会怎样、进下一层的前提，并补齐这条生态从 LE 时代到 SE/AE 的演化脉络。
---

# 捏脸与身形生态地图

Skyrim 的"人物外貌"从来不是一个 mod，而是**五层叠起来的一条链**。每一层只解决自己的问题，
层与层之间靠两种东西连接：**文件覆盖**（谁在 MO2 右栏排得高，谁的网格生效）与**运行时 API**
（`skee64.dll` 里的 NiOverride 在游戏跑的时候改网格）。理解这条链，比记住任何一个 mod 名字都重要。

## 速览

| 字段 | 内容 |
|---|---|
| 作用层 | 人物外貌全链路（脸 / 身形 / 骨骼 / 物理 / NPC 分配）的**分类与依赖模型** |
| 本页性质 | **导航页**，不装任何东西；真正的安装动作在 [`learning-path.md`](learning-path.md) 与 [`../07-workflow/install-order.md`](../07-workflow/install-order.md) |
| 依赖 | 无（它是别的条目的索引） |
| 影响范围 | 决定你装东西的**顺序**与排错时先怀疑哪一层 |
| 关键限制 | 五层**不是并列关系**：上层坏了，下层一定跟着异常；反过来下层坏了不会让上层报错 |
| 版本敏感性 | 强 —— L0 层一崩，L1~L4 全部静默失效（详见 [`game-version-1-7-x.md`](game-version-1-7-x.md)） |

要点：

- **链是自下而上的**：L0 前置是地基，它是唯一"崩了就什么都不工作"的一层。
- **L2 身形是本区的成本中心**：绝大多数症状（穿模、sliders 缺失、身材不生效）其实都出在这一层。
- **L3 骨骼与 L2 身形互为前提**：没有 XPMSE 就没有物理骨骼可挂；身形不是 physics 变体，挂了也不抖。
- **L4 分配不是必需层**：不装它，玩家角色照样能捏完整不打折，它只决定 NPC 是否"身材统一"。
- **两条红线**：同一性别同时只能启用一个身形家族；CBPC 与 SMP 争同一个 body 插槽。
- **操作层面的建议**：一次只加一层、每层加完立刻验收，这是唯一有效的排错策略（见"配置与使用"）。

## 前世今生

### 时间线

| 时间 | 事件 | 意义 |
|---|---|---|
| 2011-12 | **CBBE** 前身 Caliente's Big Bottom Edition 问世，随后改名 Beautiful Bodies；作者自述 2011-12-04 做出第一个配得上该身体的服装 mod | "先有身形、后有衣服"的家谱由此开始（出处为作者访谈转载，详见"来源"） |
| 2012 前后 | **Dimonized UNP**（dimon99）在 LE 发布 | 第二个身形大家族出现，此后 UNP 与 CBBE 的 UV 分裂成为永久格局 |
| 2012-03-15 | **Enhanced Character Edit（ECE）** 在 Nexus 发布 | LE 时代捏脸的事实标准，靠 `characterMakingExtender` 插件与 slot 存档工作（年份见"来源"，标注为二手记载） |
| LE 中期 | UUNP（Unified UNP）面世，把 UNP 各变体统一并做成 BodySlide 可构建形态 | "身形可滑块化"的起点 |
| 2015-12-24 | BodySlide 的 Fallout 4 页首传（ousnius / Caliente） | BodySlide 本身是从 FO4 起家的，**早于它的 Skyrim 版本** |
| 2016-10 | Special Edition 发售，骨骼由 XPMSE 接管为事实标准 | LE 资产开始大规模向 SE 迁移 |
| 2016-11-02 | **BodySlide and Outfit Studio** 的 Skyrim SE 页面首传 | "构建 / 转换服装"成为独立工种 |
| 2018-02-20 | BodySlide 与 Outfit Studio 拆成两个可执行文件、配置文件分开 | 仓库 commit 记录，一手 |
| 2018-08-05 | **RaceMenu** 的 Skyrim SE 页面首传（Created by Expired，uploaded by expired6978） | 捏脸界面 + 运行时 morph（NiOverride / CharGen，即 `skee64.dll`）进入 SE；页面同时致谢 ECE Team 的 ECE Morphs |
| 2019-11-18 | SKSE64 的 Nexus 页面首传 | L0 有了统一的发布渠道 |
| 2020-02-07 | **Address Library for SKSE Plugins** 首传（meh321） | DLL 插件从此不必为每个 1.6.x 小版本重编，L0 迎来稳定器 |
| 2021-10-22 | **Faster HDT-SMP** 首传（DaydreamingDay 上传） | 物理层有了持续维护的现代分支 |
| 2024-10-08 | FSMP 2.5.1 —— **最后一个基于 SKSE 而非 CommonLibSSE 的版本** | 物理层开始向 CommonLib 系切换，埋下后来兼容 1.7.x 的伏笔 |
| 2026-08-20 / 08-27 | Bethesda 时隔约两年半更新，**1.7.99 / 1.7.104** 与 SKSE **2.3.0 / 2.3.1** 相继发布 | 生态再次整体进入"等待重编译"状态（详见 [`game-version-1-7-x.md`](game-version-1-7-x.md)） |
| 2026-08-23 | RaceMenu 作者发帖：1.7.99 版已完成但被 SKSE 的 Papyrus bug 卡住，转向 **CommonLibSSE-NG** 重写 | 本区最核心的 L1 组件进入重写期 |
| 2026-10-04 | **BodySlide 5.9.1** 发布 | L2 的工具链仍在活跃维护（含 morph 相关的 `LOCKEDNORM` 修复） |

### 它是怎么长成现在这个样子的

**第一段：LE 的"裸体替换 + 骨骼物理"。** 早期所谓"美化"，本质上只有两个动作 —— 把
`femalebody_0/1.nif` 换掉（这就是全部"身形"），以及给身体加带上/null 骨骼做 **BBP / TBBP**
（骨骼驱动的胸部与臀部摆动）。那时的 Elden Ring 式实时布料是不可能的：骨骼能带动的节点就那么几根，
衣服永远是刚性贴在身上的。捏脸则由 **ECE** 统治：它用 `characterMakingExtender` 插件绕过
原版菜单，所谓"保存脸"就是把一组滑块值和顶点编辑结果写进 `CME_save` 目录的 **slot** 文件，
下次进游戏用 "Slot Load" 滑块把它读回来（社区经验，见"来源"）。

**第二段：SE 换引擎带来的重写。** SE 换了网格格式（LE 的 `NiTriShape` + `NiTriShapeData`
变成合并后的 **`BSTriShape`**，详见 [`morph-and-nif-basics.md`](morph-and-nif-basics.md)），
LE 的所有身体与服装网格式不能直接用了，于是整个行业经历了一次强制翻新。正是在这个窗口里，
**RaceMenu** 被移植到 SE（2018-08），它带来的不只是一个更好看的菜单，而是把 **NiOverride /
CharGen 运行时 morph 能力**带进了 SE —— 这是"玩家能在游戏里拖滑块、且衣物跟着变"的技术前提。
同期 **BodySlide** 成为服装适配的通用工具，"构建了没有"取代"装了没有"，成为判断身形是否生效的问句。

**第三段：三件套定型。** 之后的格局就稳定下来：**RaceMenu（捏脸 + 运行时 morph）+
BodySlide（离线构建 + morph 导出）+ 物理（CBPC 或 FSMP）**。三者各管一段、互不重叠，
而 **XPMSE** 骨骼是全部物理类 mod（以及靠额外节点做效果装备）的共同底座。

**第四段：分配层与 1.7.x。** 当足够多玩家拥有了一份漂亮的 Zeroed Sliders 身形后，
"NPC 全是同一个身材"变成新的抱怨，于是出现了 [`RaceMenu BodyGen`](../05-distribution/racemenu-bodygen.md)
和它的重写者 [OBody / OBody NG](../05-distribution/obody-ng.md) —— 这层直接消费 L2 的 `.xml` 预设库。
到 2026 年 8 月 Bethesda 再次更新，五层里的 L0/L3/L4 迅速跟进，**唯独 L1 的 RaceMenu 没跟上**，
于是整条链在 L1 处断开。这就是当前（2026-10）的局面。

## 它解决什么问题

没有这张地图之前的典型困境：

| 困境 | 没有模型时 | 有了五层模型之后 |
|---|---|---|
| "我装了 XX 但没效果" | 只会重装 | 先判断它属于哪一层，再看该层的验收点是否满足 |
| "改了衣服就崩 / 改了脸就崩" | 全盘回滚重来 | 知道服装属于 L2、脸 nif 属于 L1，可以只回滚一层 |
| "想加物理，要从头装吗" | 不确定 | L3 依赖 L2 已成事实，只需要确认身形是 physics 变体 |
| "为什么我调的身材 NPC 没有" | 以为是 bug | 知道运行时 morph 只作用于玩家，NPC 走 L4 分配或 L2 烘焙 |

一句话：**这张地图把"症状"翻译成"层"，把"层"翻译成"该去读哪一篇"。**

## 配置与使用

先看清五层（下面每张表就是一层），再按 [`learning-path.md`](learning-path.md) 的阶段推进。
用法：**每装完一层就停手验收，验收不过不要进下一层。**

### L0 前置框架

| 项 | 内容 |
|---|---|
| 这层在改什么 | 让 DLL 插件能被加载、让 Menu/ Papyrus 层可用（SKSE64、Address Library、SkyUI、PapyrusUtil / JContainers / MCM Helper 等） |
| 典型 mod | [`../01-prerequisites/skse64.md`](../01-prerequisites/skse64.md)、[`../01-prerequisites/skse-plugin-frameworks.md`](../01-prerequisites/skse-plugin-frameworks.md)、Address Library |
| 不装会怎样 | 任何 SKSE 插件静默失效：**菜单打不开、滑块全空、物理不动**，且往往**没有任何报错** |
| 进下一层的前提 | 控制台 `getskseversion` 有输出；SKSE 日志里没有 "plugin could not be loaded" |

### L1 脸

| 项 | 内容 |
|---|---|
| 这层在改什么 | 脸部几何（网格与 head part）、脸部纹理、表情 morph、以及**捏脸界面本身** |
| 典型 mod | [`../02-face/racemenu.md`](../02-face/racemenu.md)、[`../02-face/high-poly-head.md`](../02-face/high-poly-head.md)、[`../02-face/expressive-morphs.md`](../02-face/expressive-morphs.md)、[`../02-face/face-textures.md`](../02-face/face-textures.md)、[`../02-face/face-headparts-resources.md`](../02-face/face-headparts-resources.md)、[`../02-face/facelight.md`](../02-face/facelight.md) |
| 不装会怎样 | 只有原版菜单那几个滑块；或装了 High Poly Head 却没有对应发型/妆容资源，反而更糟 |
| 常见症状 | 黑脸、没滑块、预设读不进去 —— 三种不同病因，见 [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md) 与 [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md) |
| 进下一层的前提 | 能进捏脸菜单、能存读预设、无黑脸 |

### L2 身形（成本中心）

| 项 | 内容 |
|---|---|
| 这层在改什么 | 身体**网格**本身、它的服装生态、以及配套滑块（`.tri` / BodySlide 项目） |
| 典型 mod | [`../03-body/cbbe.md`](../03-body/cbbe.md) / [`../03-body/cbbe-3ba.md`](../03-body/cbbe-3ba.md) / [`../03-body/unp-bhunp.md`](../03-body/unp-bhunp.md) / [`../03-body/himbo.md`](../03-body/himbo.md) / [`../03-body/ube.md`](../03-body/ube.md)，工具为 [`../03-body/bodyslide-outfit-studio.md`](../03-body/bodyslide-outfit-studio.md) |
| ⚠️ 红线 | **身形家族互斥**：CBBE 系与 UNP 系不能同时启用；且两族**皮肤 UV 不通用**，错配会在手/颈/脚出现接缝（见 [`../06-troubleshooting/neck-seam.md`](../06-troubleshooting/neck-seam.md)） |
| 不装会怎样 | 永远只有原版身材；直接装上别族做的衣服也会退回原版体型 |
| 进下一层的前提 | BodySlide 里 Batch Build 过，**并勾了 `Build Morphs`**，进游戏能看到身形滑块那一栏 |

### L3 骨骼与物理

| 项 | 内容 |
|---|---|
| 这层在改什么 | 骨骼挂点（XPMSE 提供的额外节点）、胸/臀/腹/头发/衣物的**实时模拟**与碰撞 |
| 典型 mod | [`../04-physics/xpmse-skeleton.md`](../04-physics/xpmse-skeleton.md)、[`../04-physics/cbpc.md`](../04-physics/cbpc.md)、[`../04-physics/hdt-smp.md`](../04-physics/hdt-smp.md)、[`../04-physics/faster-hdt-smp.md`](../04-physics/faster-hdt-smp.md)、[`../04-physics/physics-hair-and-cloth.md`](../04-physics/physics-hair-and-cloth.md) |
| 不装会怎样 | 身体不抖；物理发型/衣物像一块硬板、完全不跟随动作；依赖额外骨骼节点的服装（如 SMP 披风）失去作用 |
| 常见症状 | 不抖 / 头发穿透 / 开局 CTD —— 见 [`../06-troubleshooting/physics-not-working.md`](../06-troubleshooting/physics-not-working.md) |
| 进下一层的前提 | XPMSE 装了且在正确的加载位置；身形选的是带物理节点的变体（3BA / BHUNP 等） |

### L4 分配

| 项 | 内容 |
|---|---|
| 这层在改什么 | 把已有身形/预设**分给 NPC**，让 NPC 不再是同一个身材 |
| 典型 mod | [`../05-distribution/obody-ng.md`](../05-distribution/obody-ng.md)、[`../05-distribution/autobody.md`](../05-distribution/autobody.md)、[`../05-distribution/racemenu-bodygen.md`](../05-distribution/racemenu-bodygen.md) |
| 不装会怎样 | 玩家捏得再好，NPC 仍是一片统一：全都用烘焙出来的那一个体型 |
| 进下一层的前提 | **L2 已完成 Zeroed Sliders + Build Morphs 基础构建** —— 分配工具消费的是 BodySlide 的 `.xml` 预设库；没构建就没有东西可分配 |

### 依赖方向（关键）

```
L0 前置  ──→  L1 / L2 / L3 / L4 全部依赖它（它崩，全链路静默失效）
L2 身形  ──→  依赖 L3 的骨骼节点（没有 XPMSE 就没有物理骨骼可挂）
L3 物理  ──→  依赖 L2 的网格带物理变体（身形要选 physics 版本）
L1 脸    ──→  与 L2 的皮肤 UV 必须同族（CBBE 皮肤 ↔ CBBE 系身形）
L4 分配  ──→  依赖 L1 的 RaceMenu morph API + L2 的 .tri / 预设库
```

### 两条互斥红线

1. **同一时刻只能启用一个女性身形 + 一个男性身形。** CBBE 与 UNP / BHUNP 不能共存，
   男性链（HIMBO 一类）与女性链互不影响，可以各留一个。
2. **CBPC 与 HDT-SMP 争同一个 body 插槽。** 想要"身体用 CBPC、头发衣服用 SMP"必须做额外处理
   （把 `cbp.dll` 改名 `zcbp.dll` 或编辑 `defaultBBPs.xml`），详见
   [`../04-physics/physics-overview.md`](../04-physics/physics-overview.md)。

## 排错

症状 → 判据 → 处理（本页只做**分层定位**，具体手法在指到的条目里）：

| 症状 | 判据（看到它说明是这一层） | 处理方向 |
|---|---|---|
| 菜单打不开、滑块全空、所有 mod 都像没生效 | **首先怀疑 L0**：控制台 `getskseversion` 无输出 / SKSE 日志里有 plugin 加载失败 | 核 [`version-matrix.md`](version-matrix.md)，确认游戏↔SKSE↔插件版本一致 |
| 捏脸界面**是原版那个** | RaceMenu 没加载成功，而不是"装了但是效果没开" | 同 L0，多为版本错配 |
| 眼窝或嘴部出现黑洞 / 部件错位 | L1 的 head part 资源缺失，或网格的骨骼 bind/部件 index 不一致 | [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md) |
| **脸是黑的** | L1 层的 FaceGen 数据与当前加载的贴图/网格不一致 | 同上；黑脸有四种修法 |
| 身形滑块那一栏**根本不存在** | L2：没勾 `Build Morphs`，或 morph `.tri` 被别的 nif 覆盖 | [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md)、[`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md) |
| 裸体好看，**穿上衣服就崩/穿模** | L2：衣服网格与身体的**起点形状不一致**，或压根不是同一身形家族做的 | 重做 Zeroed Sliders + Batch Build，见 [`../06-troubleshooting/clipping.md`](../06-troubleshooting/clipping.md) |
| 身体不抖、物理发型像贴片 | L3：DLL 没加载 / 身形不是 physics 变体 / FOMOD 游戏版本档选错 | [`../06-troubleshooting/physics-not-working.md`](../06-troubleshooting/physics-not-working.md) |
| 我的身材很完美，**NPC 全是同一个** | 这不是故障：运行时 morph 只作用于玩家。要走 L4 分配或 L2 烘焙 | [`../05-distribution/obody-ng.md`](../05-distribution/obody-ng.md) |
| 更新了游戏之后**启动就崩** | L0/L1：版本跳变导致 DLL 与游戏版本不匹配；2026-08 起还有一个特有的 overlay nif 崩溃 | [`game-version-1-7-x.md`](game-version-1-7-x.md)、[`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md) |

## 取舍与建议

- **不要按"看起来最漂亮的顺序"装，要按 L0→L1→L2→L3→L4 装。** 倒着装是绝大多数疑难杂症的来源。
- **想要效果最全就装全五层；但每多一层就多一份维护成本。** 只想捏脸的玩家完全可以止步于 L1
  （见 [`learning-path.md`](learning-path.md) 的目标 A）。
- **L4 是唯一可以无条件跳过的层。** 它内容丰富度与排错难度不成正比，新手可以先不要。
- **L3 请二选一想清楚。** CBPC（球体近似、轻量、CPU 友好、管不了头发衣服）与 SMP/FSMP
  （逐顶点、能做头发衣物、更吃 CPU）不是"都装更好"的关系，详见
  [`../04-physics/physics-overview.md`](../04-physics/physics-overview.md)。
- **选家族时不要摇摆。** 一旦选了 CBBE 系或 UNP 系，皮肤、服装、`BodySlide` 预设都要在同一族里找；
  中途换族 = 全部服装重建。
- **当下（2026-10）的现实建议**：如果你的核心诉求是捏脸，留在能跑 RaceMenu 的版本上，
  比追最新版游戏重要得多 —— 详见 [`game-version-1-7-x.md`](game-version-1-7-x.md) 的决策树。

## 该往哪读

- 我不确定从哪开始 → [`learning-path.md`](learning-path.md)
- 名词看不懂 → [`glossary.md`](glossary.md)
- 版本对不上 → [`version-matrix.md`](version-matrix.md)
- 想懂原理（morph 为什么能动）→ [`morph-and-nif-basics.md`](morph-and-nif-basics.md)
- 已经出故障了 → [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md)
- 不确定哪项 Source 可信 → [`../08-sources/unreliable-and-unconfirmed.md`](../08-sources/unreliable-and-unconfirmed.md)

## 来源

- **Nexus mod 发布页（一手）**：RaceMenu `https://www.nexusmods.com/skyrimspecialedition/mods/19080`
  （Files 页：当前版本 0.4.20.0，主文件要求 SKSE64 AE 2.2.6+ 且 Game Version 1.6.1170；
  Original upload 2018-08-05；Created by Expired / uploaded by expired6978）
- **Nexus mod 发布页（一手）**：BodySlide and Outfit Studio `https://www.nexusmods.com/skyrimspecialedition/mods/201`
  （当前 5.9.1，最后更新 2026-10-04；Created by Ousnius and Caliente；SE 页首传 2016-11-02）
- **Nexus mod 发布页（一手）**：Address Library for SKSE Plugins `https://www.nexusmods.com/skyrimspecialedition/mods/32444`
  （Original upload 2020-02-07，Created by meh321）
- **Nexus mod 发布页（一手）**：FSMP - Faster HDT-SMP `https://www.nexusmods.com/skyrimspecialedition/mods/57339`
  （Original upload 2021-10-22，uploaded by DaydreamingDay；2.5.1 为最后一个基于 SKSE 的版本）
- **GitHub 仓库（一手）**：`https://github.com/ousnius/BodySlide-and-Outfit-Studio`（2018-02-20 拆分 BS/OS 可执行文件；LICENSE 为 GPLv3+）
- **CBBE 身世（社区经验 / 作者访谈转载）**：作者接受 skyrimromance.com 访谈的转载记录
  （原名 Caliente's Big Bottom Edition → Beautiful Bodies；2011-12-04 首个配套服装 mod；后续由 Jeir 与 Ousnius 维护）
- **ECE 发布时间（社区 / 作者博客二手记载）**：modder Novelyst 的文章记载 ECE 于 2012-03-15 发布于 Nexus；
  ECE 的 slot 机制（`CME_save`、"Slot Load" 滑块、依赖 `characterMakingExtender` 插件）依据
  社区装机文档与 namu wiki 整理 —— **二手，未在 Nexus 原始页面逐字核实**
- **RaceMenu 1.7.x 现状（一手，作者本人）**：Nexus RaceMenu Posts 区置顶帖（2026-08-23）
- **分层模型与依赖图：本工作区归纳**（由各层官方页 + 上述时间线交叉比对得出，非单一来源陈述）
