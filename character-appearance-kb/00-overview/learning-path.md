---
id: learning-path
title: 学习路径与选型建议——七个阶段，一次只装一层
category: 00-overview
kind: tutorial
version: 2.0.0
updated: 2026-10-25
tags: [总览, 入门, 学习路径, 选型]
aliases: [learning path, 怎么开始, 新手, 该装哪个身形, 选 CBBE 还是 UNP, 新手路线, 从零开始, 怎么验证装好了, 先捏脸还是先身形, 最小依赖集, 阶段顺序, 需要装物理吗, 男性身形怎么选, wabbajack 一步到位]
source: https://stepmodifications.org/wiki/SkyrimSE:0.1.0
summary: 把"从零到能捏出想要的角色"拆成阶段 0 环境确认 → 1 前置 → 2 脸 → 3 身形 → 4 物理 → 5 分配 → 6 排查，每阶段给出学什么、装什么、怎么验证学会了、常见翻车点，并附最小依赖集与家族选型判据。
---

# 学习路径与选型建议

## 速览

| 字段 | 内容 |
|---|---|
| 作用层 | 装配顺序与学习顺序（对应 [`ecosystem-map.md`](ecosystem-map.md) 的五层） |
| 阶段数 | **7 个**（阶段 0 环境确认 → 1 前置 → 2 脸 → 3 身形 → 4 物理 → 5 分配 → 6 排查） |
| 前置知识 | 无；但说这句话时你已经需要能用模组管理器（MO2 / Vortex）建立实例 |
| 影响范围 | 决定"装多少"与"什么时候停手验收" |
| 关键限制 | **每阶段都要验收，验收不过不要进下一层**；跨阶段跳做的排错成本远高于逐步做 |
| 版本敏感性 | 极强 —— 阶段 0 没做对，后面六个阶段的症状全部伪装成"mod 有问题" |

要点：

- **多装的部分就是将来排错的成本。** 先确定目标，再决定装多少（目标 A~D 见"取舍与建议"）。
- **"构建了没有"取代"装了没有"**：本区绝大多数功能要你在 BodySlide 里点过 Build 才生效。
- **运行时 morph 只作用于玩家** —— 这条决定了阶段 5（分配）是否存在。
- **如果想省掉全程**：阶段 0~5 可以被一个 Wabbajack modlist 一步替代（见最后一节）。
- **2026-10 的特殊状况**：阶段 0 新增了一道"要不要留在 1.6.1170"的判断题，见 [`game-version-1-7-x.md`](game-version-1-7-x.md)。

## 前世今生

"先装什么、后装什么"这件事是有历史的，**今天的推荐顺序是十几年失败经验堆出来的**：

| 时代 | 当时的通行做法 | 留下什么教训 |
|---|---|---|
| LE 早期 | 手动覆盖 `Data` 里的网格，装一个算一个 | 没有"层"的概念，错误会静默累积；后来才有 Mod Organizer 式的 Staging 与"不要直接往 `Data` 里丢文件"的规矩 |

| SE 初期（2016~2018） | 大量 LE 模组被移植，各自为战 | `BSTriShape` 换了格式之后，直接搬运的 LE 资产一类就崩；"先验证搬过来的资产能不能进游戏"成为第一步 |
| 2018 之后三件套定型 | RaceMenu + BodySlide + 物理引擎 | **BodySlide 的 Zeroed Sliders + Build Morphs 成为公认的标准起点** —— 它不是某篇教程的发明，而是社区发现"批量构建隆起 benchmark 不一致→后续一切都错"后的收敛结果 |
| 2021 之后 | 分配工具（OBody / OBody NG）普及 | 它们把"单次正确构建"变成了硬性要求：**它们消费的是你的 BodySlide 预设库，没库就没有东西可分配** |
| 2026-08 之后 | Bethesda 更新到 1.7.x | 学习路径被迫在最前面加一个**版本决策**：这一次的坑在于 DLL 生态跟不上，而不是某个 mod 坏了 |

