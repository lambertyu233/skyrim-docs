---
id: learning-path
title: 学习路径与选型建议
category: 00-overview
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [总览, 入门, 学习路径, 选型]
aliases: [learning path, 怎么开始, 新手, 该装哪个身形, 选 CBBE 还是 UNP]
source: https://stepmodifications.org/wiki/SkyrimSE:0.1.0
summary: 按"只想捏脸 / 想改身形 / 想上物理 / 想给 NPC 分配"四种目标给出最小依赖集，并给出 CBBE 与 UNP 家族的选择判据。
---

# 学习路径与选型建议

## 一、先确定目标，再决定装多少

不同目标的最小依赖集差别很大，**多装的部分就是将来排错的成本**。

### 目标 A：只想捏出好看的脸

```
SKSE64 → Address Library → SkyUI
→ RaceMenu
→ 一张脸纹理（皮肤）→ 眼 / 眉 / 发 / 须 资源
→ （可选）High Poly Head
→ （可选）Facial Animation / Facelight
```

**不需要**身形、骨骼、物理。捏脸是独立的一层。

### 目标 B：想改身形（体型）

```
A 的全部
→ 骨骼：XPMSE
→ 身形家族二选一：CBBE 系 或 UNP 系
→ 皮肤贴图（必须与身形同族）
→ BodySlide and Outfit Studio（构建身形与服装）
```

**关键动作**：BodySlide 里勾 **Build Morphs**，否则 RaceMenu 里没有身形滑块。

### 目标 C：想有物理（抖动 / 碰撞 / 物理头发）

```
B 的全部
→ 物理引擎：Faster HDT-SMP（推荐）和/或 CBPC
→ 身形必须选 physics 变体，并在 BodySlide 构建带物理的身形
→ 头发/衣物物理只有 HDT-SMP 能做
```

### 目标 D：想让 NPC 也有不同身材

```
B（+C）的全部
→ 分配工具三选一：RaceMenu BodyGen（内置）/ OBody NG / AutoBody
```

## 二、CBBE 还是 UNP？

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

## 三、男性角色

上述讨论默认是女性身形。男性身形（如 **HIMBO**、Tempered Skins 面向的男性网格）是**另一条独立的链**，
与女性身形不冲突，可以同时启用一套。AutoBody 同时支持 **CBBE 与 HIMBO** 预设分发。

## 四、推荐的自学顺序

1. [`glossary.md`](glossary.md) —— 先看得懂术语，否则教程读不下去。
2. [`version-matrix.md`](version-matrix.md) —— 明确自己的游戏版本对应哪几个 SKSE 版本。
3. [`../01-prerequisites/skse64.md`](../01-prerequisites/skse64.md) —— 把前置装稳。
4. 按目标 A→B→C→D 的顺序推进，不要跳级。
5. [`../07-workflow/install-order.md`](../07-workflow/install-order.md) —— 具体的安装次序与 MO2 覆盖规则。

## 五、可参考的教程（外部）

| 教程 | 性质 | 链接 |
|---|---|---|
| STEP Guide（Step Modifications 官方 wiki） | **本领域最权威的"从零到稳定"指南** | `https://stepmodifications.org/wiki/SkyrimSE:0.1.0` |
| Wabbajack 官方文档 | 用现成 modlist 跳过装配 | `https://wiki.wabbajack.org/` |
| GamerPoets | MO2 / BodySlide / RaceMenu 的实操演示 | `https://www.gamerpoets.com/` |

> 注意：`modding.wiki` 域名**并不托管 STEP 的 Skyrim SE 指南**（实测其相关页面 404）；
> STEP 的官方 wiki 是 `stepmodifications.org`。这是一个容易走错的路。

## 来源

- STEP Guide：`https://stepmodifications.org/wiki/SkyrimSE:0.1.0` —— **一手（官方策划指南）**
- BHUNP 硬依赖清单：`https://www.loverslab.com/files/file/10630-bhunp-3bbb-body-for-le` —— **一手（作者文件页）**
- Wabbajack 文档：`https://wiki.wabbajack.org/` —— **一手**
- "CBBE 与 UNP 互斥、UV 不通用"：Nexus 发布页描述 + 社区一致确认 —— **一手 + 社区经验（一致）**
- `modding.wiki` 不托管 STEP 指南：**本工作区实测（2026-09-22，WebFetch 三页均 404）**
