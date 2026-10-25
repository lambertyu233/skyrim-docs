---
id: skse64
title: SKSE64 与 Address Library
category: 01-prerequisites
kind: tool
version: 3.0.0
updated: 2026-10-25
tags: [前置, SKSE, Address Library, 版本, 1.7]
aliases: [脚本扩展, 地址库, skse 版本对应, 怎么装 skse, skse64_loader, getskseversion, 1.6.1170, skse 2.2.6, skse 2.3.1, address library 装错, se ae 地址库, skse 是什么, skse 历史, skse 启动器, 游戏版本不匹配, 前置链]
source: https://skse.silverlock.org/
summary: SKSE64 与游戏本体精确版本对应的硬事实（1.6.1170↔2.2.6、1.7.99↔2.3.0、1.7.104↔2.3.1、GOG 1.6.1179↔2.2.6）、Address Library 的 SE/AE 二选一静默失效坑，以及"最小前置链推荐停在 1.6.1170"的理由与操作。
---

# SKSE64 与 Address Library

> **一句话**：SKSE64 是整条捏脸/身形链的地基，Address Library 是让第三方插件免于随游戏版本重编译的
> 解耦层。两者共享同一条铁律——**版本必须与游戏可执行文件精确对应**，错配的表现
> 不是崩溃，而是**功能静默消失**。

本页管"装哪个、怎么装、版本对不对"。版本对照的**权威表**在本库
[`../00-overview/version-matrix.md`](../00-overview/version-matrix.md)，1.7.x 事件的完整时间线与
决策树在 [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)——
**本页结论若与那两篇冲突，以那两篇为准。**

## 速览

| 项 | 内容 |
|---|---|
| 作者 | SKSE64：**ianpatt**（Ian Patterson）与 **behippo**（Stephen Abel）；Address Library：**meh321** |
| 性质 | 注入式**脚本扩展器**（SKSE64）+ **地址映射数据库**（Address Library） |
| 官方分发 | SKSE 唯一官方点 `skse.silverlock.org`；Address Library：Nexus `mods/32444` |
| 支持平台 | **仅 Steam 与 GOG** 版 Skyrim SE/AE；**不支持** Epic / Microsoft Store / Game Pass |
| 版本铁律 | SKSE64 与 `SkyrimSE.exe` **精确对应**：1.6.1170↔2.2.6、1.7.99↔2.3.0、1.7.104↔2.3.1、GOG 1.6.1179↔2.2.6 |
| Address Library | **SE（1.5.x）与 AE（1.6.x/1.7.x）两套独立数据库**，装错的表现是插件全部静默失效 |
| 影响范围 | 缺它或版本错 → 依赖 SKSE 的**全部**功能消失（捏脸、身形滑块、物理、分配工具） |
| 维护状态 | SKSE 活跃（2026-08 起已跟进 1.7.x）；**下游插件普遍没跟上** |

要点：

- **第一性事实**：SKSE64 是原生 DLL 注入，版本与游戏强绑定——错了不是"降级可用"，
  而是 DLL 直接拒绝加载。
- **2026-08 起版本分裂**：Steam AE 进入 1.7.x（1.7.99↔2.3.0、1.7.104↔2.3.1），
  **GOG 仍停在 1.6.1179↔2.2.6**，两条线不可串。
- **Address Library 的坑是静默的**：装错 SE/AE 数据库，游戏照常运行，但依赖它的插件
  全部失效，没有任何报错。