所以今天这条路径的核心精神只有一句：**让每一步都可验收，把不可验收的环节降到最少。**

## 它解决什么问题

没有路径时的三种典型翻车：

| 翻车方式 | 后果 | 有路径之后 |
|---|---|---|
| "看到好看的就装" | 装完不知道是哪个生效；出问题只能全盘重装 | 一次加一层，天然知道嫌疑人是谁 |
| 先装 Physics 再装身形 | 骨骼没有可挂的节点；或反过来：身形不是 physics 变体 | 阶段顺序本身就是依赖顺序 |
| 只装工具不构建 | "我装了 3BA 但游戏里还是原版身材" | 阶段 3 的验收强制要求 Bodies 被 Batch Build 过 |

---

## 配置与使用

### 七阶段一览

| 阶段 | 名称 | 你要得到的东西 | 一句话验收标准 |
|---|---|---|---|
| **0** | 环境确认 | 知道自己停在哪个游戏版本上 | 控制台 `getskseversion` 能打出版本，且与你要用的 mod 要求一致 |
| **1** | 前置框架 | 能加载 DLL 插件 | 能通过 SKSE 启动器正常进游戏，SKSE 日志无加载失败 |
| **2** | 脸 | 能捏一张能存能读的脸 | 能进捏脸菜单、存读取消/导入一张 `.jslot`、无黑脸 |
| **3** | 身形 | BodySlide 构建完毕、滑块可用 | 游戏里能看到身形滑块那一栏，拖了身体会变 |
| **4** | 物理 | 身体/头发/衣物开始动 | 角色走动时可见物理响应；FSMP 的 `smp` 命令有输出（或 CBPC 有明显抖动） |
| **5** | 分配 | NPC 不再千篇一律 | 城里几个 NPC 看得出体型不同 |
| **6** | 排查 | 一套自己的容错流程 | 遇到新症状时能在五层里定位出一层 |

> **阶段 0~5 是"加东西"，阶段 6 是"学会减东西"。** 后者才是长期能力。

---

### 阶段 0：环境确认（2026 年必做）

**学什么**：`SkyrimSE.exe` 的版本号；它与你所装 DLL 的关系。

**装什么**：什么也不装。

**怎么验证学会了**：

1. 看清游戏版本：Steam 版可在游戏属性或 `SkyrimSE.exe` 详细信息里看；更可靠的是
   `Documents/My Games/Skyrim Special Edition/SKSE/` 下的日志，它会打印运行时版本。
2. 装上 SKSE 之后在控制台敲 `getskseversion`，有输出且版本号对得上。
3. 对着 [`version-matrix.md`](version-matrix.md) 逐项核对自己要用的那几个 DLL。

**常见翻车点**：

- **Steam 自动更新**：一次后台更新就能把整套打回解放前。
  （在 Steam 里限制自动更新，或使用官方/社区提供的降级手段；GOG 用户的版本节奏与 Steam 不同，别照搬。）
- **不知道自己是 GOG 还是 Steam**：两者的 Address Library bin 与部分 mod 的版本档**不相同**。
- **2026-08 之后的特殊坑**：升级到 1.7.x 之后，若磁盘上残留旧版 RaceMenu 的 8 个 overlay nif，**会直接让游戏崩溃** —— 详见 [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md)。

---

### 阶段 1：前置框架

**学什么**：SKSE64 的作用；Address Library 为何能免去重编译之苦；哪些工具把 PapyrusUtil / JContainers / MCM Helper 写成前置。

**装什么**：`SKSE64`（版本必须对应）→ `Address Library`（对应分支）→ `SkyUI`，再按目标追加
PapyrusUtil / JContainers / MCM Helper 等。详见 [`../01-prerequisites/skse64.md`](../01-prerequisites/skse64.md) 与 [`../01-prerequisites/skse-plugin-frameworks.md`](../01-prerequisites/skse-plugin-frameworks.md)。

