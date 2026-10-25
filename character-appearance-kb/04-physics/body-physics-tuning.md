---
id: body-physics-tuning
title: 身体物理调参完全指南（乳摇 / 臀抖 / 腹弹）
category: 04-physics
kind: tutorial
version: 1.0.0
updated: 2026-10-25
tags: [物理, 调参, 乳摇, CBPC, 配置, 碰撞球, 3BA]
aliases: [调乳摇, 奶摇, 乳摇参数, 晃动幅度, 身体物理调参, CBPConfig, 弹跳配置, 胸部晃动, 臀抖, 腹弹, 乳摇不生效, jiggle, 胸部物理, 身体晃动]
source: https://www.nexusmods.com/skyrimspecialedition/mods/21224
summary: 乳摇与身体物理的百科全书式调参指南：CBPC 配置体系全家福（CBPCMasterConfig / CBPConfig / CBPConfig_3b / 幅度文件 / 碰撞配置 / System.ini）、每个参数的含义与调节方向、源码定案的双值体重格式、条件配置与实时调参工作流、把乳摇调大的实战乘数、改配置不生效的完整排查。
---

# 身体物理调参完全指南（乳摇 / 臀抖 / 腹弹）

> **一句话**：上古卷轴5 里胸/臀/腹的一切"抖"都由模改引擎实时解算，
> 当代主流是 **CBPC**（身体）——它的全部旋钮都在 `Data\SKSE\Plugins\` 下的
> 几类文本配置里。本卷把每个文件、每个参数、每种调法讲透，并给出
> "把乳摇调大"的完整处方与"改了不生效"的排查树。

本卷是**操作层**手册：引擎怎么选、原理是什么，见
[物理方案总览](physics-overview.md)；CBPC mod 本身的前世今生与安装，见
[CBPC](cbpc.md)；完全不抖的排查，见[物理不生效](../06-troubleshooting/physics-not-working.md)。
本卷只管一件事：**配置已经装好了，怎么把它调成你想要的手感**。

## 速览

| 项 | 内容 |
|---|---|
| 调什么 | CBPC（`cbp.dll`）驱动的身体物理：胸（Breast）、臀（Butt）、腹（Belly）、腿（Thigh/Calf）、生殖器碰撞 |
| 在哪调 | `Data\SKSE\Plugins\` 下的 `CBPConfig*.txt`（弹跳参数）、`CBPCMasterConfig*.txt`（主控）、`CBPCollisionConfig*.txt`（碰撞球）、`CBPCSystem.ini`（性能） |
| 配置格式 | 别名制单值（`Breast.stiffness 0.05`）与逐骨骼**双值**（`ExtraBreast1L.stiffnessX 0.03 0.020` = 体重 100 值 + 体重 0 值，运行时按体重插值）两种 |
| 有无 MCM | **没有**。CBPC 不提供游戏内菜单；改文本配置 + 重启生效（或用 Tuning.rate 热重载，见下文） |
| 实时调参 | `Tuning.rate = 60`（每秒重载弹跳配置）/ `TuningMode = 1`（每 120 帧重载碰撞配置）——调完必须关回 0 |
| 游戏内工具 | [Physics Editor](#游戏内手段physics-editor-与自动重置)（切引擎 / 拟合碰撞球）、3BA 系身形的 MCM 物理开关 |
| 最大坑 | **同名文件冲突只有一个生效**（MO2 覆盖规则）；双值格式只改一个数 = 只改了对应体重 |
| 版本锚点 | CBPC v1.6.1（2026 年社区可确认）；配置解析逻辑以 1.5 系源码（MIT）核对，与官方文档一致 |

要点：

- **乳摇不是 SMP 管的**。HDT-SMP/FSMP 驱动头发/斗篷/服装；胸臀腹的弹跳与碰撞归
  CBPC。装了 SMP 胸部也会动（3BA 的 SMP 模式），但两条路线的手感、开销、
  可调项完全不同——本卷默认你走 CBPC 线。
- **"胸多大"和"怎么晃"是两层**：尺寸由身形预设（BodySlide/RaceMenu morph，如
  [CBBE 3BA](../03-body/cbbe-3ba.md) + [OBody NG](../05-distribution/obody-ng.md)）决定；
  晃动由本卷的弹簧/阻尼/幅度参数决定。换体型后碰撞球可能需要重新贴合。
- **所有参数都是"改了立刻知道对不对"的**：配合 Tuning.rate 热重载，调参不需要
  反复重启游戏（但有坑，见[实时调参工作流](#实时调参工作流tuningrate-与-tuningmode)）。
- **不要直接改原 mod 的文件**：装新 mod/更新会丢。做补丁 mod，放对 MO2 位置，
  见[安装与生效链](#安装与生效链改的文件为什么没生效)。

## 前世今生

调参这件事的历史，就是"身体物理配置格式"的演化史。

| 时间 | 事件 | 对调参的意义 |
|---|---|---|
| LE 早期（日期未确认） | **polygonhell** 发布 CBP Physics，后以 **MIT** 释出源码 | 奠基 `CBPConfig.txt` + `Tuning.rate` 实时调参范式（默认值故意调得很软，方便调试） |
| 2018-11 | **Shizof** 发布 **CBPC**（Nexus SSE 21224），在 CBP 源码上加碰撞 | 配置文件家族成型：`CBPConfig.txt` / `CBPCollisionConfig.txt` / `CBPCMasterConfig.txt` / `CBPCSystem.ini` |
| 2019-2020 | 与 CBBE 3BBB/3BA 生态互相成就 | 出现**逐骨骼**配置 `CBPConfig_3b.txt`（3BA 三乳骨 ExtraBreast1/2/3）与 3BA 专用节点映射 |
| CBPC 1.1.0 | 支持拆分配置文件 | **所有** `CBPConfig` 开头的 .txt/.ini 都会被加载，第三方配置可以按文件分发、即插即用 |
| CBPC 1.4.0 | 支持节点条件配置 | `Conditions = ...` + `Priority = ...`：按种族/姓名/ faction 给不同 NPC 不同弹跳 |
| CBPC 1.5.0 | 链式节点分组 `< >` + 空壳配置校验 | 3 乳骨这类链式骨骼可强制顺序执行防抖；"有条件没参数"的配置文件被忽略 |
| 2019-2026 | 第三方弹跳配置生态 | 官方页列举 **Sinful CBP / Immersive CBP Config / CBP Physics Config**；官方推荐参考 **avidichard 的 3BA Bounce Config Guide**；社区持续产出 Daddy Dubs / Niah / Petite to Plenty 等预设 |
| 2026-07-25 | **Physics Editor**（Nexus 186341，TwistedModding）上线 | 第一次有像样的游戏内物理编辑：切引擎、实时改配置、按蒙皮网格拟合碰撞球 |
| 2026 | CBPC **v1.6.1**（社区可确认）；FSMP 4.1.1 | "FSMP 头发衣物 + CBPC 身体"的双引擎分工定型 |

### 它从哪来

调参需求是引擎自带的：polygonhell 的 CBP 文档就写明"默认设置非常像果冻，
主要是为了方便看出什么没生效"，并给出 `Tuning.rate = 60` 的实时调参工作流——
**这个 mod 从第一天起就是设计成给你调的**。

### 中间经历了什么

两条线。**格式线**：从单文件全局值 → 按 `CBPConfig*` 前缀拆分的多文件 →
按部位/身形的专用文件（`_3b` / `_BBP` / `_butt` / `_leg` / `_SOS`）→ 条件配置。
**生态线**：官方 FOMOD 内置弹跳配置 → 第三方整份替换（Sinful CBP 等）→
整合包层面的预设叠加（多个 mod 各带一份同名配置，靠 MO2 覆盖决出胜者）。

### 现状

v1.6.1 之后 Nexus 页面是否有更新**未确认**（发布页在成人内容墙后，本轮未能直读；
版本号经镜像站转载的文件描述确认）。配置体系本身稳定，社区工作流成熟：
**改文本 + Tuning.rate 热重载 + Physics Editor 游戏内精修**。

## 它解决什么问题

**没有这套配置系统之前**：物理 mod 只有"装/不装"两个状态——引擎用一套写死的
参数驱动所有身材的所有人，结果是要么不晃，要么晃得离谱，且碰撞球与身材对不上
（乳房穿过手臂、腹部被穿透）。

**配置系统解决的四类问题**：

| 问题 | 对应配置 |
|---|---|
| 手感不对口（太硬/太软/余晃太长） | `CBPConfig.txt` / `CBPConfig_3b.txt` 的弹簧、阻尼、位移参数 |
| 碰撞球与身材不匹配 | `CBPCollisionConfig.txt` 的球体/胶囊坐标（可换预设或用 Nifskope/Physics Editor 拟合） |
| NPC 一多就卡 | `CBPCSystem.ini` 的距离/角度剔除、SkipFrames |
| 想给特定角色特定手感 | `Conditions = ...` 条件配置（按种族/姓名/faction） |

## 安装与生效链：改的文件为什么没生效

CBPC 的安装见 [cbpc.md](cbpc.md)，此处只讲**与调参直接相关的生效链**——
因为"改了配置没反应"的头号原因不是参数写错，而是**文件根本没被读到**。

### 安装顺序（每步附验证点）

1. **SKSE64**（版本与游戏一对一号）。
   验证：`Data\SKSE\Plugins\` 其它插件能加载。
2. **XPMSSE**，安装时第一屏选 `Physics Extensions`，其余全 `None`。
   验证：骨架文件在位且**没有任何 mod 覆盖它**。
3. **FNIS 或 Nemesis** 跑一次（动画 mod 的要求；Skeleton Arm Fix 按需勾）。
4. **物理身形**（如 3BA 的物理版）并 **BodySlide 构建**。
   验证：Outfit 下拉出现带 Physics/3BBB 的身体项目——没有这一步，
   后面所有参数都是无米之炊。
5. **CBPC**，FOMOD 里 **SSE/VR 版本选对**，弹跳配置按乳骨数选
   （1 乳骨身形一套，3BA/BHUNP 三乳骨另一套）。
   验证：`Data\SKSE\Plugins\cbp.dll` 存在；进游戏胸部会晃。
6. **第三方弹跳配置 / 自己的补丁**。
   验证：见下——这是最容易"装了像没装"的一步。

### 生效链规则一：同名文件，只有一个 mod 的生效

CBPC 只读**合并后的** `Data\SKSE\Plugins\` 目录。两个 mod 都带
`CBPConfig_3b.txt` 时，**优先级高的那份覆盖低优先级的**，不是合并、不是叠加。

- **MO2 优先级**：`modlist.txt` 里**越靠前优先级越高**（GUI 里越靠下越高，
  Overwrite 在最底压一切）。完整规则见
  [冲突解决](../../mo2-usvfs-kb/05-usage/conflict-resolution.md) 与
  [顺序问题](../../mo2-usvfs-kb/05-usage/warnings-and-order-problems.md)。
- **实操结论**：想让自己的补丁生效，把它放到**被覆盖目标的左侧/上方**
  （GUI 里更靠下、靠近 Overwrite）。整合包里"补丁 mod 压主件"的所有实例
  都是这个排法（本工作区实测：多个补丁-主件对的行序全部吻合）。
- **排查手段**：MO2 右栏的 `SKSE\Plugins\` 看每个文件的**来源 mod**；
  或直接在合并视图里确认你的文件是谁的。

### 生效链规则二：文件命名决定加载

源码定案（`config.cpp` 的 `loadConfig()`）：CBPC 启动时枚举
`Data\SKSE\Plugins\`，加载**所有**满足以下条件的文件——

- 前缀 `CBPConfig`（大小写不敏感，打不开时还会转小写重试一次）；
- 后缀 `.txt` 或 `.ini`。

推论（调参必知）：

- ✅ `CBPConfig_3b.txt`、`CBPConfig_我的调法.txt`、`CBPConfig.ini` 都会被加载；
- ❌ 叫 `MyBounceConfig.txt`（没有 CBPConfig 前缀）**不会**被加载——
  改了没反应的第一嫌疑；
- ❌ 文件不在 `SKSE\Plugins\` 根下（比如放进了子文件夹）不会生效；
- 多个文件都设了同一个参数时，后加载的覆盖先加载的——**别在五个文件里
  设同一个 `Tuning.rate`**，否则不知道听谁的（社区经验：统一只在
  `CBPConfig.txt` 里设）。
- 碰撞配置同理：`CBPCollisionConfig.txt` 之外的
  `CBPCollisionConfig_*.txt`（如 `_Female` / `_Yuriana`）按条件加载，
  见[条件配置](#条件配置conditions-与-priority)。

### 生效链规则三：双值格式——两个数分别管两种体重 ⭐ 源码定案

3BA 逐骨骼配置（`CBPConfig_3b.txt` 及 `_Gravity` / `_armor` / `_BBP` 等同族文件、
幅度文件）每行是**两个数**：

```
ExtraBreast1L.stiffnessX 0.03 0.020
```

**常见误解**：这是"参考值 + 生效值"（一些整理帖这么说）——**错的**。

源码定案（CBPC 1.5 系源码，MIT，`config.cpp` 的 `loadConfig()`）：

```cpp
if (tok0.size() > 0 && tok1.size() > 0 && tok2.size() > 0) {
    const float calcValue = atof(tok2.c_str());
    config[tok0][tok1] = calcValue;          // 第一个数 → config（100 体重）
    config0weight[tok0][tok1] = calcValue;
}
if (tok0.size() > 0 && tok1.size() > 0 && tok3.size() > 0) {
    config0weight[tok0][tok1] = atof(tok3.c_str());  // 第二个数 → config0weight（0 体重）
}
```

`Thing::updateConfig` 把两套值灌入 `*_100` / `*_0` 端点，
`updateConfigValues` 再按角色体重逐参数插值：

```cpp
actorWeight = CALL_MEMBER_FN(actorRef, GetWeight)();
stiffness = GetPercentageValue(stiffness_0, stiffness_100, actorWeight);
```

**正确解读**：

| 行 | 含义 |
|---|---|
| `ExtraBreast1L.stiffnessX 0.03 0.020` | 体重 100 的角色刚度 0.03；体重 0 的角色刚度 0.020；中间体重线性插值 |
| 只写一个数 `LBreast.stiffness 0.01` | 两种体重都用 0.01 |

**调参直接后果**：

- 想让**所有体重的角色**都用新值 → **两个数都改成新值**；
- 只改第一个数 → 只有体重 100 的角色变了，体重 0 的角色还是旧值；
- 想"瘦角色更晃、胖角色更挺" → 故意把两个数改成不同值（这是格式的设计用途）。
- 同理，**调试时把角色体重设为 0 或 100**：中间体重的生效值是插值结果，
  小改动可能看不出效果（社区经验，与源码插值机制吻合）。
- 别和碰撞球的权重格式搞混：碰撞球是 `x0,y0,z0,r0 | x100,y100,z100,r100`
  ——**0 在前、100 在后**；弹跳双值是 **100 在前、0 在后**。顺序相反。

> 体重 0/100 双值这套设计贯穿整个身型生态（BodySlide 预设、morph 也都是
> "体重 0 一个值、体重 100 一个值"），见
> [bodyslide-presets.md](../03-body/bodyslide-presets.md)、
> [morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)。

## 配置文件全家福

全部位于 `Data\SKSE\Plugins\`（MO2 合并视图）。**加粗**为最常见必改文件。

| 文件 | 管什么 | 格式 | 调参频率 |
|---|---|---|---|
| `cbp.dll` | 引擎本体（+ `cbp.pdb` / `cbpc.log`） | — | 不动 |
| **`CBPConfig_3b.txt`** | **3BA 三乳骨逐骨骼弹跳**（ExtraBreast1/2/3 L/R），乳摇主文件 | 双值 | ⭐ 最高 |
| `CBPConfig.txt` | 全局默认（别名制：Breast/Butt/Belly…）+ `Tuning.rate` | 单值 | 高 |
| `CBPConfig_3b_Gravity.txt` / `_MoreGravity` | 重力偏置/修正（倒立不下垂等） | 双值 | 中 |
| `CBPConfig_3b_armor.txt` | 穿衣时的胸部推挤（breastClothedPushup 等） | 双值 | 低 |
| `CBPConfig_BBP.txt` | 1 乳骨身形（BBP 骨骼，别名 LBreast/RBreast） | 双值 | 按身形 |
| `CBPConfig_belly.txt` / `_butt.txt` / `_leg.txt` / `_SOS.txt` | 部位专属覆盖 | 双值 | 按需 |
| **`CBPConfig_BreastAmplitude.txt`** | **胸部晃动总倍率**（另 Belly/Butt/Leg 各有） | 双值 | ⭐ 最高 |
| **`CBPCMasterConfig.txt`** | 主控：节点→别名映射、TuningMode、MalePhysics、链式节点排序 | ini 段 | 低（但关键） |
| `CBPCMasterConfig_3BA.txt` 等 | 分身的节点映射（3BA/SOS/Vagina/Anal） | ini 段 | 按身形 |
| **`CBPCollisionConfig.txt`** | 碰撞球/胶囊（胸/臀/腹/骨盆 vs 手/手指/生殖器）+ BellyBulge 等 | ini 段 | 高（换身形时） |
| `CBPCollisionConfig_Female.txt` / `_Yuriana.txt` | 碰撞配置变体（可带条件） | ini 段 | 按身形 |
| `CBPCSystem.ini` | 性能：SkipFrames、距离/角度剔除、日志 | ini 段 | 中 |
| `CBPCPlayerCollisionEventConfig.txt` | 碰撞事件节点（给脚本用） | ini 段 | 基本不动 |
| `CBPCBounceinterpolationconfig_*.txt` / `CBPCCollisioninterpolationconfig_*.txt` | 插值配置（切换条件配置时平滑过渡，作者示例名带 `_Test`） | 混合 | 高级 |
| `hdtSkinnedMeshConfigs\` | **SMP 侧**，不属于 CBPC | xml | 见 [FSMP](faster-hdt-smp.md) |

> 本清单与实装参数现值来自本工作区实测（一套装齐 CBPC + 3BA + 多个第三方预设的
> 整合包的 `SKSE\Plugins\` 原文）；不同安装的 FOMOD 选项会增减文件。

## 参数详解

### 坐标系与调参总原则

官方注释与社区指南一致：**X = 左右（side to side）、Y = 前后（front to back）、
Z = 上下（up and down）**。

社区指南（LoversLab《Annotated CBPConfig.txt》）给出的"症状→参数"速查：

| 症状 | 改什么 |
|---|---|
| 位移太短/太远（够不着/撞隐形墙） | `maxoffset` / `minoffset` |
| 使力太小/太大（起晃门槛） | `stiffness` |
| 太弹/太沉（弹簧感 vs 坠物感） | `timeStep` |
| 总晃动时间太短/太长（余晃） | `damping` |
| 某方向动得太少 | `linearX/Y/Z` |

### 全局参数（`CBPConfig.txt`，别名制）

文件头是官方使用说明（重点）：**别名（Breast/Butt/Belly）必须在
`CBPCMasterConfig.txt` 里先定义**；可建多个带 `Conditions` 的配置文件；
**至少要有一份不带条件的全量配置**当默认。

以下含义列为官方注释原文（中译），效果与调参建议为本卷整理：

| 参数 | 官方注释（原文要点） | 调大效果 | 乳摇调法 |
|---|---|---|---|
| `stiffness` | "Linear spring stiffness, higher is more jiggly" | 更"晃"、回弹更快 | **调小**→更软、小动作也晃得起来 |
| `stiffness2` | "Quadratic Spring stiffness, higher is more jiggly" | 同上（二次项，大位移时更明显） | 同上，配合 stiffness 一起调 |
| `damping` | "Velocity removed/tick. 1.0 would be all velocity removed" | 更快停下 | **调小**→余晃更久、停下后继续颤 |
| `X/Y/Zmaxoffset` | "Maximum number of units position can diverge from target" | 该方向位移上限更大 | **调大**→晃得更开（防撞隐形墙） |
| `X/Y/Zminoffset` | 同上（负方向） | 反方向位移下限 | 同上 |
| `timetick` | "Time Quanta for the physics in ms…Acts like inertia. Higher values make it keep its original position longer while moving" | 惯性更大、更"恋旧" | 小幅调大→更飘；太大发僵 |
| `linearX/Y/Z` | "Scale of the motion in X/Y/Z - Y is front to back, Z up and down and X side to side" | 该方向运动缩放 | **调大**→晃得更开；只想上下摇就调 `linearZ` |
| `linearXspreadforceY/Z` 等 | "Allows the force dissipated by min/maxoffsets to be spread in different directions" | 一边被限位后力改从另一边泄 | 高级；治"一边顶住后整体发僵" |
| `rotationalX/Y/Z` | "Scale of the bones rotation around the X/Y/Z axis" | 骨骼扭动更明显 | 小幅调大→晃动更"活" |
| `linearXrotationX/Y/Z` 等 | "Deliver the linear force to the wanted rotation" | 位移力转成旋转的比例 | 高级；让胸"甩"而不是"平移" |
| `timeStep` | "General physics speed. Increasing this makes all of the motion faster" | 整体变快 | 调大→晃得更急；过大易抖 |
| `collisionFriction` | "Physics deceleration by friction in collision" | 碰撞后减速更快 | 一般不动 |
| `collisionPenetration` | "Down the sensitivity of collisions / affects the actual colliding range" | 碰撞范围/灵敏度 | 调大→更容易触发碰撞（也更容易穿模） |
| `collisionMultipler` | "Push strength by collisions / doesn't affect the colliding range" | 被撞后的推力 | 调大→被撞开更远 |
| `collisionMultiplerRot` | "Rotation strength by collisions" | 被撞后的旋转 | 同上 |
| `collisionElastic` | "Add bounce by collisions but sometimes jitter can occur. 1 or 0" | 碰撞回弹 | 抖得烦就设 0 |
| `collisionX/Y/ZmaxOffset/minOffset` | "Limit the extent to which pushed by collisions" | 被碰撞推动的上限 | 调大→能被推得更远 |
| `Tuning.rate` | "Setting this to 60 would make CBPConfig files to load every 60 frames…0 turns it off. Don't leave this turned on for normal play!" | 实时调参开关 | 见专节 |

### 逐骨骼参数（`CBPConfig_3b.txt`）⭐ 乳摇主文件

3BA 身形有三节乳骨，CBPC 对**每一节、每一侧、每一根轴**单独调参。
节点名即 3BA 的骨骼名：

| 节点 | 位置 |
|---|---|
| `ExtraBreast1L` / `ExtraBreast1R` | 靠上的第一节（L=左 R=右） |
| `ExtraBreast2L` / `ExtraBreast2R` | 中间第二节 |
| `ExtraBreast3L` / `ExtraBreast3R` | 靠下的第三节（通常晃得最明显） |
| `LBreast` / `RBreast` | 1 乳骨身形（BBP 骨骼），在 `CBPConfig_BBP.txt` 里调 |
| `NPC L/R Butt`、`Belly`、`L/R FrontThigh`、`L/R RearThigh`、`L/R RearCalf` | 臀/腹/腿（别名映射见下） |

每个节点支持**全局参数的逐轴版**，外加旋转专用与碰撞专用：

| 参数族 | 例 | 说明 |
|---|---|---|
| 平移弹簧 | `stiffnessX/Y/Z`、`stiffness2X/Y/Z` | 各轴独立刚度 |
| 阻尼 | `dampingX/Y/Z` | 各轴独立阻尼 |
| 位移上限 | `X/Y/Zmaxoffset`、`X/Y/Zminoffset` | 各轴独立 |
| 旋转弹簧 | `stiffnessXRot/YRot/ZRot`、`stiffness2*Rot` | 绕各轴的扭动刚度 |
| 旋转阻尼/位移 | `damping*Rot`、`X/Y/ZmaxoffsetRot/minoffsetRot` | 同上 |
| 惯性/步长 | `timetick` / `timetickRot` / `timeStep` / `timeStepRot` | 平移与旋转分开 |
| 运动缩放 | `linearX/Y/Z`、`rotationalX/Y/Z` | 各方向幅度 |
| 力扩散 | `linearXspreadforceZ` 等 | 见上 |
| 碰撞 | `collisionX/Y/Zmaxoffset/minoffset`、`collisionFriction`、`collisionElastic`、`collisionMultipler(Rot)`、`collisionPenetration` | 与全局版同义，逐骨骼 |
| 重力 | `gravityBias`、`gravityCorrection` | 见下 |
| 穿衣 | `breastClothedPushup`、`breastLightArmoredPushup` | 见下 |

**重力参数**（`CBPConfig_3b_Gravity.txt` / `_MoreGravity`）：

- `gravityBias`：乳房质心相对骨骼根节点的前移量，改变旋转如何影响运动；
- `gravityCorrection`：重力系数补偿——重力会让胸从建模位置**下垂**，
  不想下垂就用 correction 补回来（CBP 0.2x 官方参数说明，社区转帖）。
- ⚠️ 这两个参数与"配置热重载"叠加会触发一个已知 bug，见
  [实时调参工作流](#实时调参工作流tuningrate-与-tuningmode)。

**穿衣推挤**（`CBPConfig_3b_armor.txt`）：`breastClothedPushup`（衣服）、
`breastLightArmoredPushup`（轻甲）等——穿着不同装备时胸部的基础姿态偏移。

### 幅度文件（Amplitude）

`CBPConfig_BreastAmplitude.txt`（胸）、`_BellyAmplitude` / `_ButtAmplitude` /
`_LegAmplitude`——**整节点的总倍率**，不动其他参数的前提下整体缩放晃动：

```
ExtraBreast1L.amplitude 1.0 1.0     ← 同样是双值（100 体重 / 0 体重）
ExtraBreast2L.amplitude 1.0 1.0
...
Breast.amplitude 1.0 1.0            ← 别名级总倍率
```

**这是最安全的"整体调大/调小"旋钮**：想让乳摇整体放大 30%，
把所有 `amplitude` 两个数都改成 1.30 即可，不动弹簧就不会引入抖动/穿模风险。

### 主控配置（`CBPCMasterConfig.txt`）

三件事：

**① `[Settings]`**：

| 项 | 含义 |
|---|---|
| `TuningMode` | 0=关；1=每 120 帧重载**碰撞**配置；2=每 240 帧……用于游戏内改碰撞球 |
| `MalePhysics` | 0=男性角色**自动禁用女性专用骨骼**（源码 `SimObj.cpp` 定案：breast/butt/belly/pelvis 及名字含 breast/thigh/calf 的节点全部跳过）；1=启用男性身体弹跳（与 collider 无关） |
| `NoJitterFixNodes` | 不应用抖动修复的节点名单（兼容用） |

**② `[ConfigMap]` 节点→别名映射**：语法
`节点名 = 弹跳配置别名 = 条件`。官方示例：

```
NPC L Breast=Breast=IsFemale()
NPC R Breast=Breast=IsFemale()
NPC L Butt=Butt=IsFemale()
NPC R Butt=Butt=IsFemale()
HDT Belly=Belly=IsFemale()
```

3BA 身形则需要 3BA 专用映射（如整合包实测的 `CBPCMasterConfig_3BA.txt`）：

```
NPC L Breast=LBreast=IsFemale()
L Breast01=ExtraBreast1L=IsFemale()     ← 3BA 三节乳骨
L Breast02=ExtraBreast2L=IsFemale()
L Breast03=ExtraBreast3L=IsFemale()
NPC Belly=Belly=IsFemale()
NPC L FrontThigh=LFrontThigh=IsFemale()
...
```

**映射是调参的前提**：`CBPConfig_3b.txt` 里写的 `ExtraBreast1L.*` 能生效，
正因为某份 `CBPCMasterConfig*.txt` 把 `L Breast01` 映射到了 `ExtraBreast1L`。
**映射错了/被别的 mod 覆盖了，你在 3b 文件里改的天花乱坠也没用。**

**③ `< >` 链式节点顺序执行**：3 乳骨、SOS 阴茎这类链式骨骼并行处理会抖，
用 `<` `>` 包住一组强制从上到下顺序加载：

```
<
L Breast01=ExtraBreast1L=IsFemale()
L Breast02=ExtraBreast2L=IsFemale()
L Breast03=ExtraBreast3L=IsFemale()
>
```

官方警告：`<` `>` 里别放太多节点，会损失并行处理的性能收益。

### 碰撞配置（`CBPCollisionConfig.txt`）

**碰撞球是 CBPC 碰撞的全部**——写死的球体坐标（节点局部空间），
不随身材 morph 自动适配。换体型/预设后不贴合是常态，解法见
[Physics Editor 拟合](#游戏内手段physics-editor-与自动重置)或下面的 Nifskope 流程。

**结构**：

```
[ExtraOptions]        # 特殊选项
[PlayerNodes]         # 预定义（删了就没碰撞）
[AffectedNodes]       # "被推"的节点：胸/臀/腹/骨盆/脊椎1
[ColliderNodes]       # "推人"的节点：双手、十指、生殖器
[各节点名]            # 球体/胶囊坐标
```

**`[ExtraOptions]`**（官方注释中译）：

| 项 | 含义 |
|---|---|
| `BellyBulge` | 阴道穿透时腹部隆起的倍率；0=关闭 |
| `BellyBulgeMax` / `BellyBulgePosLowest` / `BellyBulgeSpeed` | 隆起的水平上限/垂直位置/回弹速度 |
| `BellyBulgeNodes` / `...BlackList` | 参与/排除腹部隆起的节点白/黑名单 |
| `VaginaOpeningMultiplier` / `Limit` | 阴道张开倍率与上限 |
| `AnusOpeningMultiplier` / `Limit` | 肛门张开倍率与上限 |

**`[AffectedNodes]` 排除语法**（官方注释）：`节点名 (排除碰撞体1, 排除碰撞体2)`；
`@` = 所有自身节点；`节点名 (@ColliderName)` 之类组合。

**球体格式**（0 体重值在前，100 体重值在后，`|` 分隔）：

```
[NPC L Breast]
0.0,5.0,-2.0,3.0 | 0.0,7.0,-4.0,4.0        ← x,y,z,半径 @体重0 | x,y,z,半径 @体重100
```

**胶囊格式**（两个端点用 `&` 连成一个胶囊）：

```
[NPC Genitals01 [Gen01]]
0,0,0,1.75 & 0,7.5,0,1.5 | 0,0,0,1.75 & 0,7.5,0,1.5
```

**武器碰撞体**：可按武器类型定义，也可用游戏内名称（官方指南经转载）：
`[铁剑]` 下写 `0,63,0 | -3,4,0 | 3,4,0`（三点定义三角形碰撞）。

**改碰撞球贴合身材的官方方法**（CBPC 页 PDF 指南，社区转录）：

1. Nifskope 打开 `femalebody_0.nif` / `femalebody_1.nif`
   （`meshes\actors\character\character assets\`），**别保存**；
2. 找到 `NPC L Breast` 等节点（黄点），在该节点下挂嵌套 NiNode 当参照；
3. 量出乳房中心相对节点的 x/y/z 与半径，写进配置（体重 0/100 各一套）；
4. 一般只需改 Breast/Butt 两组球，Belly/Pelvis 调半径即可
   （官方指南原话："That's usually all it takes"）。

**针对性修复实例**（作者 Shizof 在 LoversLab 原帖）：腹部被 schlong 穿透 →
把 `[HDT Belly]` 球改成 `0,-2,-12.0,4.0 | 0,-2,-12.0,4.0`，并把
`Belly.maxoffset` 提到 4~5。

### 性能配置（`CBPCSystem.ini`）

| 项 | 默认 | 含义 |
|---|---|---|
| `SkipFrames` | 0 | 跳帧；CPU 吃紧可设 1-2，动画变粗、高值可能出 bug |
| `SkipFramesPelvis` | 1 | 骨盆单独跳帧（计算量小，可减小换更平滑） |
| `GridSize` | 25 | 空间哈希格大小。**别乱动**：小了抖/碰撞失败，大了精度高但性能大降 |
| `ActorDistance` | 1024 | 超出距离的 actor 忽略碰撞 |
| `ActorBounceDistance` | 2048 | 超出距离的 actor 忽略弹跳与碰撞（官方建议留 4096；纯弹跳很便宜） |
| `ActorAngle` | 360 | 超出角度的 actor 忽略；360=不限制；0=只有玩家有物理 |
| `UseCamera` | 0 | 用相机位置/朝向判定 ActorAngle；与某些自由相机 mod 冲突时设 0 |
| `FpsCorrection` | 0 | 让晃动量与 FPS 无关（低 FPS 可能显得一顿一顿） |
| `InCombatActorCount` | 20 | 战斗中按距离处理的前 N 个 actor |
| `OutOfCombatActorCount` | 40 | 非战斗中前 N 个 |
| `Logging` | 0 | 1=写 `SKSE\CBPC-Collision.log`（掉性能、文件巨大，调试完关掉） |
| `HapticFrequency` / `HapticStrength` | 10 / 1 | VR 震动 |

**"只有远处 NPC 不抖"**：先看这三个（ActorDistance/ActorAngle/UseCamera）——
是性能设计，不是 bug。

## 条件配置：Conditions 与 Priority

想给特定 NPC/种族不同手感，用带条件的配置文件（1.4.0+）：

```
Conditions = IsFemale() AND IsRaceFormId(13745) OR IsRaceFormId(13740)
Priority = 100
```

**语义（源码定案，`ParseConditions`）**：先按 `AND` 拆、再按 ` OR ` 拆——
即 **AND 绑定比 OR 紧**（与 CK 语法一致）。`A AND B OR C` = `A AND (B OR C)`。
支持 `NOT` 前缀否定。

**条件函数**（源码 `DecideConditionType` + 官方文档经转载）：
`IsRaceFormId(esp名\|000000)` / `IsRaceName(string)` / `ActorName(string)` /
`ActorFormId(...)` / `IsInFaction(...)` / `IsPlayerTeammate()` / `IsFemale()` /
`IsMale()` / `IsPlayer()` / `HasKeywordId/Name(...)` / `RaceHasKeywordId/Name(...)` /
`IsActorBase(...)` / `IsUnique()` / `IsVoiceType(...)` / `IsCombatStyle(...)` /
`IsClass(...)`。FormID 带 esp 名 `(esp名|000000)`，主文件可省略 `(00000000)`。

**生效规则**：

- 同优先级按 `Priority` **降序**；同级则 **AND 条件项更多者（更具体）优先**；
  遍历返回**第一个条件全过的**配置（源码 `compareBounceConfigs` +
  `GetSpecificNPCBounceConfigForActor`）。
- **空壳校验（1.5.0+，源码 `IsConfigActuallyAllocated`）**：条件配置必须真的改了
  参数才算数——`stiffness`/`stiffness2`/`damping` 任一 ≥ 0.0001，或六个
  `collision*offset` 任一偏离 ±100；否则该配置被**静默忽略**。
  （想用"空条件配置"禁用某 NPC 的弹跳？至少设一个上述参数。）
- **带条件的配置必须自带全部设置**（官方警告）：不能把一套参数拆到多个
  同条件文件里。
- 碰撞配置的条件文件（`CBPCollisionConfig_*.txt`）另有
  `[Options]` 段的 `Conditions` / `Priority` / `Characters`（转成一组 ActorName OR）/
  `Races`（转成一组 IsRaceName OR）。

## 实时调参工作流：Tuning.rate 与 TuningMode

CBPC 支持**不重启游戏**看调参效果（官方文档工作流，社区多帖一致）：

1. 打开 `CBPConfig.txt`（或目标配置末尾），设 `Tuning.rate = 60`
   （每 60 帧≈1 秒重载弹跳配置）；
2. 进游戏，** Alt-Tab 出去改文件、保存**，1-2 秒内见效；
3. 调满意后把 `Tuning.rate` 设回 **0**——官方原话：
   "Don't leave this turned on for normal play!"

- 改**碰撞球**：在 `CBPCMasterConfig.txt` 设 `TuningMode = 1`（每 120 帧）或
  `2`（每 240 帧），同样调完归 0。
- **多文件都设 `Tuning.rate` 时不知道听谁的**（社区经验）：统一只在
  `CBPConfig.txt` 设一处。

⚠️ **必踩的坑：胸部周期性"抽搐/重置"**（社区经验，LoversLab CBBE 3BBB 帖）：
3BA 配置用了 `gravityBias` / `gravityCorrection`，**配置被周期性重载时重力参数
重置再循环**，表现为胸部隔一会就抽搐一下。**解法：调完参立刻把
`Tuning.rate` 和 `TuningMode` 都关回 0**——该帖多人确认"关掉 tuning mode 后
问题消失"。

## 实战：把乳摇调大、调软、调灵敏

以下处方默认你在改 `CBPConfig_3b.txt`（3BA）与
`CBPConfig_BreastAmplitude.txt`；**双值格式的两个数都要改**。

### 目标 → 参数对照表

| 想要 | 参数 | 方向 | 风险 |
|---|---|---|---|
| 整体幅度放大 | `amplitude`（幅度文件） | 1.0 → 1.2~1.4 | 最小；优先动它 |
| 小动作也晃得起来（降低起晃门槛） | `stiffnessX/Y/Z`、`stiffness2*` | **调小**（如 ×0.8） | 过软会"垂着"不动 |
| 晃得更开 | `linearX/Y/Z` | 调大（如 ×1.2）；上下摇重点 `linearZ` | 配合 maxoffset |
| 位移不撞"隐形墙" | `X/Y/Zmaxoffset`、`minoffset` | 调大（如 ×1.4） | 过大→穿模 |
| 余晃更久、停下继续颤 | `dampingX/Y/Z`（含 Rot） | **调小**（如 ×0.85） | 过小→抖个不停 |
| 扭动更明显 | `rotationalX/Y/Z` | 小幅调大（如 ×1.15） | 过大姿态诡异 |
| 晃动更快更急 | `timeStep` | 调大 | 过大→jitter |
| 更"飘"、恋旧 | `timetick` | 调大 | 过大发僵 |
| 倒立/翻腰时不下垂 | `gravityBias`/`gravityCorrection`（_Gravity 文件） | 按需 | 见抽搐坑 |

### 实例：一套"约两倍幅度"的乘数（本工作区实测用过）

以原配置为基准，整文件按乘数变换（两个数同乘，保持体重 0/100 的相对差）：

| 参数 | 乘数 |
|---|---|
| `amplitude` | 1.0 → 1.30 |
| `linearX/Y/Z` | ×1.20 |
| `rotationalX/Y/Z` | ×1.15 |
| `stiffness` / `stiffness2`（各轴） | ×0.80 |
| `stiffness*Rot` | ×0.85 |
| `damping`（含 Rot） | ×0.85 |
| `X/Y/Zmaxoffset` / `minoffset` | ×1.40 |
| `*offsetRot` | ×1.35 |
| `timetick` / `timeStep` / 碰撞 / `gravity` | **不动**（动了容易抖/穿模） |

效果：合计幅度约原来的 1.8~2 倍，起晃门槛明显降低。
**过了头**的表现与回退：胸部穿模/抖 → amplitude 回到 1.15、linear ×1.1、
stiffness ×0.9；还嫌不够猛再 amplitude 1.45、linear ×1.3、stiffness ×0.72
（再过头基本一定穿模，适可而止）。

### 为什么不是"只调大一个参数"

弹簧物理是耦合系统：只调大 `linearZ` 不改 `maxoffset`，位移很快撞上限；
只调软 `stiffness` 不改 `damping`，余晃会拖得发腻。**成套地调、小步迭代**
（每步 10-20%，配合 Tuning.rate 立刻看效果）。

### 各部位调参入口速查

| 部位 | 主文件 | 别名/节点 |
|---|---|---|
| 胸（3BA） | `CBPConfig_3b.txt` + `CBPConfig_BreastAmplitude.txt` | `ExtraBreast1/2/3 L/R` |
| 胸（1 乳骨） | `CBPConfig_BBP.txt` | `LBreast` / `RBreast` |
| 臀 | `CBPConfig_butt.txt` + `CBPConfig_ButtAmplitude.txt` | `NPC L/R Butt` → `Butt`/`LButt` |
| 腹 | `CBPConfig_belly.txt` + `CBPConfig_BellyAmplitude.txt` | `Belly` / `HDT Belly` |
| 腿 | `CBPConfig_leg.txt` + `CBPConfig_LegAmplitude.txt` | `L/R FrontThigh`、`L/R RearThigh`、`L/R RearCalf` |
| 生殖器（SOS） | `CBPConfig_SOS.txt` 等 + `CBPCMasterConfig_SOS.txt` | `Genitals01` 等 |

> 注意：某个文件能生效，**既要在 MO2 里压过别人，也要有对应的节点映射**
> （`CBPCMasterConfig_*.txt` 里把骨骼名映射到该别名）。整合包里常见的排面是：
> 一个"乳摇增强"mod 提供全套 3BA 文件 + 映射，另一个主 CBPC mod 提供 dll，
> 第三方预设补主控映射——缺了谁那一层就不生效。

## 游戏内手段：Physics Editor 与自动重置

### Physics Editor - CBPC - HDT-SMP（Nexus 186341）

TwistedModding 的 SKSE 插件（2026-07-25 首发，已更到 1.4），
**不装 esp、不占装备槽、不挂脚本**，靠 CBPC/FSMP 自身 API 干活：

| 能力 | 说明 |
|---|---|
| 切引擎 | `iMode`：0=CBPC，1=SMP（FSMP），2=Off，3=Hybrid |
| Hybrid | 按部位组（Breasts/Butt/Belly/Legs/Genitals）**各选一个引擎**，默认胸臀腹走 SMP、腿与生殖器走 CBPC；两组永不驱动同一根骨 |
| 控制台 | `physicseditor actor <mode>`——给单个 actor 临时切模式 |
| 停/起 CBPC 节点 | `bControlCBPC`：通过 **CBPC 自己的 Papyrus API**（3BA 系 mod 同款调用）按模式停/起身体节点 |
| 拟合碰撞球 | `bFitColliders`：读取该 actor 的蒙皮网格，按节点实际带权顶点**运行时生成碰撞球**（1.3 新增；每个节点少于 12 个带权顶点则保持原配置球）。**实验功能**，默认关 |
| NPC 管理 | `bNpcManager`：把超出 FSMP 预算的远处 NPC 降级到 CBPC（**实验**，官方警告忙乱场景有动画图崩溃风险） |
| GUI 配置编辑器 | 需要 **FLICK**（Nexus 181603，Fuzzlesz/powerofthree 的 ImGui 菜单框架；本机 mod 自带 ini 注释把框架名拼成 "FUCK menu framework"——笔误）。带参数说明的滑块、实时应用、自动备份到 `Data\SKSE\Plugins\PhysicsEditor\backups\` |
| 热键 | `iToggleKey` / `iOffKey`（DirectX scancode，无 GUI 时用） |

**没装 FLICK 时的用法**：改 `PhysicsEditor.ini` 的 `iMode`，或控制台
`physicseditor actor <mode>`。**换大体型预设后碰撞不贴合**，优先试
`bFitColliders = true`（配合 `bShowColliders = true` 可视化检查），
比手搓 Nifskope 快得多。

**依赖与限制**（官方页）：SKSE64 2.0.18+ / Address Library；支持
SE 1.5.97 与 AE 1.6.x；**不支持 VR**；带 SMP 数据的身体/装备不受影响。

### 自动物理重置（Auto Physics Reset）

物理卡住/抽搐时的急救：**F10 开关功能、F12 手动重置**（本工作区实测的整合包含此 mod）。
先试这个，再怀疑配置。

### 3BA 系身形的 MCM 物理开关

3BBB/CBBE 3BA 的 MCM 里有"Player 3BBB Physics Toggle Hotkey"之类的
CBPC/SMP 切换（社区经验，LoversLab 多帖）；3BA FOMOD 也有 "CBPC only" 档位
（见 [cbpc.md](cbpc.md)、[cbbe-3ba.md](../03-body/cbbe-3ba.md)）。
**切错引擎 = "我的 CBPC 配置没反应"**——排查链里别忘了这一环。

## 兼容与冲突

| 关系 | 结论 |
|---|---|
| HDT-SMP / FSMP | 争同一批骨骼；共存必须分腔（`defaultBBPs.xml` 让 SMP 忽略身体 + `cbp.dll` 改名 `zcbp.dll` 或 Engine Fixes preload）。详见 [physics-overview.md](physics-overview.md) |
| CBP（原版） | **不共存**：同名 dll，CBPC 已含其功能 |
| 改名 dll 后更新 | 先删旧 dll 再更新，否则两个同名文件冲突崩溃 |
| RaceMenu morph | morph 改节点位置 → 影响碰撞计算（官方描述经转载："可能与 Racemenu 变形不兼容"）——不是硬不兼容，但撞车时想到它 |
| Realistic Ragdolls and Force | **不兼容**：覆盖 XPMSE 骨架，CBPC 依赖原版骨架周期 |
| Dragonfly bbp | **不兼容**：动画式"假胸"老方案，卸掉 |
| Player Size Adjuster and First Person Camera Height Fix SSE | **不支持**（官方明列） |
| 香草身体/护甲 | 无物理节点，**不能**获得物理 |

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 改配置完全不生效 | ① 文件没被加载（不在 `SKSE\Plugins\` 根 / 没 `CBPConfig` 前缀）② 被别的 mod 同名覆盖（查 MO2 来源）③ 双值只改了一个数（对应体重没变）④ 体重非 0/100（插值掩盖小改动）⑤ SMP/3BA MCM/Physics Editor 正在驱动同一节点 | 按序对照；热重载开着时改错文件也会"没反应" |
| 胸部周期性抽搐/重置 | `Tuning.rate` / `TuningMode` 没关 + 3BA 的 gravityBias/gravityCorrection 被周期重置 | 全部关回 0，重启 |
| 碰撞球不贴合身材 | 配置球是写死的；换预设/morph 后必然对不上 | `bFitColliders`；或按 Nifskope 流程手测；或换带匹配碰撞配置的预设包 |
| 腹部被穿透/没有隆起 | Belly 球太小 / `Belly.maxoffset` 太小 / BellyBulge 为 0 | 按作者帖改 `[HDT Belly]` 球 + maxoffset 4-5；需要隆起时开 `BellyBulge` |
| 调大后穿模 | maxoffset/collisionPenetration/球半径过大 | 回调幅度；`collisionElastic=0`；球半径 ×0.9 左右 |
| 物理发抖（jitter） | timeStep/timetick 过大；链式节点没排序；collisionElastic | 回调步长；映射加 `< >`；关 Elastic |
| 条件配置不生效 | 空壳校验没过（没设 stiffness/damping/collision*offset）；AND/OR 语义搞反；Priority 比别人低 | 补齐参数；记牢 AND 先于 OR；提 Priority |
| 男性角色胸部在抖 | `MalePhysics=1` 被误开 | 改回 0（0 = 男性自动跳过女性专用骨） |
| 只有远处 NPC 不抖 | ActorDistance/ActorAngle/UseCamera 剔除 | 性能设计；按需放宽 |
| 开局 CTD | 改名过的旧 cbp dll 没删；FOMOD 版本档选错 | 删旧 dll；重选版本档 |

## 取舍与建议

- **先套预设，再微调**：Sinful CBP / Daddy Dubs / Niah 这类整份配置是免费的
  调参起点；在其基础上用补丁 mod 小幅覆盖，比从零手搓所有参数快得多。
- **补丁 mod 的正确姿势**：新建空 mod，只放你要改的那几个文件，
  MO2 里放到被覆盖目标的**更高优先级侧**（GUI 更靠下）。
  永远别直接改原 mod 的文件——更新即丢，且坏了没法回溯。
- **优先动 amplitude，其次 linear/damping，慎动 stiffness/timeStep**：
  前者是线性缩放，后者进耦合系统，副作用难预测。
- **性能敏感先调 `CBPCSystem.ini`**（ActorDistance/Count/SkipFrames），
  不要靠把参数全调小来"省性能"——那只会得到一具不会晃的尸体。
- **调完必做**：`Tuning.rate = 0`、`TuningMode = 0`、`Logging = 0`。
- **版本敏感**：整条链绑游戏版本（SKSE 一对一号），见
  [version-matrix.md](../00-overview/version-matrix.md)；升级
  1.7.x 前先确认各插件适配状态（[1.7.x 冲击](../00-overview/game-version-1-7-x.md)）。
  本卷结论锚定 CBPC v1.6.1；v1.6.1 之后的更新**未确认**。

## 来源

- **双值格式 = 体重100/体重0 两套值 + 按 actorWeight 逐参数插值**
  （`config.cpp` 的 `loadConfig()`：tok2→`config`（100）、tok3→`config0weight`（0）；
  `Thing::updateConfig/updateConfigValues`：`GetPercentageValue(v0, v100, actorWeight)`；
  碰撞球同样按体重插值）、**`CBPConfig*` 前缀 + `.txt/.ini` 的文件发现规则**、
  **Conditions 先拆 AND 再拆 OR + NOT 前缀、条件函数清单、Priority 降序/AND 多者优先/先匹配先得**、
  **1.5.0 空壳校验 `IsConfigActuallyAllocated`**、**`MalePhysics=0` 时男性跳过
  breast/thigh/calf 等节点**、**`< >` 链式顺序执行及其性能警告**、
  **`Tuning.rate` → `configReloadCount`**：CBPC 1.5 系源码（Discrim0/CBPC-1.5-AE-AS，
  基于 CBPC 页提供的 MIT 源码）—— **一手（源码）**
  `https://github.com/Discrim0/CBPC-1.5-AE-AS`
  （原源码自 CBPC Nexus 页下载；1.6.1 与 1.5 系的逐行差异**未逐行核对**，
  但下述官方文档描述的同一版本史与行为与此源码一致）
