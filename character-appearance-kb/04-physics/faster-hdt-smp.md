---
id: faster-hdt-smp
title: Faster HDT-SMP（FSMP）
category: 04-physics
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [物理, FSMP, HDT-SMP, 多线程, 性能]
aliases: [faster hdt smp, hdt smp 加速, 物理性能, daymareon, 57339, fsmp 是什么, fsmp 安装, smp 命令, smp detail, smp dumptree, avx2, fsmp 版本, 怎么装 fsmp, fsmp 已知问题]
source: https://www.nexusmods.com/skyrimspecialedition/mods/57339
summary: FSMP 百科全书：HydrogensaysHDT → aers → Karonar1 → DaymareOn 的 fork 链、相对原版的改动（多线程、ImGui 菜单、JSON 全局配置）、FOMOD 游戏版本档位与 AVX2 选项、smp 控制台命令（dumptree/detail/list/report/reset）、与 XPMSE 的耦合、Performance.xml 预设，以及维护者自述的已知问题。
---

# Faster HDT-SMP（FSMP）

> **一句话**：FSMP 是 HDT-SMP 的现代维护版——同一套 XML 配置生态，换掉引擎实现
> （多线程 Bullet）与配置层（ImGui 菜单 + JSON），官方口径是
> **"massively improves performance…replaces it totally. Do not install [原版]"**。

- Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/57339`
- GitHub：`https://github.com/DaymareOn/hdtSMP64`
- 上传者 **DaydreamingDay**，代码维护 **DaymareOn**
- **现代用户应该装的 SMP。**

## 速览

| 项 | 内容 |
|---|---|
| Nexus / 仓库 | **57339** / `github.com/DaymareOn/hdtSMP64` |
| fork 链 | HydrogensaysHDT（原创）→ aers（修复与改进）→ Karonar1（bug 修复）→ DaymareOn（构建维护） |
| 当前版本 | **4.1.1**（2026-08-27） |
| 构建档位 | `vs2022-windows-{nocuda,cuda}-{avx,avx2,avx512}`（另有 `usernameak/hdtSMP64` 的 CUDA 分支） |
| 依赖 | CommonLibSSE-NG + Address Library for SKSE Plugins |
| 前置 | SKSE64 + XPMSE；内置菜单用 SKSE Menu Framework（随包 vendor） |
| 维护状态 | 活跃维护（2026 年仍有提交与文档更新） |

要点：

- **它只是引擎**：官方 wiki 原话——"It doesn't provide any xml physics configuration
  file. It doesn't know the difference between a cape and a breast."
  物理配置永远来自各个衣物/发型 mod 的 XML。
- **多线程 Bullet** 是性能提升的核心；对 CPU 指令集有 **AVX2 档位**可选（默认不带）。
- 全局配置从 XML 迁到 **JSON**（`configs.json` / `userConfigs.json`）；
  逐物品 XML 仍在 `hdtSkinnedMeshConfigs`，格式未变。
- 配置菜单从 SkyUI MCM 换成 **DLL 内置的 ImGui 菜单**；4.x 不再强制
  SkyUI / JContainers / PapyrusUtil / ConsoleUtil。
- 装/卸任意时刻都可以，**不动存档与加载顺序**（官方 wiki 承诺；唯一例外是
  永远不要装 1.37 版，会毁档）。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 2018-2019 | hydrogensaysHDT 淡出，MIT 释出 [HDT-SMP](hdt-smp.md) 源码 | fork 链的起点 |
| 2019-2020 | **aers** 接手修复与改进（AE 版本管理、CUDA 合并试水、`smp list` 命令诞生） | 修复积累期 |
| 2019-12 → 2021 | **Karonar1** 系统修 bug：项目与 dll 改名 `hdtSMP64`、NPC 距离/角度剔除、护甲处理重构、facegen 头部件物理 | 稳定性与 NPC 性能的代际修复 |
| 2021-10-21 起 | **DaymareOn / DaydreamingDay** 的 FSMP 上传 Nexus 57339 并维护至今 | 现代主线；wiki 称自该日起累计独立下载已过 200 万 |
| 2023-2024 | 4.x：ImGui 配置菜单 + JSON 全局配置落地（`configs.json` / `userConfigs.json`） | 配置层现代化，摆脱 SkyUI 依赖 |
| 2026-08-27 | **4.1.1** | 当前版本 |

