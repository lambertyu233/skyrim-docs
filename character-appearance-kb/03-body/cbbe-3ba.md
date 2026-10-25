---
id: cbbe-3ba
title: CBBE 3BA（3BBB Advanced）—— 当代事实标准
category: 03-body
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [身形, 3BA, 3BBB, CBBE, 物理身形]
aliases: [cbbe 3ba, 三乳骨, acro, 事实标准身形, amazing body, 3ba 是什么, 3bbb 是什么, cbbe smp, 怎么装 3ba, 3ba 物理, acro748, 3bbb advanced, cbbe 3bbb body amazing, 3ba 预设]
source: https://www.nexusmods.com/skyrimspecialedition/mods/30174
summary: CBBE 3BA 完整百科：3BBB/3BA 术语与 HDT-SMP 官方页两个 addon 的区分、Acro748 的归属、它在 CBBE 基底上增加的骨骼/权重/物理能力、成为事实标准的原因、依赖链与 3BAv2 的兼容性后果，以及安装构建与排错。
---

# CBBE 3BA（3BBB Advanced）

> **一句话**：3BA 是 CBBE 的物理扩展——同一具基底网格，加上 3 根乳房骨、
> 重绘的顶点权重与 CBPC/SMP 双物理支持；它没有取代 CBBE，而是成了当代女性身形的事实标准。

## 速览

| 项 | 内容 |
|---|---|
| 作者 | **Acro**（Nexus ID **Acro748**，多页 credits 确认） |
| 发布 | LoversLab `CBBE 3BBB Advanced`（经 **Ousnius 授权**）先行；后以 **CBBE 3BA** 名义上传 Nexus SE 30174 |
| 当前版本 | **未确认**（Nolvus 2022 年用 ~2.45；3DMGAME 转载帖标注 Nexus 页 2025-03-01 有更新；Nexus 页在墙后，以 Files 页为准） |
| 基底 | **CBBE**（同基底网格，皮肤/衣服生态互通） |
| 硬前置 | CBBE · XPMSSE **4.61+** · CBPC **1.5.1+** · BodySlide |
| 半前置 | HDT-SMP（SE）/ FSMP（AE）/ PapyrusUtil——选 "CBPC only" 时可免 |
| 迭代 | **3BAv2**（2021 年底之后为其制作的服装才与 3BAv2 原生兼容） |
| 维护状态 | 低频更新，仍在维护（第三方页显示 2025 年有更新） |

要点：

- **3BA 是 CBBE 的扩展，不是替代品**：任何为 CBBE 设计的皮肤与服装都与 3BA 兼容。
- 它把 **3BBB 骨骼**（每侧乳房 3 根骨）植入身体并**重绘顶点权重**，让抖动更流畅。
- 身体从此**可以用 CBPC**——不必只依赖 SMP，低配用户的 CPU 占用问题得到缓解，
  而且 SMP 与 CBPC **可以在游戏过程中切换**。
- "事实标准"是社区共识 + 生态归纳，不是官方声明；依据是绝大多数新衣服/预设写明 for CBBE 3BA。

## 术语先分清

| 缩写 | 含义 |
|---|---|
| **3BBB** | **3 Breast Bones Body** —— 带 3 根乳房骨的身体（术语，不是文件名） |
| **3BA** | **CBBE 3BBB Advanced**，发布页也常称 "Amazing Body"（惊人身体） |
| **CBBE SMP (3BBB)** | HDT-SMP 官方页列出的 addon 之一：CBBE SE 的**官方 SMP 身体与配置预设** |
| **CBBE 3BBB (3BA)** | HDT-SMP 官方页列出的另一个 addon：**编辑过的** CBBE SE 身体与配置预设 |

> **最容易混的一对**：HDT-SMP 官方页把 `CBBE SMP (3BBB)` 与 `CBBE 3BBB (3BA)`
> 列为**两个不同的 addon**——前者是官方 SMP 身体与配置预设，后者是**编辑过**的
> CBBE SE 身体与配置预设（3BA 属于后者）。它们不是同一个文件，别混装。

