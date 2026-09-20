---
id: settings-tabs
title: 设置页参考（General / Nexus / Plugins / Workarounds）
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 设置, Settings, Workarounds, Log Level]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 齿轮按钮打开设置：General 管语言/皮肤/日志/路径/分类，Nexus 管账号与服务器，Workarounds 管加载机制等特殊开关。
kind: reference
---

# 设置页参考（General / Nexus / Plugins / Workarounds）

入口：工具栏 `settings`（wrench）按钮。

## General 标签页

- **Language**：界面语言下拉。当前支持英语（美式）、捷克语、荷兰语、法语、德语、日语、韩语、俄语、西班牙语、土耳其语，以及**中文（简体与繁体）**。
- **Style**：选择皮肤。`dark.qss` 大概是最流行的。
- **Log Level**：控制写入 `ModOrganizer.log` 的内容量。
  - `Debug` 最详细、排错最有用；`Info` 信息较少、遇到 bug 时帮助有限；`Error` 只记录错误、几乎不提供上下文。
  - 日志**只在 MO 建立 VFS 的初始化阶段**产生；游戏实际加载阶段的开销可忽略。Tannin 的说法是：性能上"没有值得一提的 CPU 影响，都是磁盘 I/O；即便 Debug 级别 MO 也不会产生很多日志，实际游戏中几乎没有（MO 的活动主要在启动和加载阶段）"。
- **Advanced**：可修改 `downloads`、`mods`、`webcache` 的存放目录。用 SSD 且不想把下载归档放上去时很有用；多份 MO 共用一处已装 mod 时也有用。
- **User Interface**：紧凑下载界面 / 下载元信息显示的开关组合。
- **Reset Dialogs**：重置所有勾选过"记住选择（Remember Selection）"的位置。
  - 典型用途：你曾在安装含 BSA 的 mod 时选了"总是解包"，现在想恢复询问——用 Reset Dialogs 即可。
- **Configure Mod Categories**：编辑 mod 分类，见[自定义 mod 分类](mod-categories.md)。

## Nexus 标签页

- **Login Info**：填 Nexus 账号密码可免去每次输入；勾选可让 MO 自动登录。**以加密形式存于 `ModOrganizer.ini`**。
- **Offline Mode**：勾选后 MO 不访问互联网。
- **Proxy Settings**：`Use HTTP Proxy` 让 MO 使用系统代理设置。
- **Associate with "Download with manager" links**：把 Nexus 上的 Download with Manager 链接关联到你所管游戏对应的 MO。
- **Servers**：下载过 mod 后，MO 会记录已知服务器及其连接速度。把左框里的服务器**拖到右框**即设为首选——**Premium 用户**可借此指定 Premium 服务器以获更快速度。

## Plugins 标签页

- 各插件的具体开关与参数都在这里配置，见[插件体系](plugins-extensibility.md)。

## Workarounds 标签页

| 项 | 说明 |
| --- | --- |
| **Steam App ID** | Steam 用于该游戏的 ID。**除非你确信它错了，否则别动**。详见[加载机制与 Steam App ID](load-mechanism.md)。 |
| **Load Mechanism** | MO 作用于游戏的方式：`Mod Organizer`（默认）、`Script Extender`、`Proxy DLL`。**默认机制不出问题就别改**；`Proxy DLL` 是个"大 hack"，应优先避免。详见[加载机制与 Steam App ID](load-mechanism.md)。 |
| **NMM Version** | MO 作为 user agent 时声称的 NMM 版本。若 Nexus 封禁了某个 NMM 版本，可能需要调高。 |
| **Hide inactive ESPs/ESMs** | 隐藏未激活的插件。**当前有 bug，勿用**。 |
| **Force-enable game files** | 勾选则强制加载基础游戏文件（如 Skyrim 的 `Skyrim.esm` 及其相关 BSA）；**取消勾选**可禁用基础文件——在做"基于该引擎的整体转换 mod"时可能有用。 |
| **Display mods installed outside MO** | 控制是否把真实 Data 目录里的所有"插件 + BSA" mod 显示为 Non-MO mod。关闭只会移除装在 Data 里的 mod，不会移除官方 DLC。 |
| **Back-date BSAs** | 仅 Skyrim 的 Archive Invalidation 替代方案。**跑 Skyrim 且未启用 Archive Invalidation 时必须勾选**，否则原版 BSA 可能覆盖你的 loose file，非常难排查。见 [BSA 管理与解包](bsa-management-usage.md)。 |

> 相关：[界面总览](ui-layout.md)、[插件体系](plugins-extensibility.md)、[加载机制与 Steam App ID](load-mechanism.md)、[下载管理与 Nexus 集成](downloads-and-nexus.md)。
