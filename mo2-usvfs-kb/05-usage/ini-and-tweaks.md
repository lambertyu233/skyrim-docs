---
id: ini-and-tweaks
title: 游戏 INI 与 ini tweaks
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, INI, tweaks, Configurator, INI Editor]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: MO 首次启动会复制一份游戏 INI；用 Puzzle 菜单的 Configurator/INI Editor 编辑；可为 mod 建 ini tweak 覆盖任意 ini 设置。
kind: tutorial
---

# 游戏 INI 与 ini tweaks

## 编辑游戏 INI

- MO **首次启动时会复制一份游戏 INI**。此后你对默认游戏 INI 文件的修改**不会**反映到 MO 里。
- 编辑入口：打开 **Puzzle 菜单**（工具栏 tools 按钮）：
  - 选 `Configurator` 启动 GUI 版 INI 编辑器；
  - 或点 `INI Editor` 启动文本版编辑器。
- INI Editor 是分标签页的文本编辑器，编辑的是**当前 MO profile** 对应的游戏 ini 文件；顶部下拉框可选择 `[Display]` 之类的节，直接跳到该节。

## ini tweaks

**ini tweak** 是"随 mod 一起生效的 ini 设置"，用来避免手工反复改 ini。

### 创建 tweak

1. **双击**左窗格任意 mod（比如你的补丁 mod）打开信息面板。
2. 切到 **INI-Files** 标签页。
3. 在**左下方小框里右键** → `Create Tweak`。
4. 输入名字（如 `Particle Tweak`）→ OK。
5. 在右侧大框里粘贴你要的设置，例如先写节名 `[Particles]`，下一行写 `iMaxDesired=6000`。
6. 点 `Save` 保存，关闭信息面板；重新打开该面板，tweak 旁会有一个复选框，**勾选即激活**。

- 也可以直接为一个具体 mod 创建它需要的 tweak（例：Skyrim Flora Overhaul 需要 `[Grass]` 下的 `iMaxGrassTypesPerTexure=XX`），这样该 mod 启用时 tweak 也随之启用。

### 一个便捷的起步方式（用来存放"自定义 ini tweaks"）

1. 让 Overwrite 里**有文件**时（没有就先随便跑个会产出的工具，或按旧做法：关闭 MO，在 `mods` 目录里新建一个空文件夹再启动 MO）；
2. 右键 Overwrite → `Create Mod`，命名如 `Custom ini Tweaks`；
3. 双击该新 mod 打开信息面板 → INI-Files 标签页 → 按上面的办法创建 tweak。

### ini tweak 的语义（重要）

据 Tannin 原话，ini tweaks **不是去修改** `skyrim.ini` / `skyrimprefs.ini`，而是**替代**它们：

- 若某设置在 ini tweak 中存在，那么该设置**优先于任何其它 ini**；
- 按当时的实现，ini tweak 甚至**应当能覆盖其它 ini 文件的设置**（例如 SKSE 插件的）——不过他本人未验证过。

### 为什么有用

- 把"随配置变化"的设置（如 STEP 推荐的各项设置、Darnified UI 需要的 `[Fonts]` 段）做成 tweak 放进一个 mod。
- 这样**切换 profile 时只需启用/禁用该 mod**，不必去手工编辑 ini 本身。

> 相关：[文件树、隐藏文件与冲突面板](hide-files-and-filetree.md)（INI-Files 标签页）、[Profile 切换](profile-switching.md)、[Overwrite 目录与维护](overwrite-dir.md)。
