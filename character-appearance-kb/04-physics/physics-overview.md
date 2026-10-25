---
id: physics-overview
title: 物理方案总览与选型
category: 04-physics
kind: concept
version: 2.0.0
updated: 2026-10-25
tags: [物理, 总览, 选型, SMP, CBPC, HDT-PE]
aliases: [物理方案, 选哪个物理, smp 还是 cbpc, 物理总览, 抖动原理, 物理引擎对比, bbp, tbbp, 身体物理头发物理, 物理打架, 物理怎么选, hdt-pe 是什么, smp cbpc 插槽, 物理方案历史]
source: https://www.nexusmods.com/skyrimspecialedition/mods/57339
summary: 四代物理方案（BBP/TBBP 动画式 → HDT-PE → HDT-SMP/FSMP 与 CBPC）的原理差异与对比表、SMP 与 CBPC 的关键区别（顶点 vs 球体、粒子数、开销来源）、"两个 dll 争 body 插槽"这个必踩的坑及解法，以及与身形、骨骼的耦合关系和诊断入口。
---

# 物理方案总览与选型

> **一句话选型**：身体用 CBPC，头发和衣服用 HDT-SMP（实际装它的现代 fork
> [FSMP](faster-hdt-smp.md)）。这条结论不是玄学，而是两套引擎机制差异的直接推论。

本页是 `04-physics` 分类的总入口：先在这里选对方案，再去看具体条目
（[XPMSSE 骨骼](xpmse-skeleton.md)、[HDT-SMP](hdt-smp.md)、[FSMP](faster-hdt-smp.md)、
[CBPC](cbpc.md)、[物理头发与衣物](physics-hair-and-cloth.md)）。

## 速览

| 项 | 内容 |
|---|---|
| 作用层 | 网格顶点层（SMP）/ 骨骼挂接的球体层（CBPC）；**不是 morph、不是骨骼动画** |
| 四代方案 | **BBP/TBBP**（Havok 骨骼动画式，写在动画里）→ **HDT-PE**（HDT Physics Extensions，游戏内建 Havok 骨骼级物理）→ **HDT-SMP / FSMP**（Bullet + 蒙皮网格逐顶点，真碰撞）/ **CBPC**（球体近似，实时每帧） |
| 关键文件 | SMP：`Data/SKSE/Plugins/hdtSkinnedMeshConfigs/*.xml`（引擎）+ 每个物理 mod 自带的配置；CBPC：`cbp.dll` + `CBPConfig.txt` 类配置 |
| 硬依赖 | 两者都依赖 **XPMSSE**（提供物理骨骼节点）与 **SKSE64**；CBPC 还依赖 FNIS/Nemesis 行为补丁 |
| 影响范围 | 胸/臀/腹弹动、头发/斗篷/裙摆摆动、身体碰撞，以及由此产生的全部性能问题 |
| 关键限制 | **CBPC 完全不能处理头发和衣服**；SMP 与 CBPC 默认争同一批骨骼，共存必须显式配置 |

要点：

- **第一性事实**：Skyrim 原版物理（Havok）只覆盖布帘、吊桥之类的场景物件，
  **不包含胸部/臀部/腹部弹跳**——角色身上的一切"抖"都是模改加上去的。
- **BBP/TBBP 是"假抖"**：运动写在行为/动画文件里，是回放预制动画；
  真正的实时物理从 HDT-PE 开始。BBP/TBBP 的骨骼名（`NPC L/R Breast` 等）沿用至今。
