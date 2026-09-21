---
id: install-mods
title: 安装 mod：四种途径与三大打包格式
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 安装, FOMOD, BAIN, 手动安装, Mod Exists]
aliases: [怎么装 mod, 安装 mod, 打 mod 流程, mod 打包格式]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 用 Downloads 双击、Archive 按钮、右键 Install Mod 或 Steam Workshop 安装；Simple/BAIN/FOMOD 三格式，都不是则走手动安装。
kind: tutorial
---

# 安装 mod：四种途径与三大打包格式

## 开始安装的四种方式

1. 通过 MO 从 Nexus 下载归档，完成后在右窗格 **Downloads** 标签页**双击该文件**安装。
2. 点工具栏的 **Archive** 按钮，浏览到归档包，选中并打开。
3. 在**左窗格右键** → `Install Mod…`，浏览到归档包并打开。
4. 通过 **Steam Workshop** 安装（需先经 MO 启动游戏启动器，见下）。

## Mod Exists 对话框（同名 mod 已存在）

当要安装的 mod 与现有 mod 同名（装可选文件或更新时经常出现）会弹出此框：

| 按钮 | 何时用 | 行为 |
| --- | --- | --- |
| **Merge** | 安装 mod 的**可选文件/附加组件** | 把文件**追加**进现有 mod，**覆盖同名文件**。 |
| **Replace** | **把 mod 升级到含全部资源的新版本** | **先删除** mod 内所有文件，再装入新文件。 |
| **Rename** | 想**独立保留**内容，或**并存两个版本** | 以另一个名字安装。 |
| **Cancel** | — | 终止安装。 |

- 勾选 **Keep Backup** 再配合 Merge 或 Replace，会在安装前**备份 mod**。
- 恢复备份的方法：右键 mod → `Open in explorer` → 删除高亮的 mod 文件夹 → 把紧邻其下、名字带 `_backup` 后缀的文件夹改名回原 mod 名。

## 命名

- 打开多数归档时，`Name` 框会显示从下载时收集的 meta 信息解析出的名字；没有 meta 则显示"文件名去掉附加的 Nexus ID 与版本号"。
- 点下拉箭头可给出建议名（同 Nexus ID 的其它 mod、归档名、带 ID/版本号的归档名、Nexus 上的真实 mod 名）。

## 三大打包格式

- **Simple（简单归档）**：最常见也最省事，弹出 `Quick Install` 窗口只有三个选择——`OK` 直接安装、`Manual` 进手动安装对话框、`Cancel` 取消。
  - 在 Settings → Plugins 里把 `Simple Installer` 的 `enabled` 设为 `false` 可关闭快速安装；把 `silent` 设为 `true` 则简单归档**全自动安装**（省一次点击），某些必须手动装的 mod 需临时关掉该设置。
- **BAIN（Bash Installer）**：打开 BAIN 包安装窗口，按 mod 页面或 readme 说明**勾选所需选项**后点 `OK`；`Package.txt` 按钮可打开包内 package.txt（没有则置灰）；`Manual` 进手动安装。
- **FOMOD（Fallout Mod）**：按脚本格式二选一——**XML 脚本**走内置 FOMOD 插件，**C# 脚本**走外部 NCC 插件。按向导提示安装即可。
- 不属于以上三类的归档会打开**手动安装对话框**。

> 任何一次新装 mod 都会**自动取得最高数值优先级**；启用后就会覆盖冲突的低优先级 mod 文件。另外：**目前不能同时安装多个 mod**。

## 手动安装

- 打开手动安装对话框后，注意左下角：**红字 `No game data at top level`** 表示尚未定位到数据目录；第一次出现会有小教程引导。当它变成**绿字 `Looks good`** 时，才能点 `OK` 安装。
- 大多数情况是"一个 data 文件夹 + 一个 readme"：**右键 data 文件夹 → `Set data directory`** 即可；选错了就右键 `Unset data directory`。
- 复杂归档需要自己整理：
  - 右键某层级 → `Create directory` 新建文件夹；
  - **拖放**移动文件（Ctrl+左键可多选一起拖）；
  - **取消勾选**某个文件/文件夹即不安装；
  - 右键 readme → `Open` 查看内容。
- 装歪了也不要紧，可在已安装 mod 的 [Filetree 面板](hide-files-and-filetree.md)里继续调整。

## FOMOD 安装出问题时

- **强制用外部 NCC 插件安装**（内置插件装错文件，或该 FOMOD 的 XML mod 检测脚本只认外部安装器）：
  1. 点工具栏 wrench 打开 Settings → `Plugins` 标签页；
  2. 点 `FOMOD Installer`，把 `prefer` 的值双击改为 `False`；
  3. OK 后重装该 FOMOD。装好后**建议把 `prefer` 改回 `true`** 恢复默认行为。
- **用 FOMM 安装**（Fallout 系）：确保 Overwrite 为空 → 经 MO 启动 FOMM → Package Manager → Add Package 选 FOMOD（问是否拷贝选否）→ 按需安装并退出 → 右键 Overwrite → `Create Mod` 命名即可。
  - 需要识别"已装其它 mod"的 FOMOD（如根据已装内容改写菜单文件的 HUD 类 mod）**必须在 VFS 激活时安装**，而 MO 安装 mod 时 VFS 未激活，所以要用上面这种绕行办法。
- **命令行方式被弃用**：自 1.2.17 起必须用 FOMM 的场景已越来越少。

## Steam Workshop mod 的安装

1. 确保 Overwrite 为空。
2. 在 Steam Workshop 订阅该 mod。
3. **通过 MO 启动游戏启动器**，等文件下载完后退出启动器。
4. 右键 Overwrite → `Create Mod`，命名并确定。
5. 在 Steam Workshop 退订该 mod，对下一个 mod 重复以上步骤。
- 更新 Workshop mod：重复整个流程并移除旧版本。

> 相关：[启用 mod 与激活插件](enable-and-activate.md)、[更新、合并与卸载](update-and-uninstall.md)、[插件体系：安装器](plugins-extensibility.md)。