### 它从哪来

FSMP 不是新引擎，而是**同一条 SMP 血脉的维护线**。aers 与 Karonar1 解决了原版
遗留的大量稳定性问题（护甲系统重构、NPC 距离剔除、facegen 支持），
DaymareOn 在其上做构建分发与功能演进。Nexus 57339 是它的发布阵地。

### 中间经历了什么

两个关键改动定义了 4.x：**多线程 Bullet**（性能）与**内置 ImGui 配置菜单**
（易用性 + 去 SkyUI 化）。全局配置从 `configs.xml` 迁到 `configs.json`，
用户 tweak 存 `userConfigs.json`，升级不丢设置。

### 现状

活跃维护，文档体系（wiki + SMP Modder Guide + DynamicHDT Papyrus API）是各物理
方案里最全的。**它与原版 HDT-SMP 是替代关系，不是共存关系。**

## 相对原版的改动

| 项 | 改动 |
|---|---|
| **性能** | 官方描述：*"massively improves performance over the original HDT-SMP, and replaces it totally. Do not install [原版]"* |
| **并行** | 基于 Bullet 的**多线程**实现 |
| **配置界面** | **SKSE Menu Framework（Dear ImGui）** 内置菜单取代旧 MCM（旧 MCM 依赖 SkyUI / JContainers / PapyrusUtil / ConsoleUtil，现已移除） |
| **全局配置** | 从 XML 迁到 **JSON**：`configs.json`（出厂默认）之上叠 `userConfigs.json`（用户设置），首次运行应用 Default 预设 |
| **诊断工具** | `smp report` 校验整个 load order；ImGui 菜单内置 Validation 页面与 Measures 性能页 |
| **卸载安全性** | 官方 wiki：随时装/卸/重装，不威胁存档与加载顺序 |

> ⚠️ 4.x **本身不再强制** SkyUI / JContainers / PapyrusUtil / ConsoleUtil，
> 但**你装的其他 mod 可能仍需要它们**——别因为这条就把它们全删了。

## 安装

### FOMOD 游戏版本档位

| 游戏版本 | 对应 SKSE64 |
|---|---|
| **1.6.1170.0** | 2.2.6 |
| 1.6.659（GOG） | 2.2.2 |
| 1.6.640 | 2.2.2 |
| 1.6.353 | 2.1.5 |
| 1.6.1170 以下各版 | 以 FOMOD 列表为准 |
| 1.5.97（SE） | 2.0.20 |
| VR | 2.0.12 |

**安装时必须在 FOMOD 里选对游戏版本档**——选错的典型表现是物理不生效或开局崩溃。

### 步骤与验证点

1. **前置**：SKSE64（与游戏版本匹配）、**Address Library**、**XPMSE**。
   - 验证点：`Data\SKSE\Plugins\Address Library for SKSE Plugins` 已装；
     XPMSE FOMOD 选了 Physics Extensions。
2. **装 FSMP 主文件**，FOMOD 选游戏版本档；**CPU 支持 AVX2 时勾选 AVX2 档**
   （默认不带，社区建议支持就开）。
   - 验证点：`Data\SKSE\Plugins\hdtSMP64.dll` 存在；未同时装原版 SMP。
3. **装带物理的衣物/发型**（各自携带 `hdtSkinnedMeshConfigs` XML）。
   - 验证点：该目录下出现对应 XML。
4. **进游戏**：默认热键打开内置配置菜单（SKSE Menu Framework 框架缺失时
   **菜单不显示，但物理照常工作**）。
   - 验证点：披风/头发摆动；不抖跑 `smp report`（见下）。

