---
id: xpmse-skeleton
title: XP32 Maximum Skeleton Special Extended（XPMSSE）
category: 04-physics
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [物理, 骨骼, XPMSE, XPMSSE, 节点]
aliases: [xp32, xpmsse 是什么, xpmss, 骨架, skeleton, 骨骼节点, 武器挂点, xpmse 安装, 怎么装 xpmsse, skeleton_female.hkx, xpmse 历史, xpmse 前缀, 骨骼家族, xpmse fomod]
source: https://www.nexusmods.com/skyrimspecialedition/mods/1988
summary: XPMSSE 百科全书：从 XP32 Maximum Skeleton 到 XPMSSE 的谱系、v5.06  changelog、四类骨骼节点前缀与 BBP/TBBP/3BBB 家族、为什么它是物理与身形的必装前置、与 RaceMenu 插件（武器样式/SOS/SAM 滑块）的关系、FOMOD 安装选项与 FNIS Skeleton Arm Fix，以及"绝不删 skeleton_female.hkx"这条硬警告。
---

# XP32 Maximum Skeleton Special Extended（XPMSSE）

> **一句话**：XPMSSE 是 Skyrim 角色骨骼的事实标准替换——物理引擎要挂的节点、
> 身形 mod 要写的骨骼、RaceMenu 要调的滑块，全都定义在它身上；**不装它，就没有现代物理**。

- 全称 **XP32 Maximum Skeleton Special Extended**（SE/AE 版）；
  前身 **XP32 Maximum Skeleton Extended（XPMSE）**（LE 版）。
