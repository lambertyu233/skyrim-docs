---
id: overlay-nif-ctd
title: 启动/捏脸崩溃：RaceMenu overlay NIF
category: 06-troubleshooting
kind: reference
version: 3.0.0
updated: 2026-10-25
tags: [排错, 崩溃, CTD, RaceMenu, overlay, 1.7]
aliases: [overlay nif, 启动崩溃, 捏脸崩溃, 进游戏就崩, 捏脸界面崩溃, 更新后崩溃, 1.7 崩溃, nif 解析, 八个 nif, nitrishape, character assets, 启动 CTD]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080?tab=posts
summary: 1.7.x 更新后启动/捏脸必崩的一手根因（Bethesda 改坏 NIF 解析，含 NiTriShape 但无 NiTriShapeData 的网格会崩，而 RaceMenu 的 overlay nif 全是这种）、8 个待删文件的完整清单与查找方法、与 SKSE 版本问题/mod 冲突的误诊分叉，以及"大版本更新后崩溃先清空 SKSE Plugins"的通用排错动作。
---

# 崩溃：RaceMenu overlay NIF

> **一句话**：升级 1.7.x 后启动或进捏脸就崩，**先别怀疑任何 mod 冲突**——
> 大概率是磁盘上残留的 8 个旧版 overlay nif。删掉它们，新版已打包进 BSA。

## 速览

