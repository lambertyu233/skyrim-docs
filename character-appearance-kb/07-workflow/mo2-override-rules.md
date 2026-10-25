---
id: mo2-override-rules
title: MO2 覆盖规则（左栏 vs 右栏）
category: 07-workflow
kind: concept
version: 2.0.0
updated: 2026-10-25
tags: [安装, MO2, 覆盖, 优先级, 冲突, VFS]
aliases: [左栏 右栏, 覆盖顺序, mod organizer, 虚拟文件系统, mo2 覆盖, 谁覆盖谁, 冲突面板, overwrite, 构建产物被覆盖, bsa 松散文件, mo2 优先级, 左栏右栏不一致, 怎么查冲突, mohidden]
source: https://forums.nexusmods.com/topic/5755942-the-dark-faces-bug-how-to-fix-it/
summary: MO2 的左栏（资产覆盖优先级）与右栏（插件加载顺序）是两件独立的事，以及"两者不一致"为什么会造成黑脸这类"找不到原因"的故障；含身形/皮肤的覆盖关系、BSA 与松散文件的胜负、BodySlide 构建产物的归宿与 Wabbajack 列表的特殊纪律。
---

# MO2 覆盖规则

> 本工作区另有专门讲 MO2 与 USVFS 机制的资料库（[`mo2-usvfs-kb`](../../mo2-usvfs-kb/)）。
> 本条目只讲**与捏脸/身形直接相关**的那部分。

> **一句话**：MO2 的左栏决定"**哪个文件**被读取"，右栏决定"**哪条记录**赢"——
> 它们互不影响，而"文件对不上记录"正是黑脸、滑块失效这类疑难症状的根源。

## 速览

| 项 | 内容 |
|---|---|
| 作用层 | 虚拟文件系统（VFS）的文件投影 + 插件记录级加载顺序 |
| 两个面板 | **左栏（Mods）= 资产覆盖优先级**；**右栏（Plugins）= 插件加载顺序** |
| 核心规则 | 左栏**越靠下优先级越高**；右栏**后加载者胜**（记录级） |
| 由谁决定 | 左栏：你手动拖；右栏：常由 LOOT 决定 |
| 关键文件 | 工具产物落 **Overwrite**（最高优先级）；隐藏单文件的实质是追加 `.mohidden` |
| 影响范围 | 黑脸、脖缝、穿模、滑块失效、物理 XML 失效等"查不出原因"类故障 |
| 关键限制 | **只看一个面板永远查不出来**；BSA 内容与松散文件参与同一套优先级判定 |
| 交叉库 | 机制详见 [`mo2-usvfs-kb/05-usage/conflict-resolution.md`](../../mo2-usvfs-kb/05-usage/conflict-resolution.md) |

要点：

- **两个面板是两件事**：左栏放得很好的 mod，右栏仍可能在记录层面输掉，反之亦然。
- **覆盖无处不在**：BSA 里的文件也参与优先级判定——"我明明装了"和"生效的是另一份"可以同时为真。
- **工具产物有专门归宿**：BodySlide / xEdit / FNIS 的输出默认落 Overwrite，**不要**手写进游戏目录。
- **`hide` 是精确手术刀**：保留 mod、只排除那一个冲突文件，比重装整个 mod 便宜得多。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 中期 | **Mod Organizer（MO1）** 由 Tannin 发布，引入 VFS | 第一次把"覆盖"从物理事实变成**可调整的列表排序** |
| 2016-10 前后 | Tannin 被 Nexus 聘去开发 Vortex，MO2 一度停滞；**LePresidente** 独自修到可用状态并发布 **v2.0.8**；2017 年底更多开发者加入 | MO2 由社区接手并成为事实标准（**一手：MO2 GitHub README**） |
| 2017-2018 | Vortex 发布（Nexus 官方阵营） | 两个阵营都采用 VFS，但"覆盖可见性"的设计取向不同（社区经验） |
| 2018 之后 | 3BA / BodySlide / 物理 mod 生态爆发 | 构建产物与 BSA 大量进场，"谁覆盖谁"从边缘知识变成**必备排错技能** |
| 2021 之后 | Wabbajack modlist 普及 | 出现新问题形态：**封闭实例里的覆盖关系是作者调好的，用户动它之前必须先懂它** |

### 它从哪来

"覆盖规则"这个问题是 **VFS 的直接推论**。NMM 时代文件物理落盘，覆盖是一次性的、
不可见的写操作；MO 把 mod 收进各自文件夹、用虚拟投影喂给游戏之后，
"谁赢"就变成了一条随时可改的排序——**这是mod管理史上最关键的单一设计**，
但它也把责任转移给了用户：排序错了，游戏不会报错，只会给你错的文件。