- 团队 **Team XPMSE**；Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/1988`

## 速览

| 项 | 内容 |
|---|---|
| 全称 / 团队 | XP32 Maximum Skeleton Special Extended / **Team XPMSE** |
| Nexus | **1988**（SSE 页） |
| 谱系 | xp32 的 XP32 Maximum Skeleton → XPMSE（xp32 / groovtama）→ XPMSSE（为 SE/AE 重制） |
| 当前版本 | **v5.06（2024-02-11）**；v5.05（2023-12-09）起把 VampireLord 骨骼标记为 XPMSE 骨骼 |
| 前置 | SKSE64；**FNIS SE 7.2+ 或 Nemesis**（装完跑一次）；用其 RaceMenu 插件时需要 RaceMenu |
| 影响范围 | 全部物理（HDT-SMP/CBPC）、全部物理身形（3BA/BHUNP）、武器样式、身形缩放、ragdoll |
| 维护状态 | 低频更新、仍在维护（2024-02 后暂无新版，未确认是否停更） |

要点：

- **它是"接口"不是"功能"**：节点名（`HDT Belly`、`NPC L Breast01`…）是物理 mod 与
  身形 mod 之间的契约，改名即断链。
- 官方功能清单把 **BBP / TBBP / 3BBB / HDT-SMP / CBP / CBPC** 全部列为支持项——
  一套骨架喂饱所有物理方案。
- ⚠️ **不要删除 `skeleton_female.hkx`**（作者原话级警告，见下文）。
- 安装第一屏选 **Physics Extensions**；只用 CBPC 时其余可选 None，esp 可删。
- 装完必须跑 **FNIS/Nemesis 并勾 Skeleton Arm Fix**，否则动画 mod 可能出 T-pose 类问题。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 时代（具体年份未确认） | **xp32** 发布 **XP32 Maximum Skeleton** | 原版骨骼的第一个"最大扩展"：物理骨 + 武器插槽骨的集合 |
| LE 时代 | XPMSE 由 xp32 / groovtama 维护，成为 LE 物理生态基底 | BBP/TBBP/HDT-PE 时代的通用骨架 |
| SE 发布后 | **XPMSSE** 为 SE/AE 重制，团队接手为 **Team XPMSE** | 骨架与 SE 版本对齐，进入 4.x 时代 |
| 2019-12-28（v4.71） | 调整男骨架手部缩放为 1.0；新增 4.51V rig；**移除自带的 CBPC 设置**（改由其他 mod 提供） | 骨架与 CBPC 配置解耦的开始 |
| 2020-06-13（v4.72） | **移除 `Prebreast` 骨**（旧版 CBP 才需要，已冗余）；女骨架 ragdoll 约束调松；SOS 插件 43→44 并 esl 化 | 老教程里"CBPC 需要 Prebreast"的说法从此过期 |
| 2021-01-09（v4.80） | 补齐 `NPC R/L Item01~03` 骨 | 双持/多武器插槽节点完整 |
| 2023-08-17（v5.00） | **新安装器**；新增生物骨架；新增 "RaceMenu only" 选项 | 安装形态现代化 |
| 2023-12-09（v5.05） | 把 **VampireLord 骨架标记为 XPMSE 骨架**，避免 XPMSE 脚本 fail-safe 误触发 | 吸血鬼领主相关崩溃/异常的修复 |
| 2024-02-11（v5.06） | 生物骨架更新到 **ABC 3.10** | 当前版本 |

### 它从哪来

原版 Skyrim 骨架只有基本人物骨与少量附件骨，没有乳房/臀部/腹部物理骨，
武器也只有单一背部插槽。xp32 的 XP32 Maximum Skeleton 第一次系统性地补齐这些节点；
SE 重制版（XPMSSE）由 Team XPMSE 接手后，把这些节点变成了全社区约定的接口。

### 中间经历了什么

两条主线：**节点增减**（v4.72 删 Prebreast、v4.80 补 Item 骨）与**安装器演进**
（v5.00 重做 FOMOD，分出 RaceMenu only 选项）。删除节点的版本尤其要注意：
v4.72 之后还按老教程给 CBPC 配 `Prebreast` 会直接失效。

### 现状

v5.06（2024-02-11）之后暂无新版本（是否停更**未确认**）。它仍是**无完整替代品的
事实标准前置**：Pandora 行为引擎有 XPMSE 补丁，但骨架本身仍依赖 XPMSE；
ECE SE 自带一套骨架，官方标注为"兼容但不受支持"。

## 它解决什么问题

| 没有 XPMSE 会怎样 | 它怎么解决 |
|---|---|
| 物理引擎没有挂点：HDT-SMP 只认 XPMSE 的 human skeleton | 提供 `HDT *`、`NPC *` 全套物理骨 |
| 身形没有物理骨：3BA/BHUNP 的 3BBB 骨按这套命名写 | 提供 `NPC L/R Breast01` 等标准节点 |
| 武器只能背在背上一个位置 | 提供 `MOV` 系武器插槽骨 + RaceMenu 里调样式 |
| 缩放/姿势调整没有框架 | 内置 Realistic Ragdolls & Force、Flimsy Ragdolls，RaceMenu 插件提供缩放滑块 |

官方兼容清单（发布页列举）：NiOverride Pose Adjustments + Objects SE、Deadly Mutilation、
Ecotone Dual Sheath、Flimsy Ragdolls（内置）、Magic Nipple、Realistic Ragdoll and Force、
SAM、SOS、The Joy of Perspective、True Spear Combat 等。

## 骨骼节点：前缀与家族

社区说"骨骼节点"其实在说两套分类，分开记：

### 1. 节点名前缀（命名约定）

| 前缀 | 含义 | 例子 |
|---|---|---|
| **`NPC`** | 标准网格骨骼 | `NPC L Hand [LHnd]`、`NPC R Hand [RHnd]`、`NPC L/R Breast`、`NPC L/R Breast01`、`NPC Belly`、`NPC Pelvis [Pelv]`、`NPC Spine [Spn0]` |
| **`HDT`** | **HDT 专用运动骨**（物理挂点） | `HDT Belly`、`HDT LBreasts` 等 |
| **`MOV`** | 武器插槽节点 | `Weapon Left` / `Weapon Right`、`NPC L/R Item01~03` |
| **`CME`** | 额外 CME / RaceMenu 骨 | 由 RaceMenu / ECE 自定义数据设置 |

由此两条规则：

- **`HDT`/`MOV` 前缀的节点不要改名**——名字是接口（可以改位置/旋转）；
- **旧版 XML 里用 `NPC PreBelly` 是错的**：XPMSE 2.0+ 起该骨已改名 `HDT Belly`，
  用旧名会导致低 FPS 甚至 CTD。

### 2. 物理骨骼家族（按"几根骨"分组）

| 家族 | 全称 | 骨骼 |
|---|---|---|
| **BBP** | Breast and Butt Physics | `NPC L Breast`、`NPC R Breast`（每侧 1 根） |
| **TBBP** | Tender Breast and Butt Physics | BBP 的两根 + `NPC L Breast01`、`NPC R Breast01`（共 4 根） |
| **3BBB** | 3 Breast Bones Body | 每侧 3 根乳房骨（3BA 采用；注意 UUNP/BHUNP 的"3 根"节点与之不同） |
| 其它 | —— | 腹部（`NPC Belly` / `HDT Belly`）、臀部、骨盆等 |

> BBP/TBBP 今天不再是独立 mod，而是 XPMSE 骨骼里的节点名；它们的"动画驱动"历史见
> [物理方案总览](physics-overview.md)。3BBB 与身形的对应关系见
> [CBBE 3BA](../03-body/cbbe-3ba.md)。

## 与 RaceMenu 的关系（重要）

XPMSE 附带一个 **RaceMenu 插件（XPMSSE RaceMenu）**，捏脸界面里因此多出这些面板：

- **武器样式**（背挂/腰挂等，对应 `MOV` 插槽骨）；
- 缩放 / 位置 / 旋转滑杆（骨骼级）；
- 身形相关滑杆；
- **SOS / SAM 滑杆**；
- 兽人种族滑杆；
- 第一 / 第三人称缩放。

> 也就是说：**"RaceMenu 里怎么调武器位置 / SOS 大小"的答案在 XPMSE 的面板里**，
> 不是 RaceMenu 本体功能。要求 RaceMenu **0.4.2+**（LE 旧版 3.4.5+）。
> RaceMenu 本身见 [racemenu.md](../02-face/racemenu.md)。

## 安装

### FOMOD 选项（推荐选法）

| 界面 | 选项 | 说明 |
|---|---|---|
| Skeleton Meshes | 全选（含 Skeleton Meshes） | 骨架文件本体 |
| Animation Rig Map | **Physics Extensions** | **物理必选**；只装 CBPC 也选它（其余可 None） |
| Character Creation | **RaceMenu**（用 ECE 选 ECE；都不用选 None） | 决定装谁的捏脸框架插件 |
| Weapon Style Randomizer | None（按需） | 武器样式随机化 |
| Animation Variants（箭袋/匕首/剑等） | None（按需） | 武器佩戴样式 |
| First Person / Mounted Combat Animation | None（按需） | 第一人称/马战动画 |
| Compatibility Patches | 按需（SOS、Joy of Perspective 等） | 与对应 mod 联动 |

### 步骤与验证点

1. **前置**：SKSE64；如果之后要装动画/物理 mod，FNIS SE 或 Nemesis 二选一。
   - 验证点：MO2 里能看到 XPMSSE 模组，未被其他骨架 mod 覆盖（应只有绿色 +）。
2. **装 XPMSSE**，按上表选 FOMOD。
   - 验证点：`Data\meshes\actors\character\` 下出现 XPMSE 骨架文件，
     `skeleton_female.hkx` **在**（不许删，见下）。
3. **跑 FNIS for Users**（或 Nemesis），**勾选 `Skeleton Arm Fix`**。
   - 验证点：生成的行为文件出现在 overwrite；进游戏不开 T-pose。
   - ⚠️ Skeleton Arm Fix 是**动画 mod 的要求**，不是 CBPC 的要求；但既然要装物理
     基本都会装动画，一律勾上即可。
4. **进游戏开 MCM → XPMSE**，看自检是否通过（社区说法："Groovtama says you pass"）。
   - 不通过 → 有别的 mod 提供了冲突骨架/动画，查覆盖关系。
5. **装身形与物理**：[3BA/BHUNP](../03-body/cbbe-3ba.md) → [CBPC](cbpc.md) /
   [FSMP](faster-hdt-smp.md)，顺序见 [安装次序](../07-workflow/install-order.md)。

## ⚠️ 一条硬警告

> **不要删除 `skeleton_female.hkx`。**

游戏与多个 mod 假定该文件存在；老教程里"删女骨架省事"的说法已明确被作者否决，
删除会引发难以定位的问题（角色动作错乱、崩溃等）。

## 兼容与冲突

| 关系 | 结论 |
|---|---|
| 被其他骨架 mod 覆盖 | **大忌**："bad and weird stuff happens"；XPMSE 应只有绿色 + |
| ECE SE | 自带骨架，官方标注"兼容但不受支持"；与 XPMSE 二选一 |
| FNIS / Nemesis | 必须跑一次；装/卸任何动画或骨架后都要重跑 |
| Pandora 行为引擎 | 有 XPMSE 补丁，但骨架仍用 XPMSE |
| CBPC 1.5.1+ / HDT-SMP | 硬前置（见各条目） |
| 3BA | 要求 XPMSSE 4.61+（安装时选 Physics Extensions） |

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 角色 T-pose / 手臂腿外张 | FNIS 没跑或没勾 Skeleton Arm Fix | 重跑 FNIS for Users，勾 Skeleton Arm Fix |
| 物理不挂 / 完全不抖 | 装的是别的骨架，或 Physics Extensions 没选 | FOMOD 重装选 Physics Extensions；查骨架覆盖 |
| 低 FPS 甚至 CTD，日志指向某物理 XML | XML 用了旧骨名 `NPC PreBelly` | 改成 `HDT Belly`（XPMSE 2.0+ 起改名） |
| 吸血鬼领主相关异常 / fail-safe 触发 | XPMSSE 低于 5.05 | 升级到 5.05+（该版本起标记 VampireLord 骨架） |
| RaceMenu 里没有武器/SOS 滑块 | Character Creation 选了 None，或 RaceMenu 低于 0.4.2 | FOMOD 改选 RaceMenu；升级 RaceMenu |
| MCM 里 XPMSE 自检不过 | 随从/其他 mod 用了自定义骨架被检测到 | 定位冲突骨架 mod；查覆盖（[mo2-override-rules.md](../07-workflow/mo2-override-rules.md)） |
| 卸载后角色变形 | 卸载前没把 XPMSE MCM/插件里的滑块复位 | 重装并把所有 XPMSE 相关滑块回默认，再卸载 |

## 取舍与建议

- **只要装现代身形/物理，XPMSSE 就是必装**，没有"轻量替代"可言；
- **只用 CBPC 的极简配置**：第一屏仍选 Physics Extensions，其余 None，esp 可删
  （CBPC 只需要骨架文件本身）；
- **不用 RaceMenu 捏脸**也可以选 "RaceMenu only"（v5.00 起）之外的 Basic/Minimal
  档位，但社区主流仍是 RaceMenu 全选；
- **版本升级**：跨大版本（如 4.7x → 5.x）后重跑 FNIS，并检查依赖旧骨名的 XML 配置。

## 来源

- **全称、Team XPMSE、Nexus 1988、功能清单（BBP/TBBP/3BBB/HDT-SMP/CBP/CBPC 支持）、
  兼容清单、依赖（SKSE + FNIS SE / Nemesis + RaceMenu）、卸载步骤**：
  XPMSSE 发布页描述（经 LewdCorner 转载 v5.06 页全文）—— **一手（经转载）**
  `https://www.nexusmods.com/skyrimspecialedition/mods/1988`
