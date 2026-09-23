---
id: directory-layouts-catalog
title: 目录结构全集：所有可能的摆放方式
category: 02-structure
kind: reference
version: 1.0.0
updated: 2026-09-23
tags: [OAR, 目录结构, 全集, 插入点, 源码, 实测]
aliases: [OAR 目录有几种, 摆放方式, 路径插入点, 目录布局, layout, folder layout, 实测分布]
source: https://github.com/ersh1/OpenAnimationReplacer
summary: 穷举 OAR 全部合法目录形态。源码给出的唯一硬约束——剥掉 OpenAnimationReplacer\ 后恰好两层目录，剩下的字符串必须逐字等于 data\meshes\ 下的原版动画路径；官方 4 例；本机 1920 mod 实测的 8 种插入点、419 个 submod 的路径分布。
---

# 目录结构全集：所有可能的摆放方式

> 本页把 OAR 的目录形态**穷举成一张可查表**。规则部分取自官方源码
> （`github.com/ersh1/OpenAnimationReplacer`，2026-09-23 读 main 分支），
> 分布部分取自本机实测（`D:\game\PureLOTD`，1920 个 mod）。
> 只想看"我该把文件放哪"，直接跳到下面的 §3（入口插入点）与 §4（submod 内部布局）。

## 0. 一句话硬约束

**剥掉 `OpenAnimationReplacer\<Mod>\<Submod>\` 这三段之后，剩下的字符串必须逐字等于
`data\meshes\` 下那条原版动画的路径。**

前半句决定"能插在哪"，后半句决定"submod 里面长什么样"。两次匹配都是
**转小写后的精确字符串比较**——不是模糊匹配，写错一个字母就是永久静默失效。

## 1. 源码给出的证据链

| 事实 | 出处（官方源码） |
| --- | --- |
| 在 `data\meshes\` 下**递归**查找 basename 为 `openanimationreplacer` / `dynamicanimationreplacer` 的目录 | `Parsing.cpp::CacheDirectoriesInternal`（`oarFolderName` / `legacyFolderName` / `meshesPath` 三个常量） |
| 剥掉 `…\OpenAnimationReplacer\` **后面恰好两层**目录 | `Parsing.cpp::StripReplacerPath`，注释原文：`strips the OAR/DAR substring ([Open/Dynamic]AnimationReplacer\subdirectory\subdirectory")` |
| 匹配键 = 剥完之后的路径 | `ReplacementAnimation.cpp::GetOriginalPath()` → `ConvertVariantsPath(StripReplacerPath(fullPath))` |
| 查询端把游戏请求拼成 `data\meshes\<原版路径>` 后同样转小写再查 | `OpenAnimationReplacer.cpp::CreateReplacementAnimations`（`key = ToLower(lexically_normal("data\\meshes\\" / a_path / animName))`） |
| submod 内子目录**递归**扫描；`_variants_` 开头的目录另路处理 | `Parsing.cpp::ParseNonLegacyAnimationsInDirectory` |

由此推出三条可执行规则：

1. **入口目录名固定**——必须叫 `OpenAnimationReplacer`（大小写不敏感）。
2. **它下面恰好两层**——`<Mod 名>\<Submod 名>\`，不能多也不能少。
3. **剥掉后剩下的部分逐字复现原版路径**——包括 `animations\`、`male\`、`female\` 这些段。

因此"可以插在 `Data\Meshes` 内任意位置（自 2.0.0）"的**真正含义**是：
插入点之前的东西照样被保留，插入点之后的东西照样被保留，只要**中间这段恰好三段**就行。
换个插入点，就换个"submod 里该从哪一级开始复现"。

## 2. 官方给出的摆放示例（Nexus STRUCTURE 节）

官方以 `Data\Meshes\actors\character\animations\male\mt_idle.hkx` 为例，列出四例：

```
1) Data\Meshes\OpenAnimationReplacer\MyMod\MySubmod\actors\character\animations\male\mt_idle.hkx
2) Data\Meshes\actors\OpenAnimationReplacer\MyMod\MySubmod\character\animations\male\mt_idle.hkx
3) Data\Meshes\actors\character\OpenAnimationReplacer\MyMod\MySubmod\animations\male\mt_idle.hkx
4) etc...
```

> 原文措辞："think of it as **interrupting the original animation path with a block of
> `OpenAnimationReplacer\MyMod\MySubmod\`**"，最后一个是 `etc...`——即**插入点不限于这三处**。
> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

⚠️ 注意第 1 例：插入点在 `Meshes\` 之后时，submod 里要**从 `actors\` 开始**复现整条路径。
这正是多数人只照抄第 3 例、换个 mod 就失效的原因——**插入点变了，submod 里的起点必须跟着变**。

## 3. 实测：8 种入口插入点

本机 49 个 `OpenAnimationReplacer` 根目录的实际分布（同一 mod 可以有多个根，例如角色 + 第一人称）：

| 插入点（`meshes` 之后到 `OpenAnimationReplacer` 之前） | 数量 | 代表 mod | submod 内路径起点 |
| --- | --- | --- | --- |
| `actors\character\animations\` | 32 | `Dynamic Dodge Animation` | `male\` / `female\` / 文件名 |
| `actors\character\animations\`（`Meshes` 大写） | 8 | `Feminine WnR OAR No armor CH-YZ` | 同上 |
| `Actors\Character\animations\`（三级大写） | 3 | `Draw Fix - Move Equip Animation Fix` | 同上 |
| `actors\character\_1stperson\animations\` | 2 | `Heavy Armory FOMOD Installer`、`TK dodge firstperson 8 ways dodge` | `male\` / 文件名 |
| `actors\dragon\animations\` | 1 | `Dragon Random Stagger Animation` | 文件名（非角色动画） |
| `actors\horse\animations\` | 1 | `Horse Jump Fix` | 文件名 |
| `actors\character\`（**在 `animations` 之前**） | 1 | **`Live Action 0.3.9b`** | `animations\…` |
| `Meshes\`（**直接根下**） | 1 | `Weapon Styles - DrawSheathe Animations for IED` | `Actors\Character\Animations\…` |
| `DynamicAnimationReplacer`（legacy 根，见 §6） | 30 | 各类旧 DAR 包 | 数字目录 + `_conditions.txt` |

**实证结论**：路径中 `meshes` / `actors` / `character` / `animations` 的**大小写完全无关**
（源码两端都 `ToLower`），位置也确实任意。唯一要守的是"剥离三段后能否拼回原版路径"。

真实样例（逐字来自磁盘，可直接对照）：

```
# 插入点在 Meshes\ 之后 → submod 内从 Actors 起
Weapon Styles…\Meshes\OpenAnimationReplacer\WS\2h Hip\Actors\Character\Animations\2hc_equip.hkx
  剥掉 OpenAnimationReplacer\WS\2h Hip\ → data\meshes\Actors\Character\Animations\2hc_equip.hkx ✓

