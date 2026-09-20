---
id: downloads-and-nexus
title: 下载管理与 Nexus 集成
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 下载, Nexus, meta, nxmhandler]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: MO 通过 NXM 链接下载并收集 meta（名称/版本/Nexus ID），缺失可 Query Info 补全；nxmhandler 可让多款管理器共存。
kind: tutorial
---

# 下载管理与 Nexus 集成

## 下载

- 在 Nexus mod 页面点 `Download with Manager`（需先按[安装与首次启动设置](install-and-setup.md)完成 NXM 注册），下载会出现在右窗格 **Downloads** 标签页。
- 也可手动下载，然后用工具栏 **Archive** 按钮安装。
- 手动下载的文件**不会**自动出现在 Downloads 标签页；想让它出现，需手动拷进 MO 的 `downloads` 文件夹，再按下面的步骤补 meta。

## meta 信息

- 下载完成后 MO 会收集 meta：mod 名称、版本、Nexus ID。安装时它决定 MO 建议的 mod 名；装好后 Nexus ID 与版本号会写进该 mod 的信息里。
- 若没收到 meta，Downloads 里该文件前会出现警告图标。补全方法：
  1. 右键该下载文件 → `Query Info`；
  2. 若让你在**两个或更多 Nexus ID** 中选，选正确那个（**通常是数字更大的**）；都不对就取消；
  3. 若让你**输入 Nexus ID**，填正确数字（即 `nexusmods.com/mods/<数字>` 末尾的数字）；
  4. 若让你**选择正确的文件**，选对；列表里没有就取消。
- **补全失败的三种常见原因**：
  1. 作者没给该文件设版本号；
  2. 该 mod 的文件超过 30 个，而 MO 探到的 30 个里没有正确那一个；
  3. 该文件在 Nexus 上不存在。
- 可直接用文本编辑器（如记事本）编辑 `downloads` 文件夹里的 `<modname>.meta`，像普通 ini 一样填。这些信息**不影响 MO 功能**，只用于标明来源；留空 MO 也照常工作。
- 注意：若安装时把多个 mod **合并**成一个，之后卸载该 mod 时**只有一个** `<modname>.meta` 会更新，可能出现在 Downloads 里仍显示"已安装"的假象。
- 你可能会看到 `1 orphaned meta file will be deleted` 之类的提示——那是下载期间作占位符的临时文件被清理，属正常。

### Downloads 中的状态

- `Done` = 下载完成但未安装；`Installed` = 已安装；`Uninstalled` = 已卸载。
- 文件可**删除**（移入回收站）或**从视图移除**（仍留在 MO 的 downloads 文件夹）；勾选左下角 `Show Hidden` 可再次看到被移除的文件。
- 通过 MO 下载的 mod 存放在 `<ModOrganizer>/downloads`。

## 首选下载服务器

- Settings → `Nexus` 标签页底部：把左框里的服务器**拖到右框**即设为首选（服务器只在首次下载某个 mod 时才被识别）。
- **Premium 用户**可借此把 Premium 服务器排到前面以获得更快速度。

## Download with Manager 点了没反应？

按顺序排查：

- 点一下工具栏的 **globe** 按钮。
- Settings → `Nexus` → 点 `Associate with "Download with manager" links`。
- 进入 ModOrganizer 目录运行 **nxmhandler**：若它指向 MO，点 `Register Active` → 提示处点"是" → 关闭；若没指向 MO，在窗口里右键 `Add`，选所处理的游戏，浏览到对应的 `ModOrganizer.exe`，OK 后点 `Register Active` 并确认。
- **Google Chrome**（旧版方法）：关闭 Chrome → 打开 `%LOCALAPPDATA%/Google/Chrome/User Data/Local State` → 搜索 `nxm` → 删除 `"nxm": false` 那一行（即使是 true 也删）→ 保存 → 下次点击时 Chrome 会弹窗询问，点 `Launch`。
  - ⚠️ 该 Chrome 方法在**较新版本的 Chrome 上已失效**。
- **Firefox**：在选项的"应用程序"里搜索 `nxm`，指向 ModOrganizer 目录内的 nxmhandler。

## 与其它 mod 管理器共存（多游戏）

MO 首次运行会独占 nxm 链接关联，而 MO 只支持部分游戏（而 Nexus Mod Manager 支持更多）。如果你同时用别的管理器管其它游戏，就会冲突。解决办法：

1. 运行 MO 目录下的 `nxmhandler.exe`；
2. 在空白处右键 → `Add`；
3. 支持的游戏里选 `Other`，用文件浏览按钮指向另一个客户端（如 NMM 的 `NexusClient.exe`），OK；
4. 到 Nexus 的[游戏列表](https://www.nexusmods.com/games/about/games/)点开目标游戏主页，看 URL 末段即游戏标识（例：Dragon Age 2 是 `dragonage2`），复制它；
5. 回到 nxmhandler，**双击** `other` 改名并粘贴，关闭即可并存。
6. 需要多个游戏交给同一客户端时，重复上述步骤，用**逗号**分隔多个游戏名。

> 注意：nxmhandler 产生的实际设置，**只存在于你第一份 MO 安装的顶层 INI** 里。

> 相关：[安装 mod](install-mods.md)（装完如何安装/更新）、[第三方程序配置](third-party-executables.md)。
