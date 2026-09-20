---
id: portable-vs-instance
title: 便携安装 vs 实例安装
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 安装模式, instance, portable, LocalAppData]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: portable 每个游戏一份 MO；instanced 用一份 MO 管多游戏/多套构建，各实例数据存于 %LocalAppData%/ModOrganizer。
kind: concept
---

# 便携安装 vs 实例安装

MO（含 MO2）可以按两种模式使用：**portable（便携）**与 **instanced（实例）**。

## 便携模式（portable）

- 每个要管理的游戏，都要**单独安装一份 MO**。
- 历史最久、最正统的用法。
- 没有已知问题；唯一缺点是 MO 程序本身冗余——MO 需要升级、换主题等时要一份份维护，时间久了是个麻烦。

## 实例模式（instanced）

- **一份 MO 安装**即可管理多个游戏，和/或同一游戏的多套 mod 构建。
- 每个实例的数据存放在 `%LocalAppData%/ModOrganizer` 下。
- 可以把实例理解为 **profile 系统的扩展**：
  - **普通 profile** 允许独立管理游戏配置（INI 文件）、启用的 mod、启用的插件、mod 优先级等，但它们**都属于同一个游戏，且共享同一个 mod 列表**。
  - 想为同一游戏管理两套完全不同的构建时，这个限制很明显：两套 mod 会被合并进同一份 mod 列表，充斥大量永远不会被启用的"噪音"。
  - **实例**则让**所有东西**都能分区独立，效果等同于便携模式，却不需要多份（冗余的）MO。
- 点击工具栏上的 instance 按钮即可切换实例。

## 该选哪个

- **STEP 强烈推荐 instanced**。
- 需要注意的是：由于两种安装方式并存，第三方工具作者常常只针对自己使用的模式做适配。便携模式存在的时间远长于实例模式，因此**通常与第三方软件的开箱兼容性更好**。
- 了解两者的差异，就能轻松规避绝大部分潜在问题。

> 相关：[安装与首次启动设置](install-and-setup.md)（首次启动时选 New 建实例或选 Portable）、[Profile 切换](profile-switching.md)、[备份与恢复](backup-and-restore.md)（重装前要备份 `profiles` 等目录）。
