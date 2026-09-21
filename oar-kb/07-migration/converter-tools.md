---
id: converter-tools
title: DAR → OAR 转换工具
category: 07-migration
kind: tool
version: 1.0.0
updated: 2026-09-21
tags: [OAR, DAR, 工具, 转换, dar2oar, mapping table]
source: https://www.nexusmods.com/skyrimspecialedition/mods/93359
summary: 三个转换工具（单人转换 / 批量 fork / Rust 重写的 dar2oar）；作者明确说工具存在的意义是"好管理"而不是"兼容"——OAR 本身完全向后兼容 DAR。
---

# DAR → OAR 转换工具

## ⚠️ 先纠正一个常见误解

**这些工具不是为了"让 DAR mod 能在 OAR 里用"。** OAR **本来就完全兼容** DAR（见 [兼容策略](../00-overview/oar-vs-dar.md)）。

工具的动因是**可读性**：DAR 用文件夹名当优先级，一堆 `1750000000`、`800055`、`-30012` 你根本认不出哪个是哪个。社区的说法很直接：
> 「Legacy 区一堆数字编号根本认不出哪个是哪个。」

所以工具的价值在于：**把数字编号转成能看懂的目录名与结构**。

## 三个工具

### 1. DAR to OAR Converter（单人转换）

> Nexus mod **93359** ｜ 作者 **allycat1031 and V3kta** ｜ 版本 1.0.8（2023-06-14）

**做了什么**（官方原文）：

> 这个工具能把 DAR mod 转成新的 OAR 结构。它把 `DynamicAnimationReplacer` 文件夹里的所有文件**复制**到 `OpenAnimationReplacer` 文件夹，然后**在每一层生成所需的 JSON 文件**。
> 为了保持简单，**DAR 的数字文件夹被保留**——这也让生成配置时的优先级判定容易得多。

**怎么用**（官方原文）：

> - 选择你要转换的 DAR mod 的**根文件夹**（即 `meshes` 文件夹所在的那一层）。
> - 选好之后，你可以自定义 **OAR 输出文件夹** 和/或 **OAR Mod 名称**（写进 OAR 项目 `config.json` 里的那个）。
> - 点 **Convert**。

**作者自己列的计划**：更好的 UI、修 bug、完整的编辑器功能。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/93359>

### 2. DAR to OAR Batch Converter（批量 fork 版）

> Nexus mod **113682**

是上面那个的 **fork**，加了**批量处理**能力。

> 来源：用户在需求说明里的归类；本库未逐字核对 Nexus 页面，标记为**社区口径**。

### 3. dar2oar（GUI & CLI，Rust 重写）

> 作者 **SARDONYX-sard** ｜ 当前版本 **v1.1.0**（2026-04-29）
> 仓库：`github.com/SARDONYX-sard/dar-to-oar` ｜ Nexus mod **101822**
> 许可：MIT OR Apache-2.0（原 C# 版由 Allison Payne 以 MIT 发布，本工具是重写）

**特性**（官方 Wiki）：

> - DAR → OAR 转换（**CLI 与 GUI 两种应用**）
> - DAR 语法错误报告
> - 已实现的子命令：**Remove OAR dir（移除 OAR 目录）**、**Unhide DAR files（取消隐藏 DAR 文件）**
> - **Mapping table（映射表）**——补足 OAR 在 GUI 上的可读性
> - 可自定义的本地化系统
> - 可改 JavaScript 与 CSS

> 来源：<https://github.com/SARDONYX-sard/dar-to-oar/wiki>

## Mapping Table 是它的核心卖点

**它解决的就是"数字编号认不出"这个问题。** 官方 README 原文说明：

> **什么是映射文件？** 你可以把 DAR 的优先级文件夹名**重命名成对应优先级的特定名字**，方式是传入一份对应表，如下所示。

映射表样本（`mapping_table.txt`）：

```
8000000 Combat
8000001
8000002
8000005
8000005 Female
8001000
8001000 Unarmed
8001010
8001010 Sword
```

**解析结果**：

```
8000000  Combat
8000001  Combat_1
8000002  Combat_2
8000005  Female
8001000  Unarmed
8001010  Sword
```

> 「如你所见，如果某个优先级文件夹名**没有对应项，就会在末尾加一个序号**。」

**不传映射表时**，就直接用优先级文件夹名当目录名（于是拿到一堆 `8000001`、`8001005`……）。

> 来源：<https://github.com/SARDONYX-sard/dar-to-oar/blob/main/README.md>

### CLI 用法

```
dar2oar cli --src "./data/Smooth Moveset" --mapping-file "./settings/mapping_table.txt"
```

主要参数（官方 help 输出）：

| 参数 | 含义 |
| --- | --- |
| `--src` | DAR 源目录（**必需**） |
| `--dist` | OAR 目标目录 |
| `--name` | 写进 `config.json` 的 mod 名 & 文件夹名（不填则从 `--src` 推断） |
| `--author` | 写进 `config.json` 的作者 |
| `--mapping-file` | 分区名对应表路径 |

新版本还支持 `dar2oar convert <dir> --run-parallel --stdout --log-level ... --log-path ...` 的形式，便于脚本化批量跑（README 里给了完整的 PowerShell 批处理样例）。

> 来源：<https://github.com/SARDONYX-sard/dar-to-oar>

## 选哪个

| 场景 | 建议 |
| --- | --- |
| 就一两个 mod，想顺手看清结构 | **单人转换器（93359）**，或干脆手动（见 [手动迁移流程](manual-migration.md)） |
| 一批 mod 要批量转 | **批量 fork（113682）** 或 **dar2oar 的 CLI** |
| 想要"数字编号 → 可读名字" | **dar2oar**（有 mapping table） |
| 不想装额外工具 | **手动迁移** —— 官方推荐的方式，且能顺手简化条件 |

## ⚠️ 转换前后都要做的事

1. **备份**。转换是复制 + 生成配置，但一旦你开始改，原 DAR 结构就是你唯一的回退手段。
2. **确认旧结构已被移出 `meshes`**，否则新旧两套同时生效。见 [手动迁移流程](manual-migration.md) 的 Step 6。
3. **转换后重启游戏**并看 OAR 日志确认被识别。
4. **检查 `config.json` 有没有 BOM**（Python `json.load` 读二进制、断言开头不是 `EF BB BF`）——手改/生成都可能带 BOM。

## 相关

- [手动迁移流程](manual-migration.md)
- [OAR 与 DAR：兼容策略与 Legacy 区](../00-overview/oar-vs-dar.md)
- [排错对照表](../05-editor/troubleshooting.md)
