---
id: game-version-1-7-x
title: 1.7.x 版本冲击（2026 年 Bethesda 更新）
category: 00-overview
kind: reference
version: 1.0.0
updated: 2026-09-30
tags: [总览, 版本, 兼容性, 现状, 1.7]
aliases: [1.7.99, 1.7.104, 版本冲击, 更新后崩溃, 新版游戏, 降级, downgrade]
source: https://skse.silverlock.org/
summary: 2026 年 8 月 Bethesda 时隔两年半再次更新游戏，版本号跳到 1.7.x；SKSE、RaceMenu、Engine Fixes 等原生插件的适配现状，以及当下该留在哪个版本。
---

# 1.7.x 版本冲击

**这是 2026 年下半年本领域最大的一件事**：游戏版本号从 1.6.x 跳到 **1.7.x**，
整套依赖原生 DLL 的美化链路（SKSE → RaceMenu → 物理 → 分配工具）需要重编译或重写。

## 官方站当前状态（一手）

SKSE 官网 `skse.silverlock.org` 首页直接写着：

> **2026-08-14: After two and a half years, Bethesda has announced an incoming update to Skyrim. Please be prepared.**

当前各档（2026-09-30 核实）：

| 档位 | SKSE64 | 游戏版本 |
|---|---|---|
| **Anniversary Edition（Steam，当前）** | **2.3.1** | **1.7.104** |
| Anniversary Edition（GOG） | 2.2.6 | 1.6.1179 |
| Special Edition（1.5.x 一支） | 2.0.20 | 1.5.97 |
| VR | SKSEVR 2.0.12 | 1.4.15 |

另外 **1.7.99 → SKSE 2.3.0**（由一个明确列出版本对照的插件页给出：1.7.99/2.3.0、1.7.104/2.3.1）。

> ⚠️ 注意：**GOG 档仍停在 1.6.1179**。所以"Steam 用户已经到 1.7.104、GOG 用户还在 1.6.1179"
> 是当下的真实分裂状态，选插件版本档时不要串。

## 各 mod 的适配现状

| 组件 | 1.7.x 状态 | 依据 |
|---|---|---|
| **SKSE64** | ✅ **已支持**（2.3.1 对应 1.7.104） | SKSE 官网 —— 一手 |
| **RaceMenu** | ❌ **未发布**。作者 2026-08-23 帖：1.7.99 版**已完成**但被 SKSE 的 Papyrus 函数 bug 卡住；**1.7.104 还没做**；正在做 CommonLibSSE-NG 移植 | 作者帖 —— 一手 |
| **SSE Engine Fixes** | ❌ 待更新（社区回帖：依赖它的补丁类 mod 都在等它） | 社区回帖 |
| **Scrambled Bugs / Scrambled Updates** | ⚠️ Scrambled Updates 只支持 **1.7.99**，**暂不支持 1.7.104** | 作者与用户帖 |
| 其他原生插件 | 部分页面已明确写 **"Not supported: 1.7.x"** | 插件发布页 —— 一手 |
| **BodySlide / Outfit Studio** | ✅ 不受影响（外部工具，不挂钩游戏运行时） | 常识 + 无崩溃报告 |

RaceMenu 作者帖原文要点（2026-08-23，一手）：

> "RaceMenu for Game Version 1.7.99 is completed, but pending an update for SKSE which
> currently has some broken Papyrus functions (crash the game). Seems they made a 1.7.104,
> I haven't done this yet."

截至 **2026-09-30**，官方 Files 页最新仍为 **0.4.20.0（2026-04-21）**，页面回帖里仍在等：

> "It's not 'dead' dead.. the modder has to rewrite the whole mod because of how much was
> broken in the last update. It will take a while."（2026-09-28）

## 现在该怎么办

**结论：如果你依赖 RaceMenu（捏脸必然依赖），当下不要追新。**

| 选择 | 适用 | 代价 |
|---|---|---|
| **留在 / 降级到 1.6.1170（Steam）或 1.6.1179（GOG）** | 绝大多数人 | 需要在 Steam 里阻止自动更新（或用 downgrade 工具）；新出的 mod 会逐步只支持 1.7.x |
| **跟进 1.7.104** | 想玩最新内容、且能接受捏脸功能缺失 | RaceMenu 全功能消失（滑块、预设、overlay 都没了），且**有 CTD 风险**（见下） |

### ⚠️ 跟进 1.7.x 必读：overlay NIF 会直接崩游戏

Bethesda 在这次更新里**改坏了 Nif 解析的一个边界情况**：
**有 `NiTriShape` 但没有 `NiTriShapeData` 的网格会让游戏崩溃**，而 RaceMenu 的
overlay nif 恰好全是这种结构。详见 [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md)。

## 与其他库的一致性

`community-shaders-kb` 记录 Community Shaders 支持 **1.6.1170 / 1.6.1179 / 1.5.97**，
明确**不支持 1.7.99 / 1.7.104** —— 与本文"1.7.x 是新分支、生态尚未跟上"的判断一致。

## 来源

- SKSE 官网首页（2.3.1 = 1.7.104、2.0.20 = 1.5.97、GOG 2.2.6 = 1.6.1179、2026-08-14 警告）：`https://skse.silverlock.org/` —— **一手**
- RaceMenu 作者帖（1.7.99 完成但被 SKSE 卡住、1.7.104 未做、CLSSE-NG 移植中、overlay NIF 崩溃）：Nexus RaceMenu Posts 区 —— **一手（作者本人）**
- 1.7.99 → SKSE 2.3.0 的对照：插件发布页 sticky 中列出的版本表 —— **一手（作者整理）**
- Scrambled Updates 仅支持 1.7.99、Engine Fixes 待更新：**社区回帖**
- "Not supported: 1.7.x"：插件发布页 Supported versions 段 —— **一手**

> ⚠️ **时效提醒**：这是**进行中**的事件，适配状态每周都可能变。动手前请重新核对
> SKSE 官网首页与 RaceMenu 的 Files / Posts 页。
