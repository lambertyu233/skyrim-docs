---
id: fallrimtools-resaver
title: FallrimTools / ReSaver（存档清理）
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [存档, 清理, 脚本, 排错, 工具]
aliases: [FallrimTools, ReSaver, 存档清理, 清理存档, 卸载mod残留, 存档编辑器, 5031, save cleaner]
source: https://www.nexusmods.com/skyrimspecialedition/mods/5031
summary: 读写 Skyrim SE/LE 与 Fallout 4 存档、以树形视图编辑脚本数据的工具；最常用动作是清掉「未附着脚本实例」，但它刻意保守，别对它期待过高。
---

# FallrimTools / ReSaver

## 是什么（发布页原文要点）

> **ReSaver** 是 FallrimTools 里的主程序。前代工具（Script Scalpel、SaveTool）
> 界面难用或过滤能力有限，且**不能处理 SE 的存档格式**——ReSaver 是为解决这些问题而写的。

能力清单（发布页）：

- **读写 Skyrim SE / LE / Fallout 4 存档**（含 Crash Fixes 引入的新存档格式）；
- 显示大量存档内部信息；
- **编辑脚本数据**、终止脚本线程（右键 ActiveScript → Terminate）；
- **Mod Parsing**：解析你的 ESM/ESP/PEX/BSA，帮助定位"这段数据是哪个 mod 的"；
- 过滤（regex、按插件、按 mod），并能**预览每种清理操作会删掉什么**；
- 清理动作：删未附着脚本实例、删未定义元素、清理 formlist、删插件数据（**部分功能未实现**）。

- 要求：**Java**（纯 Java 实现）。
- 存档位置：`文档\My Games\Skyrim Special Edition\Saves`。

## 标准操作（发布页给的入门流程）

1. 打开 ReSaver → 选存档 → 看到脚本元素的树结构。
2. **Clean 菜单 → Show Unattached Instances**（先看将被删的东西）。
3. **Clean 菜单 → Remove Unattached Instances**。
4. **保存为新文件**（别覆盖唯一的存档）。
5. 进游戏测读。

> 社区还常用 `Show/Remove Undefined Elements`——
> 但它的历史"战绩"更差（更容易弄坏老存档/复杂存档），**应视为专家选项而非默认动作**。

## 诚实边界（本条目最重要的一段）

社区里对这个工具有两种声音，且**都对**：

- **它能救存档**：脚本风暴（script storm）类的存档，清未附着实例常常有效。
- **它救不了全部**：专家指出，让存档"看起来脏"的大头**不是**未附着的 Papyrus 实例，
  而 ReSaver **刻意不动**这些东西：

| 留着的东西 | 为什么 |
|---|---|
| Change Form（你访问过的 cell / ref / actor） | 无法证明是"死的"，误删会造成地形/任务/NPC 缺失 |
| 仍被引用的"垃圾" | 在引用图上仍然"附着" |
| 任务 / 剧情 / alias 状态 | 与未附着实例是两回事 |
| 活动效果、AI 包、背包冗余 | 是活状态，不是孤儿 |
| **`.skse` cosave** | 独立文件；ReSaver 的故事主要在 `.ess` 的 Papyrus 堆 |
| JContainers / 其它插件的文件存储 | 不在它的模型里 |

**结论**：它优化的是"**别把存档弄坏**"，不是"把每一字节垃圾清干净"。
跑完一轮自动清理后存档仍然很大，**不是操作失误，是它的设计边界**。

## 关于"干净存档"这个说法

发布页引用的长期争论值得记住：有观点认为
**"不存在所谓的 clean save"**——卸载 mod 后存档里总会留下被永久改变的数据，
反复装卸会累积损伤，唯一的正规做法是**读一个"装该 mod 之前"的存档**。
ReSaver 的作者没有反驳这一点的技术核心，只是提供了"尽量救"的工具。

## 现代存档的另一个半边：`.skse` cosave

一份现代 SE 存档通常是成对的：

- `X.ess`：Bethesda 存档容器（含 Papyrus VM 快照等）；
- `X.skse`：SKSE 插件的序列化数据（RaceMenu/SKEE、各类 SKSE 插件的数据）。

**只删其中一半 = 孤儿 cosave**，表现为"存档读起来怪怪的"。
**只重写 `.ess` 的清理工具，对现代 modlist 而言本身就是不完整的。**

## 使用纪律

1. **只在新副本上操作**，保留原始存档。
2. 清理后**先测试读档**，确认无误再覆盖。
3. 别指望它解决"装了新 mod 后的崩溃"——那多半不是脚本残留问题。

## 相关

- [Papyrus 日志与脚本排错](../09-diagnostics/papyrus-logging.md)（先确认是不是脚本问题）
- [PapyrusUtil SE](../01-frameworks/papyrusutil.md)、[JContainers SE](../01-frameworks/jcontainers.md)（数据不在 .ess 里的两类）
- [常见错误认知](../12-sources/common-misconceptions.md) 第 10 条
