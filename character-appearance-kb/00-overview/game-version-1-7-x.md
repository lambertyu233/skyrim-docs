---
id: game-version-1-7-x
title: 1.7.x 版本冲击（2026 年 Bethesda 更新）与"我该留在哪个版本"
category: 00-overview
kind: reference
version: 2.0.0
updated: 2026-10-25
tags: [总览, 版本, 兼容性, 现状, 1.7]
aliases: [1.7.99, 1.7.104, 版本冲击, 更新后崩溃, 新版游戏, 降级, downgrade, 该不该升级, 留在 1.6.1170, racemenu 1.7, skse 2.3.1, patreon beta, 官方还没更新吗, 阻止自动更新, 新版本能用吗]
source: https://skse.silverlock.org/
summary: 2026 年 8 月 Bethesda 时隔两年半再次更新游戏、版本号跳到 1.7.x 之后的完整时间线与各组件适配现状（SKSE 已跟进、RaceMenu 未发布），并给出当下"该留在哪个版本"的决策树与 overlay nif 崩溃的专项提醒。
---

# 1.7.x 版本冲击

**这是 2026 年下半年本领域最大的一件事**：游戏版本号从 1.6.x 跳到 **1.7.x**，
整套依赖原生 DLL 的美化链路（SKSE → RaceMenu → 物理 → 分配工具）需要重编译或重写。
**结论先行：如果你依赖捏脸，当下不要追新。**

## 速览

| 字段 | 内容 |
|---|---|
| 作用层 | 版本事件与选型决策（对应 [`ecosystem-map.md`](ecosystem-map.md) 的 L0/L1 层） |
| 事件起点 | **2026-08-14**（SKSE 官网挂出更新预告） |
| 受影响组件 | 全部原生 DLL 插件；**不受影响**：BodySlide / Outfit Studio 等外部工具 |
| 当前结论 | **SKSE 已跟进（2.3.1 = 1.7.104），RaceMenu 未发布正式版** |
| 推荐动作 | 依赖捏脸 → 留在 **1.6.1170（Steam）/ 1.6.1179（GOG）**；已在 1.7.x → 见决策树 |
| 最新核实日期 | **2026-10-25**（本表随上游发版变化，动手前请重新核对） |

要点：

- **2026-08-20 出 1.7.99 + SKSE 2.3.0；2026-08-27 出 1.7.104 + SKSE 2.3.1 + Address Library v13。**
- **GOG 档仍停在 1.6.1179**（SKSE 2.2.6），与 Steam 形成真实分裂。
- **RaceMenu 官方最新版本仍是 0.4.20.0（2026-04），主文件明确要求 Game Version 1.6.1170。**
- 升级到 1.7.x 后若磁盘上残留旧版 RaceMenu 的 **8 个 overlay nif，会直接崩游戏**。
- 本页涉及的多项社区侧信息（尤其某 mod 是否已适配）**仍属于进行中事件**，请按"来源"复核。

## 前世今生

### 精确时间线（一手核对）

| 日期 | 事件 | 出处级别 |
|---|---|---|
| 2026-08-14 | SKSE 官网首页出现警告："After two and a half years, Bethesda has announced an incoming update to Skyrim. Please be prepared." | 一手（SKSE 官网） |
| 2026-08-19 | SKSE64 **2.2.7** 上传，**仍面向 1.6.1170**，"mostly so users on 1.6.1170 get plugin preloading support" | 一手（SKSE Nexus 置顶帖） |
| 2026-08-20 | 游戏 **1.7.99** 发布，SKSE64 **2.3.0** 同步发布 | 一手（SKSE 置顶帖） |
| 2026-08-21 | **Address Library v12**（面向 1.7.99.0）上传 | 一手（Nexus Files 页） |
| 2026-08-23 | **RaceMenu 作者发帖**：1.7.99 版已完成但被 SKSE 的 Papyrus 函数 bug 卡住；1.7.104 未做；转向 CommonLibSSE-NG 重写；**并首次说明 overlay nif 崩溃问题** | 一手（作者本人） |
| 2026-08-23（同日） | FSMP 仓库出现 "fix(hooks): retarget UpdateHook2 for AE 1.7.99" 提交 | 一手（GitHub commit） |
| 2026-08-27 | 游戏 **1.7.104** 发布，SKSE64 **2.3.1**（含 "fix PlayerCharacter functions"）与 **Address Library v13**（"for ALL game versions up to 1.7.104.0"）同步上线 | 一手 |
| 2026-08-27 | **FSMP 4.1.1** 上传（Nexus Files 页标注 27 Aug 2026 3:57AM） | 一手（Files 页日期）；其面向的游戏版本 ❓ 未确认 |
| 2026-09-28 | 社区回帖仍在等待："It's not 'dead' dead.. the modder has to rewrite the whole mod…" | 社区 |
| 2026-10 初 | Nexus RaceMenu 讨论区出现由用户整理的置顶说明，称作者 **Patreon 上有 beta 可用**（文中给出 Patreon 链接）；同时提醒装 beta 前必须先删/隐藏那 8 个旧 overlay nif | 社区 / 一手链接（发帖具体日期未逐条核实） |
| 2026-10-04 | BodySlide **5.9.1** 发布（不受影响的外部工具，仍在正常迭代） | 一手 |
| 2026-10-25 | 本条目核实日：RaceMenu 官方 Files 页最新版本**仍为 0.4.20.0**，无 1.7.x 正式版 | 一手（本工作区核实） |

