---
id: racemenu-sliders-missing
title: RaceMenu 里没有滑块 / 滑块不能动
category: 06-troubleshooting
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [排错, RaceMenu, 滑块, morph, SKSE]
aliases: [没有滑块, 滑块缺失, 滑块不能动, sliders missing, racemenu 没反应, 身形滑块没有]
source: https://www.loverslab.com/topic/202366-racemenu-problem-sliders-absent-or-not-working
summary: 滑块缺失的六个原因（SKSE 版本、RaceMenu 版本、morph 未构建、esp 损坏、HPH 未选、需重开），按"整体缺失"与"只有身形滑块缺失"分流。
---

# RaceMenu 里没有滑块 / 滑块不能动

## 先分流

| 现象 | 主要嫌疑 |
|---|---|
| **所有滑块都没有**，界面像原版 | SKSE / RaceMenu 版本或安装问题 |
| **界面正常但没有身形滑块** | morph 未构建 / esp 未启用 |
| **界面正常但头部没变成高模** | HPH 未在 Head 页选择 |
| **滑块在但拖动无效果** | morph 数据缺失或被覆盖 |

## 完整检查清单

### 1. SKSE 版本与游戏版本是否匹配 ⭐

**这是最常见的原因。** 1.5.97 误用 AE 版 SKSE（或反之）
→ 所有 SKSE 插件 DLL 失效 → 滑块缺失或不动。

判断捷径：装 SkyUI，如果它弹 **"SKSE is not functioning properly"**，就是这一层的问题。

### 2. RaceMenu 版本是否匹配

AE 环境用旧版 RaceMenu → 没有（或只有部分）滑块。
对照 [`../00-overview/version-matrix.md`](../00-overview/version-matrix.md)。

### 3. morph 是否在 BodySlide 里构建了 ⭐（身形滑块）

**必须勾 `Build Morphs`**，否则不生成 `.tri` 与 NIF 里的 `BODYTRI`，
RaceMenu 无从显示身形滑块。

机制见 [`../00-overview/morph-and-nif-basics.md`](../00-overview/morph-and-nif-basics.md)。

### 4. morph 提供者 esp 是否启用

`RaceMenuMorphs*.esp`（如 `RaceMenuMorphsCBBE.esp`）需要启用。
它损坏也会导致对应滑块消失。

### 5. 构建产物是否被覆盖

BodySlide 构建出的 NIF 若被别的 mod 覆盖，`BODYTRI` 一起丢失 →
**身形滑块突然消失**。查 MO2 的 Conflicts。

### 6. High Poly Head 是否真的被选中（头部）

**HPH 不是自动生效的。** 要到 RaceMenu 的 **Head 页 / Face Part 滑杆**
把头部部件切换为高模头。

### 7. 是否需要重开捏脸界面

有时需要先建好角色，再 `showracemenu` 重开一次才加载。
SKSE 输入故障（zoom / light 不响应）也常常重开即解。

## 来源

- SKSE 版本不匹配为最常见原因、RaceMenu 版本、`RaceMenuMorphs*.esp` 损坏、
  morph 未构建、HPH 需手动选、重开 `showracemenu`：
  LoversLab 与 Nexus 论坛的 RaceMenu 滑块帖 —— **社区经验（多帖一致）**
- `Build Morphs` → `.tri` + `BODYTRI` → RaceMenu 应用：
  BodySlide 官方仓库提交记录 + wiki —— **一手（机制）**
- "构建被覆盖导致滑块消失"：**机制推论 + 社区经验**
- SkyUI 的 "SKSE is not functioning properly" 提示：SkyUI 行为 —— **一手（软件行为）**
