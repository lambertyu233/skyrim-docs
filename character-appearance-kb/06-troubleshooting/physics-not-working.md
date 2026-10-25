---
id: physics-not-working
title: 物理不生效（不抖 / 头发穿透）
category: 06-troubleshooting
kind: tutorial
version: 2.0.0
updated: 2026-10-25
tags: [排错, 物理, SMP, CBPC, 骨骼]
aliases: [物理不生效, 不抖, 没物理, 头发不抖, 头发穿透, 衣服不飘, 斗篷不飘, 物理失效, 物理没反应, smp 不工作, cbpc 没反应, smp report, 物理排查, 只有 NPC 不抖]
source: https://forums.nexusmods.com/topic/3800385-a-guide-to-hdt-smp-usersmodders/
summary: 物理失效的症状分类（完全不抖/只头发不抖/只 NPC 不抖/穿模穿透）、按序排列的十二条检查清单（从 smp report 到 XPMSE 被覆盖、SMP 与 CBPC 争插槽、XML 未挂、身形无节点、AVX 档位选错）、smp detail/list 诊断用法与两条社区经验细节。
---

# 物理不生效

> **一句话**：装了物理 mod 不抖，第一嫌疑人**不是物理 mod，而是身形**
> （没装物理变体 / 没构建）——这条能省掉大量无用功。

## 速览

| 项 | 内容 |
|---|---|
| 症状 | 胸/臀/腹不弹、头发衣服不飘、头发穿过身体、或只有一类对象不抖 |
| 高频成因 | 身形不是 physics 变体 / 未构建；XPMSE 被覆盖；SMP 与 CBPC 争插槽 |
| 首选判据 | 进游戏控制台跑 **`smp report warnings`**——直接指出哪个 mod 的物理 XML / nif 有警告 |
| 最短修复路径 | 先 `smp report`，再按"引擎 → 骨骼 → 身形 → 配置"四层顺序查 |

要点：

- **物理全是 SKSE 插件**：SKSE 与游戏版本不匹配 → 所有插件**静默失效** →
  物理自然不动，而且往往不报错。
- **CBPC 完全不能处理头发和衣服**（机制限制）：只装 CBPC，
  头发/斗篷永远不飘——这不是配置问题，是方案选错。
- **SMP 只把网格附加到 XPMSE 的 human skeleton**：装的是别的骨骼 =
  物理没有挂点；骨架被别的 mod 覆盖同样致命。
- ** morph 与物理是两套无关机制**：滑块变形是顶点位移，物理是骨骼/球体模拟，
  别混着排查（见 [morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)）。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 早期（具体年份未确认） | **BBP / TBBP** 纯动画方案流行 | 第一代"抖"：运动写在行为文件里，零实时计算；骨骼名沿用至今 |
| LE 中期（具体日期未确认） | **hydrogensaysHDT** 发布 **HDT-PE**（Nexus LE 53996） | 第二代：游戏内建 Havok 骨骼级实时物理 |
| 2015 前后 | HDT-SMP 早期测试版流传（"mesh/bullet based physics"） | 第三代萌芽：自带 Bullet、逐顶点、真碰撞 |
| 2018-11 | **Shizof** 发布 **CBPC**（Nexus SSE 21224，基于 polygonhell 的 MIT 源码） | 第三条路线：球体近似 + 每帧实算，CPU 友好 |
| 2019-2020 | hydrogensaysHDT 淡出并以 MIT 释出源码；**aers → Karonar1** fork 链 | SMP 进入社区维护时代 |
| 2021-10 起 | **DaymareOn** 的 **FSMP**（Nexus 57339）成为主线 | 多线程 Bullet + ImGui 菜单；官方口径"完全取代原版" |
| 2023-2024 | XPMSE 进入 5.x（v5.06，2024-02-11） | 物理骨骼节点集合稳定，全部方案共享同一套挂点 |
| 2026 | **FSMP 4.1.1**（2026-08-27）；**CBPC v1.6.1** | 当代标准组合：FSMP（头发/衣物）+ CBPC（身体） |
| 2026-08 | 游戏 **1.7.x** 更新 | FSMP 对 1.7.x 的支持状态**未确认**；升级前先查 Files 页（见 [1.7.x 版本冲击](../00-overview/game-version-1-7-x.md)） |

