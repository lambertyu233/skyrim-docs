---
id: usage-faq
title: 使用类常见问答（mod 管理）
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, FAQ, 排错, 常见问题]
aliases: [MO2 使用问答, 使用类 FAQ, 常见操作问题]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 收集 STEP 指南里高频的实操疑问：什么能/不能作为 mod 安装、MO 是否在正常工作、窗口异常、卸载 MO 等。
kind: reference
---

# 使用类常见问答（mod 管理）

> 关于 VFS/USVFS 层面的疑问见[常见问题（FAQ）](../06-reference/faq.md)。

## 诊断与验证

**Q：装了个 mod 但它不工作！**
A：怎么判断的？**唯一可靠的指标是游戏本身**。Skyrim 启动器**不会**显示 MO 装的 mod；Data 目录里也不会出现新文件。装完后**启动游戏看效果**。若确实无效，检查目录结构——很多 mod 打包不佳，你需要在安装时或安装后移动文件（见 [Filetree 面板](hide-files-and-filetree.md)）。

**Q：怎么知道 MO 在工作？**
A：装一个**效果肉眼可见**的 mod。另外确认 `modorganizer.log` 有被生成。

**Q：怎么看 MO 的虚拟文件系统（VFS）在干活？**
A：用 Free Commander（FCXE）或其它合适的文件管理器，**从 MO 内启动**它再去看 `<Skyrim>/data`。详见[常用工具配置配方](tool-recipes.md)。
> 注意：BSA 内的文件**不会**显示成 Data 下的散文件。

**Q：为什么我的 `<skyrim>Data` 里看不到任何 mod 文件？**
A：正常。每个 mod 装在各自的文件夹里（默认 `<ModOrganizer>/Mods/`）。`<skyrim>Data` 里只有 Skyrim、Dawnguard、Hearthfire、Dragonborn、高清材质包与 Creation Kit 这些官方文件。MO 创建 VFS，把官方内容与当前 profile 已激活的 mod 在**运行时**合并——这正是 MO 的核心功能，让 `<skyrim>Data` **保持纯净不被改动**。

## 能 / 不能作为 mod 安装

| 对象 | 结论 |
| --- | --- |
| **SKSE 本身** | ❌ 不能（否则 SKSE 脚本不加载）。**SKSE 脚本可以**作为 mod 安装。 |
| **ScriptDragon 本身** | ❌ 不能（目前是禁区）。其脚本**也许可以**，前提是放进 data 目录或 `<skyrim>/Data/asi`。 |
| **ENB** | ❌ 不能。但其附加资源（Shaders、Textures 等）**可以**作为 mod 安装。 |
| **SweetFX Shader Suite** | ❌ 不能。其附加资源（Shaders、Textures）**可以**。 |
| **FXAA Post Process Injector** | ❌ 不能。同理，其附加资源**可以**。 |

## 安装与校验

**Q：用 C# 脚本的 FOMOD（如 SkyUI）装不上？**
A：需要正确的 **.NET Framework**。

**Q：每次跑 Skyrim，Overwrite 的 `meshes/cache` 里都会多出 `.tri` 文件？**
A：那是 **RaceMenu 的 CharGen 扩展**生成的缓存。RaceMenu 每次运行都会删除旧的、生成新的，你可以**放心删除**。

**Q：我设了自动解包 BSA，现在想改回来怎么办？**
A：点击工具栏 wrench 打开 Settings → 点 `Reset Dialogs` → 提示处点"是"。

## Nexus 与更新

**Q：MO 会自动检查 mod 更新吗？**
A：**不会**——作者不想给 Nexus 制造无谓流量。但你可以右键 mod 列表 → `Check all for update`，它会检查所有 mod 的最新版本，并把有更新的标红。

**Q：为什么 MO 仍显示我"未登录"？**
A：MO **不会自动轮询** Nexus 核对这类信息。你的账号信息会一直保存，**直到你真正使用过它们**为止。执行一次会用到账号的操作后，注意标题栏的变化。

**Q：装了 mod 为什么没打上 endorsement 标记？**
A：出于技术原因，负责安装的[插件](plugins-extensibility.md)无法设置该标记。到左窗格右键 → `check all for updates`，这也会顺带设置 endorsement 标记。

**Q：为什么我无法对某个下载的 mod 执行 "Query Info"？**
A：取决于具体 mod。**Nexus 一次最多允许 MO 查询 30 个文件**；若该 mod 的下载页超过 30 个文件，正确名字可能不在给出的 30 个答案里，只能自己按命名规则核对调整。也可以考虑请作者清理下载页。

**Q：只用 MO 管部分游戏、其它游戏用 NMM 等管理器？**
A：用 MO 目录里的 `NXMHandler`，见[下载管理与 Nexus 集成](downloads-and-nexus.md)。

## 加载机制

**Q：该用哪种加载机制？**
A：**默认的就好**，除非它出问题。装了脚本扩展又不想用 MO 界面时，可以改成 `Script Extender` 机制，但**要知道：这样经 MO 装的脚本扩展插件将不工作**，必须手动装进 data 目录；而且**游戏每次更新 SE 都会失效，MO 随之失效**。
- `Proxy DLL` **只作为最后手段**；用它时，**每次游戏更新后都必须至少启动一次 MO**。
- Oblivion 用 `Script Extender` 机制最好；Skyrim 用 `Mod Organizer` 机制最好。

**Q：用了 proxy-dll 加载机制后 MO/Skyrim 不工作了，怎么办？**
A：见[加载机制与 Steam App ID](load-mechanism.md) 中的修复步骤。

## 杂项

**Q：能用 PS4 / Xbox / Steam 手柄配 MO 吗？**
A：可以，但 **MO 必须以非管理员权限安装**。

**Q：窗口老是自动缩回小尺寸，怎么固定？**
A：Settings → `Nexus`，取消勾选 `Use HTTP Proxy (Use System Settings)`。

**Q：想卸载 MO，该怎么做？**
A：
1. 在 MO 内进 Settings，把加载机制选为 `Mod Organizer`；
2. 关闭 MO，之后不再使用即可；
3. 确认不需要其中内容（如 mod 归档）后，可以删除 ModOrganizer 目录。**MO 不写注册表、也不写自身目录以外的任何位置**，除此之外无需任何卸载操作。
> 注意：**NXM 关联仍然存在**，需要另行处理（见[下载管理与 Nexus 集成](downloads-and-nexus.md)）。

> 相关：[界面总览](ui-layout.md)、[存档查看与 Fix Mods](saves-management.md)、[警告面板与潜在 mod 顺序问题](warnings-and-order-problems.md)。