| 项 | 内容 |
|---|---|
| 症状 | 更新到 **1.7.x** 后，游戏**启动或进捏脸界面时崩溃**；可能伴随 RaceMenu 报错，也可能直接退出 |
| 根因 | Bethesda 改坏 NIF 解析：**含 `NiTriShape` 但没有 `NiTriShapeData` 的网格会崩**——RaceMenu 的 overlay nif 全是这种 |
| 首选判据 | 1.7.x + 捏脸相关环境 + 启动即崩；**旧 overlay nif 在磁盘上存在**即必崩 |
| 最短修复路径 | 删除 / 隐藏 `Data\Meshes\Actors\Character\Character Assets\` 下的 **8 个文件** |

要点：

- **作者原话**：**"If you have older versions of these files locally, your game WILL crash."**
- **对策是删除，不是补文件**：新版已把这些文件打包进 BSA 以绕过该问题。
- **与 mod 冲突无关**：即使不装新 RaceMenu，残留旧 overlay nif 也会崩。
- **版本不对通常不崩**：SKSE 插件版本不匹配的典型表现是**静默失效**（功能消失），
  崩溃优先查 NIF。
- 通用原则：**游戏大版本更新后崩，先把 `Data/SKSE/Plugins` 清空做二分**。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 2026-08-14 | SKSE 官网首页警告："After two and a half years, Bethesda has announced an incoming update to Skyrim." | 事件起点（一手：SKSE 官网） |
| 2026-08-19 | SKSE64 **2.2.7** 上传，**仍面向 1.6.1170**（提供 plugin preloading） | 暴风雨前的平静 |
| 2026-08-20 | 游戏 **1.7.99** 发布，SKSE64 **2.3.0** 同步 | 大批原生插件需要重编译 |
| 2026-08-21 | **Address Library v12**（面向 1.7.99.0）上传 | 依赖链开始跟进 |
| **2026-08-23** | **RaceMenu 作者发帖**：1.7.99 版已完成但被 SKSE 的 Papyrus 函数 bug 卡住；1.7.104 未做；转向 CommonLibSSE-NG 重写；**同帖首次说明 overlay nif 崩溃问题** | **本条目根因的出处（一手：作者本人）** |
| 2026-08-27 | 游戏 **1.7.104** 发布；SKSE64 **2.3.1**（含 "fix PlayerCharacter functions"）与 Address Library **v13** 同步 | RaceMenu 与官方的差距进一步拉大 |
| 2026-10 初 | Nexus RaceMenu 讨论区出现用户整理的置顶说明，称作者 **Patreon 上有 beta**（"RaceMenu AE NG"）；同时提醒装 beta 前必须先删/隐藏那 8 个旧 overlay nif | 非官方途径；**beta 可用性未确认** |
| 2026-10-25 | 本条目核实日：RaceMenu 官方 Files 页最新版本**仍为 0.4.20.0**，无 1.7.x 正式版 | 现状：1.7.x 无官方可用 RaceMenu |

### 它从哪来

这不是一个"mod bug"，而是 **Bethesda 一次更新引入的兼容性回退**。
前因是引擎网格格式的历史分层：LE 时代形状节点是
**`NiTriShape` + 单独的 `NiTriShapeData`**（几何数据分离）；
SE/AE 改成了 **`BSTriShape`**（形状与几何数据合并成单块）。
RaceMenu 的 overlay nif 属于"有形状节点、没有几何数据块"的老结构，
在 1.7.x 改坏的新解析逻辑下直接致命。

### 为什么比以前严重

以前的版本更新是"插件要重编译"；这一次**游戏本身的向后兼容变差了**——
连增量补丁都难以简单绕过，只能靠"把散文件删掉、让 BSA 提供"这种部署层面对策。

### 现状

1.7.x 上 RaceMenu 没有官方版；作者在做 CommonLibSSE-NG 重写
（完成时间未确认）。**依赖捏脸的用户应留在 1.6.1170 / 1.6.1179**，
完整决策树见 [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)。

## 根因（作者原文，一手）

Bethesda 在 1.7.x 里改坏了 Nif 解析的一个边界情况：

> "Bethesda broke a very edge case in their Nif parsing code, meshes with `NiTriShape`
> but no `NiTriShapeData` crash the game, these happen to be all of the 'overlay' nifs
> used by RaceMenu."

也就是说：**带 `NiTriShape` 却没有 `NiTriShapeData` 的网格会让游戏崩**，
而 RaceMenu 的 overlay 网格全都是这种结构。

### 格式分层背景（为什么偏偏是 overlay nif）

| 游戏 | 形状节点 | 结构 |
|---|---|---|
| Skyrim LE | `NiTriShape` + 单独挂一个 `NiTriShapeData` | 形状与几何数据**分离** |
| Skyrim SE / AE | **`BSTriShape`** | 形状与几何数据**合并成单块** |

RaceMenu 的 overlay nif 停留在"有 `NiTriShape`、没有 `NiTriShapeData`"的
老结构上；1.7.x 之前引擎对此宽容，1.7.x 改坏解析后直接崩溃。
这也解释了为什么**新版只要把文件打包进 BSA 就能绕过**——
被 BSA 正确提供的版本带上了引擎期望的结构。

> 这也是"文件格式细节至今仍能直接影响能否进游戏"的又一例证，
> NIF 容器与 morph 机制的完整背景见
> [morph-and-nif-basics.md](../00-overview/morph-and-nif-basics.md)。

## 处理：删掉这 8 个文件

作者明确要求：如果**本地磁盘上存在旧版本**的下列文件，**必须删掉**。
新版已经打包进 BSA，不再需要散文件。

```
Data\Meshes\Actors\Character\Character Assets\face_overlay.nif
Data\Meshes\Actors\Character\Character Assets\body_overlay.nif
Data\Meshes\Actors\Character\Character Assets\hands_overlay.nif
Data\Meshes\Actors\Character\Character Assets\feet_overlay.nif
Data\Meshes\Actors\Character\Character Assets\face_magicoverlay.nif
Data\Meshes\Actors\Character\Character Assets\body_magicoverlay.nif
Data\Meshes\Actors\Character\Character Assets\hands_magicoverlay.nif
Data\Meshes\Actors\Character\Character Assets\feet_magicoverlay.nif
```

> 作者原话：**"If you have older versions of these files locally, your game WILL crash."**

### 在 MO2 里怎么找

这类文件最常见的藏身之处是 **Overwrite 目录**，或者某个早期版本的
RaceMenu / 皮肤 mod。用 MO2 的"数据" tab 或右键 mod → 搜索文件名定位，
也可以在 `Data\Meshes\Actors\Character\Character Assets\` 下直接看。

- Overwrite 目录的定位方法见跨库
  [overwrite-dir](../../mo2-usvfs-kb/05-usage/overwrite-dir.md)；
- 定位到之后**删除或 hide**（隐藏方法见
  [hide-files-and-filetree](../../mo2-usvfs-kb/05-usage/hide-files-and-filetree.md)）；
- 装作者 Patreon beta 之前同样要先做这一步（社区整理说明）。

### 验证点

删/隐藏后重启游戏：能正常启动、能进捏脸界面（或至少回到"功能缺失但不崩"的状态），
即说明这 8 个文件曾是崩溃源。若仍崩，按下一节做通用二分。

### 处理流程（一图流）

```
更新到 1.7.x 后启动/捏脸即崩
  └─► 第一步：删/隐藏 Character Assets 下 8 个旧 overlay nif
        └─► 不崩了？            → 完事（新版已从 BSA 提供）
        └─► 仍崩
              └─► 第二步：清空 Data\SKSE\Plugins 做二分，逐个加回
                    └─► 加到某个插件时崩 → 该插件未适配 1.7.x，移除或等更新
                    └─► 清空后仍崩     → 已超出本条目范围，转通用崩溃排查
