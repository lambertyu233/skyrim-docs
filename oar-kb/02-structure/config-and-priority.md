---
id: config-and-priority
title: config.json、user.json 与优先级
category: 02-structure
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, config.json, user.json, priority, 优先级, 冲突]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: replacer mod 级 config.json 只存名字与描述，submod 级存优先级与条件；User 模式生成 user.json 覆盖除名字/描述外的一切；优先级数字越大越优先，同优先级会让编辑器报警告。
---

# `config.json`、`user.json` 与优先级

## 两级配置文件的职责

| 层级 | 文件 | 存什么 |
| --- | --- | --- |
| replacer mod 级 | `config.json` | 目前**只有模组名称与描述** |
| submod 级 | `config.json` | submod 名称、描述、**优先级**、**条件**及其他功能设置 |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（STRUCTURE）

## 官方态度：别手写

官方在描述里三处强调同一件事：

> **你不必用文本编辑器手动编辑 `.json` 文件。虽然可以这么做，但游戏内编辑器能完成一切，而且更容易、更安全。** 手改配置文件很容易不小心出错。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

**但改造场景下你迟早要手写**（批量化、脚本化）。这时最可靠的自学方法（本工作区实测）：

1. 在 `Shift+O` **作者模式**下打开一个 submod；
2. 改一个设置（勾上 Constant polling、改优先级、加一条条件）；
3. 回到文件系统，**用 git diff / 对比工具看 `config.json` 多出了什么字段**。

字段名、值的格式（什么时候用 `{}`、什么时候用数组）全都一目了然，比查文档快且准。

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`。

## 优先级：数字越大越优先

| 来源 | 怎么定 | 备注 |
| --- | --- | --- |
| OAR 原生 submod | `config.json` 里的 **`priority`** 字段 | 数字，**越大越优先** |
| DAR 旧格式 | **文件夹名**就是优先级 | 必须是 `-2147483648 ~ 2147483647` 内不为 0 的整数 |
| DAR 的 ActorBase 派发目录 | 恒为 **0** | 即"按哪个 NPC 用哪套"分文件夹的写法 |

同名动画被多个 submod 命中时 → **取优先级最高的那个**。

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`；官方描述提到 DAR 侧"priority is not defined by the folder names"（即 DAR 是文件夹名定优先级）。

## 什么时候会"顶掉"别人

改造一个动画包之前，**先查这个文件名在整合里还有谁在提供**：

```bash
find "…/mods" -iname "bow_idledrawn.hkx" -printf "%10s  %p\n"
```

一眼能看出：

- 有几个来源；
- 各自文件大小（**大小差异大 = 动画内容/骨骼绑定不同**，是判断"谁是专业包"的快速线索）。

一个刻意拉满的优先级会**压制整合里所有同类动画包**。要不要压，取决于你的意图：

- **想让自己的改动赢** → 保持高优先级；
- **只想在别人没覆盖的状态下生效**（例如只想管潜行、不想影响站姿）→ 应该**收窄条件**，而不是靠优先级硬顶。

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`。

## 冲突排查的正确姿势

游戏内 `Shift + O` → 控制台选中目标 actor（或直接输 FormID）→ 找到那条动画 → **「替换列表（replacements）」标签页**。它会：

- 按**优先级**列出该动画的**所有**替换项；
- 高亮当前**实际胜出**的那个；
- 多个 submod **优先级相同**时，编辑器会给出**警告**（同优先级的结果不可预期，**必须避免**）。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（编辑器：additional tab 按优先级列出所有替换；编辑器会在多个 submod 优先级相同时显示 warning）

## User 模式与 `user.json`（关键机制）

编辑器的三种模式里，**User 模式**是给"用户不改原 mod 文件"用的：

> **User 模式**会生成一个 `user.json`，它会**覆盖 `config.json` 里除 submod 名称与描述之外的一切**。这个模式让用户能做**个性化调整**——改优先级、改条件、禁用动画——**而不影响原始文件**。用户配置文件**可以安全删除**，删掉后会改用原来的 `config.json`。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

实践含义：

- **面向 mod 作者**：Author 模式写 `config.json`（随 mod 分发）。
- **面向使用者**：User 模式写 `user.json`（放在 MO2 的 overwrite 里，或跟随 mod）。
- **想回退**：删掉 `user.json` 即可。

> 社区用法（巴哈姆特）：这正是教程作者说的"**干净的管理使用者自订动作，不会更改到原版 OAR/DAR 动作模组的设定**"。来源：<https://forum.gamer.com.tw/Co.php?bsn=2526&sn=154942>

## 一个真实 `config.json` 的样子（含嵌套 OR）

来自社区（LoversLab 用户贴出的 Gunslicer 包 `Dialogue/config.json`）：

```json
{
  "name": "Dialogue",
  "priority": 800053,
  "replaceOnLoop": false,
  "conditions": [
    { "condition": "IsFemale", "requiredVersion": "1.0.0.0" },
    { "condition": "HasKeyword", "requiredVersion": "1.0.0.0",
      "negated": true, "Keyword": { "editorID": "ElderNPC" } },
    { "condition": "IsChild", "requiredVersion": "1.0.0.0", "negated": true }
  ]
}
```

> 来源：<https://www.loverslab.com/topic/245858-how-to-have-both-follower-and-pc-play-idle-animations-with-oar-conditions>

从这段能读出几条**字段事实**（与官方文档互相印证）：

- 顶层 `conditions` 数组**本身就是 AND**，不需要写 `AND`；
- 取值组件写成**对象**：`{ "editorID": "ElderNPC" }`（关键字可用 `editorID` 而非 formID——这是官方提到的 EditorID 支持）；
- **取反用 `"negated": true`**（编辑器里就是那个 `Negate` 勾选框）；
- `requiredVersion` 逐条都写。
- 还出现了一个顶层开关 `replaceOnLoop`（保留到循环时的行为；对应编辑器里的"循环时保留随机结果"一族设置）。

## 相关

- [目录结构与路径插入规则](directory-structure.md)
- [游戏内编辑器](../05-editor/in-game-editor.md)
- [条件系统总览](../03-conditions/conditions-overview.md)
