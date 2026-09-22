---
id: directory-structure
title: 目录结构与路径插入规则
category: 02-structure
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 目录结构, replacer mod, submod, 路径]
aliases: [OAR 目录怎么放, 动画放哪个文件夹, 路径规则, directory structure, meshes 放哪, mod 文件夹结构]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 自 2.0.0 起 replacer mod 可放在 Data\Meshes 内任意位置——把 OpenAnimationReplacer\MyMod\MySubmod\ 这段插进原始动画路径的任意处，后面保留原始相对路径。
---

# 目录结构与路径插入规则

## 两级结构：replacer mod 与 submod

官方原文（STRUCTURE 节）：

> 每个 *replacer mod* 包含一个或多个 *submod*，外加一份目前只记录模组名称和描述的 `.json` 配置文件。每个 *submod* 包含替换动画和一份 `.json` 配置文件，里面记录该 submod 内所有动画的全部信息，例如 submod 名称、描述、**优先级、条件**和其他功能。

这个 `replacer → submods` 结构之所以存在，主要是**因为大多数动画替换 mod 本来就是这么工作的**——它们包含多个文件夹，各自带不同条件和动画。现在这些子文件夹都能收进一个文件夹，结构更整洁。

```
OpenAnimationReplacer
├── Replacer mod 1
│      ├── Submod A
│      │      ├── [animation files]
│      │      └── config.json   ← submod 配置文件
│      ├── Submod B
│      │      ├── [animation files]
│      │      └── config.json
│      └── config.json          ← replacer mod 配置文件
└── Replacer mod 2
       ├── Submod C
       │      ├── [animation files]
       │      └── config.json
       └── config.json
```

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（STRUCTURE）

## 谁是 submod？——`config.json` 的位置说了算

这是本库补充的一条**实用判据**（与官方结构一致，只是把推论说白）：

- **`config.json` 所在的那个文件夹，就是 submod 的根**；它覆盖该文件夹及其**所有子文件夹**里的 hkx。
- 如果某个子文件夹**自己又放了一份 `config.json`**，它就变成一个**独立的 submod**，与父级互不干扰。
- 这就解释了为什么专业动画包（如 Gunslicer 的包）是"两层 `config.json`"：顶层只写名字和描述，每个功能文件夹各写自己的条件和优先级。

> 意味着你可以用**嵌套结构**给同一套动作做多个变体，各自带独立条件——这是 DAR 那种"一个优先级文件夹一套条件"做不到的。

> 来源（判据）：本工作区实测记录 [实战](../../oar-kb/08-practices/)（原 `OAR/` 目录的内容已并入本库）；结构与官方的 "config.json <- the submod configuration file" 注解一致。

## 路径插入规则（自 2.0.0）

官方原文：

> 自 **2.0.0** 起，replacer mod 放在 **`Data\Meshes` 内的任何位置**都会被识别。理解正确放法的一个简单办法，是把它想成**用一段 `OpenAnimationReplacer\MyMod\MySubmod\` 插进原始动画路径中**。

以原本位于 `Data\Meshes\actors\character\animations\male\mt_idle.hkx` 的动画为例，以下任一写法都合法：

```
Data\Meshes\OpenAnimationReplacer\MyMod\MySubmod\actors\character\animations\male\mt_idle.hkx
Data\Meshes\actors\OpenAnimationReplacer\MyMod\MySubmod\character\animations\male\mt_idle.hkx
Data\Meshes\actors\character\OpenAnimationReplacer\MyMod\MySubmod\animations\male\mt_idle.hkx
```

规则一句话：**把 `OpenAnimationReplacer\<替换模组名>\<子模组名>\` 插进原始动画路径的任意位置，后面保留原始相对路径。**

**实际最省事的做法**：插在 `animations\` 这一层——因为行为文件里的引用是以 `Animations\` 开头的，动画本体也确实住在 `...\character\animations\` 下，这一层最不容易记错。

> 来源（"最实用"这条）：本工作区实测记录 [实战](../../oar-kb/08-practices/)（原 `OAR/` 目录的内容已并入本库）。

## 命名规则（与 DAR 的重大差异）

- **优先级不再由文件夹名决定**！文件夹**可以任意命名**。
- 但官方明确请求：**避免使用非英文字符/符号**，它们很可能会**无法被正确读取**。作者原话里甚至有点认命：「欢迎懂 Unicode 字符串与文件路径的人来提 PR，我放弃了。」
- 命名建议：**可辨认但简短**——显示名称反正定义在 `.json` 里，而 Windows 有路径字符上限。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（STRUCTURE / miscellaneous notes）

⚠️ 本工作区的实测补充：这条"避免非英文"是**成立**的——但要注意区分两类东西：
- **文件夹名**（replacer mod 名、submod 名）→ 建议全英文；
- **`.json` 里的 `name` / `description` 字段**→ 中文没问题（那是给人看的文字，不是路径）。

## 运行时不能做什么

> 请记住，游戏运行时**不能**物理地往 mod 里新增或删除动画文件，也**不能**增删 mod 本身——改动只在**重启游戏后**生效。
> 不过你**可以**在编辑器里禁用动画或子模组。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（STRUCTURE）

## 相关

- [`config.json`、`user.json` 与优先级](config-and-priority.md)
- [替换的心智模型](../08-practices/animation-key-model.md)
- [变体](../02-structure/variants.md)
