---
id: plugins-extensibility
title: 插件体系：扩展、安装器与工具
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 插件, 安装器, 扩展, 黑名单]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: MO 插件分 extensions / installers / tools 三类，在 Settings → Plugins 里配置开关与参数；有崩溃嫌疑的插件会被列入黑名单。
kind: concept
---

# 插件体系：扩展、安装器与工具

MO 可通过插件扩展。插件可用 **C++/Qt** 或 **Python** 编写（Python API 目前比 C++ 略受限，且要求用户自行安装 Python）。配置入口：`Settings` → `Plugins` 标签页。

插件分三类：**extensions（扩展）**、**installers（安装器）**、**tools（工具）**。

## Extensions（扩展）

为 MO 增加对新编程语言的支持能力。

- **Python Proxy**：让 MO 能运行 Python 插件；也可指定代理使用的 Python 位置。
  - `enabled`（布尔，默认 `true`）：启用/禁用该插件。
  - `python-dir`（文本）：Python 安装根目录，例如 `C:/Python27`。

## Installers（安装器）

让 MO 处理各式各样打包方式的 mod 归档。

| 插件 | 作用与参数 |
| --- | --- |
| **BAIN Installer** | 安装为 Wrye Bash 包管理器打包的归档。**目前不支持 wizards**。 |
| **Bundle Installer** | 处理"包中包"（如 `.7z` 里套一个 FOMOD）的代理安装器。 |
| **Fomod Installer** | 安装用 XML 描述安装选项的归档（FOMOD = *Fallout Mod*，源自 Fallout Mod Manager）。<br>`enabled`（默认 `true`）；`prefer`（默认 `true`）——设为 `true` 时接管所有 xml FOMOD；设为 `false` 则只要外部 NCC 插件还能用就不使用它。 |
| **Manual Installer** | 几乎能装任何包，但需要用户交互。通常是最后兜底方案。 |
| **Fomod Installer external** | 调用基于 NMM 的外部工具 **NCC** 来装 FOMOD。比内置的慢、集成度差，但**兼容性更好**（NCC 除 xml 外还支持 **C# 脚本**）。<br>⚠️ **当 FOMOD 使用 C# 脚本时，无论设置如何都必定调用这个外部安装器。** |
| **Simple Installer** | 一键安装"简单数据层格式"的 mod。<br>`enabled`（默认 `true`）：关闭后总是弹出手动安装窗口；`silent`（默认 `false`）：设为 `true` 则所有简单归档**自动安装**，跳过 Quick Install 菜单。 |

> 关于 FOMOD 的实战取舍见[安装 mod](install-mods.md)（可临时把 `prefer` 设为 `false` 强制走 NCC）。

## Tools（工具）

这类插件行为类似独立工具，但**可能干扰 MO 主程序**（例如请求当前 profile 信息、在虚拟目录里解析文件名）。

| 插件 | 作用与参数 |
| --- | --- |
| **BSA Extractor** | 安装 mod 时解包其中的 BSA。`enabled`（默认 `false`）：启用后，下次安装含 BSA 的 mod 会弹出对话框询问是否解包，并可选"记住该设置"。 |
| **FNIS Checker** | 提示你该在启动游戏前跑 FNIS。`enabled`（默认 `false`）；`sensitive`（默认 `false`）——设为 `true` 会更激进地提示（几乎每次改动 profile 元素都提示）。 |
| **INI Editor** | 编辑游戏配置的基础文本编辑器。`external`（默认 `false`）决定 ini 是否用外部 Windows 文本编辑器打开；`associated`（默认 `true`）决定用"打开（Open）"的关联程序，为 `false` 时用 Windows 的"编辑（Edit）"命令（通常仍是记事本，可在注册表里改）。 |
| **NMM Import** | 把通过 NMM 安装的 mod 导入 MO。**测试不足**。 |
| **Preview Base** | 提供预览各类文件的能力。 |
| **Basic Diagnosis Plugin** | 检查与其它插件无关的问题，见下。 |

### Basic Diagnosis Plugin 的检查项

| 参数 | 默认 | 含义 |
| --- | --- | --- |
| `check_errorlog` | `true` | 上次运行某个程序时发生错误则警告。 |
| `check_overwrite` | `true` | Overwrite 目录里有文件则警告（见 [Overwrite 目录](overwrite-dir.md)）。 |
| `check_font` | `true` | 字体配置引用了**未安装的字体**时警告。配置文件是 `Data/interface/fontconfig.txt`；缺字体时字母会显示成方框，通常是字体替换 mod 装坏了。 |
| `check_conflict` | `true` | 有与 MO 功能冲突的 mod 被安装时警告（目前只检查 Nitpick，而 MO 已内置该 mod 的修复）。 |
| `check_missingmasters` | `true` | 有插件缺 master 时警告。 |
| `ow_ignore_empty` | `false` | 检查 Overwrite 时忽略空目录。 |
| `ow_ignore_log` | `false` | 检查 Overwrite 时忽略 `*.log` 文件与空目录。 |

## Blacklisted Plugins（插件黑名单）

- 此处列出已被**列入黑名单、禁止启用**的插件。
- 当 MO 检测到某插件**可能引起崩溃**时，会把它拉黑。
- 在列表里按 **Delete 键**可移除条目。

> 相关：[安装 mod](install-mods.md)（安装器实际表现）、[设置页参考](settings-tabs.md)、[Overwrite 目录与维护](overwrite-dir.md)。
