---
id: tool-recipes
title: 常用工具在 MO2 中的配置配方
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 工具, LOOT, xEdit, Wrye Bash, FNIS, SkyProc, SKSE, Creation Kit]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: LOOT、xEdit、Wrye Bash、FNIS、SkyProc、SKSE、Creation Kit、BodySlide、SBW、FreeCommander 的配置步骤与注意事项。
kind: reference
---

# 常用工具在 MO2 中的配置配方

以下步骤都从[配置第三方程序](third-party-executables.md)的 `Modify Executables` 对话框出发（未特别说明即：点齿轮 → 填 Title → 浏览 Binary → Add → Close）。

## LOOT

1. Title 填 `LOOT`，Binary 选 `LOOT.exe`。
2. 若你用 LOOT 管多个游戏，在 `Argument` 里加 `--game=<name>`，其中 `<name>` 为 `Skyrim`、`FalloutNV`、`Fallout3` 或 `Oblivion`。

> 注意：插件页内置的 `Sort` 按钮就是 LOOT，但**缺少报告窗口与元数据编辑功能**。

## xEdit（TES5Edit / TES4Edit / FNVEdit / FO3Edit）

- Binary 选 `xEdit.exe`；在 `Arguments` 里加 `-tes5 -edit`（`tes5`=Skyrim、`tes4`=Oblivion、`fo3`=Fallout 3、`fnv`=Fallout NV）。
- **取消勾选 `Close MO when Started`**。
- 另一种省事做法：把 xEdit 重命名成与游戏对应的名字（如 Skyrim 就叫 TES5Edit）。
- 关于保存位置：勾选 `Backup Plugins` 时文件写回原位置并覆盖，同时在 Overwrite 的 `TES5Edit Backups` 文件夹里生成备份；**不勾选**时直接覆盖原文件、不生成备份。（这与老版本 MO 行为不同——老版本无论如何都把改动写进 Overwrite。）

## Wrye Bash

- **独立版**：Binary 选 `Wrye Bash.exe`（通常在安装目录的 `Mopy` 文件夹里，一般在游戏目录内）。
- **Python 版**：Binary 选 32 位的 `pythonw.exe`（如 `C:/Python27`），`Start in` 指向 Mopy 目录，`Arguments` 填 `"…/Mopy/Wrye Bash Launcher.pyw"` 的完整路径（在资源管理器里 Shift+右键该文件 → `复制为路径`）。
- 注意事项：
  - 从 MO 启动 Wrye Bash 时，它能识别 MO 的插件（esp/esm），但会把它们**当作手动安装**处理。
  - 关闭 Wrye Bash 的 **Auto-Ghost** 功能，可避免 ESP 文件被从各自文件夹搬到 Data。
  - 有些版本（如 Fallout 3 的 Wrye Flash）没有独立版，只能用 Python 方案。

## FNIS（Fore's New Idles for Skyrim）

- Binary 指向 `<ModOrganizer>/mods/Fores New Idles in Skyrim - FNIS/tools/GenerateFNIS_for_Users/GenerateFNISforUsers.exe`。
- **跑完 FNIS 后 Overwrite 里会出现文件**：右键 Overwrite → `Create Mod`，命名如 `FNIS Output`，取消勾选改为勾选启用。
- 以后每次更新 FNIS 行为，都要打开 Overwrite，把新文件**拖回该 mod**。
- 若报 "This application cannot be started"，多半是**忘了在左窗格启用该 mod**。

## SkyProc Patchers（ASIS / Automatic Variants / Reproccer 等）

- 它们是 Java 的 `.jar`，不是真正的 exe。添加方式：
  1. 在右窗格 **Data** 标签页找到 `SkyProc Patchers` 目录，展开到目标程序；
  2. 右键 `.jar` → `Add as executable`；命名并完成。
- 明说事项：
  - 需要 **32 位 Java**；可能要求你指定 Java 可执行文件，通常是 `Program Files` 下 `.../Java/jre7/bin/javaw.exe`。
  - 也可以不改可执行列表，直接在 Data 标签页右键该 jar → `Open/Execute`。
  - 在 `Arguments` 末尾加 ` -noboss` 可绕过 BOSS。