### 它从哪来

一切始于"让胸部和臀部动起来"。理解四代方案的分野（动画式 → Havok 骨骼级 →
Bullet 逐顶点 / 球体近似）是排查的前提：**很多"不抖"其实是方案与期望不匹配**，
比如用 CBPC 期待头发物理。

### 中间经历了什么

最大的分叉是 **SMP 的 fork 链**（原作者淡出 → aers → Karonar1 → DaymareOn）：
原版停在 LE 与 SE 1.5.97，AE（1.6.x）用户实际都在用 FSMP。
第二条是 **CBPC 从 CBP Physics 独立出来**：polygonhell 的 MIT 释出是它存在的前提。

### 现状

没有唯一赢家，而是**双引擎分工**：FSMP 管头发/衣物，CBPC 管身体部位。
两者都要挂 XPMSE 的骨骼节点，于是有了"两个 dll 争 body 插槽"这个必踩的坑。

## 症状分类（先分流）

| 症状 | 指向 |
|---|---|
| 完全没有任何物理（身体也不抖） | 引擎层问题（SMP/CBPC 未生效：SKSE 版本 / dll 被覆盖 / 骨架不对） |
| 身体抖、头发不动 | 方案选错（只装了 CBPC，机制限制）或头发缺 XML |
| 只有 NPC 不抖（玩家正常） | NPC 距离/角度剔除（性能设计）、non-wig 头发限制、facegen 约束（FSMP 已知问题） |
| 某一件衣服不飘 | 那件衣服缺 XML 或被覆盖 |
| 头发穿过身体 | 碰撞体定义/不匹配；或引擎在跑但配置没挂对 |
| 物理"打架"、互相拉扯 | SMP 与 CBPC 抢同一批骨骼，没做分腔 |

## 检查清单（按顺序）

### 1. 先跑 `smp report warnings`

```
smp report warnings
```

FSMP 内置的命令，会**校验整个 load order 的物理 XML 与 `.nif`** 并报告警告。
**这是效率最高的一步**——别先逐个 mod 试。

### 2. SKSE 版本对不对

SKSE 与游戏版本不匹配 → 所有 SKSE 插件静默失效 → 物理自然不动。
版本对照见 [version-matrix.md](../00-overview/version-matrix.md)；
1.7.x 的冲击见 [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)。

### 3. 装的是不是正确的物理 mod

- 只装 **CBPC** → **头发和衣服永远不会动**（机制限制，不是配置问题）；
- 只装 **SMP** → 身体可能不如 CBPC 自然，但会动；
- 两者都装 → 需要显式配置，否则**互相覆盖**（见第 5 条）。

方案差异见 [physics-overview.md](../04-physics/physics-overview.md)。

### 4. XPMSE 是否装了且没被覆盖 ⭐

HDT-SMP / FSMP **只把网格附加到 XPMSE 的 human skeleton**。
装的是别的骨架 → 物理没有挂点。需要带物理骨骼的版本
（3BA 要求 XPMSSE 4.61+，BHUNP 要求 4.67+），安装时第一屏选
**Physics Extensions**。⚠️ 不要删 `skeleton_female.hkx`；
⚠️ 任何东西覆盖这个骨架都是大忌（"bad and weird stuff happens"）。
详见 [xpmse-skeleton.md](../04-physics/xpmse-skeleton.md)。

### 5. SMP 与 CBPC 是否在抢插槽 ⭐

两者默认争同一批骨骼。共存必须：

- 编辑 **`defaultBBPs.xml`** 让 SMP 忽略身体；
- 且把 **`cbp.dll` 改名 `zcbp.dll`**（或 Engine Fixes preload），保证 SMP 先加载。