- **CBPC 用球体近似、每帧实算**，作者原话："不是预计算或假物理，只是用球体代替顶点做计算"。
- **SMP 逐顶点模拟最精细但最重**；CBPC 球数少、对 CPU 友好——这是"身体 CBPC、衣物 SMP"分工的成本根源。
- **装了物理 mod 不抖，第一嫌疑人不是物理 mod，而是身形**（没装物理变体 / 没构建），见[物理不生效](../06-troubleshooting/physics-not-working.md)。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 早期（具体年份未确认） | **BBP / TBBP** 纯动画方案流行：骨骼运动直接写在行为文件里，动画包里常见 "BBP/TBBP motions" 之名 | 第一代"抖"：Havok 回放预制动画，零实时计算，但动作生硬、与环境无关 |
| LE 中期（具体日期未确认） | **hydrogensaysHDT** 发布 **HDT-PE**（HDT Physics Extension，Nexus LE 53996） | 第二代：用游戏内建 Havok 给乳房/臀部等加实时物理，动画师不再需要手搓抖动动画 |
| 2015 前后 | HDT-SMP 早期测试版在社区流传，被描述为 "mesh/bullet based physics" | 第三代萌芽：自带 Bullet 引擎、逐顶点，不再依赖 Havok 物件管理 |
| 2018-11（发布帖日期见来源） | **Shizof** 发布 **CBPC**（Nexus SSE 21224），基于 **polygonhell 以 MIT 释出的 CBP Physics 源码** | 第三条路线：球体近似 + 每帧实算，对 CPU 友好，专攻身体部位 |
| 2019-2020 | hydrogensaysHDT 淡出模改，以 **MIT** 释出源码；社区出现 **aers → Karonar1** 的修复 fork 链 | SMP 进入"社区维护"时代 |
| 2021-10-21 起 | **DaymareOn / DaydreamingDay** 的 **FSMP**（Nexus 57339）上线并持续维护 | 现代 SMP 主线：多线程 + ImGui 配置菜单，官方口径"完全取代原版" |
| 2023-2024 | XPMSE 进入 5.x 时代（v5.06，2024-02-11） | 物理骨骼节点集合稳定，全部方案共享同一套挂点 |
| 2026 | FSMP 4.1.1（2026-08-27）；CBPC v1.6.1 | 当代标准组合：FSMP（头发/衣物）+ CBPC（身体） |

### 它从哪来

一切始于一个朴素需求：**让胸部和臀部动起来**。社区第一代答案是 BBP/TBBP——
不动引擎，把抖动写成动画。XPMSE 作者 groovtama 在 LoversLab 的原话区分了两代路线：
"BBP and TBBP = animation based，HDT PE/SMP = Physics based"（BBP/TBBP 是动画驱动，
HDT PE/SMP 是物理驱动）。hydrogensaysHDT 的 HDT-PE 第一次把实时物理带进这个领域，
SMP 又进一步换成自带 Bullet 引擎、逐顶点计算；Shizof 的 CBPC 则走了第三条路：
不上顶点，用几个球体近似身体部位，换取极低的 CPU 开销。

### 中间经历了什么

最大的分叉是 **SMP 的 fork 链**：原作者淡出 → aers 修复 → Karonar1 系统修 bug →
DaymareOn 构建维护（FSMP）。原版 HDT-SMP 停留在 LE 与 SE 1.5.97，**AE（1.6.x）用户
实际都在用 FSMP**。第二条分叉是 **CBPC 从 CBP Physics 独立出来**：polygonhell 以 MIT
释出源码是 CBPC 存在的前提，Shizof 在其上加了碰撞功能。

### 现状

没有"唯一赢家"，而是**双引擎分工**：FSMP 管头发/衣物（唯一能管它们的方案），
CBPC 管身体部位（CPU 友好、可跑大量 NPC）。两者都要挂 XPMSE 的骨骼节点，
于是有了下面这个必踩的坑。

## 它解决什么问题

**没有物理 mod 之前**：角色身上一切静态——胸部不抖、斗篷不飘、头发穿过身体；
动画师想让胸部动，只能给每套动画手搓 BBP/TBBP 抖动关键帧。

**物理 mod 的解法**是给"可动部位"提供挂点与实时求解器。按方案分四代：

