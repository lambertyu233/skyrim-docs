---
id: skse-plugin-frameworks
title: SKSE 插件框架：PapyrusUtil / JContainers / MCM Helper / po3 Extender
category: 01-prerequisites
kind: reference
version: 2.0.0
updated: 2026-10-25
tags: [前置, 框架, PapyrusUtil, JContainers, MCM Helper, po3]
aliases: [papyrus extender, 前置框架, skyui, papyrusutil 是什么, jcontainers 是什么, mcm helper 是什么, 依赖库, StorageUtil, JsonUtil, racemenu 不依赖 papyrusutil, 怎么查前置, 生态黏合剂, UIExtensions, 13048, 53000, po3 extender]
source: https://www.nexusmods.com/skyrimspecialedition/mods/13048
summary: 捏脸与身形类 mod 常引用的通用框架库各自做什么、作者与版本状态、安装注意，写透"PapyrusUtil 不是 RaceMenu 前置"这条被广泛误传的关系，并给出一套查清"一个 mod 到底要什么"的实用判断法。
---

# SKSE 插件框架

这些**不是身形 mod**，而是被身形/捏脸 mod **当作前置引用**的通用库。它们自身不产生
任何外观变化，但缺了会让宿主 mod **静默失效**——所以本库把它们归在"前置"层。

> **一句话**：这一层是 modlist 的"生态黏合剂"：** PapyrusUtil 补数据存储、JContainers 补嵌套结构、
> MCM Helper 补配置菜单、po3 Extender 补脚本函数、SkyUI 承载 MCM、UIExtensions 补自定义菜单。**
> 管理它们只有一个办法：**看每个 mod 页面的 Requirements 段**，不凭"我已经装了类似的"省略。

## 速览

| 项 | 内容 |
|---|---|
| 定位 | 被宿主 mod 引用的通用 SKSE 插件/脚本库，自身不产生游戏内容 |
| 共同前置 | **SKSE64**（版本匹配）+ **Address Library**（多数成员 4.1+ 起需要） |
| 界面载体 | **SkyUI**（MCM 的承载者，事实必装） |
| 影响范围 | 缺一个 → 依赖它的那批 mod 集体静默失效；症状高度同质 |
| 关键纪律 | 版本按**游戏版本**分档；框架之间**多数可共存**，不是二选一 |

要点：

- **框架类问题的症状高度同质**：菜单不出现、设置不保存、脚本静默不执行。
  排查顺序永远是"**版本与前置**"，而不是"冲突"。
- **一条被广泛误传的关系**：**PapyrusUtil 不是 RaceMenu 的前置**（RaceMenu 只列 SKSE64）。
  详见下文专节。
- **两条易混的"同名不同物"**：MCM Helper ≠ SkyUI 自带功能；po3 Papyrus Extender ≠
  powerofthree's Tweaks（后者是引擎修复，见
  [po3 Tweaks（工具库）](../../skyrim-tools-kb/09-diagnostics/po3-tweaks.md)）。
- **JContainers 与 PapyrusUtil 不是二选一**：数据模型不同，经常被不同 mod 同时依赖。
- 各成员的 Nexus 编号：PapyrusUtil **13048** · JContainers **16495** · MCM Helper **53000** ·
  po3 Extender **22854** · SkyUI **12604** · UIExtensions **17561**。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 时代 | **PapyrusUtil** 由 **meh321** 制作（原始版） | Papyrus 第一次有了可靠的持久化容器 |
| 2014 前后 | LE 的 **JContainers**（作者 **silvericed**，MIT）出现 | 把 JSON 结构（嵌套数组/字典）带进 Papyrus |
| 2018-04-14 | **JContainers SE** 首发（Nexus 16495，移植上传者 **ryobg**） | SE 生态的 JSON 容器方案定型 |
| 2020-02-07 | **Address Library** 发布 | 框架层与插件层一起进入"按游戏版本分档"时代 |
| 2021-08-01 | **MCM Helper** 首发（**Parapets**，Nexus 53000，MIT） | "写 Papyrus 菜单"变成"写一个 JSON" |
| 2021 起 | **powerofthree's Papyrus Extender** 持续更新（Nexus 22854） | 现代脚本 mod 的常用函数库 |
| 2026 年 | JContainers 4.3.x 提供面向 **SKSE 2.3.1 / 游戏 1.7.104** 与 GOG 1.6.1179 的构建（2026-09） | 框架层对 1.7.x 的跟进比内容插件快 |

