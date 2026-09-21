---
id: oar-vs-dar
title: OAR 与 DAR：兼容策略与 Legacy 区
category: 00-overview
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [OAR, DAR, 兼容性, Legacy, 迁移]
aliases: [OAR 和 DAR 冲突吗, DAR 还能用吗, Legacy 是什么, oar dar, DAR 转换, 旧 mod 兼容]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: OAR 与 DAR 本体不兼容，但完全向后兼容 DAR 格式的动画 mod——它们会被自动转换，并在编辑器里统一归入名叫 Legacy 的一个 replacer mod 之下。
---

# OAR 与 DAR：兼容策略与 Legacy 区

## 三条关系一句话说清

| 问题 | 答案 |
| --- | --- |
| 两个插件能同时启用吗？ | **不能**。OAR 与 Dynamic Animation Replacer **本体**不兼容。 |
| 老 DAR 动画 mod 还能用吗？ | **能，完全兼容**。官方原话：*"It just works"*。 |
| 需要把老 mod 转成新格式吗？ | **不需要**。转换是自动的、运行时的；转换工具只是为了让目录更好管理。 |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 自动转换是怎么发生的

作者原文：

> 凡是被放在 `DynamicAnimationReplacer` 文件夹里的 mod，也会在载入游戏时被读取并转换成新结构。因为它们缺少新功能，这些新功能**默认全关**，所以行为会和以前完全一致——除了像"随机条件的结果会在动画循环/回声时重新掷"这类改进。

> DAR 里没有 *Replacer mod → Submod* 这个概念，所以**所有 DAR mod 都被当作 submod**，归属于编辑器里一个名叫 **Legacy** 的大 replacer mod。它们的名字就是**它们的文件夹名**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

也就是说：

- DAR 的 `_CustomConditions\<数字编号>\` 目录 → OAR 里变成 `Legacy` 下的一个 submod；
- **submod 的名字是那个数字编号**（因为 DAR 就是用编号区分的）；
- 想找某个 DAR mod 的编号，直接**用 MO2 打开那个 mod 的文件夹**看目录名即可（社区做法）。

> 社区案例（巴哈姆特）：作者在教程里就是靠 MO2 打开文件夹，认出自己那个高跟鞋 mod 的编号是 `68601`–`68606`。来源：<https://forum.gamer.com.tw/Co.php?bsn=2526&sn=154942>

## DAR 与 OAR 的结构差异（这也是要迁移的理由）

| | DAR | OAR |
| --- | --- | --- |
| 条件写在 | `_conditions.txt`（文本） | `config.json`（JSON，编辑器可视化编辑） |
| 优先级来源 | **文件夹名**就是优先级数字 | `config.json` 里的 `priority` 字段；**文件夹名随便起** |
| 层级 | 一个"优先级文件夹"= 一套条件 | **replacer mod → submod** 两级；嵌套子文件夹可各自成为独立 submod |
| 独立于原文件的用户改动 | 需要改动/污染原 mod 文件 | **User 模式**生成 `user.json`，覆盖 `config.json`，可随时删除 |
| 随机变体 | 多个同条件 submod + 随机条件 | **变体文件夹** `_variants_<动画名>`，无需随机条件 |
| 条件复用 | 无 | **PRESET**（2.2.0） |
| 扩展 | 无 | **SKSE 插件 API** 注册自定义条件 |

> 来源（结构差异）：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 一个必须知道的"DAR 时代遗留"现象

**DAR 的编号长这样：`1750000000`、`68601`、`-30012`。** 光看数字你根本认不出它是哪个 mod 的什么动画。这是社区做转换工具、做 mapping table 的直接动因——**不是为了兼容（OAR 本来就兼容），是为了可读性**。

详见 [转换工具](../07-migration/converter-tools.md)。

## 迁移的两条路

1. **什么都不做**：让 OAR 当 Legacy 读。能跑，只是编辑器里名字是数字，不好管理。
2. **迁到 OAR 原生结构**：
   - 小量、精修 → 在编辑器**作者模式**下从 Legacy submod 导出配置，手动搬到新结构（官方推荐做法）；
   - 大量、批量 → 用 [转换工具](../07-migration/converter-tools.md)。

两条路的具体步骤见 [手动迁移流程](../07-migration/manual-migration.md)。

> 提示：官方明确建议迁移时**顺便看看新条件**——很多 DAR 时代用一长串条件凑出来的逻辑，OAR 里有一句话就能表达的写法。也注意 DAR 的部分条件已被**改名或合并**（见 [DAR 旧条件对照](../03-conditions/dar-condition-renames.md)）。

## 相关

- [OAR 是什么](what-is-oar.md)
- [手动迁移流程](../07-migration/manual-migration.md)
- [DAR 旧条件改名/合并对照](../03-conditions/dar-condition-renames.md)