| 代 | 方案 | 原理 | 计算时机 | 精度 | 性能 | 现状 |
|---|---|---|---|---|---|---|
| 一代 | **BBP / TBBP** | 骨骼运动**写在行为/动画文件里**，Havok 回放预制动画 | 无（播放动画） | 低 | 极轻 | 已淘汰；骨骼名沿用 |
| 二代 | **HDT-PE** | 游戏内建 **Havok** 骨骼级物理 | 每帧 | 中 | 轻 | 被 SMP 取代 |
| 三代 A | **HDT-SMP / FSMP** | **Bullet + 蒙皮网格逐顶点**，自带碰撞体 | 每帧 | 高 | 重（FSMP 已大幅优化） | 当代主选（头发/衣物） |
| 三代 B | **CBPC** | **球体近似**，每帧实算 | 每帧 | 中 | **轻（CPU 友好）** | 当代主选（身体部位） |

> BBP/TBBP 的全称（Breast and Butt Physics / Tender Breast and Butt Physics）与
> "动画驱动 vs 物理驱动"的定性，见 BHUNP 作者 Bakafactory 的科普博客与 groovtama 的
> LoversLab 回帖（来源节）。它们今天**不再是独立 mod**，而是 XPMSE 骨骼里的两组节点名。

### 一代方案为什么被淘汰

BBP/TBBP 不是"低级版实时物理"，而是**另一种东西**——预置动画。这带来三个硬伤：

1. **不响应环境**：跑、跳、转身各播各的，角色撞到什么都没反应；
2. **动画师的永久负担**：每套新动画都要单独做抖动关键帧，所以旧动画包名字里
   常带 "BBP/TBBP motions" 字样；
3. **与实时物理互斥**：同一部位被两套系统抢， historically 引发过兼容问题
   （LE 时代 "xpmse with both hdt and bbp will cause issues" 的社区记录）。

理解这一点有助于解释今天的现象：**BBP/TBBP 的骨骼名还在每具身形的骨架里，
但已经没有任何 mod 用动画方式驱动它们**——它们只是物理引擎的挂点。

## SMP 与 CBPC 的关键区别

两套引擎常被混为一谈，但差异是机制性的：

| | **HDT-SMP / FSMP** | **CBPC** |
|---|---|---|
| 模拟对象 | **蒙皮网格的顶点**（skinned mesh 的每个顶点都是一个粒子） | 骨骼上挂接的**球体**（spheres） |
| 粒子数 | 与网格精度成正比：一顶物理头发数百至上千顶点，一件斗篷可达数千 | 每部位固定几个球（胸/臀/腹各一组），与网格精度无关 |
| 开销来源 | **顶点数 × 碰撞检测 × 每帧约束求解**；网格越细越贵，NPC 一多成本线性叠加 | 球数少、计算简单，**跑大量 NPC 时开销可控** |
| 能做什么 | 头发/斗篷/裙摆与**身体、地面**碰撞；风力；细腻摆动 | 胸/臀/腹弹动，及这些部位（外加阴道等，若身形有对应节点）与**手、生殖器**的碰撞 |
| 不能做什么 | ——（但最吃 CPU） | **完全不能处理头发和衣服**——它没有对应网格的蒙皮信息 |
| 配置文件 | `hdtSkinnedMeshConfigs/*.xml`（每个物品一个） | `CBPConfig.txt` 类文本配置（可调球体贴合身形） |
| 前置 | SKSE64 + Address Library（FSMP）；早期原版需 OpenCL 2.0 | SKSE64/SKSEVR + XPMSSE + FNIS/Nemesis |
| 作用范围 | 只附加到 **XPMSE 的 human skeleton** | XPMSE 骨骼节点 |

> **一句话**：SMP 是"给网格做物理"，CBPC 是"给几个球做物理"。
> 所以"我装了 CBPC 但头发不动"不是配置问题，是**方案选错了**（详见
> [physics-hair-and-cloth.md](physics-hair-and-cloth.md)）。

