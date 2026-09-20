---
id: ui-layout
title: 界面总览：工具栏、左窗格与右窗格
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 界面, 工具栏, 左窗格, 右窗格, 图标]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 工具栏六按钮加三状态位；左窗格管 mod 与优先级（含 Flags 图例），右窗格管插件、归档、Data、存档、下载。
kind: reference
---

# 界面总览：工具栏、左窗格与右窗格

## 工具栏

左上六个按钮（依次为 archive、globe、profile、gear、puzzle、wrench）：

| 按钮 | 作用 |
| --- | --- |
| **archive（归档）** | 浏览并打开 mod 归档包来安装 mod。**注意：只能安装归档包内的 mod**，非归档形式无法用它安装。 |
| **globe（地球）** | 用浏览器打开所管游戏的 Nexus 主页；同时把 MO 设置为可通过 `Download with Manager` 下载该游戏的 mod。 |
| **profile（档案）** | 设置不同的 mod 配置组合，见 [Profile 切换](profile-switching.md)。 |
| **gear（齿轮）** | 管理可在 MO 内运行的第三方可执行程序，见 [配置第三方程序](third-party-executables.md)。 |
| **tools（工具）** | 打开各类可扩展插件：默认含 INI Editor、NMM Import、Configurator。 |
| **settings（设置）** | 配置 MO 的各方面行为，见 [设置页参考](settings-tabs.md)。 |

右上还有三个：

- **warning 图标**：提示 MO 设置存在**潜在问题**。点击后会在窗口底部日志里显示检测到的问题；**图标灰掉表示一切正常**。
- **update 按钮**：更新 MO 到最新版。**变色 = 有更新可点**；灰 = 暂无更新。
- **help 菜单**：需要帮助时用它。点击 help 后，把光标指向界面控件，**能解释的控件会变成问号**，左键点击即可阅读说明；还含 MO wiki 链接、`Report Issue`（跳官方 bug 追踪器）、以及各引导教程入口。

## 左窗格（mod 列表）

- 按当前 profile 显示**全部已安装 mod**、它们的**优先级顺序**与**启用状态**。
- 可按名称、标记（flag）、分类、版本号、优先级、安装日期、Nexus ID 排序。
- **Ctrl+左键可多选**，再按**空格键**批量切换选中状态。

### Flags 列图标图例

| 图标 | 含义 |
| --- | --- |
| 闪电 + 绿加号 | 该 mod 会覆盖低优先级 mod 的文件，**且自身文件不会被任何人覆盖**。 |
| 闪电 + 红减号 | 该 mod 不覆盖任何 mod，但**有文件会被高优先级 mod 覆盖**。 |
| 闪电 + 绿加号与红减号 | 既覆盖低优先级 mod，也有文件被高优先级 mod 覆盖。 |
| 闪电（无加减号） | 该 mod 会被其它 mod 完全覆盖——**装了等于没装**。 |
| 红 X | MO 不认为该 mod 含有效数据（名称变灰且斜体）。右键选 `Ignore missing data` 可清除该标记（会在 mod 目录里放一个空的 textures 文件夹凑成"有效"）。 |
| 心形问号 | 该 mod 尚未 endorsement。 |
| 便签 | 你给该 mod 添加过 notes。 |

### 版本列的颜色

- **绿色** = 已是最新版；**红色** = 有新版可用；**红色且前置警告图标** = 你的版本号数字更高，但与 Nexus 当前版本对不上。

### 优先级列

- 数值越大，资源覆盖优先级越高；同名冲突时**高数值者覆盖低数值者**。
- 默认且推荐**按优先级升序排序**，方便直接拖放调整。

> 提示：只有在左窗格使用 `No groups` 分组方式**且** `Priorities` 列激活时才能拖放排序。**自 1.2.15 起所有分组方式都支持拖放**，若你没看到该功能，请升级 MO。

## 右窗格（标签页）

- **Plugins**：所有已启用 ESM/ESP 的加载顺序管理（见 [启用 mod 与激活插件](enable-and-activate.md)）。
- **Archives**：mod 内含 BSA 时在此列出，可解包（见 [BSA 管理与解包](bsa-management-usage.md)）。
- **Data**：展示"通过 MO 启动的程序"所看到的 Data 目录——File 列是文件名，Mod 列是来源 mod；**来源名显示红色**表示另有激活的 mod 提供了同名文件并正在覆盖它（悬停红名可看冲突文件位置）。勾选底部 `Show only conflicts` 只看冲突文件。
  - 右键菜单：`Open/Execute`、`Add as Executable`（把 Data 里的程序快速加进可执行列表）、`Hide`（加 `.mohidden` 后缀使其失效）、`Write to file`（导出整个虚拟 Data 目录及来源清单）、`Refresh`。
- **Saves**：存档与缺失插件（见 [存档查看与 Fix Mods](saves-management.md)）。
- **Downloads**：所有通过 MO 下载的 mod（见 [下载管理与 Nexus 集成](downloads-and-nexus.md)）。

## 其它相关页面

- [筛选、分组与冲突高亮](filters-and-grouping.md)
- [文件树、隐藏文件与冲突面板](hide-files-and-filetree.md)
- [自定义 mod 分类](mod-categories.md)
- [警告面板与潜在 mod 顺序问题](warnings-and-order-problems.md)