- 捏脸链的推荐站位：**游戏 1.6.1170 + SKSE 2.2.6/2.2.7**（GOG 为 1.6.1179 + GOG 档 2.2.6）。
- 遇到"某个功能整体不见"，第一动作是**核对版本**，不是翻冲突。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 2016-10 | Special Edition 发布，SKSE64 随之出现 | 从这一刻起"游戏更新 ↔ 脚本扩展器重编"成为常态 |
| 2019-11-18 | SKSE64 的 Nexus 页面建立 | 后来核对版本对应关系最重要的依据就是它的 Changelog |
| 2020-02-07 | **Address Library** 发布（meh321） | 插件从"硬编码地址偏移"变成"查数据库"，1.6.x 系列小更新不再需要每个插件重编 |
| 2021-10 | Bethesda 发布 Anniversary Edition（1.6.317 起一串更新） | 版本号频繁跳变，催生各种民间"版本对照表" |
| 2026-08-14 | SKSE 官网挂出警告："After two and a half years, Bethesda has announced an incoming update" | 两年半来第一次更新预报 |
| 2026-08-19 | SKSE64 **2.2.7** 上传，**仍面向 1.6.1170**（主要为插件预加载支持） | 给留守 1.6.1170 用户的最后准备 |
| 2026-08-20 | 游戏 **1.7.99** 发布，SKSE64 **2.3.0** 同步 | 新分支开始 |
| 2026-08-21 | Address Library **v12**（面向 1.7.99.0） | 附属更新跟进 |
| 2026-08-27 | 游戏 **1.7.104** + SKSE64 **2.3.1** + Address Library **v13** | 同一天三件套；v13 官方说明 "for ALL game versions up to 1.7.104.0" |

### 它从哪来

SKSE 的传统来自 LE 时代（作者 ianpatt）。SE 之后改名 SKSE64，由 ianpatt 与 behippo
维护，形态始终没变：**一个 loader（`skse64_loader.exe`）+ 一个注入 DLL + 一组 `.pex` 脚本**。
它给 Papyrus 与内存操作打开原生做不到的口子，SkyUI、RaceMenu、物理、分配工具全部建立在它之上。

### 中间经历了什么

最大的结构性变化是 **Address Library**。在它之前，插件把引擎函数地址**硬编码进 DLL**，
游戏每更新一个小版本（1.6.353 → 1.6.640 → 1.6.1130 → 1.6.1170……）都逼着全生态重编译，
"游戏一更新，全生态瘫痪"是这个时代的集体记忆。Address Library 把地址搬进一份
**按游戏版本分档的数据库**，插件只认"库编号（ID）"，跨 1.6.x 小版本通用——
这是现代插件（FSMP、MCM Helper、PapyrusUtil 4.1+、Engine Fixes 等）的共同依赖。

### 现状

SKSE 团队跟进很快：1.7.99 当天出 2.3.0，1.7.104 当天出 2.3.1。**但下游插件没有**：
RaceMenu 官方最新版仍面向 1.6.1170，作者已转向 CommonLibSSE-NG 重写。
GOG 线则停在 1.6.1179。这就是"明明有 SKSE 2.3.1 却不能随便升"的原因——
详见 [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)。

## 它解决什么问题

| 没有它之前 | 后果 |
|---|---|
| **没有 SKSE64** | 只有原生 Papyrus 与 esp 的能力边界：没有内存级操作、没有新脚本函数，SkyUI / RaceMenu / 物理 / 分配工具**一个都不存在** |
| **没有 Address Library** | 每个插件硬编码地址；游戏每更新一次，全部插件等作者重编译，"更新即瘫痪" |

> 顺带解释一个常见疑问：**SKSE 自身不使用 Address Library**（官方明示）。
> Address Library 是给**第三方插件**用的解耦层，装它是为了别人，不是为 SKSE。

## 安装

### 步骤与验证点

1. **确认游戏版本**。Steam 版看 `SkyrimSE.exe` 属性 → 详细信息；或进游戏后控制台
   输 `getskseversion`。验证点：知道自己站在哪一档（1.6.1170 / 1.6.1179 / 1.7.x…）。
2. **下载对应版本的 `.7z`**。唯一官方来源 `skse.silverlock.org`（含 archived builds 页）。
   验证点：文件名/说明里的游戏版本与第 1 步一致。
