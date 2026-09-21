---
id: installation-guide
title: 安装指南
category: 01-installation
version: 1.1.0
updated: 2026-09-21
tags: [安装, 入门, 步骤, MO2, Vortex, 合集]
aliases: [CS 怎么装, CS 安装教程, community shaders install, MO2 装 CS]
source: https://modding.wiki/en/skyrim/developers/community-shaders/installation-guide
summary: 在纯净 Skyrim 上安装 Community Shaders 的完整步骤、前置条件与更新方法。
---

# 安装指南

本指南覆盖将 Community Shaders 安装到纯净 Skyrim 的全部需求与推荐流程。

## 开始前

1. **移除不兼容 MOD**（见 [FAQ-不兼容](../03-reference/faq.md) 与 [不兼容 MOD](../03-reference/incompatible-mods.md)）。
2. **确认满足所有需求**（游戏版本、GPU、VC Redist 等），见 [需求](requirements.md)。
3. 将 Skyrim 配置为**无边框窗口**：
   - `SkyrimPrefs.ini`：`bBorderless=1`、`bFull Screen=0`；
   - 若用 Display Tweaks：`SSEDisplayTweaks.ini` 设 `Fullscreen=false`、`Borderless=true`、`BorderlessUpscale=false`（或用[预置配置](https://www.nexusmods.com/skyrimspecialedition/mods/144637)）。
4. **关闭自动更新**：Steam 用户找到 `<库>/steamapps/appmanifest_489830.acf`，右键→属性→只读→应用；GOG 直接关闭自动更新。

## Vortex 一键安装：官方合集

Vortex 用户可以直接用官方 **Community Shaders Collection**（Nexus Collections 编号 `62eesj`）一键装齐 CS 与全部附加特性。

> ⚠️ 用了合集就**整体更新**，不要单独去更新其中某一个特性——两边版本错开会直接导致着色器编译失败（详见下文「更新」）。

MO2 用户、或想自己掌控每个组件的，按下面的手动流程走。

## 新手从哪开始

从没 mod 过 Skyrim 的，官方安装指南点名推荐先读 [A Dragonborn's Fate](https://dragonbornsfate.moddinglinked.com/intro.html)，读到 Community Shaders 这一节再回来。

## 安装步骤

> 推荐使用 **Mod Organizer 2 (MO2)** 或 **Vortex**。仅这两款获得官方支持。

1. 安装所有[前置 MOD](requirements.md)：
   - SKSE64 **手动**拖入游戏根目录（含 `SkyrimSE.exe` 的目录）；
   - Engine Fixes 分两部分：主文件用管理器正常装，**Preloader 手动**将 `d3dx9_42.dll` 拖入根目录；
   - 其余前置用管理器安装，勿手动。
2. 用管理器安装 [Community Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/86492)（Nexus 页是唯一官方支持构建，仅最新版受支持）。
3. 按需安装 [附加特性](../02-features/additional)（同样仅在官方源下载、带 CS 标识者受官方支持）。

> 若 CS 或其附加功能文件互相覆盖或被其它 MOD 覆盖，多半操作有误（除非 MOD 页另有说明）。只从官方源下载 CS 特性。

启动 `skse64_loader.exe`（MO2 用户**必须**经 MO2 启动以加载 MOD）。出现左上“Compiling Shaders”与 CS 欢迎横幅即成功。关闭弹窗前确认 END 为默认菜单键（点弹窗上的按键区可改键）。

## 安装后

- 从 ENB 迁移者看 [ENB 迁移指南](enb-migration.md)。
- 想进一步提升画质看 [Vanilla 设置指南](vanilla-setup.md)。
- 使用 Lux 者：重装并**取消**“optimized”网格；CS Light Limit Fix 已替代它们。勿勾选支持粒子光照的选项（与 CS 不兼容）。

## 更新

- 若使用 [Community Shaders Collection](https://www.nexusmods.com/games/skyrimspecialedition/collections/62eesj)，应整体更新合集，而非单独更新各特性。
- CS 更新时，部分附加特性**必须同步更新**（非可选）。用 MO2/Vortex 的 Nexus 更新检查判断哪些需更新。
- 某特性若被并入核心（见 [FAQ-废弃特性](../03-reference/faq.md)），升级 CS 时必须从 MOD 列表移除它。
- 更新后应在 END 菜单确认版本号，并完成着色器编译。

### 没出现“编译着色器”弹窗？

手动删除 Disk Cache：
- MO2：`Overwrite/ShaderCache`（不了解 Overwrite 请看教程）；
- Vortex：`<游戏>/Data/ShaderCache`。
- **只删 `ShaderCache`，勿删 `Shaders`**；同时删 `UnifiedWaterCache`。详见 [架构与缓存](../00-overview/architecture.md)。