## 使用与配置

### `smp` 控制台命令（排查第一手工具）

```
smp detail      全部被追踪 actor 的详细信息（含生效/失效的护甲与 head part）
smp dumptree    导出当前目标 NPC 的整棵节点树到日志
smp list        精简列表：哪些 NPC 被追踪、按激活状态排序
smp report [gear] [warnings]   校验整个 load order 的物理 XML 与 .nif（默认只报错误）
smp reset       重置/重载物理系统（改完配置后用）
```

> **出物理问题先跑 `smp report warnings`**——它会直接告诉你哪个 mod 的 XML 有警告，
> 比逐个 mod 试高效得多。`smp detail` / `smp dumptree` 用于确认某个 NPC 的节点与
> 护甲到底有没有被引擎追踪。

### 构建档位与 CUDA 分支

发布页提供的构建矩阵：`vs2022-windows-{nocuda,cuda}-{avx,avx2,avx512}`。
普通用户用 FOMOD 即可，无需自己编译；需要 CUDA 加速的，社区还有
`usernameak/hdtSMP64` 的 CUDA 分支（编译要求：Visual Studio 2022 + Detours +
Bullet，详见上游 README）。⚠️ CUDA 支持 historically 默认关闭且"不检查显卡能力，
显卡太旧可能崩"——没有需求就留在 CPU 档。

### 与游戏大版本的关系

FOMOD 档位目前覆盖到 **1.6.1170.0**（配 SKSE 2.2.6）。**1.7.x 的支持状态未确认**，
升级游戏版本前先查 Nexus Files 页与仓库 changelog，不要假定"最新版一定支持"。

### 配置菜单与预设

- 内置 ImGui 菜单分页：Home / **Presets** / **Simplification** / **Performance** /
  Wind / Commands / Measures / Logs / Validation；
- **MCM 里的 `Performance.xml` 预设**：随包提供的性能档位预设，卡顿时先换它；
- 手改全局配置：编辑 `configs.json`（出厂默认）或让游戏写 `userConfigs.json`，
  官方说明用户层覆盖在升级后仍然保留。

### 与 XPMSE 的耦合

FSMP 继承原版设计：**只把网格附加到 XPMSE 的 human skeleton**，
所以 XPMSE 是硬前置；非人骨架不被模拟（这一设计顺带修掉了 Lurker 骨骼被破坏的
老问题）。详见 [xpmse-skeleton.md](xpmse-skeleton.md) 与
[physics-overview.md](physics-overview.md)。

## 维护者自述的已知问题

以下来自官方仓库 README 的 "Known issues"（"This list only contains issues I have
personally observed"）：

| 问题 | 说明 |
|---|---|
| 部分选项看不出效果 | 骨骼上的 shape / collision 定义等选项存在，但似乎不起作用 |
| sphere-triangle 碰撞检测 | 未定义穿透（penetration）时的检测结果"明显是错的"，修检测本身无改善，待深入调查 |
| `smp reset` 不重载部分物品的网格 | 典型例子 **Artesian Cloaks**；疑似原始三角形网格引用被提前释放 |
| facegen NPC 的约束问题 | `smp reset` 会破坏部分带 facegen 数据 NPC 的约束；facegen 数据里未被任何网格显式引用的骨不能作约束运动骨 |
| 非假发形态的 NPC 头发 | 大多数 HDT 头发不改约束就不能作为 non-wig 头发在 NPC 上工作 |
| 物理发色偶尔错误 | 附近两个 NPC 用同一发型模型时可能出现 |
| 动态时间步 | 新机制牺牲一点物理稳定性，换取避免"一帧卡顿→掉帧连锁" |

