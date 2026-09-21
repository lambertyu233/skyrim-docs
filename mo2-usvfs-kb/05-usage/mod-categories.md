---
id: mod-categories
title: 自定义 mod 分类
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 分类, categories.dat, Nexus ID]
aliases: [自定义分类, mod 分类, categories, 给 mod 分组]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 在 Settings → Configure Mod Categories 里增删分类、关联 Nexus 分类 ID、设置父子层级；配置存于 categories.dat。
kind: tutorial
---

# 自定义 mod 分类

MO 内置的分类很有限，装 mod 时常看到有些有分类、有些没有。可自行补齐。

## 入口

`Settings` → `General` 标签页底部的 **`Configure Mod Categories`** 按钮。会打开一个列出所有现有分类的窗口（看不全就把窗口往左右拖宽一点）。

## 基本操作

- **单击**某分类选中它（整行高亮）。
- **双击** `ID`、`Name`、`Nexus IDs`、`Parent ID` 任一项即可进入编辑框。
- **右键**任意分类 → 弹出菜单可**添加 / 删除**分类。选 Add entry 会在高亮项**上方**新建一个空白分类，MO 会给它分配新 ID，名字初始为 `new`。
- `ID` 列显示的编号主要用于参照，一般无需修改；**最左侧无标题列**是分类在列表中的出现次序，可**点击拖动**调整位置。
- 其余字段都可双击（或选中后按 F2）编辑。

## 关联 Nexus 分类

1. 打开 Nexus 对应游戏的 Categories 页面（在 Nexus 主页把鼠标悬停在 `Files` 上，选 `Categories`）。
2. 悬停某个分类，浏览器里会显示链接预览，**末尾的 `CAT=<数字>`** 就是 Nexus 分类 ID（例：`CAT=67` 对应 Abodes - Player Homes）。
3. 回到 MO，选中你的新分类，**双击 `Nexus IDs` 字段**填入该数字。
4. **双击 `Name` 字段**把 `new` 改成你想要的分类名。

## 建立层级（父子分类）

- MO 有些分类是嵌套的子分类，做法是填 **`Parent ID`**（窗口最右列）。
- 例：新建分类 `FOOD`，MO 分配 ID 为 25；再建一个 `ROTTEN`，把它的 `Parent ID` 设为 25，`ROTTEN` 就成了 `FOOD` 的子分类。
- 删除分类：高亮后右键 → remove。

## 给单个 mod 改分类

在左窗格右键任意 mod：

- `Add/Remove Categories`：下拉菜单里增删分类；
- `Replace Categories`：整组替换分类；
- `Primary Category`：设置显示在 Category 列里的主分类。

## 备份分类

分类数据存放在 **`categories.dat`**。编辑满意后，关掉 MO，到 MO 文件夹复制一份 `categories.dat` 存好——将来重装 MO 时把它放回主目录，你的分类就回来了。

> 相关：[筛选、分组与冲突高亮](filters-and-grouping.md)（分类也可用作筛选条件）、[备份与恢复](backup-and-restore.md)。
