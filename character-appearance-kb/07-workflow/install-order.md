---
id: install-order
title: 安装次序
category: 07-workflow
kind: tutorial
version: 2.0.0
updated: 2026-10-25
tags: [安装, 次序, 流程, 检查清单]
aliases: [安装顺序, install order, 先装什么, 装 mod 顺序, 安装次序, 安装流程, 安装清单, 怎么装 mod, 先装什么后装什么, 装完验证什么, 安装顺序为什么重要, 分层安装, mod 安装步骤, NMM 到 MO2]
source: https://stepmodifications.org/wiki/SkyrimSE:0.1.0
summary: 从 SKSE 到物理的推荐安装次序、每一步"装完该验证什么"、三条纪律与一个反直觉建议；并解释次序问题为什么在 Skyrim 模改里是结构性的（VFS 覆盖 + BSA + 物理插槽 + 构建产物），以及从 NMM 时代到 MO2 时代的做法变化。
---

# 安装次序

> **一句话**：Skyrim 模改的"安装次序"不是礼仪问题，而是结构问题——
> VFS 覆盖、BSA 优先级、物理插槽、BodySlide 构建产物四件事互相独立，
> 任何一件不管谁赢，都会变成"出问题时查不出谁赢"。

次序错了的代价是**症状深远且难查** —— 覆盖关系一旦定型，后面所有东西都建立其上。

## 速览