### 为什么这件事比以往更严重

以前的版本更新也有类似情况，但这一次有两个不同：

1. **间隔两年半** —— 大量插件作者已经不在活跃状态，"等更新"未必会有结果。
2. **Bethesda 改坏了 NIF 解析的一个边界情况** —— 这不是"要重编译"的问题，而是**游戏本身的向后兼容变差了**，
   连带影响连目前的增量插件也没法简单绕过（详见下节）。

## 它解决什么问题

本页回答三个当下最现实的问题：

1. **我的东西还能不能用**（组件适配现状表）；
2. **我该留在哪个版本 / 该不该降级**（决策树）；
3. **已经升级并且崩了怎么办**（overlay nif 专项 + 通用二分法）。

---

## 配置与使用

### 官方站当前状态（一手）

SKSE 官网 `skse.silverlock.org` 首页当前各档（2026-10-25 核实）：

| 档位 | SKSE64 | 游戏版本 |
|---|---|---|
| **Anniversary Edition（Steam，当前）** | **2.3.1** | **1.7.104** |
| Anniversary Edition（GOG） | 2.2.6 | 1.6.1179 |
| Special Edition（1.5.x 一支） | 2.0.20 | 1.5.97 |
| VR | SKSEVR 2.0.12 | 1.4.15 |

另外 **1.7.99 → SKSE 2.3.0**（SKSE 官方 changelog 明示）。

> ⚠️ 注意：**GOG 档仍停在 1.6.1179**。所以"Steam 用户已经到 1.7.104、GOG 用户还在 1.6.1179"
> 是当下的真实分裂状态，选插件版本档时不要串。

### 各组件的适配现状

| 组件 | 1.7.x 状态 | 依据 |
|---|---|---|
| **SKSE64** | ✅ **已支持**（2.3.1 = 1.7.104；2.3.0 = 1.7.99） | SKSE 官网 + changelog —— 一手 |
| **Address Library** | ✅ **已支持**（v12 = 1.7.99.0；**v13 覆盖到 1.7.104.0**） | Nexus Files 页 —— 一手 |
| **RaceMenu** | ❌ **未发布正式版**。作者 2026-08-23 帖：1.7.99 已完成但被 SKSE 的 Papyrus 函数 bug 卡住；**1.7.104 还没做**；正在做 CommonLibSSE-NG 移植 | 作者帖 —— 一手 |
| **RaceMenu（非官方途径）** | ⚠️ Nexus 讨论区有用户整理的说明称作者 Patreon 上存在 beta（标题含 "RaceMenu AE NG"），对象为有排障意愿的用户；并强调**装之前必须处理掉那 8 个 overlay nif** | 社区整理 + 一手链接 —— **可用性未确认** |
| **Faster HDT-SMP** | ❓ **未确认**。4.1.1 于 2026-08-27 上传；仓库侧有面向 1.7.99 的提交；但社区报告对其面向的游戏版本说法互相矛盾 | Files 页 + GitHub（日期一手）；目标版本 ❓ |
| **CBPC** | ❓ **未确认**。有中文媒体报道称已兼容 1.7.104，但该来源不属于可信一手源，本库不予采信 | **未确认** |
| **SSE Engine Fixes** | ❌ 待更新（社区回帖：依赖它的补丁类 mod 都在等它） | 社区回帖 |
| **Scrambled Bugs / Scrambled Updates** | ⚠️ Scrambled Updates 只支持 **1.7.99**，**暂不支持 1.7.104** | 作者与用户帖 |
| 其他原生插件 | 部分页面已明确写 **"Not supported: 1.7.x"** | 插件发布页 —— 一手 |
| **BodySlide / Outfit Studio** | ✅ 不受影响（外部工具，不挂钩游戏运行时），当前 5.9.1（2026-10-04） | 常识 + 无崩溃报告；版本日期一手 |

RaceMenu 作者帖原文要点（2026-08-23，一手）：

