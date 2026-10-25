---
id: racemenu
title: RaceMenu（捏脸核心）
category: 02-face
kind: tool
version: 3.0.0
updated: 2026-10-25
tags: [捏脸, RaceMenu, 滑块, CharGen, NiOverride, 1.7]
aliases: [rm, 捏脸工具, 捏脸界面, showracemenu, skee, skee64, 滑块界面, racemenu 是什么, racemenu 历史, 怎么装 racemenu, racemenu 版本, expired6978, ECE, 部件标签, 捏脸崩溃]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: RaceMenu 的谱系（ECE → RaceMenu）、skee64.dll 的两大模块、以官方 changelog 串起的版本时间线、完整安装与配置（ini 字段 / skee 控制台命令 / 0.4.20 部件标签）、以及它在 1.7.x 下的现状与崩溃坑。
---

# RaceMenu

> **一句话**：RaceMenu 把原版那个"不能搜索、没有数值、不能存预设"的捏脸界面，
> 换成了整个捏脸生态的**运行时地基** —— 它既提供界面（CharGen），
> 也提供"在游戏运行时改网格与贴图"的能力（NiOverride）。

---

## 速览

| 项目 | 值 |
|---|---|
| 作者 / 上传者 | **Expired（expired6978）**，Nexus 页 credits 亦署 **Expired6978/PurpleLunchbox** |
| LE 首发 | **2013-01-08**（`nexusmods.com/skyrim/mods/29624`），末版 **3.4.5**，最后更新 2015-11-07 |
| SE 首发 | **2018-08-06**（`nexusmods.com/skyrimspecialedition/mods/19080`），SE 包由 **ousnius** 制作 |
| 当前版本 | **0.4.20.0**（主文件 2026-04-20 上传；页面 *last updated* 标 2026-04-21，两者差一天） |
| 前置 | **仅 SKSE64**。主文件要求 **SKSE64 AE 2.2.6 或更高 + 游戏 1.6.1170** |
| GOG 版 | 单独的 0.4.20.0 GOG 文件，要求 **SKSE64 GOG AE 2.2.6+ + 游戏 1.6.1179**，作者标注 **untested** |
| 权限 | 作者权限栏原文：**"You may not redistribute any files under any circumstances."**（不得以任何形式再分发） |
| 影响范围 | 捏脸、身形滑块、overlay 纹身、染色、BodyGen 分配、预设分享生态的**共同底座** |
| 维护状态 | 仍在维护，但**不支持 1.7.x**（见下） |
| VR | 独立的 **RaceMenu VR 0.4.14**（2020-08-11），装完要删 `skee64.dll/ini` |

要点：

- **前置只有 SKSE64 一项** —— 它**不依赖 PapyrusUtil**（这是本领域流传最广的误传之一，
  见 [`../01-prerequisites/skse-plugin-frameworks.md`](../01-prerequisites/skse-plugin-frameworks.md)）。
- 主体是一个 SKSE 插件 **`skee64.dll`**，内含 **CharGen** 与 **NiOverride** 两个模块，
  前者管界面，后者管"运行时改模型/贴图"。
- **`skee` 系列控制台命令自 0.4.13 起才有**，老教程里的命令在新版上无效的反过来才对：
  老版本没有这些命令。
- **RaceMenu 给的是"能力"，不是"数据"**：身形滑块长什么样由身形 mod 决定，
  能不能拖动取决于你自己有没有在 BodySlide 里勾 `Build Morphs` 构建出 `.tri`。
- **1.7.x 目前不能用**，而且已跟进 1.7.x 的人会撞上一个必崩的坑（旧 overlay NIF）。

---

## 前世今生

### 谱系：ECE → RaceMenu

Skyrim 的捏脸改造有两条源流。先出现的是 **ECE（Enhanced Character Edit）**，
由日本作者组成的 **ECE Team（tktk / RAN46 / kaeper）** 制作。RaceMenu 的 Nexus
credits 里至今保留着一行：

> `ECE Team (tktk, RAN46, kaeper - ECE Morphs)`

