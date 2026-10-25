---
id: unp-bhunp
title: UNP 家族与 BHUNP
category: 03-body
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [身形, UNP, BHUNP, UUNP, 女性身形]
aliases: [unpb, dimon99, bakafactory, unp 是什么, uunp 是什么, bhunp 是什么, unp 身形, legacy uunp, unified unp, baka haeun, bhunp 安装, unp female body renewal, dimonized unp, uunp next generation]
source: https://www.nexusmods.com/skyrimspecialedition/mods/31126
summary: UNP 家族完整百科：从 Dimonized UNP 到 UUNP、Legacy UUNP、UNP Female Body Renewal 再到 BHUNP 的家谱，UNP 全系共用原版 UV 带来的皮肤互通，BHUNP 的物理分档与"CBPC+HDT-SMP 双前置"的配置代价，以及与 CBBE 不通用的原因。
---

# UNP 家族与 BHUNP

> **一句话**：UNP 是 CBBE 之外另一大女性身形家族——全系**共用原版 UV**，
> 皮肤可与 vanilla 互换；SE 时代的现役主力是 **BHUNP**（物理 + BodySlide + 3BBB）。

## 速览

| 项 | 内容 |
|---|---|
| 家族源头 | **Dimonized UNP**，作者 **dimon99**（LE，2012 年前后） |
| SE 现役主力 | **BHUNP**（Nexus SE 31126），作者 **Bakafactory / BakaHaeun** |
| 官方全称 | Nexus 需求页写作 **"BHUNP (UUNP Next Generation) SSE"**；社区亦读作 "Baka Haeun UNP" |
| UV 体系 | **全系共用原版 UV** → 皮肤可与 vanilla 互通；**与 CBBE 不通用** |
| 硬依赖 | BodySlide · CBPC · HDT-SMP · SKSE64 · XPMSSE **4.67+** |
| 维护状态 | LE 官方文件可见 1.41V；**SE 最新版本与维护状态未确认**（Nexus 页未能直读） |

要点：

- UNP 家族的特点是**代际多、分支多**：选型前先搞清自己谈的是哪一代（见家谱）。
- **BHUNP 同时要求 CBPC 和 HDT-SMP**——这两个默认都想要 body 插槽，
  BHUNP 的分档与配置正是为了让它们各管一部分，装完务必配置，否则"物理打架"。
- 与 CBBE 的关系只有一句话：**不兼容**（不同 UV、不同皮肤体系）。
- 不要为了"对比一下"同时装 CBBE 与 BHUNP。

## 前世今生

### 家谱

| 代际 | 名称 | 作者 | 平台/年代 | 关键能力 | 现状 |
|---|---|---|---|---|---|
| 1 | **Dimonized UNP** | **dimon99** | LE，2012 前后 | 原版的替代身形；**并非**为"护甲贴合某体型"设计 | 源头 |
| 1.5 | **UNPB**（UNP Blessed Body） | 社区 | LE | 丰胸丰臀重制版 | 仍属 UNP 家族 |
| 2 | **UUNP**（Unified UNP） | 社区 | LE | 把 UNP 各变体**统一**并做成 **BodySlide 可构建** | LE 时代主力 |
| 3a | **Legacy UUNP**（Nexus 43773） | 社区 | SE | 供 **LE→SE 转换**的过渡方案 | SE 上 UUNP **不受支持** |
| 3b | **UNP Female Body Renewal**（Nexus 1699） | 社区 | SE | 原版 Dimonized UNP 的 SE 直译；带**初步物理** | **不支持 BodySlide**；已相对过时 |
| 4 | **BHUNP**（Nexus 31126） | **Bakafactory / BakaHaeun** | SE / LE | 物理 + **BodySlide** + **3BBB** | SE 现役主力 |

```
Dimonized UNP（dimon99，LE 2012 前后）
  ├─ UNPB（Blessed Body，丰胸丰臀变体）
  └─ UUNP（Unified UNP，BodySlide 化）
        ├─ [进 SE] BodySlide 不再支持 UUNP
        │     ├─ Legacy UUNP（43773，LE→SE 转换，不受支持）
        │     └─ UNP Female Body Renewal（1699，原版直译，无 BodySlide，过时）
        └─ BHUNP（31126，物理 + BodySlide + 3BBB，SE 现役主力）
```

### 它从哪来

UNP 的源头是 **Dimonized UNP**（dimon99，LE，2012 年前后）。一个容易搞错的点：
它最初只是"原版的替代身形"，**并不是**为"让护甲贴合某体型"设计的——
那是 BodySlide / CBBE 时代的产物。UNPB（Blessed Body）是同一时期的丰胸丰臀变体。

### 中间经历了什么

真正的整合发生在 **UUNP（Unified UNP）**：把各种 UNP 变体统一进 BodySlide，
让 UNP 系第一次拥有"滑块 + 构建"能力（LE 时代）。

