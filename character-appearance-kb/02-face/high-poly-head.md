---
id: high-poly-head
title: High Poly Head（高模头部）
category: 02-face
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [捏脸, 高模头, HPH, 脸部网格]
aliases: [high poly head, 高模头部, klf, 头部网格]
source: https://vectorplexus.com/files/file/283-high-poly-head/
summary: 高模头的作者、分发渠道、与 RaceMenu 的配合方式、以及 NPC 使用它必须重导 FaceGen 的流程与已知坑。
---

# High Poly Head

作者 **KouLeifoh**（缩写 **KLF**），版本 **1.4**。

> **别把它认成 KS Hairdos 的作者 Kalilies。** KLF = KouLei**f**oh。这个名字在多个 mod 的
> credits 里以 "KLF's High Poly Head" 形式出现，是同一人。

## 分发渠道（重要）

**本体不在 Nexus。** 官方源是 **Vector Plexus**：`https://vectorplexus.com/files/file/283-high-poly-head/`
Nexus 上只有**各类补丁与镜像**，例如：

| mod | Nexus | 性质 |
|---|---|---|
| High Poly Head For Custom Races | 43098 | 补丁 |
| Brows by Hvergelmir for High Poly Head - COTR - UBE | 63777 | 眉毛适配补丁 |
| Alternate High Poly Head | 148541 | 镜像，其 credits 明写 KouLeifoh 为原作者 |

> 社区有"Vector Plexus 原域名失效"的说法 —— **未确认**。
> 稳妥的备用来源是 **Wabbajack 白名单里作者备份的 Google Drive 链接**。

## 它是什么

基于**原版头部网格**的高模男女头部，并附带**互补的高模 brows / beards / scars / hair** 以适配新头型。
它提供 RaceMenu 扩展滑杆所需的 morph，并**兼容基于原版头部的纹理**。

## 与 RaceMenu 的关系

**硬前置是 RaceMenu。** 使用方式是：

> 在 RaceMenu 里到 **Face Part** 滑杆 / Head 页，把头部部件**切换为高模头**。

**它不是自动生效的。** 这是"装了 HPH 但没效果"的最常见原因。

## NPC 要用 HPH：必须重导 FaceGen

NPC 的头是**预生成**的（见 [`facegen-pipeline.md`](facegen-pipeline.md)），所以要让 NPC 用 HPH：

1. 让 HPH 成为该 NPC 所在插件的 **master**；
2. 把 NPC 的原版 head parts 替换为 HPH 部件；
3. 在 Creation Kit 里选中该 NPC → **`Ctrl+F4`** 重新导出 FaceGen。

> **限制**：对 **sculpted head mesh（带雕塑几何的头）无效** —— 只能对已导出的静态头网格替换。

## 与 ECE 的关系

**HPH 不兼容 ECE。** 两者都改头部网格，方向冲突。
社区共识是"装了 HPH 就不要装 ECE，ECE 自带的平滑功能用不上了"。
另外 **ECE、RaceMenu、EFM 三者用不同的种族 morph**，基础脸型不同，**预设不能简单互通**。

## 安装选项与坑

FOMOD 里常见的可选项（节选，来自镜像站对 1.4 安装项的转述）：

```
00 Base（必选）
01 Loose files for FaceGen in CK        在 CK 里导 FaceGen 需要
02 no Dawnguard DLC
03 vampire head fix
04 remove sunken vampire face morphs
05 symmetrical eye sockets (female)
06 Aesthetic Elves
07 Expressive Facegen Morphs            与 EFM 配套
08/09 EFA Male / EFA Female
10 High Poly Vanilla Hair
```

**社区记录过的坑**：

| 现象 | 处理 |
|---|---|
| 头部变黑/变暗 | 改一下 player weight，强制刷新皮肤着色器 |
| 眼睛闪烁或渲染异常 | 关闭 RaceMenu 再重开 |
| 切到吸血鬼种族后头被重置 | 用 vampire head fix 选项 |
| 与原版部分头发轻微穿模 | 已知问题 |
| SE 下眼睛/疤痕偏暗 | 同上，改 weight 通常可解 |

配套补丁常见：High Poly Head UV Stretch Fix（脖缝）、Bone Weight Fix、
Vanilla Presets Fix、Brows for HPH、LDD Better Eye Shape for HPH。

## 加载顺序

**HPH 要排在 Expressive Facegen Morphs 之前** —— 这是预设包作者给出的经验顺序
（社区经验，但与常见排序实践一致）。

## 来源

- 作者归属（KouLeifoh / KLF）：Alternate High Poly Head 的 credits 与 PC Gamer 署名 —— **一手（credits）+ 二手（媒体）**
- 原站与版本 1.4：`https://vectorplexus.com/files/file/283-high-poly-head/` —— **一手**
- 前置 RaceMenu、Face Part 切换、含互补高模部件、兼容原版纹理：**一手（发布页描述）**
- NPC 需 CK `Ctrl+F4` 重导、对 sculpted head 无效、FOMOD 选项：**社区经验（Nexus 论坛 / 镜像站转述安装项）**
- 安装坑（变黑/闪烁/穿模/吸血鬼重置）：**社区经验（Nexus 论坛、GameMale、tesgeneral）**
- "HPH 不兼容 ECE"、"ECE/RaceMenu/EFM 用不同种族 morph"：**社区经验（指南与搬运帖）**
- 加载顺序 HPH 先于 EFM：**社区经验（预设包说明）**
