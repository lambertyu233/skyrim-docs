---
id: bodyslide-outfit-studio
title: BodySlide and Outfit Studio——身形生态的构建工具
category: 03-body
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [身形, BodySlide, Outfit Studio, 构建, 滑块, 命令行]
aliases: [bs, os, 构建身形, 批量构建, batch build, 命令行参数, bodyslide 是什么, bodyslide 怎么用, build morphs, bodyslide 安装, outfit studio 是什么, bodyslide 历史, caliente, ousnius, 滑块构建, bodyslide 教程]
source: https://github.com/ousnius/BodySlide-and-Outfit-Studio
summary: BodySlide 与 Outfit Studio 完整百科：Caliente"想做衣服却先做出身体、又嫌手搓形状不可持续"而写出工具的前世今生，两者分工、文件格式（.osp/.osd/.nif/.tri）、滑块含义、Batch Build、最重要的 Build Morphs 复选框、与 RaceMenu 的 BODYTRI 联动、官方命令行参数、依赖库与排错。
---

# BodySlide and Outfit Studio

> **一句话**：这是身形生态的"构建工具"——**不跑它，身形 mod 就只是素材**。
> CBBE / 3BA / BHUNP / HIMBO / UBE 全都靠它把滑块数值烘焙进网格；
> 工具本身跨 Skyrim LE/SE 与 Fallout 共用一套代码，GPLv3+，至今仍在高频开发。

作者 **Ousnius 与 Caliente**，致谢 **jonwd7**（NIF 与总体帮助）、
**degenerated1123**（shader 帮助）与 **NifTools 团队**。
**官方仓库**：`https://github.com/ousnius/BodySlide-and-Outfit-Studio`（GPLv3+）。

## 速览

| 项 | 内容 |
|---|---|
| 作者 | **Caliente、ousnius**（Nexus 页署名 "Created by Ousnius and Caliente"） |
| 首发 | LE 时代（具体日期**未确认**；FO4 Nexus 页 original upload 2015-12-24） |
| 当前版本 | FO4 母页 **5.8.2**（2026-06-25）；GitHub 仓库 2026-10 仍有版本与代码提交 |
| 许可证 | **GPL-3.0**（仓库 LICENSE 文件，GPLv3+） |
| 跨游戏 | Skyrim LE/SE、Fallout 4、Fallout 76 共用代码库；2026 年起加入 Starfield 支持 |
| SE 发布页 | `https://www.nexusmods.com/skyrimspecialedition/mods/201` |
| 影响范围 | 所有身形的形状构建、衣服 conform、`.tri` morph 生成、RaceMenu 滑块数据源 |
| 维护状态 | **活跃开发**：2,000+ commits，2026-10-24 仍有提交 |
| 硬约束 | 构建产物会被后续覆盖它的 mod 静默替换（含 `BODYTRI` 丢失） |

要点：

- **两个可执行文件**：`BodySlide.exe`（构建）与 `OutfitStudio.exe`（编辑）自
  **2018-02-20** 起拆分、配置文件分离（原为同一 exe）——GitHub 提交
  "Separated BS and OS exec, split config files"。
- **`Build Morphs` 是全工具最重要的复选框**：勾了才有 `.tri`，RaceMenu 里
  才有那一栏可拖的滑块（详见下文）。
- 日常 **90% 只用 BodySlide**；"把老衣服适配到我的身形"才需要 Outfit Studio。
- 官方**命令行参数**齐全，整合包维护者可无人值守批量重建
  （流传的 `-o` / `-m` 参数并不存在，见下文纠错）。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 2011 | Caliente 发布 **CBBE**（本想做衣服，结果先做出了身体） | "人台"思路的确立（作者访谈，见 [cbbe.md](cbbe.md)） |
| 2011-2013 | Caliente 嫌**手搓形状不可持续**，写出 **BodySlide** | 具体首发日期**未确认**；LE 时代已成为 CBBE 标配 |
| 2014-11 | 仓库记录 **v2.2c**（GitHub 文件历史） | 工具已具规模（一手：仓库提交记录） |
| 2015-12-24 | **FO4 版上传 Nexus**（mods/25，original upload） | 跨游戏同一套代码库的开端（一手：Nexus 页） |
| 2015-10-29 | 仓库 LICENSE 文件就位（**GPLv3+**） | 开源许可确立 |
| **2018-02-20** | 提交 **"Separated BS and OS exec, split config files"** | BodySlide.exe 与 OutfitStudio.exe 拆成两个可执行文件、配置文件分开 |
| 2019-11-25 | 提交 "Remember 'Build Morphs' selection in config" | Build Morphs 勾选状态开始持久化 |
| 2021-03-01 | 加入 **nifly** 子模块（带命名空间） | NIF 读写库换血，影响后续所有网格操作 |
| 2026-05-27 | "Add Starfield material texture support and Catch2 tests (#579)" | 工具向 Starfield 扩张 |
| 2026-08-06 | "Add **HDT-SMP physics preview using Bullet** (#601)" | Outfit Studio 获得物理预览能力 |
| 2026-08-15 | "Render **Complex Materials for Skyrim (CS/ENB)** (#604)" | 预览支持 Community Shaders / ENB 的复杂材质 |
| 2026-10 | "Add **BSA/BA2 archive tests**"（10-11）、"Fix Starfield round-trip issues and keep cloth data"（10-18）、"Turn model space normals with the pose"（10-24） | 仍在高频开发；仓库累计 **2,040 commits** |