> "RaceMenu for Game Version 1.7.99 is completed, but pending an update for SKSE which
> currently has some broken Papyrus functions (crash the game). Seems they made a 1.7.104,
> I haven't done this yet."

> **一个值得注意的对应**：SKSE64 **2.3.1** 的 changelog 第一条就是
> "fix PlayerCharacter functions"。这与作者所说的"SKSE 的 Papyrus 函数损坏导致崩溃"
> 在时间与内容上都对得上 —— 说明 1.7.99 那版阻塞很有可能已经随 2.3.1 部分消解，
> 但作者已把精力转向 CommonLibSSE-NG 重写，**发布与否取决于他本人**（本段为基于一手事实的推断）。

### 决策树：我该留在哪个版本？

```
先看你的核心诉求 ──►
├─ 依赖 RaceMenu（捏脸 / 身形滑块 / 预设 / overlay）
│     └─► 留在 1.6.1170（Steam）或 1.6.1179（GOG）
│            · 在 Steam 里限制自动更新
│            · 已在 1.7.x 的，需要降级处理（具体手段本库不作推荐，见下）
│            · 代价：新出的 mod 会逐步只支持 1.7.x
│
├─ 只用不依赖 SKSE 的东西（纯 asset / 外部工具）
│     └─► 随便；1.7.104 亦可
│
└─ 想玩最新内容，且能接受捏脸功能缺失
      └─► 可以跟进 1.7.104，但请按下节做完清查再进游戏
            · RaceMenu 全功能消失（滑块、预设、overlay 都没了）
            · ⚠️ 必须先处理旧 overlay nif，否则直接 CTD
```

| 选择 | 适用 | 代价 |
|---|---|---|
| **留在 / 降级到 1.6.1170（Steam）或 1.6.1179（GOG）** | 绝大多数人 | 需要在 Steam 里阻止自动更新（或用降级工具）；新出的 mod 会逐步只支持 1.7.x |
| **跟进 1.7.104** | 想玩最新内容、且能接受捏脸功能缺失 | RaceMenu 全功能消失（滑块、预设、overlay 都没了），且**有 CTD 风险**（见下） |

> 关于"怎么降级"：降级手段本身存在多套社区做法且随 Steam 策略变化，本库**不在此推荐具体工具**。
> 唯一可以放心说的是：**先备份整套 `Data` 与存档**，再动手。

---

## ⚠️ 跟进 1.7.x 必读：overlay NIF 会直接崩游戏

Bethesda 在这次更新里**改坏了 NIF 解析的一个边界情况**：
**有 `NiTriShape` 但没有 `NiTriShapeData` 的网格会让游戏崩溃**，而 RaceMenu 的
overlay nif 恰好全是这种结构。这是本轮最容易被误判的一条 —— 很多人会以为是"某个 dll 坏了"。

**必须确保磁盘上不存在旧版本的这 8 个文件**（作者原帖列举）：

```
Data\Meshes\Actors\Character\Character Assets\face_overlay.nif
Data\Meshes\Actors\Character\Character Assets\body_overlay.nif
Data\Meshes\Actors\Character\Character Assets\hands_overlay.nif
Data\Meshes\Actors\Character\Character Assets\feet_overlay.nif
Data\Meshes\Actors\Character\Character Assets\face_magicoverlay.nif
Data\Meshes\Actors\Character\Character Assets\body_magicoverlay.nif
Data\Meshes\Actors\Character\Character Assets\hands_magicoverlay.nif
Data\Meshes\Actors\Character\Character Assets\feet_magicoverlay.nif
```

作者原话：

> "If you have older versions of these files locally, your game WILL crash."

新版已把这些文件打包进 BSA 以绕过该问题，所以**对策是删除/隐藏本地残留，而不是补文件**。
完整排查步骤见 [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md)。

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 更新后进游戏/读档即刻 CTD | SKSE 团队的标准建议：先清空 `Data/SKSE/Plugins` 再逐个加回，能二分出是哪个插件 | 加回到崩溃的那个为止；多半是尚未适配 1.7.x 的 DLL |
| 完全没有任何报错，只是捏脸界面变回原版 | RaceMenu 的 dll 没被加载（版本不匹配时的**常见无报错表现**） | 回到 [`version-matrix.md`](version-matrix.md) 核对；1.7.x 上没有官方 RaceMenu 可用 |
| 进捏脸菜单就崩 | 磁盘残留旧 overlay nif（八个文件之一） | 按上一节逐个清理；详见 [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md) |
| 物理不生效但不崩 | FSMP 版本档与实际游戏版本不一致（或该版本面向未知） | 检查 FOMOD 选择并重选；必要时回到与游戏版本一致的 FSMP 档。FSMP 4.1.1 的确切适配范围本库标为 ❓ 未确认 |
| 降级后 Mod 管理器报"插件缺失 / incompatible" | 正常：DLL 是按游戏版本编译的 | 装回对应版本的 DLL 即可，存档侧通常需要 clean save 相关流程 |
| 不知道去哪里查"某个插件适配了没" | SKSE 官方置顶帖把 **Modding.wiki** 作为插件适配状态的查询入口 | 查该站当前页面；**本库未逐项核实该站内容 → 未确认** |

