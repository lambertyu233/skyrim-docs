---
id: bodyslide-outfit-studio
title: BodySlide and Outfit Studio
category: 03-body
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [身形, BodySlide, Outfit Studio, 构建, 滑块, 命令行]
aliases: [bs, os, 构建身形, 批量构建, batch build, 命令行参数]
source: https://github.com/ousnius/BodySlide-and-Outfit-Studio
summary: BodySlide 与 Outfit Studio 的分工、文件格式（.osp/.osd/SliderPresets.xml）、Build Morphs 的含义、以及官方命令行参数（并纠正几个不存在的参数）。
---

# BodySlide and Outfit Studio

作者 **Ousnius 与 Caliente**。**官方仓库**：`https://github.com/ousnius/BodySlide-and-Outfit-Studio`（GPLv3+）。

这是身形生态的"构建工具"。**不跑它，身形 mod 就只是素材。**

## 两者分工

| 工具 | 做什么 |
|---|---|
| **BodySlide** | 用滑块自定义身形/服装，并**批量构建**进游戏的 Data 目录 |
| **Outfit Studio** | 在身形之间转换服装、创建滑块、修正动画权重、用画笔/变换工具编辑网格、导入导出 FBX/OBJ/NIF |

日常用的 90% 是 BodySlide；要做"把某件老服装适配到我的身形"才需要 Outfit Studio。

## 版本

- 该工具是**跨游戏同一套**（Skyrim LE/SE、Fallout 4、Fallout 76 共用代码库）。
- 母页版本 **5.8.2**（FO4 Nexus，2026-06-25）。
- SE 专用发布页：`https://www.nexusmods.com/skyrimspecialedition/mods/201`。

## 文件格式

| 扩展名 / 名称 | 是什么 | 放在哪 |
|---|---|---|
| **`.osp`** | Outfit Studio Project / SliderSet。**纯文本 XML**，记录源文件与目标文件路径、哪些滑块影响哪些网格。**一个 `.osp` 可含多个项目** | `SliderSets/` |
| **`.osd`** | Outfit Studio Data。**二进制**，存放某项目所有网格的 morph 顶点数据（v3.0 引入，取代了此前成千上万的 BSD 小文件） | `ShapeData/<Project>/` |
| **`.nif`** | 所有滑块归零时的**基础形状**网格 | `ShapeData/<Project>/` |
| **`.xml`（SliderPresets）** | 预设：一组命名过的滑块值 | `SliderPresets/` |
| **`.xml`（SliderGroups）** | 预设的分组定义 | `SliderGroups/` |

## 滑块的含义

- **滑块 0 = 游戏内体重 0，滑块 100 = 游戏内体重 100**；
  预览窗口顶部那条对应游戏内体重滑条的中点。
- 可以手输负数或 >100，但**不推荐**（易扭曲、穿模）。

## Batch Build（批量构建）

构建所选分组内的全部 outfit。CLI 里对应 `--groupbuild`。

**输出文件冲突的处理**：BodySlide 通过 `BuildSelection.xml` 解决冲突，**输者被跳过** ——
所以"我构建了但没生效"有时是这里被静默跳过了。

## `Build Morphs` 复选框（最重要的一项）

> 勾选后，BodySlide 会生成 **`.tri` morph 文件**，并在 NIF 里写入 **`BODYTRI` extra data**，
> 使 RaceMenu / NiOverride 能在游戏内应用 morph。
> **无副作用，推荐始终勾选。**

不勾的后果：**RaceMenu 里没有对应的身形滑块**。
还要注意**构建产物不能被别的 mod 的 NIF 覆盖**，否则 `BODYTRI` 一起丢掉。

机制细节见 [`../00-overview/morph-and-nif-basics.md`](../00-overview/morph-and-nif-basics.md)。

## 与 RaceMenu 的联动

RaceMenu（`skee64.dll` 内含 NiOverride）读取 `.tri` 在捏脸界面/MCM 中应用身形 morph。前提三条：

1. 勾了 `Build Morphs`；
2. 构建的是 **3BA / 3BBB 变体**（如 "CBBE 3BBB Body Amazing"），而不是被普通 CBBE 覆盖；
3. 构建产物在最终的覆盖关系中胜出。

## 官方命令行参数

> ⚠️ **纠错**：流传较广的 `-o`、`-m` 参数**并不存在于当前官方 CLI**。
> 以下是官方 wiki 的现行参数。

### BodySlide

| 长参数 | 短参数 | 作用 |
|---|---|---|
| `--groupbuild <groups>` | `-gbuild` | 按分组批量构建并退出 |
| `--build <outfits>` | `-b` | 按名称构建指定 outfit（逗号/分号/空格分隔） |
| `--filter <filter>` | `-f` | 构建名称匹配的 outfit（默认大小写不敏感子串匹配） |
| `--regexfilter` | `-regex` | 把 `--filter` 当正则 |
| `--targetdir <path>` | `-t` | 构建输出目录（默认游戏 Data 路径） |
| `--preset <name\|file>` | `-p` | 启动时选预设；可配 `--groupbuild`/`--build`/`--filter` 构建，或配 `--preview` 预览。`file.xml?预设名` 可指定文件内某预设 |
| `--trimorphs` | `-tri` | 启用 tri morph 输出（等价于 GUI 勾 `Build Morphs`） |
| `--preview <files>` | — | 直接进入预览模式（支持 `.nif` 与 `.osp`） |

**官方示例**：

```
BodySlide --groupbuild "CBBE,CBBE Vanilla Outfits" --targetdir "C:\Output" --preset "CBBE Curvy" --trimorphs
BodySlide --build "CBBE Body"
BodySlide --preset "C:\MyPresets\MyBodies.xml?My Curvy Body"
```

### Outfit Studio

`--project` / `-proj`、`--single-instance` / `-single`、
`--automation` / `-a <script>`（无头运行自动化脚本），外加位置参数指定文件。

## 来源

- 分工、文件格式、CLI 参数、版本：**官方 GitHub 仓库 README 与 wiki** —— **一手**
  `https://github.com/ousnius/BodySlide-and-Outfit-Studio/wiki/Command%E2%80%90line-arguments`
- `.osp` / `.osd` 的区别：**ousnius 本人在 LoversLab 的解释** —— **一手**
- `Build Morphs` ↔ `.tri` / `BODYTRI` ↔ RaceMenu：官方仓库提交记录（"Write only a single BODYTRI extra data when building"）
  + 社区一致确认 —— **一手（机制）+ 社区经验（联动细节）**
- "`-o` / `-m` 不存在"：**与官方 wiki 参数表逐条比对后得出的纠错结论**，属本资料库的辨析
- `BuildSelection.xml` 冲突解析：官方 wiki —— **一手**
