---
id: racemenu
title: RaceMenu（捏脸核心）
category: 02-face
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [捏脸, RaceMenu, 滑块, CharGen, NiOverride]
aliases: [rm, 捏脸工具, 捏脸界面, showracemenu, skee, 滑块界面]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: RaceMenu 的功能、前置、morph 与雕塑机制、控制台命令、内置补光与高分辨率战纹设置，并澄清它不依赖 PapyrusUtil。
---

# RaceMenu

作者 **expired6978**。Nexus SE 版：`https://www.nexusmods.com/skyrimspecialedition/mods/19080`
（LE 旧版：`mods/29624`，末版 3.4.5）。

它把原版那个简陋的捏脸界面换成**可搜索、可分类、有数值、能存预设、能编辑 NPC** 的完整工具，
是整个捏脸生态的地基。

## 前置

**只要求 SKSE64。** 主文件对应 SKSE64 **2.2.6**（AE 1.6.1170）。

- RaceMenu **不依赖 PapyrusUtil**（常见误传，见
  [`../01-prerequisites/skse-plugin-frameworks.md`](../01-prerequisites/skse-plugin-frameworks.md)）。
- 从 **2.7** 起 **CharGen Extension 已完全并入本体**。作者 FAQ 原文意思：
  如果你之前单独装过 CharGen Extension，**应当卸载**。
- 与本体内置模块重复的散装脚本应删除：
  `CharGen.pex` / `NiOverride.pex` / `RaceMenu.pex` / `RaceMenuBase.pex` /
  `RaceMenuLoad.pex` / `RaceMenuPlugin.pex`。

## 它内部是什么

RaceMenu 的主体是 SKSE 插件 **`skee64.dll`**，内含两个模块：

| 模块 | 作用 |
|---|---|
| **CharGen** | 角色创建界面本身（滑块、分类、搜索、雕塑） |
| **NiOverride** | 运行时叠加机制：应用 morph、纹理覆盖（overlay）、着色 |

源码在作者的合集仓库里：`https://github.com/expired6978/SKSE64Plugins`（子目录 `skee64`）。
提交记录中可见 "Update to 1.6.1170"、"Update RM to 1.7.99" 等 —— **这是核版本对应关系的一手材料**。

## 滑块是怎么来的

滑块本质是 morph 开关，而 morph 数据来自 `.tri` 文件（由 **BodySlide 勾 `Build Morphs`** 生成）。
所以"RaceMenu 里没有身形滑块"通常不是 RaceMenu 的问题，而是**没有构建 morph**。
机制详见 [`../00-overview/morph-and-nif-basics.md`](../00-overview/morph-and-nif-basics.md)。

界面上的改进包括：SkyUI 风格分类、**搜索过滤**、AARRGGBB 着色、数值显示、相机移动。

## 雕塑（Sculpt）

顶点级编辑，适合滑块的线性叠加做不出的细节：

| 工具 | 用途 |
|---|---|
| Inflate / Deflate | 沿法线鼓起或凹陷 |
| Smooth | 平滑 |
| Move | 拖拽顶点 |
| **Mask** | 限定编辑区域（**不影响导出**，仅作为编辑辅助） |
| History | 撤销历史 |
| Clear Sculpt | 清空雕塑 |
| **Import Geometry** | 导入雕塑几何（配合预设的 `.nif`） |

## 内置补光（不是 facelight mod）

RaceMenu.esp 自带 **Light On/Off**：在角色正前方生成白色光源，
仅用于**捏脸界面内看清脸部**。它不是独立的脸部照明 mod，出了菜单就没有。
需要常驻补光看 [`facelight.md`](facelight.md)。

## 高分辨率战纹

面部纹身/战纹默认 256，可在 `Data/SKSE/SKSE.ini` 加：

```
[Display]
iTintTextureResolution=2048
```

## 控制台命令（`skee`，0.4.13+）

```
skee reload tints                      重新加载 tint 数据
skee erase bodymorph|transforms|sculpt|overlays
skee erase bodymorph-cache
skee preset-save PATH                  导出到 Data/SKSE/Plugins/CharGen/Exported/PATH.jslot
skee preset-load PATH
skee dump bodymorph|transforms|itemdata
```

## 其它值得知道的细节

- **预设改成了 JSON**：`.jslot` 文件，旧二进制 `.slot` 仍可读但不再被写出。见
  [`racemenu-presets.md`](racemenu-presets.md)。
- **与 ECE 的关系**：基本可共存（先装 ECE 再装 RaceMenu），但**预设不互通**，且不建议两者同用。
  作者提供 CharGen Export 作为 ECE → RaceMenu 的迁移途径。
- **overlay NIF 的位置**：某些游戏版本更新后，旧的 overlay NIF 会引发崩溃。
  作者提示删除本地这些文件（由新版 BSA 提供）：
  `Data\Meshes\Actors\Character\Character Assets\` 下的
  `face_overlay.nif` / `body_overlay.nif` / `hands_overlay.nif` / `feet_overlay.nif`
  以及对应的 `*_magicoverlay.nif`。
- **部件标签（0.4.20.0 新增）**：可为部件打标签供搜索，
  路径 `Data/SKSE/Plugins/CharGen/Tags/<MODNAME>/parts.json` 与 `tags.json`；
  类型映射为 **Face=1, Eyes=2, Hair=3, Beard=4, Scar=5, Brow=6**。

## 来源

- RaceMenu Nexus 发布页（前置、ChGen 并入、JSON 预设、skee 命令、Sculpt、补光、tint 分辨率）—— **一手**
- RaceMenu Files 页与 changelog（0.4.19.16 = 1.6.1170；0.4.20.0）—— **一手**
- GitHub `expired6978/SKSE64Plugins`（`skee64` 源码与提交记录）—— **一手**
- 作者 Nexus 帖（overlay NIF 警告、CommonLibSSE-NG 迁移计划）—— **一手（但计划部分属"未发布"，标为未确认）**
