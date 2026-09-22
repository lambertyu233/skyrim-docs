---
id: skse-plugin-frameworks
title: SKSE 插件框架：PapyrusUtil / JContainers / MCM Helper / po3 Extender
category: 01-prerequisites
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [前置, 框架, PapyrusUtil, JContainers, MCM Helper, po3]
aliases: [papyrus extender, 前置框架, skyui]
source: https://www.nexusmods.com/skyrimspecialedition/mods/13048
summary: 捏脸与身形类 mod 常要求的四个框架库各自做什么，以及一个被广泛误传的点：PapyrusUtil 并不是 RaceMenu 的前置。
---

# SKSE 插件框架

这些不是"身形 mod"，而是被身形/捏脸 mod **当作前置引用**的通用库。
它们自身不产生外观变化，但缺了会让宿主 mod 静默失效。

| 框架 | 作者 | 作用 | Nexus |
|---|---|---|---|
| **PapyrusUtil SE** | exiledviper（维护）、meh321（原始） | `StorageUtil` 数据存储、`JsonUtil`、`MiscUtil` 等原生函数 | 13048 |
| **JContainers SE** | ryobg（SE 移植） | 给 Papyrus 提供 JSON 数据结构与持久化 | — |
| **MCM Helper** | Parapets | 简化 MCM 创建、持久化 INI 设置、热键注册 | 53000 |
| **powerofthree's Papyrus Extender** | powerofthree (po3) | 扩展 Papyrus：官方口径 **374+ 新函数、37 事件** | 22854 |

- **PapyrusUtil 4.6 起已支持 1.6.1170**；4.1+ 需要 Address Library。
- **po3 Extender 的依赖链是**：SKSE64 + Address Library + powerofthree's Tweaks（注意是三层）。
- **MCM Helper 的依赖**：SKSE64 + Address Library + SkyUI。
- **SkyUI** 本身是 MCM 与搜索界面的载体，几乎所有带配置菜单的 mod 都要求它。

## ⚠️ 一条被广泛误传的前置关系

> **PapyrusUtil 不是 RaceMenu 的前置。**

RaceMenu 的 Nexus 发布页只列 **SKSE64**。RaceMenu 的 `skee64.dll` 自带
**NiOverride** 与 **CharGen** 两套实现（2.7+ 起 CharGen Extension 已完全并入本体，
若你曾单独装过 CharGen Extension，作者明确要求**卸载它**）。

PapyrusUtil 会出现在"依赖清单"里，是因为**别的** mod（部分身形、高跟、动画类）需要它 ——
把它记在 RaceMenu 名下会导致排错时找错方向。

### 版本不匹配时该删的散装脚本

RaceMenu 自带的这些 `.pex` 若在别处残留旧版本，会引发版本冲突提示，应删除：
`CharGen.pex` / `NiOverride.pex` / `RaceMenu.pex` / `RaceMenuBase.pex` /
`RaceMenuLoad.pex` / `RaceMenuPlugin.pex`。

## 一个实用的判断法

看到一个 mod 报"缺前置"，别急着找同名 mod 装上。按这条链往上追：

```
宿主 mod → 需要哪个框架 → 那个框架又需要什么 → 有没有 Address Library
```

**框架类问题的症状高度同质**：菜单不出现、设置不保存、脚本静默不执行。
这类症状的排查顺序永远是"版本与前置"，而不是"冲突"。

## 来源

- PapyrusUtil SE：`https://www.nexusmods.com/skyrimspecialedition/mods/13048`（4.6 支持 1.6.1170、4.1+ 需 ADL）—— **一手**
- powerofthree's Papyrus Extender：`https://www.nexusmods.com/skyrimspecialedition/mods/22854`（函数/事件数量、依赖链）—— **一手**
- MCM Helper：`https://www.nexusmods.com/skyrimspecialedition/mods/53000` —— **一手**
- JContainers SE 版本信息：Wildlander 清单交叉印证 —— **社区经验**
- **PapyrusUtil 非 RaceMenu 前置、CharGen Extension 须卸载、应删除的散装 `.pex`**：
  RaceMenu 发布页与作者 FAQ —— **一手（本工作区在撰条目时对 RaceMenu 描述页做了逐句核对）**