### 中间经历了什么

最大的分叉是 **BSA 的处理**。早期社区流传"BSA 是黑盒、松散文件永远赢"，
实测（含本工作区引用的 MO2 机制文档）表明：**BSA 内容同样被拉进虚拟目录树，
与松散文件一起参与同一套优先级判定**（见
[`../../mo2-usvfs-kb/03-architecture/bsa-priority-resolution.md`](../../mo2-usvfs-kb/03-architecture/bsa-priority-resolution.md)）。
高优先级 mod 的 BSA 盖过低优先级 mod 的松散文件，完全可能。

第二个分叉是 **Overwrite 的角色演化**：它原本只是"工具写出的新文件的临时落点"，
实践中大量用户把 BodySlide 输出永久堆在里面，导致"文件来历不可追溯"——
现在的共识是把它当**中转站**而非仓库（见
[`../../mo2-usvfs-kb/05-usage/overwrite-dir.md`](../../mo2-usvfs-kb/05-usage/overwrite-dir.md)）。

### 现状

MO2 提供了三个层级的覆盖可见性：**Conflicts 面板**（逐文件）、
**warning 面板**（顺序问题的自动复核）、**Filetree**（核对装没装歪）。
三者都基于同一套底层规则（FileEntry 多来源优先级）。真正需要人工判断的，
只剩"资产层与记录层是否一致"这一件事——这正是本条目的主题。

## 它解决什么问题

**没有覆盖规则时**：mod 之间互相覆盖是静默的。你装了 A 和 B 两个改同一张贴图的 mod，
游戏用哪一份取决于排序，而排序往往没人管过。于是：

| 症状 | 用户的第一反应 | 实际原因 |
|---|---|---|
| 脸变黑 | "FaceGen 坏了？重装 NPC 美化？" | head parts 与头网格对不上（记录 vs 资产不一致） |
| 滑块拖了没反应 | "RaceMenu 坏了？身形坏了？" | 构建产物被后装的同名 nif 覆盖 |
| 物理不抖 | "物理 mod 坏了？" | 物理 XML 或 dll 被覆盖 / 两个引擎抢插槽 |

**它的解法**是把"覆盖"变成三件可操作的事：**看见**（Conflicts 面板）、
**裁决**（左栏排序）、**取巧**（hide 单文件 / Overwrite 中转）。

## 工作原理：两个面板是两件事

| | 左栏（Mods） | 右栏（Plugins） |
|---|---|---|
| 控制什么 | **资产覆盖**：`.nif` / `.dds` / `.hkx` 等文件谁覆盖谁 | **插件加载顺序**：`.esp` / `.esm` / `.esl` 的记录谁赢 |
| 机制 | 虚拟文件系统（VFS）把文件投影进游戏 | 记录级的"后加载者胜" |
| 粒度 | **文件级**（同名路径整份替换） | **记录级**（可只赢一条记录） |
| 由谁决定 | 你手动拖 | 常由 LOOT 决定 |
| 调错了会怎样 | 读到错的那份文件（贴图/网格/配置） | 记录赢家与资产赢家不是同一个 mod |

**它们互不影响。** 左栏放得很好的 mod，右栏仍可能在记录层面输掉。

### 为什么这条值得单独写一条

因为**黑脸、脖缝、穿模这三类"查不出原因"的故障，根源常常就在这条不一致上**。

以黑脸为例：

1. 修改 NPC 记录的 mod（假设是 A）在**右栏赢了** → 引擎按 A 的 head parts 去找 FaceGen；
2. 但 A 的 FaceGen 文件在**左栏输了**，被另一个 mod B 的同 FormID 文件覆盖；
3. 于是 head parts 与头网格对不上 → **脸变黑**。

**只看一个面板永远查不出来。**

## 使用与配置：实用的排查动作

### ① Conflicts 面板（逐文件看谁覆盖谁）

双击左栏任意 mod → **Conflicts** 标签页。右侧三个数字从上到下是：

1. **处于冲突中、且正在覆盖其它 mod** 的文件数；
2. **处于冲突中、正被其它 mod 覆盖** 的文件数；
3. **不与任何已启用 mod 冲突**的文件数。

- 上框 = 本 mod 覆盖低优先级 mod 的文件；想让别的 mod 提供该文件，把本 mod 优先级调低。
- 下框 = 本 mod 被高优先级 mod 覆盖的文件（此框中无法 hide）。
- 传统口诀：**红色 = 这个 mod 覆盖了别人；绿色 = 这个 mod 被别人覆盖。**