- 排错：
  - **报缺 master、esp 排序错**：把该 esp 放到它依赖的 master 之后；再给参数加 ` -noboss`；重跑。替代方案：用 SUM（SkyProc Unified Manager）启动，把 SUM 设置成不跑 BOSS。
  - **报找不到东西或随机错误**：Java 过期 → 装最新 Windows x86 离线版 JRE。
  - **报内存相关错误**：用 SUM 在 Other Settings 里分配更多内存；和/或关闭所有 Java 程序后，给 `java.exe`、`javaw.exe` 打 **4GB patch**。

## SKSE（Skyrim Script Extender）

- 默认会被自动识别；否则手动把 `skse_loader.exe` 加为可执行程序，并勾选 `Close MO when started`。
- **SKSE 本身不能作为 mod 安装**（这样 SKSE 脚本不会加载）。但**可以把 SKSE 的脚本、以及 SKSE 插件作为 mod 安装**（前提是**没有**把加载机制改成 Script Extender）。
- 排错 "Couldn't read arguments"：说明参数写错。在 `Modify Executables` 里选中 SKSE，删除/修正参数，点 `Modify` 保存。SKSE 的合法参数包括：`-h`、`-help`、`-editor`、`-priority <level>`、`-altexe <path>`、`-altdll <path>`、`-crconly`、`-waitforclose`、`-fpslimit <max fps>`、`-v`、`-msinfo`、`-noskiplauncher`、`-launchsteam`、`-affinity <mask>`、`-forcesteamloader`。
  - 改完后，**在这个错误参数下创建的 SKSE 快捷方式都要删掉重建**。

## Creation Kit（CK）

- 通常自动识别，无需配置。若需手动添加：Binary 选 `CreationKit.exe`，并**勾选 `Overwrite Steam AppID` 填 `202480`**，否则 CK 看不到你的 mod。
- 通过 MO 用 CK 的已知限制：
  - CK 运行期间，往 mod 目录里新增的文件**要重启 CK 才可见**；
  - 保存后 esp **会被移进 Overwrite**；
  - CK 的脚本编译器是 64 位程序，MO 处理不了——要编译脚本只能把脚本临时放进 Data，或使用 *Papyrus Compiler Patch for x64 Systems*。

## BodySlide 2 and Outfit Studio

1. 装归档时 MO 检测不到游戏数据：选 `Set data directory` → `OK` → 提示处选 `Ignore`。
2. 左窗格会出现**红 X** 标记：右键 mod → `Ignore missing data`。
3. 勾选启用该 mod。
4. 再按通用步骤把 `BodySlide.exe` 加为可执行程序（该 mod 内的其它程序同理）。

## Simple Borderless Window（SBW）

- Binary 选 Skyrim 目录下的 `SBW.exe`，**勾选 `Close MO when started`**。
- 注意：要让 Skyrim 以窗口模式启动，**每个 profile 的 `skyrimprefs.ini` 都要把 `bFull Screen` 改为 0**。
- 效果：游戏内看起来仍是全屏，只是没有边框。

## Free Commander XE（FCXE）

- **必须装 32 位版本**（MO 只支持 32 位程序）。
- 用途：从 MO 内启动它，导航到 `<Skyrim>/data`，即可**看到 MO 暴露给所有 MO 内启动程序的 VFS 视图**——这是验证 MO 是否正常工作最直观的方式（用资源管理器看同一目录只会看到干净的原版文件）。
- ⚠️ 注意 FCXE **不是 VFS 的完整还原**：BSA 内的文件仍留在 BSA 里，不会显示成 Data 下的散文件，所以别把它当成 VFS 的真实全貌。
- ⚠️ 出于技术原因，**不能用 Windows 资源管理器或基于它的程序**做这件事；Total Commander（TC）等替代文件管理器可用，FCXE 与 TC 均实测正常。

> 相关：[配置第三方程序与快捷方式](third-party-executables.md)、[启用 mod 与激活插件](enable-and-activate.md)、[Overwrite 目录与维护](overwrite-dir.md)。