**3BBB 与 UUNP 的"3 根骨"不是同一套**：UUNP/BHUNP 一侧只有 **2 根**乳房骨，
且骨骼节点与 3BBB 的 3 根不同。所以"都是 3 乳骨"的说法不准确——
**只有 3BBB/3BA 是每侧 3 根**；骨骼节点越多，可控性与效果上限越高，
但仍取决于配置质量与网格比例。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 3BBB 概念期 | "3 Breast Bones Body" 作为物理身形术语在社区流传 | 每侧 3 根乳房骨成为高端物理身形的标志（社区经验） |
| LE→SE 之交 | Acro 制作 **CBBE 3BBB Advanced**，经 **Ousnius 授权**，发布于 LoversLab | 3BA 的 direct 前身 |
| SE 早期 | 并入 CBBE 3BBB 页，并以 **CBBE 3BA** 名义上传 Nexus 30174 | 获得 Nexus 主阵地 |
| 2021 年底 | **3BAv2** 迭代 | 之后为 3BAv2 制作的服装才与其原生兼容 |
| 2022 | Nolvus 等整合包采用 ~2.45 | 随整合包进一步普及 |
| 2025-03 | Nexus 页仍有更新（3DMGAME 转载帖标题标注） | 维护仍在继续；具体版本号未确认 |

### 它从哪来

3BA 的作者是 **Acro**（LoversLab ID `Acro748`）。起点是 **CBBE 3BBB Advanced**——
一个经 Ousnius 授权、在 LoversLab 发布的 CBBE 物理增强版；后来它并入
CBBE 3BBB 页面，并以 **CBBE 3BA** 的名义上传 Nexus（SE 30174）。
Nexus 上多个第三方 mod 的 credits 明确写着 "CBBE 3BA (3BBB) by Acro748"，
作者归属可以确认。

### 中间经历了什么

关键迭代是 **3BAv2**。它带来一个隐蔽的兼容性后果：

> **2021 年底之后为 3BAv2 制作的服装才与 3BAv2 兼容；
> 更老的 CBBE/3BBB 服装需要转换。**

这是"关注了/穿某件衣服时穿模"的一个常见隐蔽成因——衣服本身没坏，
只是它为上一代 3BA 做的。

### 现状

低频更新、仍在维护（第三方页显示 2025 年页面有更新，具体版本号**未确认**）。
它没有后继取代者：UNP 系的对应位是 BHUNP，新世代 base 是 UBE，
但新衣服仍然优先出 3BA 版本——这就是"事实标准"的含义。

## 它解决什么问题

**没有它之前**：纯 CBBE 是**静态**的——没有物理骨骼、没有顶点权重，
胸/臀/腹不会动；想抖只能整体换带 HDT 配置的身形，而 SMP 的 CPU 占用
对低配机器不友好，且装了 SMP 就难回头。

**3BA 的解法**：

1. 把 **3BBB 骨骼权重植入身体**，并**重新绘制骨骼权重使其更加分散**——
   表现更流畅、更有"弹性"而不是生硬摆动（发布页原述）；
2. 身体**同时支持 CBPC**：不必只依赖 SMP，低配用户可用 CBPC 获得物理，
   而且**能在游戏过程中随时切换 SMP 与 CBPC**（发布页原述）；
3. 附带各种物理预设与额外的身体 morph/滑块。

## 它增加了什么

在 CBBE 基底上新增：

- **受物理控制的骨骼**：3 根乳房骨，以及腹部 / 大腿 / 小腿等；
- **重绘的顶点权重**：让上述骨骼的位移更分散、更自然；
- **大量额外 morph**（RaceMenu 里因此多出一批滑杆）；
- **RaceMenu Morphs 组件**（如 `RaceMenuMorphsCBBE.esp`）——它决定捏脸菜单里
  身形那一栏有哪些滑块、叫什么名字；真正的变形数据仍来自你构建的 `.tri`
  （三层来源见 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md)）。

> 装了 3BA 不一定要再装基础 CBBE，但**基础 CBBE 自带所有原版服装转换**，
> 所以通常两者都装：3BA 覆盖身体，CBBE 提供服装基础。

## 安装

### 步骤

1. **前置**：CBBE、[BodySlide and Outfit Studio](bodyslide-outfit-studio.md)、
   XPMSSE 4.61+（安装时选 Physics Extensions）、CBPC 1.5.1+。
   - 验证点：BodySlide 的 Outfit 下拉里出现 `CBBE 3BBB Body Amazing`。