**怎么验证学会了**：

- 通过 `skse64_loader.exe` 能进游戏；
- 控制台 `getskseversion` 有输出；
- SKSE 日志里没有 "could not be loaded" / "disabled" 之类字样；
- SkyUI 的 MCM 菜单能打开（说明 Papyrus 层通了）。

**常见翻车点**：

- **SKSE 只拷贝了部分文件**（dll 拷了、`Scripts` 没拷）→ 症状是"一半功能没有"。
- **装了 AE 版给 SE 用**，或反过来。
- **Address Library 自身用过旧 bin**（v13 覆盖到 1.7.104.0；SE/AE 的 bin 不通用）。
- **SKSE 团队自己的提醒**：更新后崩溃先清空 `Data/SKSE/Plugins` 再逐个加回 —— 这条至今是最有效的二分法。

---

### 阶段 2：脸

**学什么**：捏脸界面由谁提供；head part 是什么；FaceGen 与 morph 是两套东西。

**装什么**：[`RaceMenu`](../02-face/racemenu.md) → 脸纹理与眼/眉/发/须资源 →（可选）[`High Poly Head`](../02-face/high-poly-head.md)、[`EFM / EFA`](../02-face/expressive-morphs.md)、[`Facelight`](../02-face/facelight.md)。

**怎么验证学会了**：

- 能进捏脸菜单且**不是原版那个界面**；
- 能导出/导入一张 `.jslot` 预设并得到同一张脸；
- 换一张 FaceGen 之后没有黑脸。

**常见翻车点**：

- **黑脸**（最高频）：FaceGen 数据与当前加载内容不一致。见 [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md)。
- **装了 HPH 却没有配套资源**：head part 缺失会让眼睛/嘴变黑洞。
- **morph 类资源只影响玩家**：例如 EFM 明确只作用于玩家，NPC 的脸是预生成的 —— 不要指望它改 NPC。
- **皮肤 UV 与未来的身形要同族**：现在选定的皮肤贴图基本锁死了阶段 3 能选哪个家族。

---

### 阶段 3：身形（成本中心）