### ② hide：保留 mod，只排除一个文件

右键冲突文件 → `Hide`，**实质是给文件追加 `.mohidden` 扩展名**让它不生效；
恢复：Filetree 标签页右键 → `Unhide`。两个 mod 互相覆盖不同文件、
而你更想要两者各一部分时，这是唯一的精确手段（详见
[`../../mo2-usvfs-kb/05-usage/hide-files-and-filetree.md`](../../mo2-usvfs-kb/05-usage/hide-files-and-filetree.md)）。

### ③ Filetree：核对"东西到底装对目录没有"

双击 mod → **Filetree** 显示其全部文件（含 MO2 生成的 `meta.ini`，**勿动**）。
**FOMOD 装歪**的情况在这里一眼可见——装歪的文件根本不在预期路径上，
后续一切覆盖分析都是错的。

### ④ Overwrite：工具产物的中转站

BodySlide 生成的网格、xEdit 清洗出的 `.esp`、LOOT 排序结果、FNIS 输出等，
经 VFS 写出时默认落入 `overwrite\`。它优先级最高，"盖"住一切同名文件——
这正是工具产物立即生效的原因，但也意味着**它里面堆的东西会压掉你正式 mod 的文件**。
维护纪律：定期把内容归档进对应 mod 文件夹，别当仓库用（见
[`../../mo2-usvfs-kb/05-usage/overwrite-dir.md`](../../mo2-usvfs-kb/05-usage/overwrite-dir.md)）。

### ⑤ SSEEdit：核对记录层谁赢了

资产层查完，用 **SSEEdit** 看记录层面谁赢了，与资产层面是否一致。
黑脸类问题的终极判据就是这一步：**记录赢家与资产赢家必须是同一个 mod**。

### ⑥ warning 面板：顺序问题的自动复核

工具栏 warning 图标表示左栏顺序存在**潜在问题**，选中后点 **Fix** 让 MO2 重排。
它管**资源**顺序，与 LOOT 管的**插件**顺序不是一回事（见
[`../../mo2-usvfs-kb/05-usage/warnings-and-order-problems.md`](../../mo2-usvfs-kb/05-usage/warnings-and-order-problems.md)）。

## 与身形/皮肤的覆盖关系

| 资源 | 谁应该覆盖谁 |
|---|---|
| 身形网格 | 你的身形 mod 应**覆盖**原版与其他身形（但只能启用一个身形 mod） |
| 皮肤贴图 | 皮肤 mod 应在身形**之后**（覆盖） |
| BodySlide 输出 | 应在最终 Data 中**胜出**，否则 `BODYTRI` 丢失 |
| FaceGen | NPC 美化 mod 的 FaceGen 应在其他 FaceGen 之前（覆盖） |

三条展开说明：

### BodySlide 构建产物被覆盖 = 滑块静默失效

`Build Morphs` 生成的是 `.tri` + NIF 里的 `BODYTRI` 指针。后装的任何同名 nif
都会覆盖掉这份指针，**界面不报错、滑块只是没反应**。判据：拖滑块无变化时，
先在 Conflicts 面板查该 nif 的赢家是不是你的构建产物（机制见
[`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)，
症状排查见 [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md)）。

### BSA vs 松散文件：不是"松散永远赢"

BSA 内容同样被拉进虚拟目录、**参与同一套优先级判定**：想让松散文件盖过 BSA 内的资源，
让松散文件所在 mod 优先级**高于** BSA 所属 mod 即可；反之，高优先级 mod 的 BSA
会压过低优先级 mod 的松散文件。还受"存档失效（archive invalidation）"与
BSA 加载顺序影响（机制见
[`../../mo2-usvfs-kb/03-architecture/bsa-priority-resolution.md`](../../mo2-usvfs-kb/03-architecture/bsa-priority-resolution.md)）。

**判据**：你明明装了某个贴图 mod 却没生效，先查它的文件是不是在 BSA 里、
而赢家 mod 的优先级更高。

### 构建产物的正确归宿

**BodySlide 输出要放进 MO2 的 Overwrite 或一个专门的 mod 文件夹**，
不要直接写进游戏目录 —— 否则它会绕开 VFS 的覆盖关系，变成没人能追溯的"幽灵文件"。

## Wabbajack 列表的特殊纪律

Wabbajack 装出来的列表是一个**封闭的 MO2 实例**：

