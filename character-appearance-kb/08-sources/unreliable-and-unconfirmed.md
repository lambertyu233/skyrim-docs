---
id: unreliable-and-unconfirmed
title: 不可信来源与未确认事项
category: 08-sources
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [来源, 辨析, 不可信, 未确认, 内容农场]
aliases: [不可信来源, csdn, 假信息, 别信, ai 生成]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: 本领域的内容农场/AI 聚合站黑名单与判据，以及撰写时确认过的"未确认事项"清单——避免把转述或臆测当成现状。
---

# 不可信来源与未确认事项

## 一、不做事实来源的站点类型

本工作区有一条硬纪律：**不用 CSDN、toolify、AI 聚合站、内容农场**。

### 已识别并排除的域名（部分）

```
tsight.io        "深度解析"类文章，结构工整但无可核验的版本号/路径
gifpow.com       "2026 完整指南"，含夸张断言（"全光追"式表述）
2023game.com     "梦里 / Dreamlike 整合包" 等无实证内容
maoxu.com / bajiujiu.com / 233leyuan.com
jingyan.baidu.com
部分门户的转载号（搜狐等，常见"整合包十大排行"式文章）
```

### 判据（三条，很好用）

1. **有没有版本号？** 真文档会说"BodySlide 5.8.2""SKSE 2.2.6"。
2. **有没有文件路径？** 真文档会说 `Data\SKSE\Plugins\CharGen\Presets\`。
3. **有没有指向发版者的链接？** 真文档会链到 Nexus mod ID 或 GitHub 仓库。

三条都答不上来的，**无论写得多漂亮都不用**。

## 二、本领域已知的"错误知识"清单

以下说法在本轮调研中被判定为**错误或被误传**，请勿采信：

| 说法 | 实际情况 |
|---|---|
| **RaceMenu 需要 PapyrusUtil** | **不需要**。RaceMenu 只要求 SKSE64，`skee64.dll` 自带 NiOverride 与 CharGen |
| **RaceMenu 的 morph 滑块范围是 -1 到 +1** | **不准确**。`.jslot` 里存的是浮点（实测样例 `0.50000`）；滑块上限由 `RaceMenuMorphs*.psc` 的 `OnSliderRequest` 中 `Float factor` 决定（社区记录默认 `2.0`）。**以实际界面为准** |
| **BodySlide 预设可以直接当 RaceMenu 预设用** | **不能**。`.xml`（0~100，每个滑块存体重 0 与 100 两个值）与 `.jslot`（浮点 `bodyMorphs`）格式、刻度、生效方式都不同，只能逐滑块手工换算 |
| **手动拖 RaceMenu 滑块能改变 NPC 身材** | **不能**。运行时 morph 只作用于玩家。NPC 要靠 BodyGen / OBody NG / AutoBody 分配，或给单个 NPC 做专属裸体网格 |
| **BodySlide CLI 有 `-o` / `-m` 参数** | **不存在**。现行参数是 `--groupbuild` / `--build` / `--filter` / `--targetdir` / `--preset` / `--trimorphs` 等 |
| **HPH 的作者是 Kalilies** | **不是**。是 **KouLeifoh（KLF）** |
| **`modding.wiki` 是 STEP 的 Skyrim SE 指南** | **不是**，该域名相关页面 404；STEP 官方 wiki 是 `stepmodifications.org` |
| **HDT-SMP 的仓库是 `hydrogensaysHDT/hdt-skyrim-smp`** | **错**，实测 404；正确是 **`hdt-skyrimse-mods`** |
| **Skyrim Outfit System 是"给 NPC 分配身形"的工具** | **不是**。它是外观/换装系统。分配身形的是 **BodyGen / OBody NG / AutoBody** |
| **SPID 的 Outfit Distribution 能分配身形** | **不能**，它分配的是**服装** |
| **The Eyes of Beauty SE 的版本是 10.x** | **10.x 是 LE 的版本号体系**；SE 官方移植是 **1.2** |
| **CBPC 可以做头发/衣服物理** | **不能**。头发与衣物必须用 HDT-SMP / FSMP |
| **"九大猫 / 醉梦 / 陶德"是整合包** | 检索后**均未确认存在**（详见 [`../07-workflow/chinese-modpacks.md`](../07-workflow/chinese-modpacks.md)） |

## 三、⭐ 未确认事项清单（明确标注，勿当现状）

以下各项在本轮调研中**未能取得可靠来源**，条目中已相应标注：

| 事项 | 状态 |
|---|---|
| **CBBE SE 当前最新版本** | 二手来源给出 1.6.1 与 1.6.2，**不一致**；Nexus 页在内容墙后 |
| **BHUNP SE 当前最新版本 / 维护状态** | **未确认**（LE 官方文件可见 1.41V） |
| **CBBE 3BA 当前最新版本** | 仅确认到 2.45 左右；存在 3BAv2 迭代 |
| **CBPC 确切最新版本** | 社区提及约 1.6.x，**未确认** |
| **XP32 / XPMSSE 5.06 的 changelog 细节** | 来自镜像站转述，**非 Nexus 原文** |
| **Brows（Aesthetic）版本** | 4.0.1 与 4.1.0 两种记录，**未确认唯一最新值** |
| **KS Hairdos 发型数量** | 983 与 883 两种口径，统一表述为"约 980+" |
| **"BHUNP" 的正式展开式** | 社区读作 "UNP Bearer" 等，**官方未给** |
| **Facelight Plus 的 Nexus 发布状态与作者** | 仅见社区指南站，**未确认** |
| **Better Lighting for Face Light / Facelight Plus 的 Nexus ID** | **未确认** |
| **AutoBody 与 OBody NG 的先后/取代关系** | 社区说法不一致，**未确认** |
| **"Vector Plexus 原域名失效"** | 社区传言，**未确认**；稳妥来源是 Wabbajack 白名单 GD |
| **Actor 的 `GetNthHeadPart` / `SetNthHeadPart` 函数页** | 仅见于 CK wiki **示例**，未单独确认 |
| **RaceMenu 的 1.7.99 / CommonLibSSE-NG 版本是否已发布** | 作者帖中的**计划**，未确认已发布 |
| **RaceMenu morph 滑块的精确上下限** | 社区记录由 `OnSliderRequest` 的 `factor` 决定（默认 2.0），但该讨论针对 `RaceMenuMorphsUUNP.psc`，**未在 CBBE 版脚本上确认** |
| **「拖 morph 只对玩家与 EFF 随从直接生效」** | **未找到来源支持**。可确认的只有「只影响玩家」；给单个 NPC 固定身材的途径是「构建专属裸体网格 + ArmorAddon + 设为裸体皮肤」（社区经验） |
| **CK 官方站在本轮检索时停机** | 骨骼系统条目因此缺少一手官方引文，**待补** |

## 四、为什么要把这一条写进资料库

因为**转述失真**在这个领域特别严重：

- 版本号在搬运过程中会被"顺手改新"；
- 一个 mod 的依赖清单会被加上它其实不需要的前置；
- 作者名会被就近联想成另一个知名作者（如 KouLeifoh → Kalilies）。

**踩过的坑不要踩第二遍。** 新增条目时如果发现本清单里的某一项可以确认了，
请**直接更新本条目**（提升 `version`），而不是在别处悄悄写一个不同的说法。

## 来源

- 上表中"实际情况"列的各项，其依据均已写在各对应条目的"来源"小节中 ——
  请沿条目内的引用逐条复核
- 排除域名清单：**本工作区检索过程中识别（2026-09-22）**
- "三条判据"：**本工作区总结的方法论**