**学什么**：身体网格会被装备网格替换这一事实；Zeroed Sliders + Build Morphs + Batch Build
这条主线；`.tri` 与 `BODYTRI` 的关系。机制详见 [`morph-and-nif-basics.md`](morph-and-nif-basics.md) 与 [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

**装什么**（家族二选一，皮肤与服装必须在同一族里）：

```
骨骼 XPMSE
→ 身形：CBBE → 3BA    或    BHUNP
→ 同族皮肤贴图
→ BodySlide and Outfit Studio（构建身形与服装）
```

见 [`../03-body/cbbe.md`](../03-body/cbbe.md)、[`../03-body/cbbe-3ba.md`](../03-body/cbbe-3ba.md)、[`../03-body/unp-bhunp.md`](../03-body/unp-bhunp.md)、[`../04-physics/xpmse-skeleton.md`](../04-physics/xpmse-skeleton.md)、[`../03-body/bodyslide-outfit-studio.md`](../03-body/bodyslide-outfit-studio.md)。

**怎么验证学会了**：

- **勾 `Build Morphs` 并 Batch Build 过**（不是只 Build 身体）；Group Filter 里别忘了 `Unassigned` 组；
- 进游戏能看到那一栏身形滑块，拖动时身体变化；
- 裸体好看且**穿衣服也不破皮**（这是起点统一的证明）；
- 装了多个身体版本时，Batch Build 弹出的冲突列表要**统一选同一个身体**。

**常见翻车点**：

- **只 Build 了身体没 Batch Build 服装** → 一穿衣服就穿模（最高频）。
- **忘了勾 `Unassigned` 组** → 一批服装永远没被构建到。
- **把预设直接 Build 进身体**（没用 Zeroed Sliders）→ 起点不统一，之后怎么调都会错位。
- **Zeroed Sliders 里看到 100% 的滑块就去改** → 那是**有意设计**，不要动。
- **两套预设体系混**：BodySlide 的 `.xml` 与 RaceMenu 的 `.jslot` 不能互导。
- **构建产物被别的 mod 覆盖**（MO2 右栏顺序问题）→ 见 [`../07-workflow/mo2-override-rules.md`](../07-workflow/mo2-override-rules.md)。

---

### 阶段 4：物理

**学什么**：CBPC（球体近似）与 SMP/FSMP（逐顶点 + Bullet）是**两条并列路线**，不是新旧关系；
身体用 CBPC、头发衣服用 SMP 需要额外处理（改 dll 名或改 `defaultBBPs.xml`）。

**装什么**：[`XPMSE`](../04-physics/xpmse-skeleton.md)（安装时选 Physics Extensions）→ [`CBPC`](../04-physics/cbpc.md) 与/或 [`Faster HDT-SMP`](../04-physics/faster-hdt-smp.md) →（可选）[`物理发型/衣物`](../04-physics/physics-hair-and-cloth.md)。整体取舍见 [`../04-physics/physics-overview.md`](../04-physics/physics-overview.md)。

**怎么验证学会了**：

- 角色走动/跳跃时身体、头发有响应；
- FSMP 的控制台命令 `smp list` / `smp detail` 能列出被追踪的 actor（命令本身层面也因此验证 DLL 已加载）；
- CPU 占用可接受（FSMP 的 `Performance.xml` 可选预设与 AVX2 构建档是两条常见的减负手段）。

**常见翻车点**：

- **身形不是 physics 变体**（没在 FOMOD 里选带物理节点的版本）→ 装啥都不抖。
- **FSMP 的 FOMOD 游戏版本档选错** → 物理不生效或开局 CTD。
- **CBPC 与 SMP 抢同一个 body 插槽** → 表现为"其中一个完全不起作用"。
- **同时装了原版 SMP 与 FSMP** → 不要两个都装。
- 详见 [`../06-troubleshooting/physics-not-working.md`](../06-troubleshooting/physics-not-working.md)。

---

### 阶段 5：分配（可跳过）

**学什么**：为什么调好的身材只有玩家有 —— 因为运行时 morph 只作用于玩家；NPC 要么走烘焙、要么走分配。

**装什么**：三选一 —— [`OBody NG`](../05-distribution/obody-ng.md)（推荐）、[`AutoBody`](../05-distribution/autobody.md)、[`RaceMenu BodyGen`](../05-distribution/racemenu-bodygen.md)（RaceMenu 内置）。

**怎么验证学会了**：进城看几个 NPC 体型不同即是成功了；能按种族指定偏好（如让兽人偏向大体型预设）算进阶。

**常见翻车点**：

- **没做阶段 3 的基础构建** → 分配工具扫不到任何预设，表现为"菜单里空空如也"。
- **BodyGen 的 ini 没在末尾留空行** → 数据读不出来。
- **期待它改变玩家自己** → 它管的是 NPC。

---

### 阶段 6：排查（这才是长期能力）

**学什么**：一套固定动作 —— **症状 → 判据 → 定位到层 → 禁用一半/回滚一层**。

**怎么验证学会了**：能回答"这个症状最可能是哪一层"，并知道代价最小的那一步验证方式（例如把构建产物单独放到一个抬高优先级的 mod 里，看症状是否消失）。

**推荐工具与思路**：

- `../06-troubleshooting/` 的七篇症状条目：[`黑脸`](../06-troubleshooting/dark-face.md)、[`脖子接缝`](../06-troubleshooting/neck-seam.md)、[`穿模`](../06-troubleshooting/clipping.md)、[`滑块缺失`](../06-troubleshooting/racemenu-sliders-missing.md)、[`预设不生效`](../06-troubleshooting/preset-not-applied.md)、[`物理不生效`](../06-troubleshooting/physics-not-working.md)、[`overlay nif 崩溃`](../06-troubleshooting/overlay-nif-ctd.md)。
- 装配层面的通用做法见 [`../07-workflow/install-order.md`](../07-workflow/install-order.md) 与 [`../07-workflow/mo2-override-rules.md`](../07-workflow/mo2-override-rules.md)。

## 排错

症状 → 判据 → 应该退回哪个阶段重验证：

| 症状 | 判据 | 退回阶段 |
|---|---|---|
| 所有 mod 都像没生效、控制台 `getskseversion` 无输出 | SKSE 根本没加载 | **阶段 0 / 1** |
| 只有原版捏脸界面 | RaceMenu 的 dll 没加载，多半是版本不对 | **阶段 0 / 1** |
| 更新之后启动即崩 | 版本错配（含 1.7.x 的 overlay nif 特例） | **阶段 0** |
| 身形滑块那一栏不存在 | 缺 `.tri`/`BODYTRI`，或被覆盖 | **阶段 3** |
| 裸体好、穿衣服崩 | 服装没参与 Batch Build / 服装不属于该家族 | **阶段 3** |
| NPC 身材一模一样 | 没做分配（或本来就不该期待） | **阶段 5** |
| 物理无论如何都不动 | DLL 未加载 / 非 physics 变体 / 版本档错 | **阶段 4** |
| 一切正常但越装越慢/偶发崩溃 | 层级累积导致的资源或冲突问题 | **阶段 6**（二分禁用） |

## 取舍与建议

### 一、先确定目标，再决定装多少

不同目标的最小依赖集差别很大，**多装的部分就是将来排错的成本**。

#### 目标 A：只想捏出好看的脸

```
SKSE64 → Address Library → SkyUI
→ RaceMenu
→ 一张脸纹理（皮肤）→ 眼 / 眉 / 发 / 须 资源
→ （可选）High Poly Head
→ （可选）Facial Animation / Facelight
```

**不需要**身形、骨骼、物理。捏脸是独立的一层（阶段 2 为止）。

#### 目标 B：想改身形（体型）

```
A 的全部
→ 骨骼：XPMSE
→ 身形家族二选一：CBBE 系 或 UNP 系
→ 皮肤贴图（必须与身形同族）
→ BodySlide and Outfit Studio（构建身形与服装）
```

**关键动作**：BodySlide 里勾 **Build Morphs**，否则 RaceMenu 里没有身形滑块。

#### 目标 C：想有物理（抖动 / 碰撞 / 物理头发）

```
B 的全部
→ 物理引擎：Faster HDT-SMP（推荐）和/或 CBPC
→ 身形必须选 physics 变体，并在 BodySlide 构建带物理的身形
→ 头发/衣物物理只有 HDT-SMP 能做
```

#### 目标 D：想让 NPC 也有不同身材

```
B（+C）的全部
→ 分配工具三选一：RaceMenu BodyGen（内置）/ OBody NG / AutoBody
```

### 二、CBBE 还是 UNP？

这是最常问的问题。**没有客观优劣，只有生态与偏好**，但有一条硬约束：

> **两族互斥，且皮肤 UV 不通用。** 选定之后，所有皮肤贴图、服装都要在同一族里找。

| 维度 | CBBE / CBBE 3BA | UNP / BHUNP |
|---|---|---|
| 生态规模 | 最大，服装与预设最多 | 较小但稳定 |
| 当代事实标准 | **3BA**（CBBE 3BBB Advanced） | **BHUNP** |
| 皮肤 UV | CBBE 自有 UV | UNP 系 UV |
| 常见搭配 | CBBE → 3BA → 皮肤 → BodySlide | BHUNP → 皮肤 → BodySlide |
| 物理依赖 | XPMSE、CBPC、BodySlide；可选 FSMP | XPMSE 4.67+、CBPC、HDT-SMP、BodySlide |

**给新手的判据**：如果你要装的**服装/预设包大多写明 for CBBE 3BA**，就选 CBBE 系。
如果你已经在用 BHUNP 的皮肤或预设，就留在 UNP 系。**不要为了"试试"两套都装。**

### 三、男性角色

上述讨论默认是女性身形。男性身形（如 **HIMBO**、Tempered Skins 面向的男性网格）是**另一条独立的链**，
与女性身形不冲突，可以同时启用一套。AutoBody 同时支持 **CBBE 与 HIMBO** 预设分发。

### 四、想跳过全程：Wabbajack

阶段 0~5 可以用一个现成的 modlist 一步到位。代价是你失去了"知道自己装了什么"的能力，
所以即使走 Wabbajack，**阶段 6 的排查能力仍然是必需品**。参见
[`../07-workflow/wabbajack.md`](../07-workflow/wabbajack.md) 与
[`../07-workflow/chinese-modpacks.md`](../07-workflow/chinese-modpacks.md)。

### 五、外部可参考的教程

| 教程 | 性质 | 链接 |
|---|---|---|
| STEP Guide（Step Modifications 官方 wiki） | **本领域最权威的"从零到稳定"指南** | `https://stepmodifications.org/wiki/SkyrimSE:0.1.0` |
| Wabbajack 官方文档 | 用现成 modlist 跳过装配 | `https://wiki.wabbajack.org/` |
| GamerPoets | MO2 / BodySlide / RaceMenu 的实操演示 | `https://www.gamerpoets.com/` |
| 更多社区指南索引 | 本库整理 | [`../07-workflow/tutorials-and-guides.md`](../07-workflow/tutorials-and-guides.md) |

> 注意：`modding.wiki` 域名**并不托管 STEP 的 Skyrim SE 指南**（实测其相关页面 404）；
> STEP 的官方 wiki 是 `stepmodifications.org`。这是一个容易走错的路。
> **补充**：`modding.wiki` 另有用途 —— SKSE 团队在自己的置顶帖里把它作为
> "SKSE 及其依赖插件的适配状态"的查询处。也就是说：**查 STEP 指南走 `stepmodifications.org`，
> 查某个 DLL 插件有没有适配新版本，可以去看 SKSE 官方给的 Modding.wiki 状态页**
> （具体内容以该站当前页面为准，本库未逐项核实）。

## 来源

- STEP Guide：`https://stepmodifications.org/wiki/SkyrimSE:0.1.0` —— **一手（官方策划指南）**
- BHUNP 硬依赖清单：`https://www.loverslab.com/files/file/10630-bhunp-3bbb-body-for-le` —— **一手（作者文件页）**
- Wabbajack 文档：`https://wiki.wabbajack.org/` —— **一手**
- "CBBE 与 UNP 互斥、UV 不通用"：Nexus 发布页描述 + 社区一致确认 —— **一手 + 社区经验（一致）**
- **Zeroed Sliders + Build Morphs + Batch Build 为主流标准起点的做法**：OBody NG 安装指南（第三方整理文档）—— **社区文档**；
  机制侧解释见 LoversLab 关于"应以什么基准构建网格"的讨论 —— **社区经验**
- **`modding.wiki` 不托管 STEP 指南**：**本工作区实测（2026-09-22，WebFetch 三页均 404）**
- **SKSE 团队在 Nexus 置顶帖中把 Modding.wiki 作为插件适配状态的查询入口**：Nexus SKSE64 Posts 区置顶 —— **一手**；
  该站插件状态表的具体内容**本库未逐项核实 → 未确认**
- FSMP 的 `smp` 控制台命令（`list` / `detail` / `dumptree`）与 `Performance.xml`：Nexus FSMP 页面与仓库 README —— **一手**
- 2026 年 1.7.x 造成的"阶段 0 必须加一道版本判定"：Nexus RaceMenu Posts（作者 2026-08-23）—— **一手（作者本人）**