- **参数注释（stiffness/damping/offsets/timetick/linear/rotational/timeStep/
  collision*/Tuning.rate 的官方定义）、"至少要一份无条件全量配置"、
  1.1.0 拆分文件、1.4.0 条件配置、1.5.0 链式分组与空壳校验、
  Tuning.rate=60 实时调参工作流、Nifskope 拟合碰撞球指南、FOMOD 与弹跳配置、
  Sinful CBP / Immersive CBP Config / CBP Physics Config、avidichard 3BA Bounce
  Config Guide、与 RRF/Dragonfly bbp/Player Size Adjuster 不兼容、
  "可能与 RaceMenu 变形不兼容"、武器碰撞体按名称/类型定义**：
  CBPC Nexus 21224 发布页描述与页内 PDF 指南（页面在成人内容墙后，
  经 3DMGAME/aqxaromods 等镜像站转载 v1.6.1 文件描述全文）—— **一手（经转载）**
  `https://www.nexusmods.com/skyrimspecialedition/mods/21224`
- **`gravityBias`（乳房 COG 前移量）与 `gravityCorrection`（重力系数/下垂补偿）
  的语义**：CBP 0.2x 官方参数说明（巴哈姆特转帖）—— **一手（经转述）**
- **调参"症状→参数"四问（maxoffset/stiffness/timestep/damping）与坐标系
  X=水平/Y=深度/Z=垂直**：LoversLab《Annotated CBPConfig.txt》（2019-09-22）
  —— **社区经验（单帖，但与官方注释互相印证）**