2. **装 3BA 主文件**，FOMOD 选择物理方案（见下表）。
3. **（半前置）** 若没选 "CBPC only"：SE 装 [HDT-SMP](../04-physics/hdt-smp.md)、
   AE 装 [FSMP](../04-physics/faster-hdt-smp.md)、装 PapyrusUtil。
   - 验证点：`Data\SKSE\Plugins\hdtSMP64.dll`（或 FSMP 对应文件）存在。
4. **构建**：Outfit 选 `CBBE 3BBB Body Amazing`，Preset 选预设
   （新手建议先 `Zeroed Sliders` 并勾 `Build Morphs`），Batch Build。
   - 验证点：构建列表含身体与全部 3BA 衣服；冲突列表统一选 3BA 身体。
5. **游戏内**：进游戏看是否抖动；不抖按
   [physics-not-working.md](../06-troubleshooting/physics-not-working.md) 排。

### FOMOD 物理选项

| 选项 | 效果 |
|---|---|
| CBPC only | 只用 CBPC；SE 下可免 HDT-SMP，CPU 最友好 |
| SMP / 两者都装 | HDT-SMP（或 AE 下的 FSMP）接管 SMP 部分；CBPC 仍管碰撞 |
| 玩家 / NPC 预设 | 玩家与 NPC 的身体预设不同，按需构建 |

## 使用与配置

### 构建什么

```
BodySlide → Outfit/Body: CBBE 3BBB Body Amazing
BodySlide → Preset:     Zeroed Sliders（或你的预设）+ 勾 Build Morphs
```

完整工作流（为什么用 Zeroed Sliders、为什么要 Batch Build）见
[morph-runtime-vs-bake.md](morph-runtime-vs-bake.md)。

### 游戏内切换物理强度

发布页（2021 年版描述）记载：玩家默认热键 **Num+**、NPC 默认 **Num9**，
按 A/B/C/D 档调节抖动强度（A 最平、D 最晃）；热键可在 MCM 禁用或改键，
也可以改回 MCM 咒语方式触发。⚠️ **该热键信息来自旧版描述，当前版本可能已变，
以发布页与游戏内 MCM 为准。**

### CBPC 与 SMP 的分腔

3BA 的精髓是**两套物理引擎各管一部分**：CBPC 管碰撞与部分弹动，
SMP（HDT-SMP/FSMP）管布料级模拟。两者都要 body 插槽，装完务必按
[physics-overview.md](../04-physics/physics-overview.md) 配置，否则会"物理打架"。
想单独关某部位物理，可用第三方 disabler 配置（如 Nexus 74836）。

### NPC 分配

RaceMenu 滑块只作用于玩家；NPC 身材用
[OBody NG](../05-distribution/obody-ng.md) / [RaceMenu BodyGen](../05-distribution/racemenu-bodygen.md)
分配（OBody NG 读的就是你 `SliderPresets` 里的 `.xml`）。

## 兼容与冲突

| 关系 | 结论 |
|---|---|
| 与 CBBE | 同基底扩展；CBBE 皮肤/衣服通用 |
| 与 CBBE SMP (3BBB) | **不同 addon**（见"术语先分清"）；别混装两个 SMP 身体 |
| 与 3BAv2 服装 | 2021 底之后的服装原生兼容；更老的需转换 |
| 与 BHUNP | 平行生态，可分别构建；很多衣服同时提供两版 |
| 与 UBE | 可并存；UBE 只取 3BA 的物理配置（见 [ube.md](ube.md)） |
| 与 UNP/UUNP | 不通用（UV、滑块组、骨骼都不同，见 [unp-bhunp.md](unp-bhunp.md)） |
| 与 YgNord / TeraElin2 / 独特角色 mod | 发布页标注兼容 |

### 为什么它成了事实标准

1. **同时支持 CBPC 与 HDT-SMP**，可自由切换，甚至游戏内切换；
2. 对 CPU 友好（相对纯 SMP 方案）；
3. **morph 与预设生态庞大**——绝大多数新服装、预设都写明 for CBBE 3BA；
4. 有 **3BAv2** 持续迭代。