### 它从哪来

Papyrus 的先天不足催生了整层框架：**没有可靠的持久化容器**（跨存档记不住状态）、
**没有嵌套数据结构**（数组不能套数组）、**没有配置菜单框架**（作者要手写大量 UI 脚本）、
**函数集太小**（很多检测与操作做不到）。上面每个成员各补一块。

### 中间经历了什么

- **SE 移植潮**：LE 时代的库由社区移植到 SE（JContainers 由 ryobg 移植，PapyrusUtil SE
  由 **exiledviper** 接手维护）。
- **Address Library 化**：4.1+ 之后的 PapyrusUtil、MCM Helper 等纷纷改为依赖 Address Library，
  从此这些框架自身也**按游戏版本分档**发布。
- **1.7.x 分裂**：2026-08 游戏进 1.7.x 后，框架层跟进最快（JContainers 2026-09 即有
  1.7.104 构建），但内容插件（RaceMenu 等）没跟上——见
  [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)。

### 现状

全部成员仍在维护；共同特征是**分游戏版本的下载文件**（含 GOG、VR 变体），
装错档的表现通常是"行为诡异"而不是干脆报错。

## 它解决什么问题

| 原生 Papyrus 的边界 | 谁来补 |
|---|---|
| 没有可靠的持久化容器（变量随存档丢失） | **PapyrusUtil** 的 `StorageUtil` |
| 想把配置写到外部文件、可手改 | **PapyrusUtil** 的 `JsonUtil` |
| 需要嵌套数组 / 字典 / JSON 语义 | **JContainers** |
| 写配置菜单要手写大量 Papyrus UI 代码 | **MCM Helper**（JSON 定义菜单） |
| 想要的原生函数不存在（更细检测、对象操作） | **po3 Papyrus Extender** |
| MCM 菜单往哪显示 | **SkyUI** |
| 需要列表/轮盘/选择等自定义菜单 | **UIExtensions** |

## 成员档案

### PapyrusUtil SE（Nexus 13048）

- **作者**：LE 原始 **meh321**；SE 维护 **exiledviper**。
- **提供**：`StorageUtil`（把数据以 form + 变量名为键挂在任意 form 或全局）、
  `JsonUtil`（同模型但写外部 `.json`）、`MiscUtil`、`ActorUtil`。
- **版本注意**：**4.1+ 需要 Address Library**；4.6 起支持 1.6.1170。
  社区排错文档给出的版本映射（**社区文档，按游戏版本选用**）：
  1.5.97 → 3.9 · 1.6.353 → 4.3 · 1.6.640 → 4.4 · GOG 用 GOG 专用文件。
- **日志**：`Documents\My Games\Skyrim Special Edition\SKSE\PapyrusUtilDev.log`。
- **坑**：它是**被覆盖大户**——Campfire 等 mod 会打包旧版 PapyrusUtil，
  后装会把它覆盖回旧版，症状是依赖它的 mod 报"函数不存在"或行为诡异（社区经验）。

### JContainers SE（Nexus 16495）

- **作者**：LE 原始 **silvericed**（MIT）；SE 移植上传者 **ryobg**，2018-04-14 首发。
- **提供**：嵌套数组、字典（associative containers）、JSON 文件读写、内嵌 Lua 脚本、
  C++ 接口。典型用途：复杂配置持久化、mod 间文件交换结构化数据。
- **版本状态**：当前 4.3.x；2026-09 起提供面向 **SKSE 2.3.1 / 游戏 1.7.104**、
  GOG 1.6.1179（SKSE GOG 2.2.6）、VR（1.4.15 / SKSE 2.0.12）的构建。
- **与 PapyrusUtil 的关系**（最常被问）：

| | PapyrusUtil | JContainers |
|---|---|---|
| 数据模型 | 平铺键值 + 一维列表 | 任意嵌套（JSON） |
| 存储位置 | form 挂载 / 外部 `.json` | 外部文件 |
| 依赖它的 mod | 极多 | 较多 |

两者**不冲突、可共存**，而且经常同时出现——因为不同 mod 选了不同方案。
"装了 PapyrusUtil 还要不要 JContainers"的答案：**看宿主 mod 的 Requirements**。

### MCM Helper（Nexus 53000）

