---
id: manual-migration
title: 手动迁移流程（DAR → OAR 原生结构）
category: 07-migration
kind: tutorial
version: 1.0.0
updated: 2026-09-21
tags: [OAR, DAR, 迁移, 手动, 编辑器]
aliases: [手动迁移, DAR 改 OAR 原生, migration, 怎么从 DAR 迁过来, config.json 迁移]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 官方推荐做法——在编辑器作者模式下从 Legacy submod 导出配置（或复制到剪贴板），手动搬到结构正确的新文件夹，再顺手用新条件简化。
---

# 手动迁移流程（DAR → OAR 原生结构）

## 先决定要不要迁

| 目标 | 该做什么 |
| --- | --- |
| 只要能用 | **什么都不做**。OAR 会把它当 `Legacy` 读 |
| 要能编辑、要干净管理 | 迁移 |
| 只有一两个 DAR mod | **手动迁移**（本页） |
| 有一堆 | 用 [转换工具](converter-tools.md) |

## 官方给的做法

官方描述原文：

> 把 DAR mod 移植到 OAR 时，你可以在游戏内编辑器的 **作者模式** 下，从 **legacy submod 保存一份配置文件**。
> **那个文件插件不会读取**，但你可以手动把它移到结构正确的新文件夹里。**这应该能省掉你重做条件的功夫。**
> 不过**请考虑新的条件和/或功能**——你也许能简化或改进你的条件。
>
> 还有一个按钮可以**把配置复制到剪贴板**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（miscellaneous notes）

## 完整步骤

### Step 0 · 起游戏，选中目标

1. 进游戏，按 **`~`** 打开控制台，**鼠标点选角色**选中求值目标（通常是自己）。
2. 再按 **`~`** 关闭控制台。
3. 按 **`Shift + O`** 打开 OAR 编辑器。

> 这一步别省——没有求值目标，条件图标、当前值、预览按钮都不工作。

### Step 1 · 切到作者模式

在编辑器右上的三个单选按钮（检视 / 使用者 / 模组作者）里选 **作者模式（Author）**。

### Step 2 · 找到 Legacy 区的那个 submod

- 展开 **`Legacy`** 这个 replacer mod。
- 里面的名字是**数字编号**（DAR 的优先级文件夹名）。
- **怎么知道是哪个编号？** 用 MO2 打开该 DAR mod 的文件夹，看 `meshes\...\DynamicAnimationReplacer\_CustomConditions\` 下的目录名。

> 社区实例：巴哈姆特教程里，作者认出自己那个高跟鞋 mod 的编号是 `68601`–`68606`。
> 来源：<https://forum.gamer.com.tw/Co.php?bsn=2526&sn=154942>

### Step 3 · 导出配置

两种方式，任选：

| 方式 | 用途 |
| --- | --- |
| **保存配置文件** | 在 Author 模式下保存，得到一个**插件不会读取**的配置文件；手动搬走即可 |
| **复制配置到剪贴板** | 直接拿到 JSON 文本，粘进你新建的 `config.json` |

> 作者说这个导出的文件"插件不会读取"——所以**它不会污染现有加载**，纯粹是给你搬运用的草稿。

### Step 4 · 建新结构

在 `Data\Meshes` 内任意位置（推荐插在 `animations\` 这一层）：

```
…\animations\OpenAnimationReplacer\<你的Mod名>\<你的Submod名>\
    ├── config.json      ← 把导出的内容粘进来
    └── <原动画>.hkx      ← hkx 内容一字不改，只是换个位置/名字
```

规则见 [目录结构与路径插入规则](../02-structure/directory-structure.md)。

### Step 5 · 顺手改进条件

官方"强烈建议"这一步，而且理由很实际：

> 请考虑新的条件和/或功能——你也许能简化或改进你的条件。

对照 [DAR 旧条件改名 / 合并对照](../03-conditions/dar-condition-renames.md) 与 [容器条件](../03-conditions/condition-containers.md)。最常见的三类改进：

| DAR 时代的写法 | OAR 的更好写法 |
| --- | --- |
| 一堆 `IsEquippedRightType` + `IsEquippedLeftType` 拼一起 | 一个 `IsEquippedType` + `OR` 两条（左手 true/false） |
| 十个 `ValueEqualTo` / `IsActorValueEqualTo` 之类 | 一个 `CompareValues` |
| 手工复制一长串条件到每个 submod | 一个 **`PRESET`** |

### Step 6 · 处理旧结构（关键！）

⚠️ **`DynamicAnimationReplacer\` 是 OAR 的合法入口。** 留在 `meshes` 里会被当成 `Legacy` replacer mod 一起加载。**不移走，新旧两套同时生效，行为不可预期。**

正确做法：把它**移到 `meshes` 之外**（哪怕是 mod 根目录下的 `_备份\`），就不会被扫描。

```bash
mkdir -p "$MOD/_备份_原DAR结构"
mv "$MOD/meshes/actors/character/animations/DynamicAnimationReplacer" "$MOD/_备份_原DAR结构/"
```

> 来源（这条是本工作区实测的硬结论）：[实战](../../oar-kb/08-practices/)（原 `OAR/` 目录的内容已并入本库）。

### Step 7 · 重启游戏验证

- **运行时不能物理增删动画文件**，所以改完必须**重启游戏**。
- 重启后用 `Shift+O` 的**替换列表**标签页确认新 submod 出现在该动画的替换项里、且优先级没问题。
- 用**动画日志**"演"一遍，确认走的是你新做的那套。

## 另一种选择：保留 Legacy

**不迁移也有它的道理**：

- 你只是借用别人的动画，不需要长期维护；
- 你的改动全在 User 模式里（写 `user.json`），原 mod 一个字没动——这时**根本不用迁移**。

官方也提到 DAR 老 mod **可以在游戏内被编辑**，并且**可以保存用户配置**（0.6.1 起）：

> 现在你可以为 legacy mod 保存用户配置了。你也可以在想要撤销改动时重新载入它们，或者直接删掉用户配置以重新载入原始配置（全都通过游戏内 UI）。

> 来源：<https://bakemono.app/p/patreon/25643772/80648390>

**这也是最省事的路线**：把 Legacy mod 当"只读的上游"，你的改动全部落在 `user.json`。

## 相关

- [转换工具（批量）](converter-tools.md)
- [DAR 旧条件改名/合并对照](../03-conditions/dar-condition-renames.md)
- [OAR 与 DAR：兼容策略与 Legacy 区](../00-overview/oar-vs-dar.md)
- [实战：改造别人的动作包](../08-practices/authoring-workflow.md)