```

> 判断自己在哪一步的判据：**删掉 8 个文件前必崩、删后不崩** = overlay nif 问题；
> **删不删都崩** = 另有插件或环境问题，走第二步。

## 判断分叉点（别误诊）

| 看起来像 | 其实 |
|---|---|
| "RaceMenu 没更新所以崩了" | 部分是，但**即使不装新 RaceMenu，残留旧 overlay nif 也会崩** |
| "某个皮肤/妆容 mod 坏了" | 先确认是不是这 8 个文件被某个 mod 带进来了 |
| "SKSE 插件版本不对" | 版本不对通常是**静默失效**（功能消失）而不是崩溃；崩溃优先查 NIF |
| "1.7.x 下捏脸界面变回原版（但不崩）" | 这是 dll 没被加载的**无报错表现**，与 overlay nif 崩溃是两回事 |
| "mod 冲突，逐一禁用试" | 先删 8 个文件再二分——这是成本最低的一次排除 |
| "脸变黑" | 与崩溃无关，是 FaceGen 数据缺失——转 [dark-face.md](../06-troubleshooting/dark-face.md) |

## 更一般的排错动作

SKSE 官网给了一条通用建议，在本场景同样适用：

> "Having crashes on startup after a game patch? **Remove the files from `Data/SKSE/Plugins` and try again.**
> Mods using plugins probably need to be updated."

也就是：**游戏大版本更新后崩，先把 `Data/SKSE/Plugins` 清空一次做二分**，
再逐个加回。加回到崩溃的那个为止——多半是尚未适配 1.7.x 的 DLL。

配套的保守动作：

1. **升级前备份**整套 `Data` 与存档（降级手段本库不推荐，先备份再动手）；
2. 记录"当前各 DLL 版本 + 游戏版本"，它就是你的回滚清单；
3. 不要混用不同游戏版本的 bin/dll（Steam/GOG、SE/AE/VR 各不相同）；
4. 组件适配状态以 SKSE 官网与各 mod 的 Files / Posts 页为准，
   **不要信二手媒体清单**。

## 与其他库的一致性

`skyrim-tools-kb` 记录 SKSE64 与 Address Library 的版本矩阵，可与本条目交叉核对；
`community-shaders-kb` 记录 Community Shaders 支持 1.6.1170 / 1.6.1179 / 1.5.97、
明确**不支持** 1.7.99 / 1.7.104——与本文"1.7.x 生态尚未跟上"的判断一致。
本库内的版本决策入口是 [version-matrix.md](../00-overview/version-matrix.md)
与 [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)。

## 取舍与建议

- **依赖捏脸 → 留在 1.6.1170（Steam）/ 1.6.1179（GOG）**：这是当下成本最低的路；
- **已在 1.7.x 且不想降级**：至少把 overlay nif 清理做掉，并接受"捏脸回到原版"；
- **追 beta 要谨慎**：作者 Patreon beta 的存在来自社区整理说明，
  **可用性与适配版本未确认**，装前同样先删 8 个文件；
- **把这条当"版本更新标准动作"记**：以后每次 Bethesda 大更新，
  都先查"有没有新的解析层不兼容 + 各插件适配状态"。

## 来源

- **8 个 overlay nif 文件名、"NiTriShape 无 NiTriShapeData 会崩"、
  "旧版本残留必崩"、新版已打进 BSA**：
  RaceMenu 作者帖（2026-08-23）—— **一手（作者本人）**
  `https://www.nexusmods.com/skyrimspecialedition/mods/19080?tab=posts`
- **"更新后启动崩溃先移除 `Data/SKSE/Plugins`"**：
  SKSE 官网 Contact 段 —— **一手（SKSE 团队）** `https://skse.silverlock.org/`
- **1.7.x 时间线（2026-08-14 警告 / 08-19 SKSE 2.2.7 / 08-20 1.7.99 + SKSE 2.3.0 /
  08-21 Address Library v12 / 08-27 1.7.104 + SKSE 2.3.1 + v13）、
  RaceMenu 0.4.20.0 仍要求 1.6.1170、Patreon beta 的社区整理说明、
  "1.7.x 下捏脸变回原版是 dll 未加载的无报错表现"**：
  [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md) —— **本库整理（一手来源见该条）**
- **LE `NiTriShape` + `NiTriShapeData` vs SE `BSTriShape` 的格式差异**：
  Beyond Skyrim「Arcane University」NIF 技术文档与
  [morph-and-nif-basics.md](../00-overview/morph-and-nif-basics.md) —— **社区权威技术文档**
- **FSMP 4.1.1 面向的具体游戏版本**：**未确认**（Files 页日期一手，适配范围社区说法矛盾）