进 SE 时出了名的一次断裂：**BodySlide 不再支持 UUNP**。社区抗议之后，
维护方放出 **Legacy UUNP（Nexus 43773）** 供 LE→SE 转换——注意这是**过渡方案**，
SE 上的 UUNP 处于**不受支持**状态。同期还有 **UNP Female Body Renewal（Nexus 1699）**，
它是原版 Dimonized UNP 的 SE 直译，带初步物理支持，但**不支持 BodySlide**，
已相对过时。

### 现状

SE 上的现役主力是 **BHUNP**：同时支持物理与 BodySlide，并跟进到 3BBB。
HDT-SMP 官方页的 body physics addon 列表里也列有 `BHUNP SE`——
它已被物理引擎生态正式接纳。LE 侧官方文件可见 1.41V；
**SE 侧最新版本与维护状态未确认**，请以 Nexus / LoversLab 文件页为准。

## 它解决什么问题

**没有它之前**：UNP 只是静态身形——没有 BodySlide 构建能力时，
每件衣服都要作者手工贴合；进了 SE 之后 UUNP 断了支持，
UNP 用户要么困在 LE，要么用一个不支持 BodySlide 的直译版。

**BHUNP 的解法**：在 UNP 的比例审美与**原版 UV** 之上，
补上三件现代装备——**BodySlide 构建**、**物理（3BBB 骨骼 + 碰撞）**、
以及与 3BA 生态同档的**滑块/预设**体系。于是 UNP 系用户
第一次不必迁去 CBBE 也能拿到全部现代功能。

## 它包含什么

| 组件 | 说明 |
|---|---|
| 基础身形三档 | **BHUNP 3BBB / TBBP / BBP** |
| 物理部位 | Breasts / Butt / Thighs / Calves / Vagina / Belly 的物理与碰撞 |
| 乳房骨骼 | **3 根**（与 3BBB 同级；注意与 UUNP 的 2 根不同） |
| BodySlide 资产 | 组与滑块定义，可被 OBody NG 等分配工具读取 |
| **Ref 体** | Vagina / Breasts Ref，**仅供 modder 使用**，明确标注"不可用于游玩" |

## 安装

### 步骤

1. **前置**：SKSE64、[BodySlide and Outfit Studio](bodyslide-outfit-studio.md)、
   XPMSSE 4.67+（安装时选 Physics Extensions）。
   - 验证点：BodySlide 的 Outfit 下拉里出现 `BHUNP 3BBB Advanced Ver 3` / `Ver 4`。