### 它从哪来

Caliente 的起点是"想做衣服 mod"：给 Skyrim 做衣服，先得有一具像样的身体（CBBE），
有了一致的人台，还得让每件衣服都能按不同体型变形——**手搓形状不可持续**，
于是他把"选滑块 → 生成网格"这件事做成了工具：BodySlide。
衣服与身形之间的转换、滑块创建、权重修正越来越复杂，
又在同一程序里长出了 **Outfit Studio**。

### 中间经历了什么

ousnius 加入后工具进入 SE 时代并扩展到 Fallout；2018-02 两个功能拆成独立 exe；
2021 年换用 nifly 处理 NIF。它始终跟着上游游戏与渲染生态走：
2026 年的提交列表（Starfield cloth、CS/ENB Complex Material、Bullet 物理预览、
BSA/BA2 测试）说明它已是一个**多游戏、仍在维护的通用工具**，而非 Skyrim 专用遗物。

### 现状

Skyrim 侧形态已十年未变（选身体 → 选预设 → Build），
但底层在持续现代化。对玩家唯一的实际影响：
**版本新旧不影响 `.osp` / SliderPresets 的兼容性**，新版本照旧读老身形 mod 的资产。

## 它解决什么问题

**没有它之前**：身形 mod 只发几个固定体型（Slim/Curvy/Vanilla），
想要中间值只能自己改网格；衣服与身体对不齐（穿模）没有系统化解法；
 morph 数据（RaceMenu 滑块）根本无处生成。

**它的解法**是三层：

1. **滑块体系**：身形 mod 用 `.osp` 声明"哪些滑块影响哪些网格"，
   BodySlide 按数值生成新顶点；
2. **批量一致**：Batch Build 把同一组数值一次烘焙给身体 + 所有衣服，
   保证起点一致（这是不穿模的前提）；
3. **morph 数据出口**：`Build Morphs` 生成 `.tri`，把"运行时调节能力"
   交接给 RaceMenu / NiOverride。

> 为什么"起点一致"重要、两条变形路径如何叠加，见
> [运行时 morph 与离线烘焙](morph-runtime-vs-bake.md)——那是本工具存在的理由。

## 它包含什么 / 工作原理

### 两者分工

| 工具 | 做什么 |
|---|---|
| **BodySlide** | 用滑块自定义身形/服装，并**批量构建**进游戏的 Data 目录 |
| **Outfit Studio** | 在身形之间转换服装、创建滑块、修正动画权重、用画笔/变换工具编辑网格、导入导出 FBX/OBJ/NIF；2026 年起带 Bullet 物理预览 |

日常用的 90% 是 BodySlide；要做"把某件老服装适配到我的身形"才需要 Outfit Studio。

### 文件格式