- **v5.06（2024-02-11，生物骨架 ABC 3.10）、v5.05（2023-12-09，VampireLord 标记）、
  v5.04~v5.00、v4.81（CamSpin）、v4.80（Item 骨）、v4.72（移除 Prebreast、
  女骨架约束调松、SOS 43→44 esl 化）、v4.71（男骨架手缩 1.0、4.51V rig、
  移除自带 CBPC 设置）**：XPMSSE changelog（同上转载页）—— **一手（经转载）**
- **谱系 xp32 → XPMSE（xp32/groovtama）→ XPMSSE**：Nexus 页 credits 与社区史料 ——
  **一手（经转述）+ 社区经验**
- **四类节点前缀（NPC/HDT/MOV/CME）、`NPC PreBelly` → `HDT Belly` 及旧名导致
  低 FPS/CTD**：XPMSE 官方 FOMOD 说明（经 3DM 与俄站转述）—— **官方说明，经转述**
- **FOMOD 选项顺序（Skeleton Meshes → Physics Extensions；Character Creation 选
  RaceMenu/ECE/None）**：STEP 指南 XPMSE 页 —— **社区指南（与官方 FOMOD 一致）**
  `https://step-project.org/wiki/SkyrimLE:XPMS_Extended`
- **"Skeleton Arm Fix" 是动画 mod 的要求而非 CBPC 的要求；CBPC 安装 XPMSSE 时
  第一屏选 Physics Extensions、其余 None、可删 esp**：CBPC 发布页描述（经转载）——
  **一手（经转载）**
- **"不要删除 skeleton_female.hkx"**：XPMSSE 发布页粗体警告（经转载）—— **一手（经转述）**
- **FNIS 勾 Skeleton Arm Fix、T-pose 重跑 FNIS、MCM 自检 "pass"**：Nexus 论坛与
  社区指南 —— **社区经验（多帖一致）**
- **v5.06 之后是否有更新**：**未确认**（Nexus Files 页本轮未能直读）