| 项 | 内容 |
|---|---|
| 作用层 | 装配顺序（对应 [`ecosystem-map.md`](../00-overview/ecosystem-map.md) 的五层） |
| 适用管理器 | 任意；推荐 **MO2**（次序 = 左栏排序，可随时调整而无需重装） |
| 推荐步骤 | **14 步**：前置 → 骨骼 → 身形 → 构建 → 脸 → 物理 → 分配 → NPC 美化 |
| 每步验收 | 两张表：**装完一步先验证，不过不进下一步** |
| 三条纪律 | 只启用一个女性身形 · 裸身与服装同一预设构建 · 装完身形/骨骼先跑一次行为补丁 |
| 关键限制 | 次序不能替代依赖；**"构建了没有"取代"装了没有"** |
| 版本敏感性 | 极强 —— 1.6.1170 与 1.7.x 决定整条链能不能用，见 [`game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md) |

要点：

- **次序问题的本质是"覆盖"**：同名文件谁生效、哪条记录谁赢、哪个 dll 抢到插槽，都与先后有关。
- **MO2 时代次序 = 排序**：左栏拖一下就改掉覆盖关系，这是 NMM 时代做不到的（见"前世今生"）。
- **每层装完就进游戏看一眼**：出错时嫌疑人只有一个（见末尾的反直觉建议）。
- **两套预设体系不通用**：BodySlide 的 `.xml` 与 RaceMenu 的 `.jslot` 不能互导，别在次序上搞混，机制见 [`morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

## 前世今生

"先装什么、后装什么"是有历史的，**今天的推荐顺序是十几年失败经验堆出来的**：

| 时间 | 事件 | 意义 |
|---|---|---|
| 2011-2012 | Skyrim LE 发布，社区主力管理器是 **NMM**（及其前身 Oblivion Mod Manager） | **物理覆盖时代**：mod 文件直接写进游戏 `Data`，**后装的覆盖先装的**，装错只能卸了重装 |
| LE 中期 | **Mod Organizer（MO1）** 由 **Tannin** 发布，引入 **虚拟文件系统（VFS）** | mod 不再落盘到游戏目录；覆盖关系变成"列表排序"，随时可改、可回退 |
| 2016 | NMM 宣布 end-of-life（年份为**社区转述，具体公告原文未核实**）；Nexus 聘请 Tannin 开发新管理器 | Nexus 官方工具换代（Tannin 被聘一事为 **MO2 GitHub README 一手自述**） |
| 2016-10 | **Skyrim SE 发布**；MO2 一度停滞，后由 **LePresidente** 修到可用状态并发布 **v2.0.8**，2017 年底更多开发者加入 | MO2 成为社区主线管理器（**一手：MO2 GitHub README**） |
| 2017-05 | Nexus 官方 news 帖宣布新管理器定名 **Vortex** | Nexus 阵营的 VFS 后继者（**一手：Nexus news 帖**） |
| 2018-01/02 | Vortex 限量 alpha 与全量 alpha 先后开放 | "Vortex（Nexus 生态）vs MO2（社区）"的双工具格局延续至今 |
| 2018-2020 | BodySlide 的 **Zeroed Sliders + Build Morphs + Batch Build** 成为公认起点 | 本表第 9 步的内容定型——不是某篇教程的发明，是社区收敛结果（**社区经验**） |
| 2021 之后 | **OBody NG** 等分配工具普及 | 它们消费你的 BodySlide 预设库，把"单次正确构建"变成硬性要求（见 [`obody-ng.md`](../05-distribution/obody-ng.md)） |
| 2026-08 之后 | Bethesda 更新到 **1.7.x** | 次序表最前面被迫加一道**版本决策**：坑在 DLL 生态跟不上，不在某个 mod 坏了 |

### 为什么次序问题在 Skyrim 模改里是结构性的

四个原因互相独立，每一个都足以让"装完再说"失败：

1. **VFS 覆盖**：MO2 里同名路径的文件按优先级裁决，**优先级最高的来源才被进程读取**，其余被隐藏。安装时不决定谁赢，排序才决定——所以"装的时候没冲突"毫无意义。
2. **BSA**：BSA 归档的内容也会被拉进虚拟目录树、**与松散文件一起参与同一套优先级判定**。高优先级 mod 的 BSA 会盖过低优先级 mod 的松散文件，反之亦然（机制见 [`../../mo2-usvfs-kb/03-architecture/bsa-priority-resolution.md`](../../mo2-usvfs-kb/03-architecture/bsa-priority-resolution.md)）。
3. **物理插槽**：SMP 与 CBPC **想挂的是同一批骨骼**，两个都装而不配置会互相覆盖；身形还必须选对 physics 变体（见 [`physics-overview.md`](../04-physics/physics-overview.md)）。
4. **构建产物**：BodySlide 的输出是**工具生成的文件**，落在 Overwrite 或专门 mod 里；后装的任何同名 nif 都会把 `BODYTRI` 覆盖掉，滑块**静默失效**（见 [`mo2-override-rules.md`](mo2-override-rules.md)）。

### 从 NMM 时代到 MO2 时代，做法变了什么

| | NMM 时代 | MO2 时代 |
|---|---|---|
| 文件落在哪 | 直接写进游戏 `Data`（物理覆盖） | 各自独立文件夹，经 VFS **虚拟投影** |
| "次序"指什么 | **安装顺序**：后装赢，改次序要卸载重装 | **左栏排序**：拖一下就改，无需重装 |
| 卸载 | 可能留残渣、可能误删共享文件 | 禁用即从虚拟视图消失，游戏目录始终干净 |
| 冲突可见性 | **不可见**（不提示同名文件冲突） | Conflicts 面板逐文件显示谁覆盖谁 |
| 工具产物（BodySlide/xEdit 输出） | 直接落 `Data`，与原版文件混在一起 | 落 **Overwrite**（高优先级），可归档进正式 mod |
| 想回 vanilla | 逐个卸载，心惊胆战 | 禁用全部 mod 即是 vanilla |

> **核心变化**：次序问题没有消失，只是从"**装的时候**"移到了"**装完之后**"。
> NMM 时代装错 = 物理事故；MO2 时代装错 = 排序问题，可逆、可查。

### 现状

次序本身已被工具大幅简化（MO2 的 warning 面板能自动复核一部分顺序问题，LOOT 管插件顺序），
真正需要人守规矩的是**构建产物**与**版本决策**两件事。前者靠第 9 步的验收，
后者见 [`game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md) 与 [`version-matrix.md`](../00-overview/version-matrix.md)。

## 它解决什么问题

**没有次序时的三种典型翻车**：

| 翻车方式 | 后果 | 有次序之后 |
|---|---|---|
| "看到好看的就装" | 装完不知道是哪个生效；出问题只能全盘重装 | 一次加一层，天然知道嫌疑人是谁 |
| 先装物理再装身形 | 骨骼没有可挂的节点；或身形不是 physics 变体 | 阶段顺序本身就是依赖顺序 |
| 只装工具不构建 | "我装了 3BA 但游戏里还是原版身材" | 第 9 步验收强制要求 Bodies 被 Batch Build 过 |

**次序表真正给出的**是"每一层的依赖方向"：框架 → 骨骼 → 身形 → 皮肤 → 构建 → 脸 → 物理 → 分配。
方向反了，症状会伪装成"mod 有问题"。

## 安装

### 推荐次序

```
1. SKSE64（版本必须匹配游戏）
2. Address Library（SE / AE 两套，别装错）
3. SkyUI
4. 其它 SKSE 插件框架（PapyrusUtil / JContainers / MCM Helper / po3 Extender）
5. 骨骼：XPMSE（≥ 4.6）
6. 行为补丁跑一次（FNIS / Nemesis / Pandora）
7. 身形家族（女性：CBBE 系 或 UNP 系，只能选一个；男性身形独立）
8. 皮肤贴图（必须与身形同族）
9. BodySlide and Outfit Studio → 构建身形 + 服装（勾 Build Morphs）
10. RaceMenu（+ High Poly Head，+ EFM/EFA）
11. 脸部件资源（眼 / 眉 / 发 / 须）+ 对应 HPH 补丁
12. 物理：Faster HDT-SMP（和/或 CBPC）→ 按需配置
13. （可选）NPC 身形分配：BodyGen / OBody NG / AutoBody
14. NPC 美化 mod（如装了，注意 FaceGen 对齐）
```

> 第 0 步（本表之前）：**确认游戏版本**。控制台 `getskseversion` 能打出版本且与 mod 要求一致，
> 才算有了出发的资格。2026-10 的特殊判断题见 [`game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)。

### 每一步"装完该验证什么"

| 步 | 验证 |
|---|---|
| 1 | 用 `skse64_loader.exe` 能启动；`Data/SKSE/Plugins/` 有对应文件 |
| 3 | SkyUI 不报 "SKSE is not functioning properly" |
| 5 | 骨骼文件在 `meshes/actors/character/character assets/` |
| 6 | 行为补丁工具输出无错 |
| 7 | **只有一套**女性身形生效 |
| 9 | **勾了 `Build Morphs`**；构建日志无错误 |
| 10 | 进游戏能打开 RaceMenu 界面，**且能看到身形滑块** |
| 12 | 身体/头发有物理反应 |
| 13 | NPC 身材不再千人一面 |

### 三个最值得反复强调的验收点

- **第 9 步的"勾了 Build Morphs"不是可选项**：不勾，RaceMenu 里那一栏就是空的（判据见 [`racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md)）。
- **第 9 步要 Batch Build 全部服装**，别只 Build 身体；Group Filter 里别忘了 `Unassigned` 组。
- **第 10 步"能看到滑块"是分层验收的总闸门**：脸层之前的所有层有问题，都会在这里现形。

## 使用与配置

次序表不是一次性的。**日常每加一层，都有固定的追加动作**：

| 你刚装了 | 必须追加的动作 | 不做的后果 |
|---|---|---|
| 一件新护甲/一件衣服 | 进 BodySlide，同一预设 **Batch Build** 这件新装备 | 一穿就穿模（判据见 [`clipping.md`](../06-troubleshooting/clipping.md)） |
| 新身形或新皮肤 | 确认与既有身形同族；重建所有相关网格 | 皮肤 UV 不匹配、破皮 |
| 新骨骼/新动画包 | **重跑一次行为补丁**（FNIS / Nemesis / Pandora） | 动画/物理不生效或行为错乱 |
| 新物理 mod | 检查是否与既有引擎抢同一批骨骼（SMP vs CBPC） | "其中一个完全不起作用" |
| 新的 NPC 美化 | 检查 FaceGen 对齐（覆盖关系） | 黑脸（判据见 [`dark-face.md`](../06-troubleshooting/dark-face.md)） |
| 游戏版本更新 | 对照 [`version-matrix.md`](../00-overview/version-matrix.md) 逐项换版本 | 所有 SKSE 插件静默失效 |

**排序工具各管什么，别混**：

| 工具 | 管哪一栏 | 说明 |
|---|---|---|
| **LOOT** | 右栏（插件加载顺序） | 记录级"后加载者胜" |
| **MO2 的 warning 面板** | 左栏（资产覆盖顺序） | 自动复核"潜在 mod 顺序问题"，可点 Fix 重排（机制见 [`../../mo2-usvfs-kb/05-usage/warnings-and-order-problems.md`](../../mo2-usvfs-kb/05-usage/warnings-and-order-problems.md)） |
| **你自己的拖拽** | 左栏 | 覆盖关系的最终裁决者；详见 [`mo2-override-rules.md`](mo2-override-rules.md) |

## 三条纪律

### ① 女性身形只能启用一个

CBBE 与 UNP / BHUNP 互斥。同时启用 = 覆盖关系取决于排序，结果不可预期。

### ② 裸身与服装用同一个预设构建

否则穿模。见 [`../06-troubleshooting/clipping.md`](../06-troubleshooting/clipping.md)。

### ③ 装完身形/骨骼先跑一次行为补丁

FNIS / Nemesis / Pandora 生成行为文件，物理与动画都依赖它。
**顺序上它要早于物理 mod 真正生效。**

## 一个反直觉但重要的建议

> **不要一次装完再一起测。** 每完成一个"层"就进游戏看一眼。
>
> 五层一起装然后出错，你有几十种组合要排除；
> 每层装完就测，出错时嫌疑人只有一个。

这条建议的反直觉之处在于：它**感觉**更慢（频繁进游戏），但它是唯一能让
"排错成本"不随 mod 数量指数增长的办法。多装的部分就是将来排错的成本——
先确定目标，再决定装多少（目标分解见 [`learning-path.md`](../00-overview/learning-path.md)）。

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 所有 mod 像没生效、控制台 `getskseversion` 无输出 | SKSE 根本没加载（版本错配） | 回第 1 步；对照 [`version-matrix.md`](../00-overview/version-matrix.md) |
| 只有原版捏脸界面 | RaceMenu dll 没加载 | 检查 SKSE 与游戏版本；见 [`racemenu.md`](../02-face/racemenu.md) |
| 更新之后启动即崩 | 版本错配（含 1.7.x 的 overlay nif 特例） | 见 [`overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md) |
| 身形滑块那一栏不存在 | 缺 `.tri` / `BODYTRI`，或被覆盖 | 回第 9 步；查覆盖关系（[`mo2-override-rules.md`](mo2-override-rules.md)） |
| 裸体好、穿衣服崩 | 服装没参与 Batch Build / 不属于该家族 | 同预设 Batch Build；见 [`clipping.md`](../06-troubleshooting/clipping.md) |
| NPC 身材一模一样 | 没做分配（或本来就不该期待） | 第 13 步；运行时 morph 只作用于玩家 |
| 物理无论如何都不动 | DLL 未加载 / 非 physics 变体 / 版本档错 / 没跑行为补丁 | 见 [`physics-not-working.md`](../06-troubleshooting/physics-not-working.md) |
| 某层装完"没反应"，但别的层正常 | 构建产物或同名文件被后装的 mod 覆盖 | 用 Conflicts 面板定位；见 [`mo2-override-rules.md`](mo2-override-rules.md) |
| 一切正常但越装越慢/偶发崩溃 | 层级累积导致的资源或冲突问题 | 二分禁用，逐层回退 |

## 取舍与建议

- **只想捏脸**：做到第 10 步就停，不需要身形/骨骼/物理——捏脸是独立的一层。
- **想改身形**：第 5~9 步是成本中心，**第 9 步的构建质量决定后面一切**。
- **想跳过全程**：一个 Wabbajack modlist 可以替代第 0~13 步，代价见 [`wabbajack.md`](wabbajack.md)。
- **想用现成整合包**：先读 [`chinese-modpacks.md`](chinese-modpacks.md)——那类"成品"同样逃不过本篇的四条结构原因。
- **次序表的本质**：它不是"安装说明书"，而是**依赖方向的声明**。任何新 mod 进场，
  先问"它依赖谁、覆盖谁、产物落在哪"，再决定放哪。

## 来源

- 整体次序骨架（SKSE → ADL → SkyUI → 骨骼 → 身形 → 皮肤 → BodySlide → RaceMenu → 物理 → 行为补丁）：
  **社区共识**，与 Nexus 论坛的 CBBE 3BA 安装问答、STEP 指南一致 —— **社区经验（多源一致）**
- 排序原则（master/DLC → 修复 → 框架 → 身形皮肤骨骼 → 服装 → NPC 美化 → 补丁）：
  STEP 官方策划指南 —— **一手（指南）**
  `https://stepmodifications.org/wiki/SkyrimSE:0.1.0`
- "XPMSE ≥ 4.6"、"身形 physics 变体"、"`Build Morphs`"：各 mod 官方说明 —— **一手**
- **MO2 历史（Tannin 创建 MO2 支持 64 位游戏；被 Nexus 聘去开发 Vortex 后停更；
  LePresidente 修到可用并发布 v2.0.8；2017 年底更多开发者加入）**：MO2 GitHub README —— **一手**
  `https://github.com/ModOrganizer2/modorganizer`
- **NMM 前身为 Oblivion Mod Manager、2016 年 EOL**：第三方下载站与百科转述 ——
  **社区转述（具体公告原文未核实）**
- **Vortex 2017-05 定名、2018-01 限量 alpha**：Nexus 官方 news 帖 —— **一手**
  `https://www.nexusmods.com/capes/news/13386`
- **MO2 左栏越靠下优先级越高、BSA 内容参与同一套优先级判定、Overwrite 为工具产物落点、
  warning 面板与 LOOT 分管两栏**：`mo2-usvfs-kb` 对应条目 —— **一手（工具机制）**
  `../../mo2-usvfs-kb/05-usage/conflict-resolution.md` ·
  `../../mo2-usvfs-kb/03-architecture/bsa-priority-resolution.md` ·
  `../../mo2-usvfs-kb/05-usage/overwrite-dir.md` ·
  `../../mo2-usvfs-kb/05-usage/warnings-and-order-problems.md`
- **Zeroed Sliders + Build Morphs + Batch Build 为主流标准起点**：OBody NG 安装指南（第三方整理）
  —— **社区文档**；机制侧见 [`morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)
- **SMP 与 CBPC 抢同一批骨骼、身形须选 physics 变体**：[`physics-overview.md`](../04-physics/physics-overview.md) 及其来源
- **未确认**：MO1 的确切首发日期；NMM EOL 公告的原文与确切日期；
  "NMM 时代用户占比"等无法量化的一手数据