## 与其他库的一致性

`community-shaders-kb` 记录 Community Shaders 支持 **1.6.1170 / 1.6.1179 / 1.5.97**，
明确**不支持 1.7.99 / 1.7.104** —— 与本文"1.7.x 是新分支、生态尚未跟上"的判断一致。
`skyrim-tools-kb` 亦有 SKSE64 与 Address Library 的版本矩阵，可与本库交叉核对。

## 取舍与建议

- **绝大多数人：不要追新。** 捏脸是整条链的入口，RaceMenu 缺失 = 后面四层全废。
- **已经在 1.7.104 且不想降级**：至少把 overlay nif 清理做掉；同时接受"捏脸界面回到原版"的现实。
- **不要混用不同游戏版本的 bin/dll**：Steam/GOG、SE/AE/VR 四条链的插件文件各不相同。
- **不要相信二手媒体清单**：本轮检索中出现过若干"某某 mod 已兼容 1.7.104"的说法（含中文聚合站），
  这些**不构成本库的可信来源**，一律以作者的 Nexus Files 页 / GitHub Releases 为准。
- **长期建议**：把"当前各 DLL 版本 + 游戏版本"记在一个文本里存档，下次更新时它就是你的回滚清单。
- **给观望者的保守做法**：保留一份锁定在 1.6.1170 的游戏副本，与另一个可更新的副本分开。

## 来源

- **SKSE 官网首页（一手）**：`https://skse.silverlock.org/`
  （**2.3.1 = 1.7.104**、**2.2.6 = 1.6.1179**（GOG）、**2.0.20 = 1.5.97**、VR 2.0.12；2026-08-14 更新警告）
- **SKSE64 Nexus 置顶帖与 Changelog（一手）**：`https://www.nexusmods.com/skyrimspecialedition/mods/30379`
  （**2.3.0 = 1.7.99**、**2.3.1 = 1.7.104**（含 "fix PlayerCharacter functions"）；2026-08-19/20/27 的更新说明；
  "更新后崩溃先移除 `Data/SKSE/Plugins`"；把 Modding.wiki 作为插件适配状态查询入口）
- **Address Library（一手）**：`https://www.nexusmods.com/skyrimspecialedition/mods/32444`
  （v12 面向 1.7.99.0（2026-08-21）；**v13 "All in One (1.7.104.0)"，2026-08-27**）
- **RaceMenu 作者帖（一手，作者本人）**：Nexus RaceMenu Posts 区 2026-08-23 置顶帖
  （1.7.99 完成但被 SKSE 卡住、1.7.104 未做、CommonLibSSE-NG 移植中、overlay nif 崩溃与八个文件路径）
- **RaceMenu Files 页（一手）**：`https://www.nexusmods.com/skyrimspecialedition/mods/19080?tab=files`
  （最新 0.4.20.0；主文件要求 Game Version 1.6.1170；GOG 可选文件要求 1.6.1179；本条目 2026-10-25 复核）
- **Nexus RaceMenu 讨论区由用户整理的 beta 说明（社区）**：称作者 Patreon 上有 beta
  （`<https://www.patreon.com/expired6978/posts/racemenu-ae-ng-168258762>`），发帖时间为 2026-10 初（具体日期未逐条核实）
  —— **beta 的可用性与发布状态：未确认**
- **FSMP（一手日期 / ❓适配范围）**：Nexus Files 页（4.1.1，2026-08-27）；仓库 `https://github.com/DaymareOn/hdtSMP64`
  （2026-08-23 submit "retarget UpdateHook2 for AE 1.7.99"）
- **Scrambled Updates 仅支持 1.7.99、Engine Fixes 待更新**：Nexus 回帖 —— **社区经验**
- **"Not supported: 1.7.x"**：插件发布页 Supported versions 段 —— **一手**
- **Community Shaders 的版本立场**：见 `community-shaders-kb` —— **一手（CS 官方）**
- ❓ **本轮未能核实的项（请勿当作结论）**：FSMP 4.1.1 面向的具体游戏版本；CBPC 是否已适配 1.7.104；
  RaceMenu Patreon beta 的适配版本与稳定性；Modding.wiki 插件状态表的具体内容

> ⚠️ **时效提醒**：这是**进行中**的事件，适配状态随时可能变。动手前请重新核对
> SKSE 官网首页与 RaceMenu 的 Files / Posts 页。