也就是说，**RaceMenu 直接沿用了 ECE 的 morph 资源**。这不是"两个竞争 mod"的关系，
而是**后继者把前代的资源并入自己**。ECE 走的是 CME（CharacterMakingExtender）
那套 `CME_save` 目录 + 二进制 slot 的路线，RaceMenu 走的是 SKSE 插件 + 运行时
morph 的路线；两者都改同一个角色创建菜单，**不能同时生效**。

### 时间线

| 时间 | 事件 | 意义 |
|---|---|---|
| 2013-01-08 | RaceMenu **LE 版**首发（Nexus 29624） | 与 ECE 并列的两套捏脸方案之一 |
| 2015-11-07 | LE 末版 **3.4.5**（修斩首尸体崩溃、修 `morphs.ini` 解析、默认关闭 parallel morphing 与 face overlay） | LE 时代收尾 |
| 2018-08-06 | **SE 页建立**（Nexus 19080），credits 记 **ousnius - (Creating SE package)** | 进入 SE 生态；作者仍是 expired6978 |
| 2018-08-21 | 发布 **Modders Package**（脚本源码与模板） | 第三方插件（身形滑块）生态的起点 |
| 未确认 | 0.4.9 ~ 0.4.12（染发槽、`bAllowAllMorphs` 恢复、ENB 线框修复、 dyes 的 multiply 混合模式、预设肤色存取修复） | 功能补课期 |
| 未确认 | **0.4.13**：加入 `skee` 控制台命令族；实验性 VR 支持；修 XPMSE co-save 损坏导致的崩溃 | 从"只有界面"变成"可被脚本/命令行驱动" |
| 未确认 | **0.4.14**：**SE 与 VR 的 dll 拆开**（`skee64.dll` / `skeevr.dll`） | 解决 mod 管理器报"故意不兼容" |
| 未确认 | **0.4.15 → 0.4.16**：0.4.15 修自定义 head part 滑块崩溃与假发颜色同步；**0.4.16 修 0.4.15 引入的大范围崩溃**（任何含"没有 Character Creation 数据的 actor"的 cell，例如尸鬼 Draugr） | 0.4.15 是著名的问题版本 |
| 未确认 | **0.4.19.10**：修染料与 bodymorph 的内存泄漏；接口交换改到 post-load | 为外部插件铺路 |
| 未确认 | **0.4.19.11**：`skee.ini` 新增 **`bEnableEarlyRegistration`**（默认 OFF），changelog 原文写 **"use this for OBODY"** | 官方为第三方分配工具开的兼容模式 |
| 未确认 | **0.4.19.13**：支持 **1.6.640** 与 **GOG 1.6.659**；新增 `bBodyMorphGPUCopy` / `bBodyMorphRebind` 两项提速（默认开） | BodyMorph 性能优化 |
| 2023-12-10 | **0.4.19.15**：支持 **1.6.1130**；日志改用 spdlog；开放 Overlays / Presets 的编程接口 | 插件作者能直接读写预设 |
| 2024-01-27 | **0.4.19.16**：支持 **1.6.1170** | 此后长期是"上一代稳定版"的标配 |
| 2023-01-09（misc 文件） | **Modified Overlay Meshes**（0.0.1）：把 overlay 模板网格标为 Decal | 修水下消失与透明物体渲染顺序 |
| 2026-04-20/21 | **0.4.20.0**：**部件标签（Part selection filter and Tags）** + 更多 C++ API；新增 GOG 版（**untested**） | 目前最新 |
| 2026-08-23 | 作者原帖：**1.7.99 版已完成，但卡在 SKSE 的 Papyrus 函数 bug（会崩游戏）；1.7.104 未做**；转向 **CommonLibSSE-NG** 重写 | 现状：1.7.x 无官方可用版 |
| 2026-08-23 | 同帖：Bethesda 改坏了 NIF 解析，**含 NiTriShape 但没有 NiTriShapeData 的网格会崩**，而 RaceMenu 的 overlay nif 正是这种 | 1.7.x 下旧 overlay 文件 = 必崩 |

> 时间线里标"未确认"的行，是 changelog **有内容但 Nexus 未给出上传日期**的版本。
> 顺序依 changelog 自上而下的排列确定，**日期未确认**。