见 [physics-overview.md](../04-physics/physics-overview.md) 与
[cbpc.md](../04-physics/cbpc.md) 的「与 SMP 共存」。

### 6. 身形装的是不是 physics 变体 ⭐ 最常被忽略

身形（如 3BA、BHUNP）在 FOMOD 里通常有"带物理"和"不带物理"的选择。
装成不带物理的版本，物理引擎再对也没东西可动。

### 7. 是否在 BodySlide 构建了带物理的身形

选了 physics 变体还不够，还要**构建**（Outfit 下拉里出现带 Physics/3BBB
的身体项目才算数）。

### 8. XML 配置是否挂上

SMP 的物理配置来自每个 mod 自带的
`Data/SKSE/Plugins/hdtSkinnedMeshConfigs/<mod>.xml`——
**"某件衣服没物理"的第一嫌疑不是引擎，而是它没带 XML、XML 没被加载、
或被其他 mod 覆盖**。引擎本身不提供任何配置（官方 wiki 原话：
"它分不清斗篷和胸"）。见 [hdt-smp.md](../04-physics/hdt-smp.md) 与
[faster-hdt-smp.md](../04-physics/faster-hdt-smp.md)。

### 9. 行为补丁跑了吗

FNIS / Nemesis 需要跑一次以生成行为文件（CBPC 依赖 FNIS；
Skeleton Arm Fix 是动画 mod 的要求）。

### 10. 早期 HDT-SMP 的 OpenCL

早期 SMP 需要 **OpenCL 2.0**。"关闭 OpenCL"实际是**切到 CPU 模拟**，
不是关掉物理。

### 11. MCM 里的物理开关

如 3BBB 可以在 CBPC / SMP 之间切换——**切错了引擎就会看起来"没物理"**。

### 12. FSMP 的 FOMOD 版本档与 AVX 档位

- **游戏版本档选错**：典型表现是物理不生效或开局崩溃，FOMOD 必须选对；
- **CPU 指令集档位选错**：发布页提供 `avx` / `avx2` / `avx512` 多档，
  默认**不带 AVX2**；CPU 不支持时选了高指令集档属于选错档位
  （表现为插件加载即崩或物理不生效——**机制推论：指令集不兼容**），
  CPU 支持时建议开启（性能免费收益）。

## `smp detail` / `smp list` 诊断用法

怀疑"某个 NPC 到底有没有被引擎追踪"时，用这三个命令定位：

```
smp detail      全部被追踪 actor 的详细信息（含生效/失效的护甲与 head part）
smp list        精简列表：哪些 NPC 被追踪、按激活状态排序
smp dumptree    导出当前目标 NPC 的整棵节点树到日志
```

**诊断路径**：控制台点击目标 NPC → `smp detail` 看它的护甲 / head part
是否被追踪 → `smp list` 看追踪状态 → `smp dumptree` 把节点树导进日志核对。

> "只 NPC 不抖"的已知问题（维护者自述）：NPC 距离/角度剔除是性能设计；
  non-wig 形态的 NPC 头发大多要改约束才能工作；`smp reset` 会破坏部分
  带 facegen 数据 NPC 的约束。遇到这些先对照已知问题清单，别怀疑自己。

## 两条经验性细节（社区）

- **改 CBPC 配置不生效**时，确认：角色体重是 **0 或 100**；
  未被 SMP 覆盖；覆盖式文本配置在 MO2 左栏里位于 CBPC / 身形**之下**。
- **不兼容项**：CBPC 与 *Player Size Adjuster and First Person Camera Height Fix SSE*
  不兼容（官方明列）。

## 判断分叉点（别误诊）

