---
id: directory-structure
title: 目录结构与路径插入规则
category: 02-structure
kind: reference
version: 1.1.0
updated: 2026-09-23
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

## 实测：整合里真实存在的三种形态

> 本节只留三种最典型的形态；**完整穷举（8 种入口插入点、submod 内部全部布局、
> 源码级匹配规则）见 [目录结构全集：所有可能的摆放方式](directory-layouts-catalog.md)。**
>
> 来源：本机实测（2026-09-23，`D:\game\PureLOTD`，1920 个 mod 的整合；取样范围 = 该整合内全部含 `OpenAnimationReplacer\` 的 mod）。

**形态 A · 标准原生（新做 mod 照这个）**——`Another Jump Animation Male CH-YZ`：

```
meshes\actors\character\animations\OpenAnimationReplacer\
└── Another Jump Animation\          ← replacer mod
    ├── config.json                  ← 只写 name / description
    └── Male jump\                   ← submod
        ├── config.json              ← 优先级 + 条件
        ├── mt_jump.hkx
        └── mt_jumpfast.hkx
```

**形态 B · 条件与动画分居两个 mod（CATA 模式，最容易被看懵）**：

```
Conditional Armor Type Animations\（主体：只有 json，没有 hkx）
└── …\OpenAnimationReplacer\CATA\
    ├── config.json
    ├── Heavy Armor\config.json
    ├── Light Armor\config.json      ← 条件写在这里
    ├── No armor\config.json
    └── No armor Mage\config.json

CATA Addon - Vanargand II Male Idle Walk Run\（addon：只有 hkx，没有 json）
└── …\OpenAnimationReplacer\CATA\
    └── Light Armor\
        └── male\mt_idle.hkx …       ← 同一个 submod 路径，只补进动画文件
```

**同一个 submod 目录可以被拆在多个 MO2 mod 文件夹里**：MO2 把两者的
`CATA\Light Armor\` 合并成同一个虚拟目录，于是"条件来自主体、动画来自 addon"。
所以遇到"某 mod 里没有 `config.json` 却照常生效"时，别急着判它坏
——先去找同名路径的另一个 mod。（原理见 [VFS 节点类：一个目录可有多个来源](../../mo2-usvfs-kb/03-architecture/vfs-node-classes.md)。）

**形态 C · DAR 迁移残留（submod 目录名是数字）**——`Dynamic Dodge Animation`：

```
…\OpenAnimationReplacer\Dynamic Dodge - DMCO-0.9.6\
├── config.json
├── 6000\config.json + MCO_Dodge*.hkx
├── 6001\config.json + MCO_Dodge*.hkx
└── 6002\ …
```

submod 目录名沿用 DAR 时代的**优先级数字**。OAR 照样认（目录名已无语义，
优先级以 `config.json` 里的 `priority` 为准），但新做的 mod 没必要学这种写法。

**hkx 放哪：要不要带性别目录**——实测两种都存在：

- `CATA Addon…\Light Armor\male\mt_idle.hkx` → **保留性别目录**，男女可分别给不同文件；
- `Another Jump Animation…\Male jump\mt_jump.hkx` → hkx **直接放 submod 根下**。

官方规则是"后面保留**原始相对路径**"，其上三个示例也都带 `male\`。
⚠️「省略性别目录仍会命中」这一点只在整合里观察到实例、**未在官方文档中找到明文**；
需要区分男女动作时，按官方写法保留 `male\` / `female\` 是稳妥做法。

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

- [目录结构全集：所有可能的摆放方式](directory-layouts-catalog.md)
- [`config.json`、`user.json` 与优先级](config-and-priority.md)
- [替换的心智模型](../08-practices/animation-key-model.md)
- [变体](../02-structure/variants.md)