## 必踩的坑：两个 dll 争 body 插槽

SMP 与 CBPC **想挂的是同一批骨骼**（乳房、臀部、腹部）。两个都装、都不配置，
结果不是"叠加更好"，而是**互相覆盖、物理打架**。

共存的公认做法（二选一或并用）：

1. **编辑 SMP 的 `defaultBBPs.xml`**，让 SMP **忽略身体**、只管头发/衣服；
2. **把 `cbp.dll` 改名为 `zcbp.dll`**，利用 dll 加载顺序让 SMP 先加载
   （或用 Engine Fixes 的 preload 机制达到同样效果）。

> 这一条是**社区经验**（LoversLab 多个帖子给出同一解法），但与两套引擎"抢同一批
> 骨骼"的机制吻合，可信度较高。详细步骤与调参检查项见
> [cbpc.md](cbpc.md) 的「与 SMP 共存」一节。

## 与身形的耦合

物理**不是独立层**，装什么引擎之前要先满足身形的两个条件：

1. 身形必须选 **physics 变体**（如 3BA 的物理版本、BHUNP 的 3BBB）；
2. 必须用 **BodySlide 构建带物理的身形**（光选不够，还要构建）。

所以"装了 FSMP 还是不抖"的第一检查点不是物理 mod，而是身形：
[CBBE 3BA](../03-body/cbbe-3ba.md) 在 FOMOD 里就有 CBPC only / SMP / 两者都装的选项；
 morph（滑块变形）与物理（顶点/球体模拟）也是两套无关机制，别混
（见 [morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)）。

## 与骨骼的耦合

所有现代身形与物理都**依赖 XPMSE 提供的额外骨骼节点**：
`NPC L/R Breast`（BBP）、`NPC L/R Breast01`（TBBP 追加）、`HDT LBreasts`、`HDT Belly`、
`NPC Belly` 等。**没有 XPMSE 就没有"可挂物理的骨"**——
SMP 明确只把网格附加到 XPMSE 的 human skeleton，CBPC 同样读 skeleton 信息。
详见 [xpmse-skeleton.md](xpmse-skeleton.md)。

## 诊断入口

物理不生效的完整排查（十条按序检查清单）见
[物理不生效（不抖 / 头发穿透）](../06-troubleshooting/physics-not-working.md)。
两个最高杠杆的动作：

1. 进游戏开控制台跑 `smp report warnings`——FSMP 内置，**校验整个 load order 的
   物理 XML 与 `.nif`** 并直接指出哪个 mod 的配置有警告；
2. 确认身形是物理变体且已构建（上文「与身形的耦合」）。

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 身体头发都不抖 | 引擎层未生效（SKSE 版本不匹配 / 没装 XPMSE / FOMOD 版本档选错） | 按[十条清单](../06-troubleshooting/physics-not-working.md)从头查；先跑 `smp report` |
| 身体抖、头发不动 | 只装了 CBPC（机制限制） | 补装 [FSMP](faster-hdt-smp.md)，并确认发型带 XML |
| 物理"打架"、互相拉扯 | SMP 与 CBPC 抢同一批骨骼 | 按上文「必踩的坑」分腔配置 |
| 装了 FSMP 身体还不抖 | 身形不是 physics 变体 / 没构建 / 3BA 的 MCM 切错了引擎 | 换变体 + BodySlide 重建；检查 MCM 物理开关 |
| 斗篷不飘 | 那件物品没有 SMP XML，或被其他 mod 覆盖 | `smp report` 定位；查覆盖关系（[mo2-override-rules.md](../07-workflow/mo2-override-rules.md)） |
| 开局 CTD | SMP/CBPC 版本档与游戏版本不符；或 `cbp.dll` 改名后旧文件未删 | FOMOD 重选版本档；删旧 dll 再更新 |
| 身体"抖得很假"、像在播放动作 | 老配置/老身形还在用 BBP/TBBP 动画驱动，或有动画包在抢同一部位 | 卸掉动画式 BBP/TBBP 内容，物理部位只留一套引擎驱动 |
| 升级游戏版本后全部插件失效 | SKSE 与游戏版本不匹配，所有 SKSE 插件静默失效 | 按版本矩阵换 SKSE 与各插件版本档（见下） |