| 看起来像 | 其实 |
|---|---|
| "装了 CBPC 头发不动" | **机制限制**：CBPC 没有头发/衣服网格的蒙皮信息，不是配置问题 |
| "SMP 与 CBPC 都装但互相拉扯" | 没做分腔（`defaultBBPs.xml` + `zcbp.dll`） |
| "身体抖得很假、像在播放动作" | 老配置/老身形还在用 BBP/TBBP 动画驱动，或有动画包在抢同一部位 |
| "身形滑块没了" | 不是物理问题，是 `.tri`/`BODYTRI`——转 [racemenu-sliders-missing.md](../06-troubleshooting/racemenu-sliders-missing.md) |
| "穿模" |  morph 起点不一致——转 [clipping.md](../06-troubleshooting/clipping.md) |
| "升级游戏版本后全部插件失效" | SKSE 与游戏版本不匹配；1.7.x 下 FSMP 适配状态**未确认** |
| "开局 CTD" | 版本档选错，或 `cbp.dll` 改名后旧文件没删（两个同名文件冲突） |

## 取舍与建议

- **诊断依赖 `smp report`**：把它当作"物理版的 LOOT"，出问题第一动作；
- **身体 CBPC、头发衣物 FSMP** 是当前标准分工，别期待一个引擎包打天下；
- **性能敏感**：先用菜单里的 `Performance.xml` 预设，CPU 支持 AVX2 再开指令集档；
- **别做**：同时装原版 HDT-SMP 与 FSMP（同名 dll）；同时装 CBP 与 CBPC；
  对香草身体期待物理。

## 来源

- **`smp report` / `smp detail` / `smp list` / `smp dumptree` / `smp reset` 命令、
  "引擎不提供任何 XML 配置"、已知问题清单（含 NPC 剔除 / non-wig 头发 / facegen 约束）、
  FOMOD 版本档与 AVX 档位、Performance.xml**：FSMP 官方仓库 README / wiki
  与 Nexus 57339 —— **一手**
  `https://github.com/DaymareOn/hdtSMP64`
  `https://www.nexusmods.com/skyrimspecialedition/mods/57339`
- **"SMP 只附加 XPMSE human skeleton"、XML 目录 `hdtSkinnedMeshConfigs`、
  OpenCL 2.0 与"关 OpenCL 实为切 CPU"**：HDT-SMP Nexus 30872 发布页 —— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/30872`
- **CBPC 依赖链（XPMSSE 第一屏 Physics Extensions 其余 None、FNIS/Nemesis）、
  球体近似每帧实算、"不能处理头发和衣服"、不支持 Player Size Adjuster**：
  CBPC Nexus 21224 描述（经镜像站转载 v1.6.1 文件描述全文）—— **一手（经转载）**
  `https://www.nexusmods.com/skyrimspecialedition/mods/21224`
- **XPMSSE 版本要求（3BA 4.61+ / BHUNP 4.67+）、不删 `skeleton_female.hkx`、
  骨架被覆盖的后果、FNIS Skeleton Arm Fix**：[xpmse-skeleton.md](../04-physics/xpmse-skeleton.md)
  整理自 XPMSSE 发布页 —— **一手（经转载）**
- **"CBPC 不能管头发和衣服"、`cbp.dll → zcbp.dll` 与 `defaultBBPs.xml` 分腔、
  调参不生效三检查项（体重 0/100、被 SMP 覆盖、左栏顺序）**：
  LoversLab 多帖一致 + HDT-SMP 用户指南 —— **社区经验（多帖一致）**
  `https://forums.nexusmods.com/topic/3800385-a-guide-to-hdt-smp-usersmodders/`
- **检查清单其余项（physics 变体、BodySlide 构建、MCM 开关）**：
  综合 HDT-SMP 用户/作者指南与 CBPC 专帖 —— **社区经验（多帖一致）**
- **"CPU 不支持时选高指令集档会崩或不生效"**：**机制推论**（指令集不兼容），
  档位矩阵本身为发布页一手信息
- **FSMP 4.1.1 对 1.7.x 的适配范围**：**未确认**（Files 页与社区说法矛盾，
  见 [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)）