### 现状：1.7.x

> **⚠️ RaceMenu 在 1.7.x 下不可用。** 作者 2026-08-23 原帖（一手）：
> 1.7.99 版本身已完成，但 SKSE 当前有坏掉的 Papyrus 函数会让游戏崩溃，因此压着没发；
> 1.7.104 还没做；作者把精力转到了基于 **CommonLibSSE-NG**（连带 Address Library）的重写。

作者的判断是：重写完成后 RaceMenu 也许能**自动适配后续游戏版本**，甚至向下兼容若干个
AE 版本，但**不会支持 SE**。截至 2026-10-25，官方 Files 页最新仍是 **0.4.20.0**。

因此本库的建议是：**做捏脸就留在 1.6.1170**。完整决策树见
[`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)。

---

## 它解决什么问题

### 没有它之前：原版角色创建菜单

| 原版的状况 | 后果 |
|---|---|
| 所有选项平铺，**没有分类、没有搜索** | 找一个滑块要翻半天 |
| 滑块**不显示数值** | 只能凭感觉拖，无法复现 |
| 只能选**单一**战纹 | 战纹/纹身无法叠加 |
| 战纹颜色只能从固定色板挑 | 无法填任意颜色 |
| **没有预设存取**（只有"随机"） | 捏好的脸无法保存/分享 |
| **没有顶点级编辑** | 想改的细节只能靠 morph 凑 |
| **没有纹身/战纹的运行时贴图叠加** | 想要额外的脸纹只能改原版贴图 |
| 捏完的**头网格无法导出** | 无法把玩家的脸变成 NPC/随从的脸 |

### 它怎么解决的

| 能力 | 由谁提供 |
|---|---|
| SkyUI 风格分类 + **按名称搜索过滤** | `RaceMenu.esp`（CharGen 界面） |
| 所有滑块**数值显示** | `RaceMenu.esp` |
| **多个 RGBA 战纹** + 战纹热替换 + 身体/手/脚彩绘 | `RaceMenu.esp` + NiOverride 的 overlay |
| 任意 tint 都能用 **AARRGGBB** 填色（含发色） | `RaceMenu.esp` |
| **存/读预设**（`.jslot`） | CharGen（需 CharGen v2.0.0+；见 [`racemenu-presets.md`](racemenu-presets.md)） |
| **顶点级雕塑**（Sculpt） | CharGen |
| 运行时 **overlay / 染色 / 节点变换 / 骨骼缩放** | **NiOverride** |
| **导出头网格**（给 NPC 用） | CharGen 的 *Export head* |
| 显示 **HeadPart 的名字与来源 mod** | CharGen v2.1.2+ |
| 身高 / 二头肌 / 臀 / 胸 / 胸曲线（可选 `RaceMenuPlugin.esp`） | 骨骼缩放，**只对支持骨骼缩放的网格有效**（官方举例 TBBP/BBP） |

> **关键区分**：RaceMenu **提供能力，不提供数据**。
> 你能拖哪些滑块，取决于装了哪些身形 mod；拖了有没有反应，取决于
> **你自己有没有构建出 `.tri`**。见
> [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md)。

---

## 工作原理

### 主体：`skee64.dll` 的两个模块

RaceMenu 不是一堆 Papyrus 脚本，它的主体是一个 **C++ 写的 SKSE 插件**，
文件名 `skee64.dll`（VR 为 `skeevr.dll`）。里面是两个模块：

| 模块 | 干什么 | 你能看到的部分 |
|---|---|---|
| **CharGen** | 角色创建界面本身 | 分类、搜索、数值、滑块、预设、**Sculpt**、部件标签、头网格导出 |
| **NiOverride** | 运行时**叠加层**机制：`morph`（顶点位移）、`overlay`（贴图覆盖）、`transforms`（节点变换）、`dyes`（染色）、`tint`（着色）、骨骼缩放 | 身形滑块实时生效、纹身叠加、装备染色、overlay 发光色/强度 |

源码在作者的合集仓库：`https://github.com/expired6978/SKSE64Plugins`（子目录 `skee64`），
提交记录里能看到 "Update to 1.6.1170" 之类 —— **这是核对"版本 ↔ 游戏版本"对应关系的一手材料**。

### morph 的施加路径（为什么拖滑块能立刻变形）

```
BodySlide 勾 Build Morphs
   → 生成 .tri（顶点位移数据）+ 在 nif 里写入 BODYTRI 指向它
      → 游戏内 NiOverride 读到这套 morph 名字
         → 你拖动滑块 → NiOverride 对所有含同名 morph 的网格施加位移（运行时，不改文件）
```

因为**所有网格（裸体 + 每一件已 conform 的衣服）共享同一套 morph 名字**，
所以拖滑块时衣服会跟着变。这条链条的完整解释见
[`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md) 与
[`../00-overview/morph-and-nif-basics.md`](../00-overview/morph-and-nif-basics.md)。

> 界面上做的 morph / overlay / sculpt 是**运行时状态**，随存档落在 **SKSE co-save**
> 里（[`../05-distribution/racemenu-bodygen.md`](../05-distribution/racemenu-bodygen.md)
> 记录了 BodyGen 状态同样如此；**co-save 具体格式未确认**）。
> 推论很实用：**co-save 丢失、或 mod 列表变化过大时，运行时外观会丢失或错位。**

---

## 安装

1. **确认游戏版本**：当前稳定组合是 **游戏 1.6.1170 + SKSE64 AE 2.2.6+**。
   GOG 版另有单独文件（要求 1.6.1179，作者标 untested）。版本对照见
   [`../00-overview/version-matrix.md`](../00-overview/version-matrix.md)。
   验证点：从 `skse64_loader.exe` 启动游戏，主菜单能正常进入。
2. **装 SKSE64**（唯一硬性前置）。验证点：`Data\SKSE\` 目录存在，游戏能启动。
3. **用 mod 管理器安装 RaceMenu 主文件**。SE 与 VR **不要混装**；VR 用 0.4.14 那个
   独立文件，装完**删掉 `skee64.dll` / `skee64.ini`**。
4. **启用 `RaceMenu.esp`**（`RaceMenuPlugin.esp` 可选，只在你想要身高/胸臀等骨骼缩放时启用）。
5. **清理散装旧脚本** —— 官方描述明确要求：若你看到版本不匹配警告，删除 Data 下的
   这些松散文件：

   ```
   CharGen.pex
   NiOverride.pex
   RaceMenu.pex
   RaceMenuBase.pex
   RaceMenuLoad.pex
   RaceMenuPlugin.pex
   ```

   验证点：进游戏开 `showracemenu`，界面是带搜索框与数值的 RaceMenu 界面，
   而不是一堆 `$` 占位符的原版界面。
6. **若你之前单独装过 CharGen Extension**：从 **2.7 起它已完全并入本体**，官方 FAQ 的
   意思是**应当卸载**。
7. **若你在 1.7.x 下**：先删掉本地残留的旧 overlay NIF，否则启动即崩 ——
   `Data\Meshes\Actors\Character\Character Assets\` 下的 face / body / hands / feet
   四种 `*_overlay.nif` 与 `*_magicoverlay.nif`，**共 8 个文件**；
   完整清单见 [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md)。

> 加载顺序：**RaceMenu 本体对加载顺序不敏感**，但**依赖它的东西**敏感
> （例如 High Poly Head 与 Expressive Facegen Morphs 的相对顺序，见
> [`high-poly-head.md`](high-poly-head.md) 与 [`../07-workflow/install-order.md`](../07-workflow/install-order.md)）。

---

## 使用与配置

### 界面

- 顶部类别按 **SkyUI 风格**分组，右上角可**按名称搜索**滑块。
- 每个滑块**显示数值**；tint（含发色）可直接填 **AARRGGBB**。
- 相机可上下左右平移与缩放；**Light On/Off** 在角色正前方生成一盏白光
  （只在捏脸界面内有效，出菜单就没了 —— 需要常驻补光看 [`facelight.md`](facelight.md)）。
- 支持**手柄**、支持**自定义种族**；**不修改任何原版资源**。

### Sculpt（雕塑）

顶点级编辑，用于滑块线性叠加做不出来的细节：

| 工具 | 用途 |
|---|---|
| Inflate / Deflate | 沿法线鼓起或凹陷 |
| Smooth | 平滑 |
| Move | 拖拽顶点 |
| **Mask** | 限定编辑区域（**不影响导出**，仅作编辑辅助） |
| History | 撤销历史 |
| Clear Sculpt | 清空雕塑 |
| **Import Geometry** | 导入雕塑几何（配合预设附带的 `.nif`） |
| **F5 Export head** | 导出头网格（做自定义随从脸的起点） |

> ⚠️ Sculpt 依赖 **BSDynamicTriShape** 类网格；0.4.10 修过"进入 Sculpt 页时因非
> BSDynamicTriShape 网格而崩溃"的问题。遇到进 Sculpt 就崩，先怀疑网格本身。

### 高分辨率战纹

面部纹身/战纹默认分辨率很低（256），在 `Data/SKSE/SKSE.ini` 里提高：

```
[Display]
iTintTextureResolution=2048
```

### 配置文件 `skee64.ini`

路径 `Data\SKSE\Plugins\skee64.ini`（作者 changelog 里也把它写作 `skee.ini`，
**两者指同一处配置；命名差异未确认**）。已知字段：

| 字段 | 默认 | 说明 |
|---|---|---|
| `bEnableBodyMorph` | `1` | 启用 BodySlide 辅助 morph（身形滑块的总开关） |
| `bEnableBodyGen` | `0` | 启用内置 BodyGen 随机身形（与 OBody 类工具互斥） |
| `bEnableEarlyRegistration` | **OFF** | 0.4.19.11 起的兼容模式，changelog 原文：**"use this for OBODY"** |
| `bBodyMorphGPUCopy` / `bBodyMorphRebind` | **默认开** | 0.4.19.13 起用于提升 BodyMorph 速度 |
| `bEnableTintHairSlot=1` / `uTintHairSlot=2050` | 0.4.9 起 | 自动把发色染到已装备物品（假发/头盔毛发）上 |
| `bAllowAnyRacePart` / `bAlloyAnyGenderPart` | `0` | 放宽部件跨种族/跨性别限制，官方标注**不推荐** |

> 调整 `bEnableBodyMorph=0` 也是一条很有用的**判据**：若关掉它帧数不再掉，
> 说明卡顿来自 morph 计算而非别的 mod（社区经验，LoversLab）。

### 控制台命令（`skee`，0.4.13+）

```
skee reload tints                      重新加载 tint 数据（改了 XML 后不用重开游戏）
skee erase bodymorph|transforms|sculpt|overlays
skee erase bodymorph-cache             清空内部 body TRI 缓存
skee preset-save PATH                  导出到 Data/SKSE/Plugins/CharGen/Exported/PATH.jslot
skee preset-load PATH                  加载到当前控制台选中的 actor（可以是 NPC）
skee dump bodymorph|transforms|itemdata
```

`preset-load` 那条尤其有用：**它能把预设直接套到 NPC 上**（官方 changelog 原话
"yes, it can be applied onto NPCs"）。详见 [`racemenu-presets.md`](racemenu-presets.md)。

### 部件标签（0.4.20.0 新增）

这是 0.4.20.0 的主要增量，来自作者的 Patreon 版功能下放：
**给 head part 打标签，然后在捏脸界面按标签过滤**（发型太多时尤其有用）。

类型映射（作者原帖原文）：

```
Face=1, Eyes=2, Hair=3, Beard=4, Scar=5, Brow=6
```

mod 作者在自己的 mod 里放两个文件即可：

```
Data/SKSE/Plugins/CharGen/Tags/<MODNAME>/parts.json
Data/SKSE/Plugins/CharGen/Tags/<MODNAME>/tags.json
```

`parts.json` 声明"有哪些标签"（作者给的示例）：

```json
{
  "parts": [
    {
      "type": 3,
      "tags": [
        { "name": "Short",    "label": "$TagShort" },
        { "name": "Long",     "label": "$TagLong" },
        { "name": "KSHairdo", "label": "$TagKSHairdo" }
      ]
    }
  ]
}
```

`tags.json` 声明"哪个部件有哪些标签"，左侧键可以是部件的 **EditorID**，
也可以是 `ModName.esp|D4` 这种十六进制 FormID 形式（作者示例）：

```json
{
  "0SnowGale": ["Long", "KSHairdo"],
  "0Sky189":   ["Short", "KSHairdo"]
}
```

规则要点（作者原帖）：

- `label` 可以是**翻译键**（`$TagShort`）也可以是**直接显示的文本**；
- **同一个 Form 被两个 mod 打标签时会合并**（If two mods target the same Form, Tags are merged）；
- 没打标签的部件**只是没有过滤项，不会消失**。

> `parts.json` / `tags.json` 除上述示例外的**字段细节未确认**（作者只给了示例片段）。

---

## 兼容与冲突

| 对象 | 关系 |
|---|---|
| **ECE** | 同源不同路线。**预设不互通**，且**不建议同时启用**（社区共识：两者改同一个菜单会互相打架）。作者的迁移途径是 **CharGen Export** |
| **PapyrusUtil** | **不是前置**（误传，见 [`../01-prerequisites/skse-plugin-frameworks.md`](../01-prerequisites/skse-plugin-frameworks.md)） |
| **CharGen Extension** | 2.7 起并入本体，**单独装的应当卸载** |
| **BodySlide / 身形 mod** | 身形 mod 决定滑块名字；`.tri` 由你在 BodySlide 里构建 —— 三者是"能力 / 名称 / 数据"的关系 |
| **OBody / OBody NG** | 需要 `bEnableEarlyRegistration`（官方 changelog 指定用途）。见 [`../05-distribution/obody-ng.md`](../05-distribution/obody-ng.md) |
| **BodyGen（内置）** | 与 OBody 类工具互斥，用后者时把 `bEnableBodyGen` 置 0。见 [`../05-distribution/racemenu-bodygen.md`](../05-distribution/racemenu-bodygen.md) |
| **High Poly Head** | 硬前置关系：HPH 要求 RaceMenu。见 [`high-poly-head.md`](high-poly-head.md) |
| **EFM / EFA** | EFM 需要 RaceMenu 才能用全部功能；**EFM morph 不适用于 HPH**。见 [`expressive-morphs.md`](expressive-morphs.md) |
| **1.7.x** | **不支持**（见"前世今生"） |
| **VR** | 用独立的 VR 0.4.14 文件，并删除 `skee64.dll/ini` |

---

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 界面里一堆 `$`、按钮文字异常 | SKSE64 没装好 / 不是从 `skse64_loader.exe` 启动 | 重装 SKSE64 并用它启动（社区经验） |
| 弹"版本不匹配"警告 | Data 下有散装的旧 `.pex` | 删除上文列出的 6 个 `.pex`（**官方描述要求**） |
| 身形那一栏**完全没有** | 没有构建 `.tri` | BodySlide 勾 `Build Morphs` 重构建；见 [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md) |
| 栏在但拖了没反应 | morph 数据与当前身体不是同一套 / `bEnableBodyMorph=0` | 检查 `skee64.ini`，并按 Zeroed Sliders 流程重构建 |
| 进 Sculpt 页就崩 | 网格不是 BSDynamicTriShape | 0.4.10 已修此类崩溃；确认 RaceMenu 与身形/头模版本匹配 |
| 进入含**尸鬼**的 cell 就崩 | 你装的是 **0.4.15** | 升到 0.4.16+（changelog 明写这是 0.4.15 引入的） |
| **1.7.x 下启动/加载就崩** | 磁盘上有旧 overlay NIF | 删 8 个 overlay 文件（新版已打包进 BSA），见 [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md) |
| 战纹/纹身糊 | `iTintTextureResolution` 仍是默认 256 | `SKSE.ini` 里设 2048 |
| overlay 纹身水下消失 / 与透明物体穿帮 | overlay 模板网格未标 Decal | 装官方 misc 文件 **Modified Overlay Meshes** |
| 拖滑块时帧数暴跌 | morph 计算开销 | 先试 `bEnableBodyMorph=0` 做对照（社区经验）；亦可确认 `bBodyMorphGPUCopy`/`bBodyMorphRebind` 为开 |
| 预设导进去了脸不对 | 依赖资源缺失 / HPH 未切 / morph 未构建 | 见 [`../06-troubleshooting/preset-not-applied.md`](../06-troubleshooting/preset-not-applied.md) |

---

## 取舍与建议

- **装**：几乎必然要装。只要你打算捏脸、用身形滑块、用 overlay 纹身、用预设、
  或者用任何依赖 NiOverride 的 mod（OBody、BodyGen、纹身类），RaceMenu 都是地基。
- **留在 1.6.1170**：如果你在做人物向的 modlist，1.7.x 目前拿不到可用的 RaceMenu，
  升级等于放弃整套捏脸生态。决策树见
  [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)。
- **别同时装 ECE**。需要迁移老脸时用作者提供的 **CharGen Export**。
- **别为了"多几个滑块"去开 `bAllowAnyRacePart` / `bAlloyAnyGenderPart`**，
  官方自己标了"not recommended"。
- **调不动就先查"有没有数据"**：RaceMenu 报的错往往不在 RaceMenu 身上 ——
  八成是 `.tri` 没构建、身形家族不匹配、或者依赖的头模/纹理没装。
- **不要分发它的文件**：作者权限栏明确禁止任何形式的再分发。

---

## 来源

**一手**

- RaceMenu Nexus SE 发布页（作者与上传者、credits 含 ECE Team / ousnius / schlangster、
  original upload 2018-08-06、version 0.4.20.0、权限栏原文、完整功能列表、
  "For ECE to RaceMenu migration see: CharGen Export"、需删除的 6 个 `.pex`）：
  `https://www.nexusmods.com/skyrimspecialedition/mods/19080`
- RaceMenu Nexus SE **Files 页** changelog（0.4.12 → 0.4.20.0 全部条目；主文件要求
  "SKSE64 Anniversary Edition 2.2.6 or greater and Game Version 1.6.1170"；
  GOG 文件要求 1.6.1179；VR 0.4.14 上传于 2020-08-11；Modified Overlay Meshes
  上传于 2023-01-09；Modders Package 上传于 2018-08-21；0.4.19.15 上传 2023-12-10；
  0.4.19.16 上传 2024-01-27）：`https://www.nexusmods.com/skyrimspecialedition/mods/19080?tab=files`
- RaceMenu Nexus **LE** 页（Nexus 29624、original upload **2013-01-08**、
  末版 **3.4.5**、last updated **2015-11-07**、同一套 credits）：
  `https://www.nexusmods.com/skyrim/mods/29624`
- 作者 Nexus 帖（2026-04-20）：**部件标签机制与 parts.json / tags.json 示例、
  类型映射、标签合并规则、GOG 1.6.1179 untested** —— 一手
- 作者 Nexus 帖（2026-08-23）：**1.7.99 已完成但卡在 SKSE Papyrus bug、1.7.104 未做、
  转向 CommonLibSSE-NG、NiTriShape 无 NiTriShapeData 导致崩溃与 8 个 overlay 文件清单** —— 一手
- GitHub `expired6978/SKSE64Plugins`（`skee64` 源码与提交记录）—— 一手

**社区经验**

- `skee64.ini` 中 `bEnableBodyMorph=1` / `bEnableBodyGen=0` 的推荐组合（OBody NG 安装指南类文档）
- `bEnableBodyMorph=0` 作为帧数问题的判据（LoversLab 讨论帖）
- "ECE 与 RaceMenu 不能同时用"（Nexus 论坛多帖一致）
- 界面出现 `$` 占位符即 SKSE 未正确加载（社区经验）

**未确认**

- 0.4.9 ~ 0.4.19.11 各版本的**上传日期**（Nexus changelog 未给出）
- `skee64.ini` 与 `skee.ini` 的命名差异（changelog 两种写法都出现过）
- `parts.json` / `tags.json` 除作者示例外的完整字段定义
- SKSE co-save 中 RaceMenu 运行时数据的具体格式
- ECE 的末版版本号（社区可见 1.3 / 1.4 / 1.5 多种口径）