- **作者**：**Parapets**；2021-08-01 首发，MIT 许可证，源码在 GitHub。
- **提供**：用 `config.json` 描述菜单结构（页/分组/控件/默认值），
  用户取值存 `settings.ini`（位于 `Data\MCM\Settings\`，可手工编辑、可预置推荐值）。
- **依赖**：SKSE64 + Address Library + SkyUI。
- **版本状态**：当前 1.6.2（2026-04-26）；1.5.0 起跟进 1.6.1130 并改 FOMOD 安装器。
- **坑**：**SkyUI 的 `.bsa` 被解包**会导致 MCM 加载异常（要么别解包，要么连 MCM Helper 一起解包）。

### powerofthree's Papyrus Extender（Nexus 22854）

- **作者**：**powerofthree (po3)**。
- **提供**：给 Papyrus 追加数百个原生函数与若干事件（发布页口径 **374+ 新函数、37 事件**，
  数字随版本增长，以发布页为准）。
- **依赖链是三层**：**SKSE64 + Address Library + powerofthree's Tweaks**——
  少一层都不行，这也是它最常被装漏的原因。
- **注意区分**：**powerofthree's Tweaks** 是引擎修复类 mod，与本文不是同一个东西，
  两者名字相似、用途不同、且常被同时安装（见
  [po3 Tweaks（工具库）](../../skyrim-tools-kb/09-diagnostics/po3-tweaks.md)）。

### SkyUI（Nexus 12604）

- **作者**：SkyUI Team。
- **两层价值**：① PC 友好的界面重做；② **MCM 框架**——任何在游戏内出现设置菜单的 mod
  都要靠它，这是它出现在大量 Requirements 里的真实原因。
- **坑**：用普通启动器进游戏 → **Error Code 1**（根因是启动方式，见
  [skse64.md](skse64.md)）；打开游戏内置的模组菜单会**关闭 SkyUI**，
  官方建议改用 MO2 / Vortex。
- 社区长期主流为 5.2 SE；**当前最新版本号本库未逐版核实，以 Nexus Files 页为准**。

### UIExtensions（Nexus 17561）

- **作者**：**expired6978**（与 RaceMenu 同一作者），credits 另署 Expired / snakster / Mardoxx；
  需 SKSE64 2.0.7+。
- **提供**：List / Wheel / Selection / Text Entry 等自定义菜单，供 mod 作者调用；
  [OBody NG](../05-distribution/obody-ng.md) 的预设列表热键菜单正是用它。
- **坑**：装完别忘了在 mod 管理器里**启用 `UIExtensions.esp`**——MO2/Vortex 有时不会自动启用，
  这是"OBody NG 按 O 没反应"的第一大原因。

## 安装

### 通用步骤

1. **先核游戏版本**（`getskseversion` / exe 属性）——每个框架都按游戏版本分档，
   AE/SE/GOG/VR 文件不通用（见 [`../00-overview/version-matrix.md`](../00-overview/version-matrix.md)）。
2. **装 SKSE64 + Address Library**（4.1+ 之后多数框架的前置）。
   验证点：`Data\SKSE\Plugins\` 有地址库文件。
3. **按宿主 mod 的 Requirements 装对应框架**，用 mod 管理器正常安装即可；
   升级时**直接覆盖**。
4. **启用该启用的 `.esp`**（UIExtensions 尤其容易忘）。
   验证点：插件列表里 `UIExtensions.esp` 等已勾选。

### 各框架安装注意

| 框架 | 安装形态 | 特别注意 |
|---|---|---|
| PapyrusUtil | DLL + `Data\Scripts\*.pex` | 版本必须匹配游戏；**防覆盖**（Campfire 等会打包旧版） |
| JContainers | DLL + `.pex` | 升级直接覆盖；VR 有专用档 |
| MCM Helper | FOMOD（1.5.0 起） | 需 SkyUI；**别解包 SkyUI 的 `.bsa`**（或连 Helper 一起解包） |
| po3 Extender | DLL（AE 专用文件按版本选） | 依赖链三层：SKSE + ADL + po3 Tweaks |
| SkyUI | 常规 mod | 必须从 `skse64_loader.exe` 启动 |
| UIExtensions | DLL + `.esp` | **装完记得启用 `UIExtensions.esp`** |

## 使用与配置

这一层的共同特征是**"装了没变化才对"**——它们没有自己的内容界面。
你能摸到的是它们的**配置落点**：

| 框架 | 配置/可见形态 |
|---|---|
| PapyrusUtil | 无用户配置；排错看 `SKSE\PapyrusUtilDev.log` |
| JContainers | 外部 JSON 文件（由使用它的 mod 决定路径）；**不在存档里**，卸载不自动清 |
| MCM Helper | `config.json`（菜单结构，mod 作者提供）+ `settings.ini`（用户取值，`Data\MCM\Settings\`） |
| po3 Extender | 无 UI、无配置——装了没感觉是正常的 |
| SkyUI | MCM 菜单本体（Esc → Mod 配置） |
| UIExtensions | 菜单由宿主 mod 调出（如 OBody NG 的 O 键列表） |

> 排错时的一个便利：MCM Helper 的设置落在 `settings.ini` 里，
> **直接看 ini 比进游戏翻菜单快**；整合包的“推荐设置”也常用预置 ini 发布。

## ⚠️ 一条被广泛误传的前置关系

> **PapyrusUtil 不是 RaceMenu 的前置。**

写透这件事，因为它直接决定排错方向：

1. **RaceMenu 的 Nexus 发布页只列 SKSE64**。它的主体是 C++ 插件 `skee64.dll`，
   自带 **NiOverride** 与 **CharGen** 两套实现（2.7 起 CharGen Extension 已完全并入本体，
   若你曾单独装过，作者明确要求**卸载它**）。
2. **PapyrusUtil 会出现在各种"依赖清单"里，是因为别的 mod 需要它**——部分身形、
   高跟、动画类 mod，以及 OBody NG 的 Papyrus 脚本层。把它记在 RaceMenu 名下，
   排错时会去找错方向。
3. **连带的一条**：RaceMenu 自带的这些 `.pex` 若在别处残留旧版本，会引发版本冲突提示，
   应删除：`CharGen.pex` / `NiOverride.pex` / `RaceMenu.pex` / `RaceMenuBase.pex` /
   `RaceMenuLoad.pex` / `RaceMenuPlugin.pex`。

同类误传还有两条，一并记下：

- **"MCM Helper 是 SkyUI 自带的功能"**——不是。SkyUI 提供 MCM 框架本身，
  MCM Helper 是第三方框架（让作者用 JSON 定义菜单）。两者常同装，但不是同一个东西。
- **"po3 Papyrus Extender 就是 powerofthree's Tweaks"**——不是，同作者的不同 mod
  （Tweaks 管引擎修复与调整）。

## 一个实用的判断法：怎么查一个 mod 到底要什么

看到一个 mod 报"缺前置"，别急着找同名 mod 装上。按这条链往上追：

```
宿主 mod → 需要哪个框架 → 那个框架又需要什么 → 有没有 Address Library
```

落地成五步：

1. **看 Nexus 页的 Requirements 段**（不是 Posts/评论）——作者把官方前置写在那里。
2. **看它自带哪些文件**：`Data\Scripts\` 下的 `.pex` 指向哪个框架；
   `Data\SKSE\Plugins\` 下的 DLL 基本意味着需要 Address Library。
3. **进日志**：`PapyrusUtilDev.log`、MCM 是否注册、Crash Logger 的堆栈，
   比猜快得多。
4. **症状同质化归类**：菜单不出现 / 设置不保存 / 脚本静默 → 先查**版本与前置**，
   再查冲突。
5. **查版本映射**：游戏版本 → SKSE → 各框架的对应文件档（见
   [`../00-overview/version-matrix.md`](../00-overview/version-matrix.md)）。

> **MCM 注册慢是常态**：MCM 类菜单要在不暂停的游戏里跑几分钟才出现，
> 别据此判断"没装上"（社区经验，OBody NG 排错文档同样强调这一点）。

## 兼容与冲突

| 关系 | 结论 |
|---|---|
| PapyrusUtil vs JContainers | **共存**，数据模型不同，看宿主 Requirements |
| MCM Helper vs SkyUI | **互补**：SkyUI 是框架，MCM Helper 是简化层；别解包 SkyUI 的 bsa |
| po3 Extender vs po3 Tweaks | **不同 mod**，常同装；Extender 的依赖链含 Tweaks |
| UIExtensions vs RaceMenu | 同作者；UIExtensions 的 Cosmetic/Dye 菜单还需 RaceMenu |
| 框架 vs 游戏版本 | 每个框架都按游戏版本分档（含 GOG/VR），**装错档 = 行为诡异** |
| 框架 vs 覆盖关系 | PapyrusUtil 是被覆盖大户；后装 mod 可能把它压回旧版 |

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 某 mod 报找不到函数 / 静默失效 | PapyrusUtil 或 po3 Extender 未装 / 版本过老 | 按游戏版本装对应档 |
| SkyUI 里出现"奇怪的行为" | MCM Helper 版本与游戏不匹配 | 换对应版本文件 |
| MCM 菜单根本不出现 | MCM Helper 没装或版本错；或 SkyUI bsa 被解包 | 装对版本；别解包 SkyUI bsa（或连 Helper 一起解包） |
| OBody NG 按 O 无反应 / 游戏卡住 | UIExtensions 没装或 `.esp` 未启用；或 PapyrusUtil 版本错、被覆盖 | 装 UIExtensions 并启用 esp；核对 PapyrusUtil 版本与覆盖关系 |
| JContainers 报"容器不存在" | `JContainers.dll` 被后装版本覆盖 | 查覆盖关系，让正确版本胜出 |
| 设置改了不保存 / 新开档恢复默认 | MCM Helper 的 `settings.ini` 落在 MO2 Overwrite 没归位 | 处理 Overwrite（见 [MO2 覆盖规则](../../mo2-usvfs-kb/05-usage/overwrite-dir.md)） |
| 装了框架"没变化" | **正常**：框架无 UI、无内容，装了没感觉才对 | 不用管 |

## 取舍与建议

- **原则只有一条**：**看 Requirements，不凭印象省略**。这一层没有"装了 A 就不用装 B"的
  通用规律，除非发布页明说。
- **版本映射比"最新版"重要**：框架全部按游戏版本分档；追最新版追错档比用旧档更糟。
- **RaceMenu 的前置只有 SKSE64**：别再往它头上堆 PapyrusUtil（误传，见上文）。
- **1.7.x 用户**：框架层反而是跟进最快的一层（JContainers 2026-09 即有 1.7.104 构建），
  但内容插件没跟上——版本立场见
  [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)。
- 工具视角的逐条档案见 `skyrim-tools-kb`：
  [papyrusutil](../../skyrim-tools-kb/01-frameworks/papyrusutil.md) ·
  [jcontainers](../../skyrim-tools-kb/01-frameworks/jcontainers.md) ·
  [mcm-helper](../../skyrim-tools-kb/01-frameworks/mcm-helper.md) ·
  [po3-papyrus-extender](../../skyrim-tools-kb/01-frameworks/po3-papyrus-extender.md) ·
  [skyui](../../skyrim-tools-kb/01-frameworks/skyui.md)。

## 来源

**一手**

- PapyrusUtil SE（作者/维护者、脚本清单、4.1+ 需 Address Library、4.6 支持 1.6.1170）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/13048`
- JContainers SE（silvericed 原始 / ryobg 移植、2018-04-14 首发、版本分档表、MIT 端口依据）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/16495`；GitHub `ryobg/JContainers`
- MCM Helper（Parapets、2021-08-01 首发、1.6.2 / 2026-04-26、MIT、依赖 Address Library + SkyUI、
  FOMOD 与 changelog 节点）：`https://www.nexusmods.com/skyrimspecialedition/mods/53000`