2. **装 BHUNP 主文件**，按需选基础身形档（3BBB / TBBP / BBP）。
   - 验证点：`Data\CalienteTools\BodySlide\SliderSets\` 下出现 BHUNP 滑块定义。
3. **装两个物理引擎**：[CBPC](../04-physics/cbpc.md) 与
   [HDT-SMP](../04-physics/hdt-smp.md)（或 [FSMP](../04-physics/faster-hdt-smp.md)）。
   - 验证点：两个插件 dll 都在 `Data\SKSE\Plugins\` 下。
4. **构建**：Outfit 选 BHUNP 身体，Preset 用官方 `Zeroed Sliders`
   （里面有滑块是 100% 是正常的，不要改），勾 `Build Morphs`，Batch Build。
   - 验证点：构建列表含身体与全部 for BHUNP 的衣服；冲突列表统一选 BHUNP 身体。
5. **配置分腔**：按发布页说明配置 CBPC 与 HDT-SMP 各管一部分（见下节）。
6. **游戏内**：检查物理部位是否按预期抖动。

### 硬依赖清单

```
BodySlide and Outfit Studio
CBPC
HDT-SMP
SKSE64
XPMSSE 4.67+
```

## 使用与配置

### 构建什么

```
BodySlide → Outfit/Body: BHUNP 3BBB Advanced Ver 3（或 Ver 4）
BodySlide → Preset:     Zeroed Sliders + 勾 Build Morphs
```

工作流原理见 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md)——
"起点统一到零、形状交给运行时"是穿模最少的路。

### 双物理分腔（最容易踩的坑）

> **BHUNP 同时要求 CBPC 和 HDT-SMP —— 而这两个默认都想要 body 插槽。**

BHUNP 的分档与配置正是为了让它们各管一部分（CBPC 管碰撞与部分弹动，
SMP 管布料级模拟）。装完务必按发布页说明配置，否则会出现"物理打架"——
两套引擎互相拉扯同一部位。分腔原则见
[physics-overview.md](../04-physics/physics-overview.md)；
单部位物理关闭可用第三方 disabler 配置。

### NPC 分配

RaceMenu 滑块只作用于玩家；NPC 用
[OBody NG](../05-distribution/obody-ng.md)（读取 `SliderPresets` 里的 `.xml`）
或 [RaceMenu BodyGen](../05-distribution/racemenu-bodygen.md) 分配。

## 兼容与冲突

### UV 与皮肤：全系共用原版

> **UNP / UNPB / UUNP / BHUNP 共用原版 UV** → 皮肤可互通，
> **vanilla 皮肤可直接用**；但与 CBBE **不通用**。

这正是选 UNP 系的典型理由之一：vanilla 皮肤资源（以及大量
for UNP 的皮肤包）可以直接用，不需要另找 CBBE 版。

### 与 CBBE 的关系

> **不兼容。** 不同 UV、不同皮肤体系、不同滑块组、不同骨骼。
> BHUNP 与 **UUNP 系**完全兼容。

裸体网格只能有一个赢家（覆盖规则见
[mo2-override-rules.md](../07-workflow/mo2-override-rules.md)），
所以**不要同时装 CBBE 与 BHUNP**。

### 与 3BA 的关系

平行生态：很多新衣服同时提供 "3BA - BHUNP" 两版（甚至把两者都列为前置），
因为 BHUNP 复用 3BA 的物理配置。你仍然只能**装其中一个身体**，
但**可以同时装两套衣服转换**，按你选的身体挑对应版用。

### 服装与预设

| 关系 | 结论 |
|---|---|
| for UNP / BHUNP 的衣服 | 直接用（BodySlide 构建） |
| for CBBE / 3BA 的衣服 | 不通用（滑块组与骨骼对不上），需转换 |
| for UBE 的衣服 | 不通用（UBE 是独立种族，见 [ube.md](ube.md)） |

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 物理"打架"、互相拉扯 | CBPC 与 SMP 都在管同一部位 | 按发布页分腔配置（[physics-overview.md](../04-physics/physics-overview.md)） |
| 身体不抖 | XPMSSE 低于 4.67，或没选 Physics Extensions | 升级 XPMSSE 并按说明安装 |
| 手 / 颈 / 脚接缝 | 皮肤是 CBBE 系做的 | 换 vanilla / UNP 系皮肤（[body-textures.md](body-textures.md)） |
| 穿模 | 衣服不是 for BHUNP，或没 Batch Build | 换对应版 / 同一预设全量构建（[clipping.md](../06-troubleshooting/clipping.md)） |
| RaceMenu 身形栏空白 | 未 Build Morphs / 漏勾 `Unassigned` 组 | 按 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md) 重做 |
| Ref 体出现在游戏中 | 装错了仅供 modder 的 Ref 文件 | 删 Ref 文件，只留可玩档 |

## 取舍与建议

**选 UNP 系（而非 CBBE 系）的典型理由**：

- 你已经在用 UNP 系的皮肤或预设（尤其 vanilla 皮肤可直接用）；
- 你要装的服装包写明 for UNP / BHUNP；
- 你偏好 BHUNP 的物理分档方式。

**不选当你**：你的衣服资产大多 for CBBE/3BA（那是更大的生态，见
[cbbe.md](cbbe.md) / [cbbe-3ba.md](cbbe-3ba.md)）。

**不要**：为了"对比一下"同时装 CBBE 与 BHUNP——那是纯自伤。

**版本敏感性**：BHUNP SE 的最新版本与维护状态本轮**未确认**；
UUNP 在 SE 上**不受支持**这条结论来自 Nexus 页面与社区指南，若上游有新动作请重新核实。

## 来源

- **BHUNP 作者（Bakafactory / BakaHaeun）、3 乳房骨、物理部位（Breasts/Butt/Thighs/
  Calves/Vagina/Belly）、基础身形三档（3BBB/TBBP/BBP）、Ref 体、硬依赖
  （BodySlide/CBPC/HDT-SMP/SKSE64/XPMSSE 4.67+）、与 CBBE 不兼容**：
  LoversLab 官方文件页 + Nexus 发布页 —— **一手**
  `https://www.loverslab.com/files/file/10630-bhunp-3bbb-body-for-le`
  `https://www.nexusmods.com/skyrimspecialedition/mods/31126`（LE：`mods/100306`）
- **BHUNP 官方全称 "BHUNP (UUNP Next Generation) SSE"**：多个 Nexus 依赖页
  Requirements 栏（如 Einherjr Armor 112692、Bubblegum Adventurers 157473）—— **一手（依赖页）**
- **UNP → UUNP → Legacy UUNP → UNP Renewal 的演变、UUNP 在 SE 不受支持**：
  Nexus 论坛 UNP 专题帖（资深用户/版主）+ Nexus 页面与指南 —— **社区经验（多源一致）**
- **UNP/UNPB/UUNP/BHUNP 共用原版 UV、皮肤可互通**：社区一致确认 —— **社区经验**
- **HDT-SMP 官方页 body physics addon 列表含 `BHUNP SE`**：HDT-SMP Nexus 30872
  描述正文 —— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/30872`
- **"3BBB 每侧 3 根、UUNP 只有 2 根且不同"**：LoversLab 术语表 —— **社区经验**
- **"BHUNP" 缩写**：官方展开式为 **UUNP Next Generation**（Nexus 需求页标题，一手）；
  "Baka Haeun UNP" 为**社区读法**（源自作者名，未确认是否官方用意）
- **LE 1.41V**：LoversLab 官方文件页 —— **一手**
- **BHUNP SE 最新版本 / 维护状态**：**未确认**（Nexus 页未能直读，以文件页为准）
