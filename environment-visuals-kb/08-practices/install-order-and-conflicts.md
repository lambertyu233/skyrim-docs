---
id: install-order-and-conflicts
title: 安装顺序与冲突覆盖原则
category: 08-practices
version: 1.0.0
updated: 2026-10-22
tags: [安装顺序, 覆盖, 冲突, LOOT, 补丁]
kind: tutorial
source: https://www.nexusmods.com/skyrimspecialedition/mods/2347
summary: 材质层"后装赢"、插件层按作者指定、天气/水/草/树四类"一次一个"；冲突不全靠 LOOT，读取每个发布页的 Load Order 段。
aliases: [load order, 排序, 覆盖规则, 冲突解决, mod 顺序]
---

# 安装顺序与冲突覆盖原则

## 两条正交的秩序

| 层 | 裁决规则 | 工具 |
|---|---|---|
| **资源**（贴图/网格/音效） | **后装赢**（同路径），松散文件永远赢 BSA | MO2 左侧顺序 + 安装时"是否覆盖" |
| **插件**（ESP/ESM） | **按作者指定**，LOOT 只能排序不能裁决资源 | LOOT + 手动规则 |

**LOOT 只管插件顺序，不管资源覆盖**（已在 `skyrim-tools-kb` 的
`12-sources/common-misconceptions.md` 记录）——材质冲突必须在 MO2 里看。

## 四类"一次只装一个"（互斥域）

1. **天气**（Obsidian / Cathedral / NAT / CoT……）
2. **水**（RW2 / Water for ENB / Pure Waters）
3. **全境草**（Cathedral Landscapes / Folkvangr / Verdant / Tamrielic……）
4. **全境树**（HLT / EVT / NOTWL……）

依据均在各发布页：见[天气生态](../06-weather-lighting/weather-mods-overview.md)、
[草类生态](../04-flora/grass-mods-overview.md)、
[树木生态](../04-flora/tree-mods-overview.md)。

## 作者指定的顺序（一手源汇总）

- **先 SMIM，后贴图包**（SMIM 页："generally install SMIM first and then
  texture replacers"）。
- **202X 覆盖 SMIM**（202X 页："just overwrite SMIM"）。
- **MM 覆盖 SMIM 网格**（MM readme：MM 面数更高）。
- **MM 主 esp 在本 mod 其它部件之上**；`MajesticMountains_Landscape.esm`
  与改地形 ESM 冲突时把 ESM 上放。
- **Landscape Fixes 顶部**且早于改地形高度的 mod（Bethesda.net 页）。
- **Verdant 覆盖 SFO**（"install AFTER SFO and let it OVERWRITE ALL"）。
- **NAT 必须置底**（"mandatory to use it at the very last position"）。
- **Water for ENB**：esm → Landscape Fixes 补丁 → 主插件 → 其它补丁 → FWMF 补丁。
- **HLT → Aspens Ablaze**（STEP 论坛：Aspens 插件在 HLT 后）。
- **Skyland Watercolor ESP** 放在 RW2/iNeed/Water for ENB **之后**。

## 补丁从哪来（一手源）

1. mod 自己的 Files 页（可选文件/补丁）；
2. Synthesis patcher（Water for ENB、MEZF 等官方推荐）；
3. xEdit 手搓（转发记录）；
4. 补丁 hub（Lux patch hub、QUASIPC 等）。

## 常见错误（社区经验）

- 用 LOOT 排序后不管资源冲突 → 贴图"赢了插件输了资源"。
- 覆盖提示一律"否" → 底座 mod 反而压住主包。
- 补丁装完不更新 LOOT → 插件顺序回退。

## 相关

- 覆盖机制底层 → `mo2-usvfs-kb`；排序原理 → `mo2-usvfs-kb/05-usage`
- [性能预算](performance-budget.md)、[LOD 生成完整流程](lod-generation-workflow.md)