- po3 Papyrus Extender（作者、374+ 函数/37 事件口径、三层依赖链）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/22854`
- SkyUI（MCM 框架定位、Error Code 1、内置 mod 菜单会关闭 SkyUI）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/12604`
- UIExtensions（expired6978、菜单清单、SKSE64 2.0.7+）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/17561`
- RaceMenu 发布页（**前置只列 SKSE64**、CharGen Extension 2.7 起并入应卸载、应删除的 6 个 `.pex`）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/19080`

**社区经验 / 社区文档**

- PapyrusUtil 的"游戏版本 → 框架版本"映射（3.9/4.3/4.4/GOG）、UIExtensions 未启用导致
  OBody NG 热键失效、MCM 需数分钟注册：OBody NG 排错指南（第三方整理）—— **社区文档**
- PapyrusUtil 被 Campfire 等 mod 覆盖：Nexus 论坛与 LoversLab 多帖一致 —— **社区经验**
- `Data\MCM\Settings\` 为用户设置落点：OBody NG Settings Loader 页（"MCM/Settings/OBody NG.ini"）
  与 MCM Helper 文档一致 —— **一手（相邻证据）**

**未确认**

- SkyUI 当前最新版本号（社区长期主流为 5.2 SE，本库未逐版核实）
- po3 Papyrus Extender 函数/事件数的当前精确值（以发布页为准）
