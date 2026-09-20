---
id: filters-and-grouping
title: 筛选、分组与冲突高亮
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 筛选, 分组, 冲突高亮, Namefilter]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 可按分类或 Nexus ID 分组，Filter 侧栏提供预置与自定义筛选并支持 And/Or 组合；选中 mod 时用红/绿高亮输赢双方。
kind: tutorial
---

# 筛选、分组与冲突高亮

## 分组（Grouping）

- 位置：左窗格**底部中间的下拉菜单**。
- 目前有两种分组方式：**按分类**（Categories）或**按 Nexus ID**。
- 视觉提示：分组激活时，mod 列表会被框在**绿色**框里。选 `No Grouping` 关闭分组。
- ⚠️ **分组开启时无法用拖放改优先级**（自 1.2.15 起已支持在所有分组方式下拖放）。

## 冲突高亮

除了 `Flags` 列的图标（见[界面总览](ui-layout.md)），MO 还会给与**当前选中 mod** 存在冲突的 mod 上色：

- **绿色** = "输"的一方：这些 mod 有文件不会进游戏。
- **红色** = "赢"的一方：这些 mod 会替换掉所选 mod 的文件。

## 筛选（Filters）

- 入口：左窗格**左下角的 `Filter` 按钮**，会从左弹出侧栏。
- 用**左键**选择筛选条件；按住 **Ctrl + 左键**可多选。
- **取消**某个筛选：右键高亮项 → `Deselect filter`；或 Ctrl+点击它；或点击侧栏内任意空白处。
- **组合逻辑**：侧栏底部的 `And` / `Or`。`And` 只显示**同时满足所有**所选条件的 mod；`Or` 显示满足**任意一个**条件的 mod。
- 视觉提示：筛选激活时，mod 列表会被框在**红色**框里。

### 预置筛选

| 筛选 | 选中什么 |
| --- | --- |
| `<Checked>` | 当前 profile 中**已启用**的 mod。 |
| `<Unchecked>` | 当前 profile 中**未启用**的 mod。 |
| `<Update>` | 有可用新版本的 mod（执行 `Check all for update` 后会自动选中）。 |
| `<Managed by MO>` | 安装进 MO 的 mod。 |
| `<Managed outside MO>` | 非 MO 管理的 mod。 |
| `<No Category>` | 未分配分类的 mod。 |
| `<Conflicted>` | 已启用、且与其它已启用 mod 存在文件冲突的 mod。 |
| `<Not Endorsed>` | 尚未 endorsement 的 mod（含被标记为 `Won't Endorse` 的）。 |
| **Filter Categories** | 在所有 `<...>` 预置之后，按 Category 列属性筛选，自定义分类也会出现在这里。要新增分类：右键筛选侧栏 → `Edit Categories`（详见[自定义 mod 分类](mod-categories.md)）。 |

## Namefilter

在侧栏里直接**输入 mod 名称的片段**即可快速定位。

> 相关：[界面总览](ui-layout.md)、[冲突解决与优先级](conflict-resolution.md)、[文件树、隐藏文件与冲突面板](hide-files-and-filetree.md)。
