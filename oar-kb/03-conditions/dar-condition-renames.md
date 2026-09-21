---
id: dar-condition-renames
title: DAR 旧条件改名 / 合并对照
category: 03-conditions
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, DAR, 条件, 改名, 迁移]
aliases: [DAR 条件改名, 旧条件对不上, 条件合并, condition renames, DAR 迁移后条件报错]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: OAR 实现了 DAR 的全部条件且能正确读取旧 mod，但部分条件被改名或合并；IsEquippedShout 在 DAR 里其实检查的是 Power，这是 OAR 顺手纠正的历史误解。
---

# DAR 旧条件改名 / 合并对照

## 前提

> **DAR 的所有条件都已实现。** 保证与基于 DAR 的 mod 完全向后兼容，是整个插件开发过程中的一个关键优先级。有些条件被**合并**了，有些增加了可开关的额外功能。同时有大量新条件可用。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

所以：**旧 mod 不用改就能跑**。本页的意义在于——当你在编辑器里翻 DAR 老 mod（Legacy 区）或迁移时，**看到的名字和记忆里不一样**，不要以为是错了。

## 对照表

| DAR 旧条件 | OAR 新条件 | 备注 |
| --- | --- | --- |
| `IsEquippedShout` | **`IsEquippedPower`** | 官方原话：*"because that's what it actually checked in DAR"*（因为那才是它在 DAR 里实际检查的东西） |
| `IsEquippedRight`、`IsEquippedLeft` | **`IsEquipped`** + 「左手」布尔组件 | 一个条件 + 一个 true/false 组件 |
| `IsEquippedRightType`、`IsEquippedLeftType` | **`IsEquippedType`** + 「左手」布尔组件 | 同上 |
| `IsEquippedRightHasKeyword`、`IsEquippedLeftHasKeyword` | **`IsEquippedHasKeyword`** + 「左手」布尔组件 | 同上 |
| `ValueEqualTo`、`ValueLessThan`、`IsActorValueEqualTo`、`IsActorValueLessThan`、`IsActorValueBaseEqualTo`、`IsActorValueBaseLessThan`、`IsActorValueMaxEqualTo`、`IsActorValueMaxLessThan`、`IsActorValuePercentageEqualTo`、`IsActorValuePercentageLessThan` | **`CompareValues`** | 十个条件合并成一个 |
| `IsFactionRankEqualTo`、`IsFactionRankLessThan` | **`FactionRank`** | 合并 |
| `IsLevelLessThan` | **`Level`** | 改名 |
| `CurrentGameTimeLessThan` | **`CurrentGameTime`** | 改名 |
| `CurrentPackageProcedureType` | **`CurrentPackageType`** | OAR 内部改名（3.0.0），为与 CommonLibSSE 对齐 |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## `IsEquippedShout` 这段历史值得单独说

这是 OAR 纠正 DAR 的一个**语义 bug**，社区里不常提：

> **新增条件：`IsEquippedShout`** —— 因为 **DAR 里那个原本的 `IsEquippedShout` 其实检查的是 `IsEquippedPower`**。legacy mod 会被当作它们本来想说的是 `IsEquippedPower` 来处理。**这也顺带修掉了某些 DAR mod 之前工作不正常的问题。**

> 来源：<https://bakemono.app/p/patreon/25643772/80271137>（0.5.1 开发日志）

实践含义：**你现在写 `IsEquippedPower` 就是 DAR 时代 `IsEquippedShout` 的等效行为**；而 OAR 的 `IsEquippedShout` 是一个**语义正确的新条件**（真的判龙吼）。

> 顺带一提：这个改名在 3.0.0 引入过一个 bug（运行时会把 `IsEquippedShout` 又改成 `IsEquippedPower`），**3.1.0 修复**。如果你卡在 3.0.x，注意这一点。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（3.1.0 变更条目）

## DAR → OAR 条件语法对照（文本 vs JSON）

迁移时你面对的是完全不同的语法：

**DAR 旧格式**（`_conditions.txt`，一行串联）：

```
IsActorBase("Skyrim.esm" | 0x00000007) AND IsSneaking()
```

- 格式是 `函数名("插件名" | 0xFormID)`，多个条件用 `AND` / `OR` / `NOT` **在同一行串联**；
- **FormID 要丢掉代表加载顺序的前两位**：`0xAA123456` → `0x00123456`；
- `Skyrim.esm` 的 `0x00000007` 是 **Player 这条 NPC_ 记录**——最常用的"只对玩家生效"写法。

**OAR 原生 JSON**：

```json
{
  "conditions": [
    { "condition": "IsActorBase", "requiredVersion": "1.0.0.0",
      "Actor base": { "pluginName": "Skyrim.esm", "formID": "7" } },
    { "condition": "IsSneaking", "requiredVersion": "1.0.0.0" }
  ]
}
```

- 外层数组就是 AND，**不用写 AND**；
- 数值/引用包成对象；
- 取反用 `"negated": true`；
- 组合条件用 `"condition": "OR"` + 大写 `Conditions` 子数组。

> 来源：本工作区实测记录 `oar-kb/08-practices/`（原 `OAR/` 目录的内容已并入本库）。

## 迁移时顺手做的事

官方明确建议：

> 把 DAR mod 移植到 OAR 时，你可以在编辑器**作者模式**下从 legacy submod 保存一份配置。**那个文件插件不会读取**，但你可以手动把它移到结构正确的新文件夹里。这能省掉你重做条件的功夫。不过也**请考虑新的条件和/或功能**——你也许能简化或改进你的条件。
>
> 还有一个按钮可以**把配置复制到剪贴板**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（miscellaneous notes）

完整迁移步骤见 [手动迁移流程](../07-migration/manual-migration.md)。

## 相关

- [OAR 与 DAR：兼容策略与 Legacy 区](../00-overview/oar-vs-dar.md)
- [手动迁移流程](../07-migration/manual-migration.md)
- [条件全清单](conditions-list.md)