- **不要把自己的 mod 叠上去** —— 列表更新会清掉额外添加的 mod（详见 [`wabbajack.md`](wabbajack.md)）。
- 覆盖关系是**作者调好的**：动左栏排序之前，先理解作者为什么那么排
  （多数列表的 README 会说明关键 mod 的位置）。
- 想加自己的身形/皮肤，**先学会本篇的排查动作**：叠加产生冲突时，
  你唯一能用的工具就是 Conflicts 面板 + hide，而列表的封闭性让"卸载重来"不可用。

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| NPC 脸变黑 | 记录赢家与资产赢家不是同一个 mod（head parts ↔ FaceGen 对不上） | 按"实用的排查动作"①→⑤ 走；见 [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md) |
| 拖滑块没反应 | `BODYTRI` 被后装 nif 覆盖 / 没勾 `Build Morphs` | Conflicts 面板查该 nif 赢家；重建并确认产物优先级 |
| 装了贴图 mod 没生效 | 赢家在 BSA 里且优先级更高 | 提高本 mod 优先级；或把资源做成松散文件 |
| BodySlide 输出"时灵时不灵" | 输出堆在 Overwrite 里与正式 mod 打架 | 归档 Overwrite，正式 mod 只留一份来源 |
| 卸载一个 mod 后另一个 mod 坏了 | 之前靠它的文件"垫"着（共享文件被 hide/删除） | 重装被依赖方；别用 hide 掩盖共享文件缺失 |
| 脖子接缝 | 皮肤与身形 UV/顶点不一致，常伴随覆盖错位 | 见 [`../06-troubleshooting/neck-seam.md`](../06-troubleshooting/neck-seam.md) |
| 物理 XML 改了没反应 | 配置所在 mod 优先级不够，或被另一份同名 XML 覆盖 | Conflicts 面板查 XML 赢家；见 [`../06-troubleshooting/physics-not-working.md`](../06-troubleshooting/physics-not-working.md) |
| FOMOD 装完文件路径不对 | 安装时选错了目录档 | Filetree 核对路径，重装该 mod |

## 取舍与建议

- **优先级是最后手段，不是第一手段**：能用补丁解决的记录冲突，别用覆盖去硬压。
- **正式的 mod 一个文件一个来源**：同一路径永远只有一个"应该赢"的 mod，其余靠补丁而非覆盖。
- **Overwrite 每周看一眼**：它是整个实例里优先级最高、也最不透明的文件夹。
- **动 Wabbajack 列表前先备份 profile**：封闭实例里排错成本远高于手动列表。
- **把"两个面板一起看"变成肌肉记忆**：本条目所有疑难症状的共同点，
  都是"只看一个面板查不出来"。

## 来源

- 左栏 = 资产优先级、右栏 = 加载顺序，二者独立：MO2 机制说明与社区 cheatbook ——
  **一手（工具机制）+ 社区经验**
- "左栏右栏不一致 → 黑脸"：Nexus 论坛 Black-Face 讨论 —— **社区经验（多帖一致）**
- Conflicts 面板红/绿含义、用 hide 排除单文件：
  Nexus Black-Face Fix Guide（`mods/77338`）—— **社区经验**
- Wabbajack 列表隔离、更新会清掉额外 mod：Wabbajack 官方文档 —— **一手**
  `https://wiki.wabbajack.org/user_documentation/Installing%20a%20Modlist.html`
- **左栏越靠下优先级越高、BSA 参与同一套排序、Overwrite 为工具产物落点、warning 面板 vs LOOT、
  `.mohidden` 实质、Filetree 与 meta.ini**：[`mo2-usvfs-kb`](../../mo2-usvfs-kb/) 对应条目 ——
  **一手（工具机制，引自 STEP Mod Organizer 指南与 MO2 源码仓库）**
  `../../mo2-usvfs-kb/05-usage/conflict-resolution.md` ·
  `../../mo2-usvfs-kb/03-architecture/bsa-priority-resolution.md` ·
  `../../mo2-usvfs-kb/05-usage/overwrite-dir.md` ·
  `../../mo2-usvfs-kb/05-usage/hide-files-and-filetree.md` ·
  `../../mo2-usvfs-kb/05-usage/warnings-and-order-problems.md`
- **MO2 历史（Tannin 创建、被 Nexus 聘走后停更、LePresidente 修复并发布 v2.0.8）**：
  MO2 GitHub README —— **一手** `https://github.com/ModOrganizer2/modorganizer`
- **未确认**：MO2 各版本对 BSA 加载顺序的精确算法细节（本库未逐行核对源码）；
  "archive invalidation" 对优先级的影响权重（社区有多种说法）
