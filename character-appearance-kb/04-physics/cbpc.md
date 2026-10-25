---
id: cbpc
title: CBPC（CBP Physics with Collisions）
category: 04-physics
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [物理, CBPC, 碰撞, 胶囊体, Shizof]
aliases: [cbp, 碰撞物理, 胶囊体物理, 身体物理, cbpc 是什么, cbpc 安装, cbpc 1.6.1, 弹跳配置, 乳摇, 臀抖, 腹弹, sinful cbp, cbpc config]
source: https://www.nexusmods.com/skyrimspecialedition/mods/21224
summary: CBPC 百科全书：作者 Shizof、基于 polygonhell MIT 源码的前提、球体逐帧实时模拟原理、v1.6.1 与 SSE/VR 双版本 FOMOD、1/3 乳骨身形的两组弹跳配置、XPMSSE 安装选项、与 SMP 共存的必做步骤，以及调参不生效的检查项。
---

# CBPC（CBP Physics with Collisions）

> **一句话**：CBPC 是"身体部位物理"的当代主选——用几个球体代替网格顶点做
> **每帧实算**，覆盖胸/臀/腹弹跳及它们与手、生殖器的碰撞；对 CPU 友好，
> 是纯 SMP 方案之外的低成本替代。

- 作者 **Shizof**
- Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/21224`
- 全称：**CBPC - CBP Physics with Collisions for SSE and VR**
- 基于 **polygonhell 的 CBP Physics**（作者以 **MIT** 释出源码）继续开发——
  这是它存在的前提。
- 当前版本 **v1.6.1**。

## 速览

| 项 | 内容 |
|---|---|
| 作者 / 版本 | **Shizof** / **v1.6.1** |
| 上游前提 | **polygonhell 的 CBP Physics**（MIT 释出源码，"Big thanks to polygonhell… which allowed me to create this mod"） |
| 原理 | **球体（spheres）代替顶点**做碰撞计算；**每帧计算**；**实时动态模拟，不是预计算/假物理** |
| 覆盖 | 胸/臀/腹弹跳；胸/臀/腹/阴道（及更多，若身形有对应节点）与 NPC/玩家**手、生殖器（schlongs）**的碰撞 |
| 前置 | SKSE64 / SKSEVR + **XPMSSE**（装时选 Physics Extensions，其余 None，可删 esp）+ FNIS 或 Nemesis + 带对应节点的物理身形 |
| 游戏版本 | **SSE 与 VR 双版本，FOMOD 必须选对** |
| 维护状态 | 低频更新（v1.6.1 为社区可确认的最新版；其后是否有更新**未确认**） |

要点：

- **它不是"预设动画"**：作者原话——"CBPC is not Pre-Calculated or Fake Physics.
  It just uses spheres instead of vertices to make it's calculations.
  Calculations are made every frame."
- **球体可调**：配置文件让碰撞球贴合你的身形；自定义身形有官方 PDF 配置指南。
- **完全不能处理头发和衣服**（没有那些网格的蒙皮信息）——那是
  [SMP/FSMP](faster-hdt-smp.md) 的领域，两套引擎分工见
  [physics-overview.md](physics-overview.md)。
- 设计哲学：*"a physics mod that you can't fully use in a game without murdering
  your fps is not a good physics mod at all"*——性能优先是刻进设计里的。
- 与 SMP **默认争同一批骨骼**，共存必做分腔（见下文）。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| LE/SSE 之交（具体日期未确认） | **polygonhell** 发布 CBP Physics，后以 **MIT** 释出源码 | 球体近似 + 行为补丁驱动的物理路线奠基 |
| 2018-11（发布帖日期见来源） | **Shizof** 发布 **CBPC**（Nexus SSE 21224），在 CBP 源码上加碰撞功能 | "Physics with Collisions" 的由来：弹跳 + 碰撞二合一 |
| 2019-2020 | 与 CBBE 3BBB/3BA 生态互相成就（3BA 官方前置链含 CBPC 1.5.1+） | 成为物理身形的事实标准前置 |
| 2021-2022 | 社区讨论实时节点缩放、BellyBulge 等特性（Acro748 等参与测试反馈） | 功能持续打磨 |
| 2026 | 社区可确认版本 **v1.6.1**；SSE/VR 双版本 FOMOD | 当前形态 |

### 它从哪来

**没有 polygonhell 的 MIT 释出，就没有 CBPC**——Shizof 是在 CBP Physics 源码上
继续开发并加上碰撞（Collisions）功能的。这条技术路线的核心思想从 CBP 时代就没变：
**用球体近似身体部位，把计算量控制在"能愉快玩游戏"的水平**。

### 中间经历了什么

从 CBP 到 CBPC 的关键增量是**碰撞**：乳房/臀部/腹部不只是自己抖，还能与
NPC/玩家的手、schlongs 等发生碰撞。VR 版则支持 VR 手柄与装备武器的碰撞。

### 现状

v1.6.1 之后 Nexus 页面是否有更新**未确认**（发布页在成人内容墙后，本轮未能直读，
版本号经镜像站转载的 v1.6.1 文件描述确认）。它与 SMP 的分工格局稳定：
**身体 CBPC、衣物 SMP**（见 [physics-overview.md](physics-overview.md)）。

## 它解决什么问题

**没有它之前**：身体物理要么没有（纯静态身形），要么走 HDT-PE/SMP 的
重计算路线——精度高但 CPU 占用大，NPC 一多就卡；且碰撞能力有限。

**CBPC 的解法**：

| 问题 | CBPC 的做法 |
|---|---|
| 胸部不抖 | 每侧乳房挂球体，每帧解算 |
| 想撞到手/生殖器 | 手、schlongs（SOS）也作为碰撞体参与 |
| NPC 多了卡 | 球体计算量小且与网格精度无关，**跑大量 NPC 开销可控** |
| 身形千差万别 | 碰撞球可配置（FOMOD 预设 / 第三方 `CBPConfig.txt` / PDF 指南手调） |

## 工作原理

- **球体近似**：胸/臀/腹/阴道（等部位，取决于身形节点）各挂一组球体，
  球体挂在骨骼上，随骨骼运动；
- **每帧实算**：作者强调这是动态物理模拟，**不是预计算动画或假物理**；
- **碰撞体**：NPC/玩家双手、schlongs（需 SOS SE/VR）；VR 版另支持 VR 手柄与
  装备武器；
- **节点依赖**：腹部与阴道碰撞要求身形有可用的 **Belly、Pelvis、Pussy 节点**；
- **原版身体不支持**：香草身体/护甲没有所需节点，**不能**获得物理。

## 安装

### 前置

```
SKSE64（或 SKSEVR）
XP32 Maximum Skeleton Special Extended（最新版）
FNIS 或 Nemesis（装完骨架/动画后跑一次）
```

**XPMSSE 的装法有讲究**：安装 XPMSSE 时**第一屏选 `Physics Extensions`，
其余全选 `None`**——CBPC 只需要骨架文件，**不需要 XPMSE 的脚本与 esp，可删**。
⚠️ 同时确保**没有任何东西覆盖这个骨架**（"Bad and weird stuff happens"）。

FNIS/Nemesis 跑时**勾选 `Skeleton Arm Fix`**——注意这是**动画 mod 的要求，
不是 CBPC 的要求**；不装动画 mod 可以不勾，但主流配置都会装。

### 物理身形（必需）

需要带 Breast-Butt-Belly(-Vagina) 节点的身体，官方列举：

| 身形 | 节点 | 备注 |
|---|---|---|
| CBBE SE Physics body | Breast-Butt | 需 BodySlide 构建 |
| CBBE SE Special body | Breast-Butt-Vagina | 需 BodySlide 构建 |
| UNP / UNPB | Breast-Butt-Belly | 有预构建身体与衣物 |
| Oldrim CosioHD / CBBE Special / UUNP | Breast-Butt-Belly-Vagina | 需 BodySlide 构建 |
| **CBBE 3BA / BHUNP**（3 乳骨） | 3BBB 节点 | FOMOD 里另有一组选项，见下 |

### 步骤与验证点

1. 装 SKSE64/SKSEVR、XPMSSE（Physics Extensions，其余 None）。
   - 验证点：骨架文件在位且未被覆盖。
2. 跑 FNIS/Nemesis（勾 Skeleton Arm Fix）。
3. 装物理身形并 **BodySlide 构建带物理的版本**。
   - 验证点：Outfit 下拉里出现带 Physics/3BBB 的身体项目。
4. **装 CBPC，FOMOD 里 SSE / VR 版本必须选对**（选错的典型表现是崩溃或不生效）。
   - 验证点：`Data\SKSE\Plugins\cbp.dll` 存在。
5. 按乳骨数选弹跳配置（见下）；进游戏看抖动。
   - 不抖按 [physics-not-working.md](../06-troubleshooting/physics-not-working.md) 排。

## 使用与配置

### 弹跳配置：1 乳骨 vs 3 乳骨

| 身形 | 配置来源 |
|---|---|
| **1 乳骨身形** | FOMOD 内 **10 种弹跳配置**；或第三方 `CBPConfig.txt`：**Sinful CBP**、**Immersive CBP Config**、**CBP Physics Config** 等（官方注明"兼容，可换用"）。作者建议选**更晃的配置**而非更稳的——碰撞更好玩 |
| **3 乳骨身形（CBBE 3BA / BHUNP）** | FOMOD 里**另一组选项**；Optional Files 里还有单独的 Bounce Config installer |

### 球体贴合身形

- 官方提供 **PDF 配置指南**，教怎么改碰撞球贴合自定义身形；
- 调参不生效的检查项见下文「排错」。

### 文件形态

- 主体 `cbp.dll`（SKSE 插件）；
- 文本配置 `CBPConfig.txt` 类（Sinful CBP / Immersive CBP Config 等即是）；
- ⚠️ **它覆盖 CBP**（同名 dll）：不需要、也不要同时装 CBP。
  如果你出于某种原因改过 dll 名，**更新前必须先删旧文件**，否则两个同名 mod
  冲突会崩溃。

## 兼容与冲突

| 关系 | 结论 |
|---|---|
| SOS SE / VR | 可选：把 schlong 作为碰撞体（penis collider） |
| CBP（原版） | **不要共存**：同名 dll，CBPC 覆盖它且已含其功能 |
| HDT-SMP / FSMP | 争同一批骨骼；**共存必做分腔**（见下） |
| Player Size Adjuster and First Person Camera Height Fix SSE | **不支持**（官方明列） |
| 香草身体/护甲 | 无对应节点，**不能**获得物理 |
| 3BA | 官方前置链要求 CBPC **1.5.1+**；3BA 的 FOMOD 有 "CBPC only" 档位 |

### 与 SMP 共存（必做步骤）

两者默认挂同一批骨骼（乳房/臀/腹），同时启用会**互相覆盖**。公认解法：

1. **编辑 SMP 的 `defaultBBPs.xml`**，让 SMP **忽略身体**、只管头发/衣服；
2. **把 `cbp.dll` 改名为 `zcbp.dll`**（利用 dll 加载顺序让 SMP 先加载），
   或用 Engine Fixes 的 preload 机制。

> 这是**社区经验**（LoversLab 多帖一致），但与"抢同一批骨骼"的机制吻合。
> 更完整的分腔逻辑见 [physics-overview.md](physics-overview.md)。

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 完全不抖 | 身形没有物理节点 / 没构建物理版 / XPMSE 没选 Physics Extensions | 换物理身形 + BodySlide 重建；XPMSE FOMOD 补选 |
| SSE/VR 装错崩溃或不生效 | FOMOD 版本选错 | 重装，SSE/VR 选对 |
| 改 `CBPConfig.txt` 不生效 | ① 角色体重是 0 或 100；② 被 SMP 覆盖（MCM 物理开关切错引擎）；③ 覆盖式文本配置在 MO2 左栏里**不在 CBPC/身形之下** | 逐项对照；查覆盖关系（[mo2-override-rules.md](../07-workflow/mo2-override-rules.md)） |
| 腹部/阴道不碰撞 | 身形缺 Belly/Pelvis/Pussy 节点 | 换带对应节点的身形 |
| 更新后崩溃 | 改名过的旧 dll 没删，两个文件冲突 | 删旧 dll 再更新 |
| 与 SMP "物理打架" | 没做分腔 | 按上文「与 SMP 共存」两步处理 |

## 取舍与建议

**选 CBPC 当你**：

- 主要想要**身体部位**物理（胸/臀/腹 + 碰撞）；
- 机器一般、或场景里 NPC 多（球体近似对 CPU 友好）；
- 用 3BA 且想留一条"低配退路"（3BA 支持 CBPC only 档位，甚至游戏内切换 SMP/CBPC）。

**CBPC + SMP 都装当你**：既要身体碰撞又要头发衣物物理——装，但记得分腔。

**只装 SMP 不装 CBPC 也可以**：身体会抖，但碰撞与"CPU 友好度"打折。

**不要**：同时装 CBP 与 CBPC；对香草身体期待物理；装 Player Size Adjuster…SSE。

## 来源

- **作者 Shizof、全称、基于 polygonhell 的 CBP Physics（MIT，"Big thanks to
  polygonhell…which allowed me to create this mod"）、"not Pre-Calculated or Fake
  Physics…uses spheres instead of vertices…Calculations are made every frame"、
  覆盖部位（胸/臀/腹弹跳 + 与手/schlongs 碰撞）、SSE/VR 差异（VR 手柄与武器碰撞；
  Belly/Vagina 需 Belly/Pelvis/Pussy 节点）、依赖链（SKSE64/SKSEVR + XPMSSE 最新版
  + 第一屏 Physics Extensions 其余 None 可删 esp + FNIS/Nemesis + Skeleton Arm Fix
  是动画 mod 的要求、物理身形清单（含"vanilla bodies cannot support physics"）、
  1 乳骨 10 种弹跳配置与第三方 CBPConfig.txt（Sinful CBP / Immersive CBP Config /
  CBP Physics Config，建议选更晃的）、3 乳骨（CBBE 3BA/BHUNP）另一组 FOMOD 选项与
  Optional Files 的 Bounce Config installer、覆盖 CBP 同名 dll、改名后更新须删旧文件、
  PDF 配置指南、性能设计哲学原话、版本 v1.6.1**：CBPC Nexus 21224 描述（经镜像站
  转载 v1.6.1 文件描述全文）—— **一手（经转载）**
  `https://www.nexusmods.com/skyrimspecialedition/mods/21224`
- **不支持 Player Size Adjuster and First Person Camera Height Fix SSE**：
  CBPC 发布页（经转述）—— **一手（经转述）**
- **3BA 前置链要求 CBPC 1.5.1+、"CBPC only" 档位、游戏内切换 SMP/CBPC**：
  Nexus 30174 描述（经 3DMGAME 转载）—— **一手（描述正文，经转载）**
  （见 [cbbe-3ba.md](../03-body/cbbe-3ba.md)）
- **"SMP better for outfits, CBPC better for body"、CBPC 不能管头发或衣服、
  `cbp.dll → zcbp.dll` 与 `defaultBBPs.xml` 分腔**：LoversLab 多帖一致 ——
  **社区经验（多帖一致）**
- **调参不生效三检查项（体重 0/100、被 SMP 覆盖、左栏顺序）**：CBPC 专帖与
  HDT-SMP 用户指南 —— **社区经验（多帖一致）**
- **CBPC 2018-11 发布（LoversLab 帖引用的发布 announcement）**：Nexus 论坛帖 ——
  **社区经验（转述发布帖）**
- **v1.6.1 之后是否有更新**：**未确认**（Nexus 页在成人墙后未能直读）
