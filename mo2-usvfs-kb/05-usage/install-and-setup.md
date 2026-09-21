---
id: install-and-setup
title: 安装与首次启动设置
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 安装, 首次启动, NXM, Nexus]
aliases: [MO2 怎么装, install setup, MO2 安装设置]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 安装 MO2、首次启动选择游戏与 instance、关联 NXM 链接；跑游戏前必须先手动启动游戏一次让 MO 建立注册表信息。
kind: tutorial
---

# 安装与首次启动设置

## 安装

1. 从 Nexus 登录并下载 MO 的主文件，双击安装。
2. 安装时可选组件，**推荐勾选 "Handle Nexus Links"**。
3. 建议把 MO 和所有 modding 工具装在 **UAC 受控目录之外**（即不要放进 `C:\Program Files` 之类需要提权的路径）。
4. 若安装程序无法运行，先确认杀毒软件没有拦截该可执行文件——有则加排除后重试。

## 首次启动前的关键前置

> **在第一次运行 MO 之前，必须先至少启动一次游戏本体**，以建立 MO 用来识别游戏及其安装路径所需的注册表设置。
> 很多游戏需要从 Steam 启动一次，等主菜单加载出来后再退出。

## 首次启动流程

首次启动时 MO 会让你选择初始化模式：**portable（便携）或 instanced（实例）**，详见 [便携安装 vs 实例安装](portable-vs-instance.md)（STEP 强烈推荐 instanced）。

1. 启动 MO。
2. 在 Choose Instance 窗口选 **New** 新建实例。若想用便携模式，选 **Portable** 并跳到第 4 步。
3. 在下一个窗口从下拉框选一个实例名，或自己输入（名字随意，不必是所管游戏的名字）。
4. 选择要管理的游戏。列表里没有就选 **Browse…** 定位到游戏主目录，然后点 OK。
5. 弹出教程询问时可以选择查看交互式教程，**首次使用者建议看一遍**。
6. 可能询问是否把 nxm 链接注册给 MO 处理（影响能否在 Nexus 点 "Download with Manager" 下载），**一般选 Yes**。

## 首次上手值得改的设置

- **让工具栏图标带文字**：`View` → `Toolbars` → `Icons and Text`，新手上手更快。
- **换皮肤**：工具栏 `Settings` → `General` → `Style` 下拉选皮肤，`dark.qss` 大概是最流行的。
- **改路径**：Settings → `Paths` 标签页，自定义 mod/下载等文件的存放位置（多硬盘用户尤其需要）。
- **关联 NexusMods 账号**：Settings → `Nexus` → 点 `Connect to the Nexus`，浏览器里登录并 `Authorise`；成功后按钮变成 `Nexus API Key Stored`，点 OK 并按提示重启 MO。

## 更新 MO

- 工具栏右上角的更新按钮**变色**即表示有新版本，点击按提示更新；也可在 `Help` 菜单里找到它。
- 若 MO 没能检测到更新，可手动下载最新版并覆盖安装/解压到 MO 现有目录。

### 干净安装式更新（不推荐，仅在常规更新出问题时用）

1. 进入 MO 安装目录。
2. 视安装方式二选一：
   - **instanced**：删除 Mod Organizer 文件夹内的**全部内容**（设置保存在 `%LocalAppData%/ModOrganizer`，不会丢）。
   - **portable**：删除该文件夹内的全部文件与子文件夹，**但必须保留**：`downloads`、`mods`、`overwrite`、`profiles`、`webcache`、`categories.dat`、`ModOrganizer.ini`、`nxmhandler.ini`。
3. 按上面的安装步骤装新版本。

> 下一步：了解 [便携安装 vs 实例安装](portable-vs-instance.md) 的取舍；装好后按[安装 mod](install-mods.md)开始；工具要从 MO 内启动，见[配置第三方程序](third-party-executables.md)。