3. **解压到游戏根目录**（与 `SkyrimSE.exe` 同级，**不是** `Data\`）：
   `skse64_loader.exe`、`skse64_<版本>.dll` 进根目录；
   包内 `Data\Scripts\` 合并进游戏的 `Data\Scripts\`。
   验证点：根目录出现 loader；`Data\Scripts\` 里出现 skee 等 `.pex`。
   > ⚠️ **99% 的安装失败源于把 loader/DLL 也丢进 `Data\`，或整个 `Data` 没合并。**
4. **装 Address Library for SKSE Plugins**（AE 数据库）。验证点：
   `Data\SKSE\Plugins\` 下出现地址库文件；主文件名自带面向版本（如 `All in One (1.7.104.0) v13`）。
5. **从 `skse64_loader.exe` 启动**，并在 MO2 里把它登记为可执行项（从管理器内启动，
   USVFS 才生效，详见 [Mod Organizer 2 使用](../../mo2-usvfs-kb/05-usage/third-party-executables.md)）。
   验证点：能进主菜单；`Data\SKSE\Plugins\` 可被排错时检查。

### 最小前置链（推荐停在 1.6.1170）

```
SkyrimSE.exe 1.6.1170（Steam AE）
├─ SKSE64 2.2.6 / 2.2.7
├─ Address Library for SKSE Plugins（AE 档）
├─ SkyUI
└─ 之后才是 RaceMenu / 物理 / 分配工具
```

> **为什么推荐 1.6.1170 而不是最新的 1.7.104**：1.7.x 上 SKSE 有 2.3.1、Address Library
> 有 v13，但 **RaceMenu 没有可用版本**——捏脸功能是**直接没有**，不是"降级可用"。
> 而捏脸是整条链的入口。完整决策树见
> [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)。

GOG 用户把前两行换成 **游戏 1.6.1179 + SKSE64 GOG 档 2.2.6**，并用 GOG 专属下载文件；
RaceMenu 的 GOG 文件作者标注 **untested**，遇到异常优先怀疑这条链路。

## 使用与配置

### 怎么确认装好了

| 检查 | 看到什么算对 |
|---|---|
| 目录 | `Data\SKSE\Plugins\` 存在，里面有各插件 DLL 与配置 |
| 控制台 | `getskseversion` 输出版本串（如 AE 2.2.6） |
| 日志 | `Documents\My Games\Skyrim Special Edition\SKSE\` 下有插件日志 |
| 行为 | SkyUI 界面正常（不弹 Error Code 1） |

### 版本自查四项（遇到不确定先做这个）

| 组件 | 最权威的核对位置 | 看什么 |
|---|---|---|
| SKSE64 | `skse.silverlock.org` 首页 + Nexus 页 Changelogs | 首页写"当前各档"；changelog 写某版本对应什么游戏版本 |
| Address Library | Nexus `Files` 页主文件名 | 文件名自带面向版本，如 `All in One (1.7.104.0) v13` |
| RaceMenu | Nexus `Files` 页主文件说明 | 直接写 "REQUIRES SKSE64 … and Game Version …" |
| 其他 DLL 插件 | 各自 `Files` 页历史条目说明 | 作者通常把"最后一个面向 X 的版本"写在文件说明里 |

**实践结论**：看 **Files 页而不是 Posts 页**——作者把版本要求写在文件说明里，
论坛帖混杂二手经验。

## 兼容与冲突

| 关系 | 结论 |
|---|---|
| SKSE 自身 vs Address Library | 官方明示 **SKSE 不使用** Address Library；它是给第三方插件的 |
| SE 数据库 vs AE 数据库 | **两套独立、地址不通用**；装错 = 依赖它的 DLL 插件**全部静默失效** |
| Steam vs GOG | GOG 要 GOG 专属 SKSE 文件；两边版本线不同（1.6.1179 vs 1.6.1170） |
| SE / AE / VR | 三条链的 bin/dll 不交叉；VR 用 SKSEVR 2.0.12（游戏 1.4.15） |
| Epic / MS Store / Game Pass | **明确不支持**，没有workaround |
| 插件版本 vs 游戏版本 | 每个 DLL 插件都按游戏版本编译，**没有通配档**（FOMOD 多选设计正是为此） |

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| SkyUI 弹 "SKSE is not functioning properly" / Error Code 1 | 用游戏启动器启动了，或 SKSE 没装对 | 改从 `skse64_loader.exe` 启动 |
| 游戏能启动，但所有插件功能消失（菜单没有、滑块没有） | SKSE 与游戏版本不匹配，DLL 拒绝加载 | 对照 [`../00-overview/version-matrix.md`](../00-overview/version-matrix.md) 换版本 |
| 依赖 Address Library 的插件全部失效，游戏本身照常 | ADL 装成了 SE 档（给 AE 用）或反之 | 换 AE 数据库（v13 覆盖到 1.7.104.0） |
| 启动即崩 | 某个 DLL 插件的版本档选错；2026-08 起还多一个 overlay nif 坑 | 先清空 `Data\SKSE\Plugins` 再逐个加回，二分出祸首 |
| 进游戏捏脸界面是**原版那个** | RaceMenu dll 没被加载（版本不符的常见无报错表现） | 回到版本表核对；1.7.x 上没有官方 RaceMenu |
| 升级后 Mod 管理器报"插件缺失 / incompatible" | 正常：DLL 按游戏版本编译 | 装回对应版本的 DLL |

## 取舍与建议

- **绝大多数人（依赖捏脸）**：留在 **1.6.1170（Steam）/ 1.6.1179（GOG）**，
  在 Steam 里限制自动更新。代价是新 mod 会逐步只支持 1.7.x。
- **已在 1.7.x 且不想降级**：接受"RaceMenu 全功能消失"，并先清掉旧 overlay nif
  （否则必崩，见 [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)）。
- **不要混用不同游戏版本的 bin/dll**：Steam/GOG、SE/AE/VR 四条链各不相同。
- **不要信二手媒体清单**：以作者的 Files 页 / GitHub / SKSE 官网为准。
- **升级前做两件事**：备份存档与整套 `Data`；把"当前各 DLL 版本 + 游戏版本"记成一个
  文本——它就是你的回滚清单。
- 工具视角的完整说明见
  [SKSE64（工具库）](../../skyrim-tools-kb/01-frameworks/skse64.md) 与
  [Address Library（工具库）](../../skyrim-tools-kb/01-frameworks/address-library.md)；
  插件框架层见本库 [skse-plugin-frameworks.md](skse-plugin-frameworks.md)。

## 来源

- **SKSE64 官方站（一手）**：`https://skse.silverlock.org/`
  （AE **2.3.1 = 1.7.104**、GOG **2.2.6 = 1.6.1179**、SE **2.0.20 = 1.5.97**、VR 2.0.12；
  2026-08-14 更新警告；明示不支持 MS Store / Game Pass 与 Epic 版；明示 SKSE 不使用 Address Library）
- **SKSE64 Nexus 页与 Changelog（一手）**：`https://www.nexusmods.com/skyrimspecialedition/mods/30379`
  （**2.3.0 = 1.7.99**、**2.3.1 = 1.7.104**；2026-08-19/20/27 置顶更新；"更新后崩溃先清空
  `Data/SKSE/Plugins`"）
- **Address Library（一手）**：`https://www.nexusmods.com/skyrimspecialedition/mods/32444`
  （v12 面向 1.7.99.0（2026-08-21）；**v13 "All in One (1.7.104.0)"（2026-08-27）**；
  原始发布 2020-02-07）
- **版本对应与 1.7.x 时间线**：本库 [`../00-overview/version-matrix.md`](../00-overview/version-matrix.md)、
  [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)（均 2026-10-25 核实，
  结论冲突时以它们为准）
- **"99% 安装失败源于文件放错位置"、MO2 内启动才生效**：
  `skyrim-tools-kb/01-frameworks/skse64.md` 整理（引自 SKSE 官方安装说明）—— **一手（转述）**
- **SE/AE 地址库不通用**：Address Library 发布页说明与多个插件 README 一致 —— **一手**
