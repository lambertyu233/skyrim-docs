---
id: expressive-morphs
title: Expressive Facegen Morphs 与 Expressive Facial Animation
category: 02-face
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [捏脸, EFM, EFA, 表情, morph]
aliases: [expressive facegen morphs, 表情包, 面部表情, niroku]
source: https://www.nexusmods.com/skyrimspecialedition/mods/35785
summary: 作者 Niroku 的三个面部 morph / 表情 mod 的分工、目标种族、两个文件的区别，以及"只影响玩家、不影响 NPC"这一关键限制。
---

# Expressive Facegen Morphs 与 Expressive Facial Animation

作者 **Niroku**（Nexus 用户 35150865）。三个 mod 分工容易混：

| mod | Nexus | 版本 | 作用 |
|---|---|---|---|
| **Expressive Facegen Morphs SE（EFM）** | 35785 | 1.0.0 | 替换人类/精灵的**角色创建 morph**，并为 RaceMenu 增加滑杆 |
| **Expressive Facial Animation -Male-**（EFA-M） | 19532 | 1.21 | 替换男性**表情 morph**（嘴唇/眉毛/眼睛的运动） |
| **Expressive Facial Animation -Female-**（EFA-F） | 19181 | 1.7 | 女性版 |

**一句话区分**：EFM 管"你捏出来的静态脸长什么样"，EFA 管"这张脸动起来什么样"。

## EFM

- 是 **ESL 插件**：`Expressive Facegen Morphs.esl`。
- **目标种族**：Nord、Imperial、Breton、Redguard、Elder、High Elf、Dark Elf、Wood Elf、Dremora。
- **机制**：morph（`.tri`）移动目标网格顶点，既用于角色创建也用于表情。
- 新增滑杆名带连字符（如 `Lip-Height`），在 RaceMenu 搜索框搜 **`EFM`** 可以筛出来。
- 设计目标是**平滑变形**，复杂组合也不破网格，并保证与 EFA 兼容。

### EFM 的两个文件（关键）

| 文件 | 用于 | 说明 |
|---|---|---|
| 主文件 `Expressive Facegen Morphs` | **新预设** | 含 CharGen + Race morphs、额外滑杆、meshes。**与现有预设不兼容，装前备份脸部数据** |
| 可选 `EFM - Racemenu Plugin` | **现有预设** | 只含额外 RaceMenu 滑杆，不动既有 morph |

选错文件就会得到"预设全乱"或"滑杆不出现"两种相反的结果。

## EFA 的注意事项

- **EFM 的 RaceMenu 表情滑杆不受 EFA 影响**：EFA 不引用 EFA 自己的文件，
  角色创建时想预览表情需用控制台命令设表情（通常配 opparco mfg Command / **Mfg Fix**）。
- EFA **不兼容 Female Facial Animation**（改同一批文件）。
- EFA 针对**原版头部网格**；顶点数或顺序不同的头（**如 HPH**）需要各自的补丁。

## ⚠️ 最重要的限制：只影响玩家

> **EFM 与 EFA 只影响玩家角色，不影响 NPC。**

原因在机制层面：**NPC 的脸是 FaceGen 预生成网格**，不是运行时 morph 出来的。
所以"装了 EFM 但 NPC 脸没变"不是 bug，是设计。

## 与 HPH 的配合

- HPH 的 FOMOD 里有 **Expressive Facegen Morphs** 选项（第 07 项）；
- 加载顺序：**HPH 在前，EFM 在后**。

## 来源

- 三个 mod 的 ID / 版本 / ESL / 目标种族 / 搜索词 / 两个文件区分：
  作者 Nexus 用户文件页与各发布页描述 —— **一手**
  （`https://www.nexusmods.com/skyrimspecialedition/users/35150865?tab=user+files`）
- "只影响玩家、NPC 用预生成网格"：EFM 发布页描述 —— **一手**
- "EFM 滑杆不受 EFA 影响"、需 Mfg Fix 设表情、与 Female Facial Animation 冲突：
  EFM / EFA 发布页描述 —— **一手**
- "HPH 需在 EFM 之前加载"：预设包作者说明 —— **社区经验**