> 遇到"改了配置没反应 / 某件斗篷 reset 后不恢复"，先对照本表——很可能不是你的操作问题。

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 物理完全不生效 / 开局崩 | FOMOD 版本档选错；SKSE 与游戏不匹配 | 重装选对档位；核对 SKSE 版本（[skse64.md](../01-prerequisites/skse64.md)） |
| 配置菜单不显示 | 缺 SKSE Menu Framework | 补框架；不影响物理本身 |
| CPU 占用高 | 默认档位未优化 / 未开 AVX2 | FOMOD 改 AVX2；菜单里换 `Performance.xml` 预设 |
| 某斗篷 `smp reset` 后不恢复 | 已知问题（Artesian Cloaks 类物品） | 重载存档规避；等上游修复 |
| NPC 头发不动/方向错 | facegen 约束限制 / non-wig 头发限制 | 换假发形态，或按 Karonar1 README 改约束（社区技术文档） |
| 改完全局配置无效 | 改错了文件（应改 `userConfigs.json` 层或跑 `smp reset`） | 用菜单改并让游戏写盘；或改完执行 `smp reset` |
| 毁档级事故 | 装了 1.37 版 | 官方明令永不安装该版本 |

## 取舍与建议

- **要 SMP 就装 FSMP，不装原版**——这是官方口径，也是社区一致实践；
- **CPU 支持 AVX2 就开**：默认档位偏保守，性能档位是免费收益；
- **先 `Performance.xml` 再手调**：菜单里的预设覆盖大部分场景，手改 JSON 是最后手段；
- **诊断依赖 `smp report`**：把它当作"物理版的 LOOT"，出问题第一动作；
- **深挖机制**：`github.com/DaymareOn/hdtSMP64`（wiki 有安装/配置/命令/changelog，
  Modder Guide 有 XML 编写规范与 XSD/Schematron schema）。

## 来源

- **fork 链（HydrogensaysHDT → aers → Karonar1 → DaymareOn）、"massively improves
  performance…replaces it totally. Do not install [原版]"、多线程、ImGui 菜单替代
  MCM、XML→JSON 全局配置（`configs.json`/`userConfigs.json`）、`smp report`、
  wiki 的"它不提供任何 XML 配置 / 分不清斗篷和胸"、卸载安全性与 1.37 警告、
  下载量统计口径（2021-10-21 起）**：FSMP 官方仓库 README / wiki 与 Nexus 57339
  描述 —— **一手**
  `https://github.com/DaymareOn/hdtSMP64`
  `https://www.nexusmods.com/skyrimspecialedition/mods/57339`
- **`smp list` 命令的诞生与含义（列出被追踪 NPC、按激活状态排序）**：aers /
  Karonar1 的 hdtSMP64 README changelog —— **一手（上游仓库）**
- **`smp detail` / `smp dumptree` 命令存在**：DaymareOn/FSMP-MCM 仓库 README
  （"trigger debug console commands like smp list, smp detail, and smp dumptree"）
  —— **一手（配套项目）**
- **FOMOD 游戏版本档位与 SKSE 对应表、版本 4.1.1（2026-08-27）**：Nexus 文件页
  （经本库既有收录转述）—— **一手（经转述）**
- **已知问题清单（部分选项无效 / sphere-triangle 检测 / `smp reset` 不重载
  Artesian Cloaks / facegen 约束 / non-wig 头发 / 发色 / 动态时间步）**：
  Karonar1 与 aers 的 hdtSMP64 README "Known issues" —— **一手（上游仓库，
  维护者自述）**
- **构建档位 `vs2022-windows-{nocuda,cuda}-{avx,avx2,avx512}`、CommonLibSSE-NG +
  Address Library 依赖、`usernameak/hdtSMP64` CUDA 分支**：官方仓库构建说明与
  Nexus 描述 —— **一手**
- **"4.x 不再强制 SkyUI/JContainers/PapyrusUtil/ConsoleUtil，但其他 mod 可能仍要"**：
  **社区经验（与官方改动一致）**
- **MCM `Performance.xml` 预设、AVX2 默认关闭建议开启**：Nexus 描述与社区指南 ——
  **一手 + 社区经验**