# 插入点在 animations\ 之后 → submod 内从 male\ 起
Heavy Armory FOMOD Installer\…\animations\OpenAnimationReplacer\IAA\3rdP - Katana Nothing-L\male\mt_sprintforward.hkx
  剥掉 OpenAnimationReplacer\IAA\3rdP - Katana Nothing-L\ → …\animations\male\mt_sprintforward.hkx ✓

# 插入点在 character\ 之后 → submod 内从 animations\ 起（Live Action 用的是这一种）
Live Action 0.3.9b\meshes\actors\character\OpenAnimationReplacer\Live Action\Angry_Flip\animations\male\…
  剥掉 OpenAnimationReplacer\Live Action\Angry_Flip\ → …\character\animations\male\… ✓
```

## 4. submod 内部的全部布局

### 4.1 动画文件放在哪

| 形态 | 长这样 | 什么时候用 | 实测占比 |
| --- | --- | --- | --- |
| **直放 submod 根** | `<Submod>\mt_idle.hkx` | 原版动画就在 `animations\` 根下（无性别/子目录） | 1520 个 hkx |
| **复现原版相对路径** | `<Submod>\male\mt_idle.hkx`、`<Submod>\female\…` | 原版动画在 `male\` / `female\` 下（角色待机/移动类多是） | male 41 + female 242（另有大小写变体 6+6） |
| | `<Submod>\animations\…` | 入口插在 `character\` 之后（如 Live Action） | 1749 个 hkx（最常见） |
| | `<Submod>\Actors\Character\Animations\…` | 入口插在 `meshes\` 之后 | 892 个 hkx |
| | `<Submod>\dlc01\…`、`<Submod>\horse_rider\…`、`<Submod>\tkdodge\…` | 原版动画本身就在这些子目录里 | 21 / 139 / 10 |
| **任意深度的子目录** | 任意 | 扫描是**递归**的（源码 `ParseNonLegacyAnimationsInDirectory` 递归调用自身），只要求拼回来对得上 | — |

> ⚠️ **"直放根下"不等于"可以省略性别目录"**。匹配是逐字精确的：原版在
> `animations\male\mt_jump.hkx`，你就必须放到 `<Submod>\male\mt_jump.hkx`。
> 实测里确实存在把 `mt_jump.hkx` 直接丢在 `<Submod>\` 下的包，但按源码规则那一条对不上——
> 这类包要么本来就替换的是无性别路径，要么其中一部分并未真正生效。
> **别照抄**：先确认游戏请求的完整路径再决定放哪（`Shift+O` 动画日志会显示请求路径与来源）。

### 4.2 特殊目录（都是源码里的硬编码标记）

| 目录 | 语义 | 真实样例 |
| --- | --- | --- |
| `_variants_<原文件名去掉扩展名>` | **变体目录**：放进去的 hkx 会被随机/顺序选中。`ConvertVariantsPath` 会剥掉 `_variants_` 前缀再补 `.hkx`，所以 **`_variants_mt_idle` = 替换 `mt_idle.hkx`** | `…\Idle action\female\_variants_mt_idle\mt_idle0_d.hkx`<br>`…\Live Action\Dance_F02\animations\_variants_animobjectcheer\GS152.hkx` |
| 任何**包含** `.mohidden` 的目录名 | **整棵子树被跳过**（`IsHiddenDirectoryName`，子串匹配、不区分大小写）。用来临时停用一批动画而不用删除 | 本机实测 0 个（该写法在 DAR 时代更常见） |
| `overrideAnimationsFolder` 指向的目录 | **共享动画目录**：让多个 submod 共用同一批 hkx 而不必复制。注意它的路径基准是 **submod 的父目录**（即 `<Mod>\` 下），不是 submod 内部 | 见 §5 字段表 |

变体目录的官方命名规则（原文）：`_variants_[animNameWithoutExtension]`，
"so, for `mt_idle.hkx`, the folder should be named `_variants_mt_idle` and **placed in the same location**"。
即：它替代的是那个 hkx 的位置，层级必须一致（`male\_variants_mt_idle\` ✓，不是 `_variants_mt_idle\male\`）。
变体内部的文件名**随便**（建议短名，避免超长路径）。1.2.0 引入随机模式，2.2.0 引入顺序（Sequential）模式。

## 5. 两级配置 + `user.json`

```
OpenAnimationReplacer/
└── MyMod/                    ← replacer mod
    ├── config.json           ← mod 级：name / author / description
    ├── SharedAnims/          ← 可选的共享动画目录（被 overrideAnimationsFolder 指向）
    ├── SubmodA/
    │   ├── config.json       ← submod 级：priority / conditions / 开关
    │   └── [动画文件]
    └── SubmodB/
        ├── config.json
        └── [动画文件]
