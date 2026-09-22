---
id: dark-face
title: 黑脸 / 黑头（Dark Face Bug）
category: 06-troubleshooting
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [排错, 黑脸, 黑头, FaceGen, 冲突]
aliases: [dark face, 脸变黑, npc 黑脸, 头像变黑, face discoloration]
source: https://www.nexusmods.com/skyrimspecialedition/mods/42441
summary: 黑脸的根本成因（FaceGen 数据与 head parts 不匹配导致 tint 被丢弃）、四种修法（运行时修复 / CK 重导 / 隐藏冲突文件 / 调序），以及为什么"左栏右栏不一致"是最常见的真因。
---

# 黑脸 / 黑头（Dark Face Bug）

## 症状

NPC（有时是玩家）的**头部变成黑/灰色**，身体正常。通常出现在装了多个 NPC 美化 mod 之后。

## 成因

引擎依赖 NPC 头部的**预处理 FaceGen 数据**：

```
Meshes\Actors\Character\FaceGenData\FaceGeom\<插件名>\<FormID>.nif
Textures\Actors\Character\FaceGenData\FaceTint\<插件名>\<FormID>.dds
```

当**这些 FaceGen 数据与插件里记录的 head parts 不匹配**时，
游戏会**重新生成脸，但丢弃 tint 数据 → 脸变黑**。

引发不匹配的三种典型情形：

1. **FaceGen 缺失或未导出**（改了 NPC 的脸却没 `Ctrl+F4`）；
2. **多个 mod 改同一 NPC 的脸且互相覆盖**；
3. ⭐ **MO2 左栏（资产优先级）与右栏（插件顺序）不一致** ——
   某 mod 赢了 NPC 记录（右栏），但 FaceGen 文件被别的 mod 覆盖（左栏），于是头部件与头网格对不上。

> **第 3 条是最容易被误判的一条。** 很多人会去怀疑"某个美化 mod 坏了"，
> 实际是自己排完 LOOT 后右栏变了、左栏没跟着对齐。

## 修法

### ① 运行时修复（最快，治标）

装 **Face Discoloration Fix**（作者 **Parapets**，仓库所有者 **Exit-9B**）：

- Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/42441`
- 仓库：`https://github.com/Exit-9B/Face-Discoloration-Fix`（**MIT**）
- 版本 **1.0.4**（更新到 Address Library 12，静态链接 VC++ Runtime）；
  历史：1.0.3 支持 1.6.629+，1.0.2 支持 1.6.318+，
  1.0.1 修了坏 race（RNAM）数据导致的启动崩溃并加 VR 支持。

**它的做法**：阻止游戏在重新生成脸时丢弃 tint 数据，让重生成的颜色正确。
等价于 **CK 的 `Ctrl+F4` 的运行时版本**。

**代价**：实时生成 FaceGen 比加载预处理慢 ——
作者测得预处理约 **0.2 ms/NPC**，实时生成约 **30–70 ms/NPC**。

**限制**：它**只修变色**。如果 load order 冲突破坏了 NPC 美化 mod，
它无法恢复原貌 —— **根因还在**。

### ② Creation Kit 正本清源（治本）

1. 加载相关插件（`CreationKit.ini` 需允许加载多个 master）；
2. Objects → Actors → Actor，**在子树里直接选中**目标 NPC（不要用搜索选 `*All*`）；
3. **`Ctrl+F4`** 导出 FaceGen。

### ③ MO2 隐藏冲突 FaceGen

- 在 MO2 的 **Conflicts** 里找覆盖者；
- 按 FormID 搜冲突的 `.nif` / `.dds`，把它们 **hide** 掉，
  确保 FaceGen 来自正确的美化 mod；
- 同时检查插件顺序，让该美化 mod 的 NPC 记录优先。

### ④ 调序 / 打补丁

- 让 NPC 美化 mod 位于"修改该 NPC 数据"的 mod **之后**；
- 多个 NPC 美化共存时，用 SSEEdit 逐个做 patch（合并外观记录 + 对齐 FaceGen）。

社区另有一份专门的 **Black-Face Patching Guide**（Nexus `mods/17004` 的 PDF 附件）。

## 一个重要的认知

> **CK 的 `Ctrl+F4` 会把脸重置回"当前插件数据所描述的脸"。**
> 如果你先装了美化 mod 再导出，得到的是美化后的脸；
> 但如果导出时冲突资源没理顺，你可能把脸**导成了原版样**。
> 所以 `Ctrl+F4` 不是"万能修复键"，它是"按当前数据重新生成"。

## 来源

- 成因（FaceGen 与 head parts 不匹配 → 丢 tint）与运行时代价：
  Face Discoloration Fix Nexus 页描述 + GitHub README —— **一手**
- FaceGen 路径与 `Ctrl+F4` 流程：CK wiki / UESP —— **一手**
- "左栏右栏不一致"这一成因：Nexus 论坛帖 —— **社区经验（多帖一致）**
- MO2 隐藏冲突 FaceGen：Black-Face Fix Guide（Nexus `mods/77338`、`mods/17004`）—— **社区经验**
- "`Ctrl+F4` 会重置为当前数据描述的脸"：**机制推论 + 社区一致经验**