| 扩展名 / 名称 | 是什么 | 放在哪 |
|---|---|---|
| **`.osp`** | Outfit Studio Project / SliderSet。**纯文本 XML**，记录源文件与目标文件路径、哪些滑块影响哪些网格。**一个 `.osp` 可含多个项目** | `SliderSets/` |
| **`.osd`** | Outfit Studio Data。**二进制**，存放某项目所有网格的 morph 顶点数据（v3.0 引入，取代了此前成千上万的 BSD 小文件） | `ShapeData/<Project>/` |
| **`.nif`** | 所有滑块归零时的**基础形状**网格 | `ShapeData/<Project>/` |
| **`.tri`** | morph 数据（勾 `Build Morphs` 时生成），NIF 里写 `BODYTRI` 指向它 | 输出目录内 |
| **`.xml`（SliderPresets）** | 预设：一组命名过的滑块值 | `SliderPresets/`（即 `Data\CalienteTools\BodySlide\SliderPresets\`） |
| **`.xml`（SliderGroups）** | 预设的分组定义 | `SliderGroups/` |
| **`BuildSelection.xml`** | 批量构建时的冲突解决记录 | 工具目录 |
| **`BodySlide.xml` / `OutfitStudio.xml`** | 两个 exe 各自的配置文件（2018-02 拆分后分离） | 工具目录（确切位置未确认） |

### 滑块的含义

- **滑块 0 = 游戏内体重 0，滑块 100 = 游戏内体重 100**；
  预览窗口顶部那条对应游戏内体重滑条的中点。
- 可以手输负数或 >100，但**不推荐**（易扭曲、穿模）。
- 每个滑块在预设里存**两个值**（体重 0 与体重 100），所以同一个体型
  在不同体重下可以呈现不同效果；NPC 按自己的体重在两点间线性插值
  （详见 [bodyslide-presets.md](bodyslide-presets.md)）。

### Batch Build（批量构建）

构建所选分组内的全部 outfit。CLI 里对应 `--groupbuild`。

**输出文件冲突的处理**：BodySlide 通过 `BuildSelection.xml` 解决冲突，
**输者被跳过**——所以"我构建了但没生效"有时是这里被静默跳过了。
构建列表里出现冲突解决对话框时（装了多个身体版本时必然出现），
统一选你正在用的那个身体。

### `Build Morphs` 复选框（最重要的一项）

> 勾选后，BodySlide 会生成 **`.tri` morph 文件**，并在 NIF 里写入
> **`BODYTRI` extra data**，使 RaceMenu / NiOverride 能在游戏内应用 morph。
> **无副作用，推荐始终勾选。**

不勾的后果：**RaceMenu 里没有对应的身形滑块**。
还要注意**构建产物不能被别的 mod 的 NIF 覆盖**，否则 `BODYTRI` 一起丢掉。

机制细节见 [morph-and-nif-basics.md](../00-overview/morph-and-nif-basics.md)
与 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md)。

### 与 RaceMenu 的联动

RaceMenu（`skee64.dll` 内含 NiOverride）读取 `.tri`，在捏脸界面/MCM 中
应用身形 morph。前提三条：

1. 勾了 `Build Morphs`；
2. 构建的是 **3BA / 3BBB 变体**（如 "CBBE 3BBB Body Amazing"），
   而不是被普通 CBBE 覆盖；
3. 构建产物在最终的覆盖关系中胜出。

### 依赖库

仓库 README 列出（+ GitHub 记录确认）：

| 库 | 用途 |
|---|---|
| **nifly** | NIF 文件读写（2021-03 起为子模块） |
| **wxWidgets** | GUI 框架 |
| **OpenGL / GLI / SOIL2** | 渲染与图像加载 |
| **TinyXML-2** | XML 解析（.osp / 预设） |
| **FSEngine** | BSA/BA2 存档读写 |
| **Autodesk FBX SDK** | FBX 导入导出 |
| **half / Miniball / LZ4(F)** | 半精度浮点 / 几何 / 压缩 |
| **Bullet** | 2026-08 加入的 HDT-SMP 物理预览（#601） |
| nlohmann json / fkYAML / Catch2 | 配置与测试（仓库构建记录） |

## 安装

### 步骤

1. **选对游戏版本**：Skyrim SE 用 **Nexus SE 201**；FO4 用母页（mods/25）；
   或从 GitHub Releases 取构建。**别把 FO4 版装到 Skyrim**（跨游戏同一套代码，
   但发布包按游戏分）。
   - 验证点：exe 能启动，标题栏为对应游戏语境。
2. **MO2 安装**：把工具加为 MO2 的可执行文件（工具类 mod 或独立目录均可）。
   - 验证点：MO2 工具下拉里能直接跑 BodySlide。
3. **确认两个 exe**：`BodySlide.exe` 与 `OutfitStudio.exe` 是分开的
   （2018-02 起），配置文件也分离。
4. **装身形 mod**（[CBBE](cbbe.md) / [3BA](cbbe-3ba.md) / [BHUNP](unp-bhunp.md) /
   [HIMBO](himbo.md) / [UBE](ube.md)），它们的 `SliderSets` 会被工具自动读取。
   - 验证点：BodySlide 的 Groups 里出现对应身形组。
5. **首次构建**：选 Outfit/Body → 选预设 → Build / Batch Build
   （完整工作流见 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md)）。

### 安装顺序提醒

- 工具本身不参与游戏内覆盖，**优先级无所谓**；
- 但它的**构建产物**（输出到 Data 的 nif）会被后装的覆盖同一路径的 mod 顶掉——
  装完新护甲/新身体后**重跑一次 Batch Build**是标准动作
  （覆盖规则见 [mo2-override-rules.md](../07-workflow/mo2-override-rules.md)）。

## 使用与配置

### GUI 标准流程

```
1. Group Filter   → 勾选身体与所有服装所在的组（Unassigned 必勾）
2. Outfit/Body    → 选你的主身体（如 CBBE 3BBB Body Amazing / HIMBO）
3. Preset         → 选预设（Zeroed Sliders 或你的常用体型）
4. Build Morphs   → 勾上（要 RaceMenu 滑块就必勾）
5. Build / Batch Build → 确认列表里每件都在；冲突列表统一选同一身体
```

### Outfit Studio 标准流程（转换一件衣服）

官方 wiki 的 step-by-step（一手）：

```
1. New Project → 选 conversion reference / template（如 "CBBE Body"）
2. 选要转换的衣服 nif（Skyrim 注意 _0 / _1 低/高体重变体，两个都做）
3. 删掉随衣服载入的重复身体 shape（DEL 或右键 Delete Shape）
4. 画笔修穿模——修的是 base shape，不是滑块 morph
5. Slider -> Conform All（把身体滑块数据复制到衣服顶点）
6. 逐滑块检查穿模并修（一次只编一个滑块，但可多 shape 同修）
7. 多选衣服 shape → Copy Bone Weights（衣服跟动画走的关键）
8. File -> Save Project As... → Group Manager 挂进身形主组
```

第 5 步 conform 就是 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md)
第四节"衣服拥有同一套 morph 名字"的来源；第 8 步的分组规则见
[bodyslide-presets.md](bodyslide-presets.md)。

### 官方命令行参数

> ⚠️ **纠错**：流传较广的 `-o`、`-m` 参数**并不存在于当前官方 CLI**。
> 以下是官方 wiki 的现行参数。

#### BodySlide

| 长参数 | 短参数 | 作用 |
|---|---|---|
| `--groupbuild <groups>` | `-gbuild` | 按分组批量构建并退出 |
| `--build <outfits>` | `-b` | 按名称构建指定 outfit（逗号/分号/空格分隔） |
| `--filter <filter>` | `-f` | 构建名称匹配的 outfit（默认大小写不敏感子串匹配） |
| `--regexfilter` | `-regex` | 把 `--filter` 当正则 |
| `--targetdir <path>` | `-t` | 构建输出目录（默认游戏 Data 路径） |
| `--preset <name\|file>` | `-p` | 启动时选预设；可配 `--groupbuild`/`--build`/`--filter` 构建，或配 `--preview` 预览。`file.xml?预设名` 可指定文件内某预设 |
| `--trimorphs` | `-tri` | 启用 tri morph 输出（等价于 GUI 勾 `Build Morphs`） |
| `--preview <files>` | — | 直接进入预览模式（支持 `.nif` 与 `.osp`） |

**官方示例**：

```
BodySlide --groupbuild "CBBE,CBBE Vanilla Outfits" --targetdir "C:\Output" --preset "CBBE Curvy" --trimorphs
BodySlide --build "CBBE Body"
BodySlide --preset "C:\MyPresets\MyBodies.xml?My Curvy Body"
```

#### Outfit Studio

| 参数 | 作用 |
|---|---|
| `--project` / `-proj` | 打开指定项目 |
| `--single-instance` / `-single` | 单实例模式 |
| `--automation` / `-a <script>` | **无头运行自动化脚本**（批量转换用） |
| 位置参数 | 指定要操作的文件 |

整合包维护者的典型用法：改完身形/护甲后跑一条
`--groupbuild … --trimorphs` 全量重建，避免每个用户手动点。

### 配置文件

两个 exe 拆分后配置分离：`BodySlide.xml` / `OutfitStudio.xml`。
其中 `Build Morphs` 的勾选状态会被记住（2019-11 提交），
但**升级/重装工具后仍建议进 GUI 肉眼确认一次**。

## 兼容与冲突

| 关系 | 结论 |
|---|---|
| 构建产物 vs 其他 mod 的 NIF | **后装者赢**；`BODYTRI` 随 nif 一起被覆盖 ⇒ 滑块失效。重装护甲后重跑 Batch Build |
| 多个身体版本共存 | 构建时必出冲突解决列表；**统一选同一个身体**，否则起点不一致 ⇒ 穿模 |
| CBBE vs 3BA | 3BA 是覆盖式进阶版；工具里要选 3BBB 变体（如 "CBBE 3BBB Body Amazing"） |
| 跨游戏 | 同一套代码但发布包分游戏；Skyrim 用 SE 页（201），FO4 用母页（25） |
| RaceMenu 滑块缺失 | 没勾 `Build Morphs` / 漏勾 `Unassigned` 组 / 产物被覆盖 |
| 游戏 1.7.x | 本轮**未确认**（背景见 [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md)） |

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 构建了但游戏里没变化 | 输出被其他 mod 覆盖，或 `BuildSelection.xml` 里被跳过 | 检查覆盖关系；看冲突解决列表选对没有 |
| RaceMenu 身形栏空白 / 拖了没反应 | 没勾 `Build Morphs`，或 Group Filter 漏勾 `Unassigned` | 按 [morph-runtime-vs-bake.md](morph-runtime-vs-bake.md) 工作流重做 |
| Batch Build 列表里缺衣服 | 该衣服在没勾的组里（常在 `Unassigned`） | 回 Group Filter 补勾 |
| 构建出来的模型扭曲 / 穿模 | 滑块值超出 0~100，或身体与衣服预设不一致 | 归零重做；同一预设刷全部（[clipping.md](../06-troubleshooting/clipping.md)） |
| CLI 报未知参数 | 用了流传的 `-o` / `-m`（不存在） | 按上文官方参数表 |
| Outfit Studio 打不开某个 nif | 格式/插件不受支持 | 用 `--preview` 试开；查 wiki 与 nifly issues |
| 升级工具后老项目的滑块没了 | `.osd` / `SliderSets` 没跟着走 | 重装身形 mod；别手删 `ShapeData/` |

## 取舍与建议

**什么时候用什么**：

- **普通玩家**：GUI 走标准流程（Group Filter → 身体 → 预设 → Batch Build），
  永远勾 `Build Morphs`；
- **整合包/清单作者**：CLI `--groupbuild … --trimorphs` 进构建脚本，
  用户装完即用，零手动步骤；
- **衣服作者**：Outfit Studio 做 conform / 滑块创建 / 权重修正，
  批量转换用 `--automation`。

**纪律**：

- **不要手改 `ShapeData/` 与 `.osd`**——那是工具的缓存/数据区，手改必坏；
- 预设放 `SliderPresets\` 即出现在下拉框，管理见 [bodyslide-presets.md](bodyslide-presets.md)；
- 装新护甲 → 重跑 Batch Build，把它当成"装完护甲的最后一步"。

**版本敏感性**：本条版本结论（FO4 母页 5.8.2，2026-06-25）来自 Nexus 页一手；
GitHub Releases 页本轮未能直接读取（镜像页显示 v5.7.x，与 Nexus 5.8.2 的
先后关系**未确认**），**以 GitHub Releases 与 SE 页 201 为准**。

## 来源

- **一手（GitHub 仓库）**：作者与 credits（Caliente、ousnius、jonwd7、
  degenerated1123、NifTools team）、依赖库清单、LICENSE（GPLv3+）、
  2,040 commits 与 2026 年各提交（Starfield material #579、Bullet 物理预览 #601、
  CS/ENB Complex Material #604、BSA/BA2 tests、Starfield cloth round-trip、
  model space normals with the pose）、"Separated BS and OS exec, split config
  files"（2018-02-20）、"Remember Build Morphs selection in config"（2019-11-25）、
  nifly 子模块（2021-03-01）
  `https://github.com/ousnius/BodySlide-and-Outfit-Studio`