- **TuningMode=2 + `#Tuning.rate 240` 工作流、体重 0/100 调试、3BBB MCM
  "Player 3BBB Physics Toggle Hotkey"、多文件 Tuning.rate 统一放一处、
  " belly 被穿透 → 改 [HDT Belly] 球 + Belly.maxoffset 4-5"**：
  LoversLab Petite to Plenty 配置帖 —— **社区经验（单帖，机制吻合）**
- **"Tuning 周期重载 + gravityBias/gravityCorrection → 胸部抽搐重置，
  关闭 TuningMode/Tuning.rate 后消失"**：LoversLab CBBE 3BBB Advanced 帖
  （2020-03，多人确认）—— **社区经验（多帖一致）**
- **Physics Editor 的 iMode/Hybrid/控制台命令/FLICK 依赖/bFitColliders/
  NPC manager 实验性/备份路径/SKSE 2.0.18+ 要求/不支持 VR**：
  Nexus 186341 发布页（2026-07-25 首发，changelog 至 1.4）—— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/186341`
- **FLICK = Fuzz's Legally Intelligible Core Kit（ImGui 菜单框架，F7 呼出）**：
  Nexus 181603 —— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/181603`
- **实装配置文件全家福与参数现值（3BA 节点映射、System.ini 现值、
  PhysicsEditor.ini 全文、第三方预设文件族、增强补丁乘数实例）**：
  本工作区对一套装齐 CBPC + 3BA + 多预设的整合包 `SKSE\Plugins\` 原文的
  实测核对 —— **本工作区实测**
- **v1.6.1 之后是否有更新、1.6.1 与 1.5 源码的逐行差异、
  `GetPercentageValue` 函数体（lerp 精确形式按调用签名与用法判定）**：
  **未确认**
