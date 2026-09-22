---
id: preset-not-applied
title: 预设不生效 / 脸变回默认
category: 06-troubleshooting
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [排错, 预设, jslot, 存档, 依赖]
aliases: [预设不生效, 脸变回默认, 预设没用, preset 不加载, 导入预设无效, 存档脸变了]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: 预设不生效的六类原因（依赖资源缺失、放错目录、HPH 未选、未保存应用、morph 未构建、存档 co-save 不一致）与逐项核对表。
---

# 预设不生效 / 脸变回默认

## 检查清单

### 1. 预设依赖的资源是否装齐 ⭐

这是**第一位**的原因。预设只存"滑块值与 head parts 引用"，
它引用的**头发 / 眼睛 / 眉毛 / 皮肤 / HPH** 必须已经安装并启用。

- 缺头发 → 发型回退默认或变光头；
- 缺眼睛/眉毛 → 对应部件丢失或变紫红；
- 缺皮肤 → 脸色不对。

**预设作者的要求清单就是必装清单。**

### 2. `.jslot` 是否放对目录

```
Data\SKSE\Plugins\CharGen\Presets\
```

放错目录 → 预设下拉里根本看不到它。

### 3. High Poly Head 是否被选中

HPH 预设的常见现象是"**脸是尖的 / 不像截图**" ——
解决：到 Head 页把 **Face part 从 1 切到 3（HPH）**。

### 4. 是否真的保存并应用了

在 RaceMenu 里调完滑块后**没有 Save / 应用** → 当然不生效。

### 5. 身形 morph 是否已构建

预设里的身形部分依赖 `.tri`。
BodySlide 没勾 `Build Morphs` → 身形部分无效（但脸的部分可能正常）。

### 6. 存档与当前 mod 是否一致 ⭐

**morph 与 tint 状态存在 SKSE co-save 里。**
中途增删身形 / 皮肤 / 预设类 mod，旧档可能与新配置对不上。

表现：新角色用预设正常，**读旧档就变回默认**。

### 7. 带雕塑的预设是否导入了几何

若预设附带 `.nif`（雕塑几何），需要去 **Sculpt → Import Head** 手动导入。

## 一张核对表

```
[ ] 依赖资源（发/眼/眉/皮/HPH）已装且启用
[ ] .jslot 在 CharGen\Presets\
[ ] HPH 已在 Head 页选中
[ ] 已在界面里 Save / 应用
[ ] BodySlide 勾了 Build Morphs 并重建
[ ] 是新档，或确认存档与当前配置一致
[ ] 有 .nif 的话已 Import Head
```

## 一个常被搞混的点

> **"预设不生效"和"预设效果和截图不一样"是两回事。**

- 完全不生效 → 查上面的清单；
- 生效了但不一样 → 通常是**资源版本不同**（作者的眉毛是 v2.1、你装的是 v4.0）
  或 **资源缺失导致部分回退**。仔细比对作者的要求清单。

## 来源

- 依赖资源缺失、放错目录、HPH 未选、需重开 `showracemenu`：
  LoversLab 与 Nexus 论坛预设帖 —— **社区经验（多帖一致）**
- `.jslot` 路径与 `skee preset-save/load`：RaceMenu 发布页与 changelog —— **一手**
- 需要 Import Head：RaceMenu 发布页（Sculpt 的 Import Geometry 功能）—— **一手**
- co-save 存储 morph 状态：BodyGen 文档与 NiOverride 机制 —— **社区文档（引作者原话）+ 一手机制**
- "预设效果不同"与"预设不生效"要分开："**机制推论**"