- **一手（官方 wiki）**：两者分工、文件格式（.osp/.osd/.nif）、
  CLI 参数表与官方示例、`BuildSelection.xml` 冲突解析
  `https://github.com/ousnius/BodySlide-and-Outfit-Studio/wiki/Command%E2%80%90line-arguments`
- **一手（Nexus 页）**：FO4 母页版本 5.8.2（2026-06-25）、
  original upload 2015-12-24、署名 "Created by Ousnius and Caliente"；
  SE 专用发布页 201
  `https://www.nexusmods.com/fallout4/mods/25`
- **一手（ousnius 本人解释）**：`.osp` 与 `.osd` 的区别（LoversLab）
- **一手（机制）**：`Build Morphs` → `.tri` + `BODYTRI` → NiOverride 运行时施加：
  官方仓库提交记录（"Write only a single BODYTRI extra data when building"）
  + RaceMenu 发布页
- **社区经验**："-o / -m 不存在"（本资料库与官方 wiki 逐条比对的纠错）；
  重装护甲后需重跑 Batch Build；RaceMenu 联动三前提的细节表述
- **未确认**：LE 时代首发具体日期、GitHub Releases 当前版本号、
  `BodySlide.xml` / `OutfitStudio.xml` 的运行时存放位置、1.7.x 兼容性