```

| 文件 | 位置 | 内容 | 优先级关系 |
| --- | --- | --- | --- |
| `config.json`（mod 级） | `MyMod\` | 目前只有 `name` / `author` / `description` | 无 |
| `config.json`（submod 级） | `MyMod\SubmodA\` | `name` / `description` / `priority` / `conditions` / 各开关 | 作者发布用 |
| `user.json` | 同上（与 submod 级 `config.json` 同级） | User 模式下生成 | **覆盖 `config.json` 里除 name/description 以外的一切**；删掉即回退 |

本机实测的 mod 级与 submod 级真实内容（`Live Action 0.3.9b`）：

```json
// …\OpenAnimationReplacer\Live Action\config.json     ← mod 级
{ "name": "Live Action", "author": "slizer40000", "description": "Aroused people act horny." }

// …\OpenAnimationReplacer\Live Action\Angry_Flip\config.json   ← submod 级
{
  "name": "Angry_Flip",
  "description": "Flip Off Dialogue Target",
  "priority": 348000,
  "ignoreDontConvertAnnotationsToTriggersFlag": true,
  "keepRandomResultsOnLoop": true,
  "conditions": [ { "condition": "IsInCombat", "requiredVersion": "1.0.0.0", "negated": true }, … ]
}
```

官方对 submod 级附加设置的完整清单（Nexus 原文，对应字段见括号）：

| 官方说法 | 字段（本机实测/源码） |
| --- | --- |
| Constant polling of required conditions… immediate replacement | `interruptible`（编辑器里叫 Interruptible） |
| Keeping the results of random conditions on animation loop | `keepRandomResultsOnLoop`（旧写法 `replaceOnLoop`） |
| Sharing random results throughout the whole submod | `sharedRandomResults` / 随机作用域设置 |
| Custom blend times when animations get interrupted | `customBlendTime*` 一族 |
| Ignoring the No Triggers animation clip flag | `ignoreDontConvertAnnotationsToTriggersFlag` |
| Setting a required project name（如只为 DefaultMale 加载） | `requiredBehaviorProjectName` |
| Setting the name of the folder that contains animations（多 submod 共用动画） | `overrideAnimationsFolder`（基准目录 = `<Mod>\`，**不是 submod 内**） |

> 字段名不必背：`Shift+O` → **Author 模式**改一个设置 → 用 git diff 看 `config.json` 多出什么，
> 比查文档更准。官方自己也说"不必手改 json，游戏内编辑器更安全"。

## 6. Legacy（DAR 格式）的两种形态

路径里**包含** `DynamicAnimationReplacer`（大小写不敏感）即被判为 legacy；
它们全部被归入编辑器里一个叫 **Legacy** 的大 replacer mod 之下，名字就是文件夹名。

| 形态 | 结构 | 条件来源 | priority |
| --- | --- | --- | --- |
| **A · `_CustomConditions` 型** | `…\DynamicAnimationReplacer\_CustomConditions\<整数>\<male\|female>\<file>.hkx` + 同级 `_conditions.txt` | 同目录的 `_conditions.txt` | **目录名那个整数** |
| **B · ESP + FormID 型**（按 NPC 派发） | `…\DynamicAnimationReplacer\<插件名.esp>\<FormID 十六进制>\<file>.hkx` | 自动生成 `IsActorBase` 条件 | 恒为 **0** |

- 两种都由 `Parsing.cpp` 解析：A 型读 `_conditions.txt`；B 型从路径取出 `插件名.esp` + FormID，
  用 `LookupForm` 生成 `IsActorBase` 条件（FormID **不带 `0x`**）。
- DAR 的 priority 语义是"目录名即优先级"，且 `DAR` 有 **16384 条动画的内部上限**
  （Live Action 的 changelog 记过一次因此回退的事故）；OAR 默认上限 0x7FFF，
  另有实验开关可提到 0xFFFE。
- ⚠️ 只要路径里有 `DynamicAnimationReplacer` 这个目录，它就会被当成合法入口加载。
  **做 OAR 原生结构时务必把旧的 DAR 目录移出 `meshes`**，否则新旧两套同时生效。

## 7. 跨 MO2 mod 的拼合（一个 submod 可以由多个 mod 拼成）

`Conditional Armor Type Animations`（只提供 `config.json` 与条件）+
`CATA Addon - Vanargand II Male Idle Walk Run`（只提供 `CATA\Light Armor\male\*.hkx`）
= 在 MO2 的虚拟文件系统里合并成**同一个** `CATA\Light Armor\` 目录。

所以：

- **条件可以来自一个 mod，动画来自另一个 mod**（子模组的两个必要条件被拆在两处满足）。
- 看到"某个 mod 里没有 `config.json` 却照常生效"别急着判它坏——去找同名路径的另一个 mod。
- 想替换其中一半（只换动画不换条件）也是合法的：把动画放进同名路径即可。
- 原理见 [VFS 节点类：一个目录可有多个来源](../../mo2-usvfs-kb/03-architecture/vfs-node-classes.md)。

## 8. 最容易踩的四个坑

1. **插入点换了，submod 里的起点没跟着换。** 照抄别人 `animations\OpenAnimationReplacer\…`
   的结构，却把包放在了 `character\` 下 → 拼不回去 → 永久静默失效。
2. **路径拼写差一段就失效，且不报错。** 匹配是逐字精确的；`male` 写成 `Male` 没问题（大小写无关），
   但**漏掉 `male\`** 就是另一条路径。自查手段：`Shift+O` → 动画日志 / 替换列表，
   它会显示游戏请求的路径与所有候选来源。
3. **三段层级数不对。** `OpenAnimationReplacer\Mod\`（少一层）或 `\Mod\Sub\Extra\`（多一层）
   都会导致剥离位置错位，整包失效。
4. **文件夹名用中文/符号。** 官方明确请求避免非英文（Unicode 路径读取有历史问题）；
   但 `config.json` 里的 `name` / `description` 写中文完全没问题——那是给人看的文字。

## 相关

- [目录结构与路径插入规则](directory-structure.md)（官方规则的原始转述）
- [`config.json`、`user.json` 与优先级](config-and-priority.md)
- [动画变体（Variants）](variants.md)
- [替换的心智模型：文件名的权威来源与 hkx 判定](../08-practices/animation-key-model.md)
- [实战：改造别人的动作包（六步法）](../08-practices/authoring-workflow.md)