## 版本敏感性

物理全是 **SKSE 插件**，因此整条链都绑定游戏版本：

- SKSE 与游戏版本必须一对一号（FSMP FOMOD 的版本档就是按 SKSE 版本分的）；
- 当前各档对应关系见 [version-matrix.md](../00-overview/version-matrix.md)，
  1.7.x 的冲击见 [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)；
- FSMP 对 1.7.x 的支持状态**未确认**——升级游戏版本前先查 Nexus Files 页。

## 取舍与建议

- **只想身体抖、机器一般 / NPC 多**：CBPC 优先——球体近似对 CPU 友好，
  作者的设计理念就是"不能以屠杀帧率为代价"；
- **要头发/斗篷/裙摆物理**：没有替代品，装 FSMP；
- **两者都要**：装，但按上文做分腔配置，否则不如只装一个；
- **性能敏感**：FSMP 的 ImGui 菜单有 Performance 预设（含 `Performance.xml`），
  默认不带 AVX2，CPU 支持时建议启用（见 [faster-hdt-smp.md](faster-hdt-smp.md)）；
- **别做**：同时装原版 HDT-SMP 与 FSMP（官方明确"do not install the original"）；
  同时装 CBP 与 CBPC（同名 dll 互相覆盖，见 [cbpc.md](cbpc.md)）。

## 来源

- **BBP/TBBP 是动画驱动、HDT PE/SMP 是物理驱动；BBP/TBBP 骨骼为
  `NPC L/R Breast(01)`、属 XPMSE 骨骼；HDT-PE 之前动画师必须手搓胸臀动画**：
  groovtama（XPMSE 作者）LoversLab 回帖 + Bakafactory（BHUNP 作者）科普博客
  （2019-10）—— **一手（作者原话）**
  `https://babofactory.blogspot.com/2019/10/what-is-hdt-pe-hdt-smp-bbp-tbbp-3bbb.html`
- **HDT-PE = HDT Physics Extension、用游戏内建 Havok**：HDT-PE Nexus LE 53996
  页面描述（经社区转述）—— **一手（经转述）**
  `https://www.nexusmods.com/skyrim/mods/53996`
- **CBPC 作者 Shizof、基于 polygonhell 的 MIT 源码、"用球体代替顶点、每帧计算、
  不是预计算或假物理"、依赖链（SKSE64 + XPMSSE + FNIS/Nemesis）**：
  CBPC Nexus 21224 描述（经镜像站转载 v1.6.1 版全文）—— **一手（经转载）**
  `https://www.nexusmods.com/skyrimspecialedition/mods/21224`
- **FSMP fork 链（hydrogensaysHDT → aers → Karonar1 → DaymareOn）、
  "massively improves performance…replaces it totally. Do not install [原版]"、
  只附加 XPMSE human skeleton（修 Lurker 骨骼问题）**：FSMP 官方仓库 README /
  wiki 与 Nexus 57339 描述 —— **一手**
  `https://github.com/DaymareOn/hdtSMP64`
- **SMP 适合衣服、CBPC 适合身体；CBPC 不能管头发和衣服；
  `cbp.dll → zcbp.dll` 与 `defaultBBPs.xml` 分腔配置**：LoversLab 多帖一致 ——
  **社区经验（多帖一致）**
- **CBPC 2018-11 发布（LoversLab 帖引用的发布 announcement）**：Nexus 论坛帖 ——
  **社区经验（转述发布帖）**
- **BBP/TBBP 流行的具体年份、HDT-PE 首发日期**：**未确认**（Nexus LE 旧页日期未能核实）