> 注意：这是**社区共识 + 机制归纳**，不是某个官方声明。

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 关注某件衣服时穿模 | 衣服是 3BAv2 之前做的 | 找 3BAv2 版转换，或在 Outfit Studio 里转换 |
| 身体完全不抖 | 没装 CBPC/SMP，或 XPMSSE 版本低于 4.61 | 补前置；XPMSSE 安装时选 Physics Extensions |
| 抖得生硬/穿膛 | 顶点权重被覆盖（装了别的 SMP 身体） | 检查是否混装 `CBBE SMP (3BBB)` 与 3BA 两个 addon |
| CPU 占用高 | 纯 SMP 方案 | FOMOD 改 CBPC only，或调低 SMP 预设档位 |
| RaceMenu 3BA 栏空白 | 未 Build Morphs / 漏勾 `Unassigned` 组 | 按 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md) 重做 |
| 物理"打架"、互相拉扯 | CBPC 与 SMP 都在抢同一部位 | 按 [physics-overview.md](../04-physics/physics-overview.md) 分腔配置 |

## 取舍与建议

**选 3BA 当你**：

- 你的衣服资产大多 for CBBE/3BA（绝大多数情况）；
- 你要物理，且可能需要在低配机器上切 CBPC；
- 你在跟随主流整合包。

**考虑 BHUNP 当你**：你的皮肤/预设/衣服在 UNP 系，或偏好 BHUNP 的物理分档
（见 [unp-bhunp.md](unp-bhunp.md)）。

**考虑 UBE 当你**：你追求最高网格精度并接受"每件衣服都要补丁+转换"的成本
（见 [ube.md](ube.md)）。

**不要**：为了"对比一下"同时装 3BA 与 BHUNP 的裸体网格；
也不要把 `CBBE SMP (3BBB)` 与 3BA 两个 addon 混装。

**版本敏感性**：3BAv2 分界（2021 底）直接影响旧衣服兼容性；
当前版本号**未确认**，装前以 Nexus Files 页为准。

## 来源

- **作者 Acro（Acro748）、3BA = CBBE 3BBB Advanced / Amazing Body、与 CBBE 同基底、
  "将 3BBB 骨骼权重植入身体并重新绘制使其更分散"、"身体也可使用 CBPC 且可在游戏中切换"、
  物理预设、额外滑块、前置链（CBBE / XPMSSE 4.61+ / CBPC 1.5.1+ / BodySlide；
  半前置 HDT-SMP(SE) / FSMP(AE) / PapyrusUtil）、YgNord/TeraElin2/独特角色兼容**：
  Nexus 30174 发布页描述（经 3DMGAME 转载）—— **一手（描述正文，经转载）**
  `https://www.nexusmods.com/skyrimspecialedition/mods/30174`
- **作者归属 Acro748**：Nexus 74836（CBBE 3BA 3BBB CBPC Physics Disabler Config Files）
  credits "CBBE 3BA (3BBB) by Acro748"；LoversLab 多帖 credits
  "Acro748 for CBBE 3BA" —— **一手（第三方 credits 一致）**
- **历史（LoversLab 前身 + Ousnius 授权 + 并入 Nexus 页）**：LoversLab 官方文件页
  `https://www.loverslab.com/files/file/11063-cbbe-3bbb-advanced` + Nolvus 指南 —— **一手 + 社区指南**
- **HDT-SMP 官方页把 `CBBE SMP (3BBB)`（Official SMP body and config presets for CBBE SE）
  与 `CBBE 3BBB (3BA)`（Edited CBBE SE body and config presets）列为两个 addon，
  同页还列 `BHUNP SE`**：HDT-SMP Nexus 30872 描述正文 —— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/30872`
- **3BAv2 存在、2021 底后服装才原生兼容**：Nexus 73324（KS Hairdos SMP 碰撞 bodyslides）
  描述 "setup to support 3BA v2" + 社区一致 —— **一手（依赖页）+ 社区经验**
- **热键 Num+/Num9、A~D 档、玩家/NPC 预设不同**：Nexus 30174 描述 2021 年版译文 ——
  **一手（旧版描述；当前版本可能已变）**
- **"3BBB = 3 Breast Bones Body"、UUNP 只有 2 根且不同、骨骼节点越多上限越高**：
  LoversLab 术语表 + 社区讨论 —— **社区经验**
- **Nolvus 2022 年使用 ~2.45、页面 2025-03 有更新**：Nolvus 指南与 3DMGAME 转载帖标题 ——
  **社区指南**
- **当前最新版本号**：**未确认**（Nexus 页在成人墙后未能直读）
