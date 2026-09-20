---
id: third-party-executables
title: 配置第三方程序与快捷方式
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 可执行文件, 工具, 快捷方式, Steam AppID]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 所有 mod 相关工具都必须从 MO 内启动；用齿轮按钮配置 Binary/Start in/Arguments 等字段，并可创建（profile 专属）快捷方式。
kind: tutorial
---

# 配置第三方程序与快捷方式

## 核心原则

- 所有与 mod 打交道的程序（BOSS、Wrye Bash、游戏启动器、SkyEdit、Creation Kit 等），以及你用的各种 **launcher**（如 SKSE、SBW），**都应该从 MO 内部启动**。否则它们看不到 VFS 合并后的视图。
- 部分知名工具会被**自动检测**并加入可执行列表；其余需手动添加。
- 要从 MO 启动某程序：在右上角的可执行程序下拉框里选中它，点 `Run`。

## Modify Executables（点齿轮按钮打开）

| 字段 | 说明 |
| --- | --- |
| **Title** | 显示在下拉菜单里的名字，随你取。 |
| **Binary** | 要运行的可执行文件完整路径。**只有 `.exe` / `.bat` 算可执行文件**；`.jar` / `.py` 等需要**解释器**（Java、Python），此时把**解释器**设为 Binary。 |
| **Start in** | 程序的工作目录，通常可留空。跑 `.jar` / `.py` 时可能需要设为该文件所在路径。 |
| **Arguments** | 传给二进制文件的命令行参数。Java 应用：Binary 设 `java.exe`/`javaw.exe`，参数填 `-jar <xxx.jar>`；Python 应用：Binary 设 `python.exe`/`pythonw.exe`，参数填 `<xxx.py>`。 |
| **Overwrite Steam AppID** | 仅用于**通过 Steam 分发、但不是游戏本身**的程序（已知场景就是 Creation Kit，且会自动配好）。 |
| **Close MO when started** | 勾选则启动该程序时关闭 MO。按个人偏好选。 |

### 通用配置步骤

1. 点齿轮按钮打开 `Modify Executables`。
2. `Title` 填入你想叫的名字。
3. `Binary` 右侧的省略号按钮（"Browse filesystem"）→ 浏览到程序并选中。
4. （如需）设置 `Start in`。
5. （如需）填 `Arguments`。
6. （如需）勾选 `Overwrite Steam AppID` 并填数字 / 勾选 `Close MO when started`。
7. 点 `Add` 加入列表 → 点 `Close` 关闭。

> 若程序文件与可执行文件在同一目录（如 `TESV.exe` 就在 Skyrim 目录），可跳过 Start in 相关步骤。**多数情况只需要 Title + Binary。**

## 自动识别的可执行文件

- 只有装在**默认位置**才会被自动加入，**MO 不会去搜索整个文件系统**。它们都需要位于游戏根目录（`<游戏安装目录>/`）。
- 支持的游戏包括 Skyrim、Oblivion、Fallout 3、Fallout New Vegas。
- BOSS 早期要求装在 Data 下，后来有了自己的目录，因此 MO 当前会看两处：**游戏根目录下的 `BOSS` 文件夹**与**根目录下的 `Data` 文件夹**。

| 游戏 | 自动识别 |
| --- | --- |
| Skyrim | `skse_loader.exe`、`SBW.exe`、`TESV.exe`、`SkyrimLauncher.exe`、`CreationKit.exe`、`BOSS/BOSS.exe` |
| Oblivion | `obse_loader.exe`、`oblivion.exe`、`OblivionModManager.exe`、`TESConstructionSet.exe`、`OblivionLauncher.exe`、`BOSS/BOSS.exe` 或 `Data/BOSS.exe` |
| Fallout 3 | `fose_loader.exe`、`fallout3.exe`、`fomm/fomm.exe`、`geck.exe`、`FalloutLauncher.exe`、`BOSS/BOSS.exe` |
| Fallout NV | `nvse_loader.exe`、`falloutnv.exe`、`fomm/fomm.exe`、`geck.exe`、`FalloutNVLauncher.exe`、`BOSS/BOSS.exe` |

## 通用故障排查

| 现象 | 可能原因 | 解决 |
| --- | --- | --- |
| 报 "This application could not be started. Do you want to view information about this issue?" | 该程序以 mod 形式装在 MO 里，但**在左窗格没勾选** | 在左窗格勾选它所在的 mod |
| 启动失败：MO 卡住几秒后解锁、什么都没发生 | 同上 | 同上 |
| 报 "Elevation required" | 该程序需要管理员权限 | 信任该程序就点 `Yes` |
| 程序能启动，但**不采用**你填的自定义参数 | 快捷方式是在你添加参数**之前**创建的 | 展开 `Shortcut` 下拉 → 移除所有快捷方式（手动改过名的需手动删）→ 重新创建 |

## 快捷方式

从可执行程序下拉选中程序 → 点 `Shortcut` 下拉 → 选择目标即可**切换**（再选一次即移除）：

- `Desktop`：桌面快捷方式。
- `Start Menu`：开始菜单快捷方式。
- `Toolbar`：放在 MO 自己的工具栏上。

> ⚠️ 在 `Modify Executables` 里改动的参数或选项**不会影响此前创建的快捷方式**；要让快捷方式吃上新设置，必须删掉重建。

### 改快捷方式图标

默认情况下经 MO 创建的快捷方式显示 MO 的图标。要换成程序自己的图标：
右键快捷方式 → `Properties` → `Change Icon…` → `Browse…` → 定位到程序（或图标文件）→ `Open` → `OK` → `Apply` → `OK`。

### Profile 专属快捷方式

**仅对桌面与开始菜单快捷方式有效**——这样它只会在指定 profile 下运行：

1. 先按上面的方式创建快捷方式。
2. 右键快捷方式 → `Properties`。
3. `Target` 字段原本形如 `"<ModOrganizer>/ModOrganizer.exe" "<ApplicationFolder>/Application.exe"`。
4. 在**两个引号字符串之间**插入 ` -p "Profile 名"`，替换成你的 profile 名。
5. 结果应为 `"<ModOrganizer>/ModOrganizer.exe" -p "Profile 名" "<ApplicationFolder>/Application.exe"`。
6. 点 `Apply` → `OK`；（可选）把快捷方式改名以标明它对应哪个 profile。

> 具体工具的配置配方见[常用工具配置配方](tool-recipes.md)；加载机制与 Steam AppID 见[加载机制与 Steam App ID](load-mechanism.md)。
