---
id: faster-hdt-smp
title: Faster HDT-SMP（FSMP）
category: 04-physics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [物理, FSMP, HDT-SMP, 多线程, 性能]
aliases: [faster hdt smp, hdt smp 加速, 物理性能, daymareon, 57339]
source: https://www.nexusmods.com/skyrimspecialedition/mods/57339
summary: FSMP 相对原版 SMP 的改动（多线程、ImGui 配置菜单、JSON 全局配置）、前置、1.6.1170 的档位选择，以及"它已完全取代原版"这条官方口径。
---

# Faster HDT-SMP（FSMP）

**现代用户应该装的 SMP。**

- Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/57339`
- GitHub：`https://github.com/DaymareOn/hdtSMP64`
- 上传者 **DaydreamingDay**，代码维护 **DaymareOn**

## Fork 链

```
hydrogensaysHDT（原版）
  → aers 版
    → Karonar1 的 hdtSMP64
      → DaymareOn 的 hdtSMP64（FSMP，当前主线）
```

## 相对原版的改动

| 项 | 改动 |
|---|---|
| **性能** | 官方描述：*"massively improves performance over the original HDT-SMP, and replaces it totally. Do not install [原版]"* |
| **并行** | 基于 Bullet 的**多线程**实现 |
| **配置界面** | 用 **SKSE Menu Framework（Dear ImGui）** 的内置菜单取代旧 MCM（旧 MCM 依赖 SkyUI / JContainers / PapyrusUtil / ConsoleUtil，现已移除） |
| **全局配置** | 从 XML 迁到 **JSON**（`configs.json` / `userConfigs.json`） |

## 前置

- **SKSE64**
- **Address Library for SKSE Plugins**（它用 CommonLibSSE 构建，CommonLibSSE 已内置地址库支持）
- 内置配置菜单用 SKSE Menu Framework（随包 vendor；**缺框架则菜单不显示，但物理照常工作**）

> 注意：FSMP 4.x **本身不再强制**需要 SkyUI / JContainers / PapyrusUtil / ConsoleUtil。
> 但**你装的其他身形 mod 可能仍需要**它们 —— 别因为这条就把它们全删了。

## 游戏版本档位（FOMOD）

| 游戏版本 | 对应 SKSE64 |
|---|---|
| **1.6.1170.0** | 2.2.6 |
| 1.6.659（GOG） | 2.2.2 |
| 1.6.640 | 2.2.2 |
| 1.6.353 | 2.1.5 |
| 1.5.97（SE） | 2.0.20 |
| VR | 2.0.12 |

**安装时必须在 FOMOD 里选对游戏版本档** —— 选错的典型表现是物理不生效或开局崩溃。

当前版本 **4.1.1**（2026-08-27）。

## 实用功能：`smp` 控制台命令

```
smp report [warnings] [gear]    校验整个 load order 的物理 XML 与 .nif
```

这是**排查物理问题的第一手工具** —— 它会直接告诉你哪个 mod 的 XML 有警告。

## 与 XPMSE 的耦合

FSMP 继承原版设计：只把网格附加到 **XPMSE 的 human skeleton**。
所以 XPMSE 是硬前置。

## 来源

- FSMP 取代原版、多线程、ImGui 菜单替代 MCM、JSON 全局配置：官方仓库 README 与 commit 历史、
  Nexus 页描述 —— **一手**
- 前置（SKSE64 + Address Library、CommonLibSSE 内置地址库）：官方仓库 README —— **一手**
- FOMOD 各游戏版本档位与 SKSE 对应、版本 4.1.1：Nexus 文件页 —— **一手**
- "4.x 不再强制 SkyUI/JContainers/PapyrusUtil/ConsoleUtil，但其他 mod 可能仍要"：
  **社区经验（与官方改动一致）**
- `smp report` 命令：官方仓库 README / wiki —— **一手**
