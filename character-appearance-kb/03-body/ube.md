---
id: ube
title: UBE 2.0（Ultimate Body Enhancer）—— 新增独立种族的新世代身形
category: 03-body
kind: concept
version: 2.0.0
updated: 2026-10-25
tags: [身形, UBE, 生态, 新一代, bodybase]
aliases: [ultimate body enhancer, 新身形, 身形标准, 三套并行, 新一代身形, ube 2.0, bungalow body, ube 是什么, ube 安装, johnybungalow1, ultimate body enhancer 2.0, ube 补丁, ube 种族, ube 滑块, lowresoutis]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92989
summary: UBE 2.0 完整百科：它不是身体替换而是新增独立种族（JohnyBungalow1 + lowresOutis），可与 3BA/BHUNP 并存但服装转换/皮肤/预设全线不兼容，所有服装都要 .esp 补丁 + Outfit Studio 转换；含安装流程、xEdit 一键补丁、meshes\!UBE 路径、Normals recalc 滑块，以及与"三套并行"局面的辨析。
---

# UBE 2.0（Ultimate Body Enhancer）

> **一句话**：UBE 2.0 **不是身体替换器，而是新增独立种族**——自带高模身体/头部
> （体+头约 6 万+顶点）；它能与 3BA/BHUNP 安全并存，但**所有服装都要补丁 + 转换**。
> 作者原话：**"it's not a perfect plug-n-play mod"**。

## 速览

| 项 | 内容 |
|---|---|
| 全称 | **UBE 2.0 -- Ultimate Body Enhancer 2.0**（Nexus 依赖页的正式需求名） |
| 作者 | **JohnyBungalow1 与 lowresOutis**（多页 credits 确认） |
| 社区俗称 | **"Bungalow Body and Face"**（LoversLab 官方帖标题） |
| 性质 | **新增独立种族**（基于 RaceCompability 构建），不是身体替换 |
| 规模 | 体 + 头约 **6 万+顶点**；滑块：脸 **370+** / 身体 **200+** / 生殖器 **70+** |
| 发布 | LoversLab **2023-04-20** 首发；Nexus SE **92989** |
| 当前版本 | **未确认**（Nexus 页在墙后；2026 年的翻译页标注 U.0.7，不代表主 mod 版本号） |
| 核心前置 | RaceCompability · RaceMenu · XPMSSE · CBPC · FSMP |
| 物理 | **不自带物理方案**，只取 3BA 的 SMP/CBPC 配置 |

要点：

- **可与之并存 ≠ 可与之通用**：与 3BA/BHUNP 并存安装无冲突，但 3BA/BHUNP 的
  **服装转换不兼容**、CBBE/UNP **皮肤不兼容**、原版/HPH/CotR **预设不兼容**。
- **所有服装都需要 .esp 补丁 + Outfit Studio 转换**——连首饰的 ArmorAddon 也要
  （HeadParts 除外）。UBE 自带 xEdit 脚本一键给整个加载顺序打补丁。
- 补丁后 ArmorAddon 走 **`meshes\!UBE\`** 路径（`!` 前缀让它获得最高文件优先级）。
- SE 版自带**从 AE 反向移植的 `skee64.dll`**；改体重时法线不自动更新，
  要用 **"Normals recalc"** 滑块。
- 它是 Nexus 标签体系里 **`UBE Bodybase`** 这一标签的本体，与 `CBBE Bodybase`、
  `UNP Bodybase`、`TBD Bodybase` 并列。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 2023-04-20 | JohnyBungalow1 在 LoversLab 发布 **"UBE 2.0 aka Bungalow Body and Face replacer"** | 项目首发（一手：作者帖） |
| 2023-2024 | 迁移/同步至 Nexus SE **92989**；首批依赖生态出现（Patch Compendium 等） | 进入主流分发渠道；Nexus 上传具体日期未确认 |
| 2024-2025 | 皮肤/化妆品/预设生态成型：Diamond Skin (UBE)、Freyna Skin、Jada 8.1 Skin、LDD UBE 化妆品、各类 UBE 预设 | "没有皮肤可用"开始被解决 |
| 2025-2026 | 持续更新（3DMGAME 转载帖标注 2025-07-12 更新；2026 年仍有新翻译） | 维护仍在继续；具体版本号未确认 |

### 它从哪来

作者 **JohnyBungalow1**（与 **lowresOutis** 合作）的出发点不是"再做一个身体替换"，
而是做一具**精度足够高的新身体 + 新头**：约 6 万+顶点（体+头合计），
并且**不使用 Skyrim 的模型空间法线贴图**——高模本身的细节已够，
不需要靠 model space normal 补偿肌肉线条（作者原述）。

为了实现"同一件盔甲，原版种族与 UBE 种族各穿各的模型"，
UBE 没有走"替换裸体网格"的路线，而是走**新增种族**的路线
（类似虎人/亚龙人拥有独立模型路径的方式）。

### 中间经历了什么

分水岭是生态成型：早期"没有皮肤可用"是最大劝退点
（UBE 的 UV 与任何现存身体 mod 都不同，Fair Skin 之类不能直接用）；
2024-2025 年 Diamond Skin (UBE)、Freyna Skin、Jada 8.1 Skin、
以及 LDD/Pretty Makeup/Koralina 等化妆品转换陆续出现，
"(Ultimate Body Enhancer) Patch Compendium - UBE" 这类补丁合集也成了常见前置。

### 现状

仍在维护、持续更新（2026 年仍有翻译跟进）。它与 3BA/HIMBO 的关系
**不是取代而是并行**（见"取舍与建议"）。当前版本号**未确认**——
2026 年的 RU/ES 翻译页标注 U.0.7，但那是翻译版本，不能当主 mod 版本用。

## 它解决什么问题

**没有它之前**：CBBE/UNP 系身形的网格精度有上限，
肌肉等细节依赖 model space normal 贴图"画"出来；
滑块规模与 morph 自由度也受老拓扑限制。

**UBE 的解法**：换一具**更高精度、拓扑自由**的身体与头——
6 万+顶点 + 370+/200+/70+ 的滑块规模，让"瘦、胖、柔软或肌肉夸张"
都能靠滑块捏出来；脸部甚至有 16 个精灵耳"预设"滑块这类细粒度选择。

> **代价**是作者自己列明的：性能偏重（相对）、纹理选择少、
> 每件衣服都要补丁+转换、预设不互通。作者原话：
> **"Yes, it's not a perfect plug-n-play mod. It has quite a few of caveats
> and specifics, that requires at least some form of dedication from you."**

## 它包含什么

| 组件 | 说明 |
|---|---|
| 新种族 | 基于 RaceCompability 构建的独立种族，自带身体/头部网格与纹理 |
| 独立服装路径 | 所有服装走 UBE 自己的模型路径（`meshes\!UBE\`，补丁后生效） |
| xEdit 补丁脚本 | 一键给整个加载顺序打补丁（见"安装"） |
| 反向移植 `skee64.dll` | SE 版自带，从 AE 反向移植，带法线更新功能 |
| UBE SOS addon | 独特的 SOS 附加组件；改过 `SOS_ActorMagicEffect_Script.pex`（检查 slot 53） |
| 可选：原版服装转换 | 主 mod 可选文件含 `UBE Vanilla Armor and Clothes`（NG 版需 Armory Data Manipulator）——据翻译页文件列表 |

**不包含**：自己的物理方案（只复用 3BA 的 SMP/CBPC 配置）、
CBBE/UNP 系皮肤（UV 不同，装不了）。

## 安装

### 步骤

1. **公共前置**：MO2、SKSE64、[RaceMenu](../02-face/racemenu.md)、XPMSSE、
   CBPC、[FSMP](../04-physics/faster-hdt-smp.md)。
   - 验证点：上述插件 dll 均在 `Data\SKSE\Plugins\` 下。
2. **RaceCompability**（必需）：UBE 种族由它构建。
   - 验证点：RaceCompatibility 相关文件就位。
3. **装 UBE 2.0 主文件**（Nexus 92989）。
   - 验证点：加载顺序里出现 UBE 的插件与网格文件。
4. **物理配置**：只需 3BA 的 SMP/CBPC 配置。若没装 3BA，
   从 UBE 或 3BA 的可选文件装 **"CBBE 3BA Physics Config Reinstaller"**。
   - 验证点：`SKSE\Plugins` 下出现对应 CBPC/SMP 配置文件。
5. **（可选）SOS**：想要额外功能再装；装 UBE SOS addon。
6. **（可选）生态**：**(Ultimate Body Enhancer) Patch Compendium - UBE**（补丁合集，Nexus 站内检索）、
   UBE 皮肤/化妆品、`UBE Vanilla Armor and Clothes`。
7. **给服装打补丁**（**每次新增衣服/首饰后都要重做**）：
   - 用 xEdit 跑 UBE 自带的补丁脚本，一键给整个加载顺序打补丁；
   - 验证点：目标盔甲的 ArmorAddon 指向 `meshes\!UBE\` 路径。
8. **转换服装**：在 [Outfit Studio](bodyslide-outfit-studio.md) 里把衣服转换成 UBE 身形
   （或直接用作者已转好的 UBE 版衣服 + UBE patch plugin）。

> ⚠️ **补丁脚本只做两件事**：编辑盔甲记录、把原版 nif 复制到 UBE 路径
> （若该处还没有）。它**不**做转换——"You will still need to have proper
> UBE outfit conversions. No magic here."（作者原述）

### 安装顺序提醒

- UBE 与 3BA/BHUNP **可以安全共存**，安装顺序不冲突；
- UBE 的 `.esp` 补丁应覆盖被改动的盔甲记录，注意 MO2 中补丁 mod 的优先级。

## 使用与配置

### RaceMenu

- 用 UBE 种族建角色，滑块规模：脸 370+ / 身体 200+ / 生殖器 70+；
- **已知问题**：RaceMenu 滑块有时会出现故障——作者归因于 RaceMenu 内部不完善，
  非 UBE 自身 bug（作者原述）。
- 原版/HPH/CotR 预设**不能导入**（头部拓扑、UV、morph 都不同），只能手工重捏。

### Normals recalc（SE 版特有坑）

> SE 版自带从 AE 反向移植的 `skee64.dll`（带法线更新功能），
> 但**改体重时法线不会自动更新**——用 **"Normals recalc"** 滑块
> （或拖任意其他身体滑块）手动刷新。

### OBody / 预设分配

社区常见的 UBE 分发形态是 **UBE Bodyslides + 预构建 zero-slider 网格 +
UBE patch plugin**，配合 [OBody NG](../05-distribution/obody-ng.md) 使用
（见 Zerofrost's Red Hood Armor - UBE 等转换页，社区经验）。

## 兼容与冲突

### 可以并存

| 组合 | 结论 |
|---|---|
| UBE + 3BA | ✅ 可并存安装，无冲突；UBE 只取 3BA 的 SMP/CBPC 配置 |
| UBE + BHUNP | ✅ 可并存安装，无冲突 |
| UBE + CoTR 化妆品/战彩 | ✅ 兼容（作者标注） |

### 不兼容清单

| 关系 | 结论 |
|---|---|
| 3BA / BHUNP 的**服装转换** | ❌ 不兼容，需 UBE 专用转换 |
| CBBE / UNP **皮肤纹理与覆盖层** | ❌ 不兼容（UBE 的 UV 与任何现存身体 mod 不同） |
| 原版 / HPH / CotR **预设** | ❌ 不兼容（头部拓扑、UV、morph 都不同；且法线贴图类型不同，导了也变形） |
| 独特玩家 mod（unique player mods） | ❌ 不兼容（UBE 本身基本就是一个独特玩家 mod） |
| Head Parts 白名单 mod | ❌ 不兼容 |
| Community Shaders | ⚠️ 存在不兼容（静态立方体贴图选项在 CS 下不生效）；作者明确表示不负责修复 |

### 与"三套并行"的局面

社区里容易听到"UBE 取代了 3BA"。**取证不支持这个说法。**

实际观察到的现象是：新出的盔甲/衣服 mod 会**同时提供三套 BodySlide 文件**：

```
Additional Bodyslide files for 3BA, HIMBO and UBE
```

且发布页把三者都列为**可选前置（OPTIONAL）**，互相不覆盖
（一手证据：Iron Rose Armor 发布页，Nexus SE 143045）：

| 身形 | 性别侧 | 性质 |
|---|---|---|
| CBBE 3BA (3BBB) | 女性 | 当前主流，带物理 |
| HIMBO | 男性 | 当前主流（见 [himbo.md](himbo.md)） |
| UBE 2.0 | 女性 | 新世代 base，逐步被新 mod 支持 |

**推论**：选型按"我要给哪个身形穿这套甲"来挑，**不要为了追新把 3BA 换掉**；
三套文件的存在恰恰说明作者们不做取舍。裸体网格只能有一个赢家
（覆盖规则见 [mo2-override-rules.md](../07-workflow/mo2-override-rules.md)）。

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 新衣服 UBE 角色穿不上/模型不对 | 没跑 xEdit 补丁，ArmorAddon 还指向原版路径 | 重跑 UBE xEdit 补丁脚本；确认走 `meshes\!UBE\` |
| 首饰也出问题 | 首饰同样需要 ArmorAddon 补丁（HeadParts 除外） | 补丁脚本全量重跑 |
| 皮肤贴上错位/不能用 | CBBE/UNP 皮肤 UV 不同 | 换 UBE 专用皮肤（Diamond/Freyna/Jada 等） |
| 导不进的预设 | 原版/HPH/CotR 预设拓扑不同 | 只能手工重捏；别强行导入 |
| 改了体重光照/法线怪异 | SE 版体重变化不自动更新法线 | 拖 "Normals recalc" 滑块 |
| 物理不抖 | 缺 3BA 物理配置 / CBPC / FSMP | 装 "CBBE 3BA Physics Config Reinstaller"；查 [physics-not-working.md](../06-troubleshooting/physics-not-working.md) |
| RaceMenu 滑块故障 | 作者归因 RaceMenu 内部问题 | 重开菜单/换 RaceMenu 版本；UBE Discord 反馈 |
| 帧数下降明显 | UBE 性能偏重（相对） | 只给玩家用 UBE，NPC 仍走 3BA/BHUNP |

## 取舍与建议

**选 UBE 当你**：

- 你要最高网格精度与最大滑块自由度，且愿意接受调成本；
- 你主要玩**玩家角色**（NPC 仍可用 3BA/BHUNP，两者并存）；
- 你能接受"每件新衣服都要补丁+转换"的日常维护。

**不选当你**：

- 你的皮肤/预设/衣服资产都在 CBBE 或 UNP 系；
- 你想要即插即用——作者自己都说不是 plug-n-play；
- 你主要依赖 NPC 美化整合包（那些几乎都是 3BA/BHUNP 基底）。

**务实路线**：3BA/BHUNP 做基底 + UBE 只给玩家角色用，是社区已验证的并存模式；
衣服按需各转各的版本。

**版本敏感性**：UBE 迭代快（2023 首发、2025-2026 持续更新），
当前版本号与 Nexus 上传日期**未确认**；依赖它的转换 mod 通常写死
需求名 **"UBE 2.0 -- Ultimate Body Enhancer 2.0"**，装前核对 Nexus 页。

## 来源

- **一手（作者帖）**：新种族性质、6 万+顶点、滑块规模（370+/200+/70+、16 个精灵耳滑块）、
  不用模型空间法线、独立服装路径、**每件盔甲都需 ArmorAddon 连首饰也要**、
  **xEdit 脚本一键补丁 + 补丁后走 `meshes\!UBE\`**、补丁器只改记录/复制 nif、
  **SE 版自带 AE 反向移植的 skee64.dll + "Normals recalc" 滑块**、
  SOS 脚本改 slot 53、性能偏重、与 CoTR 化妆品兼容、独特玩家/HeadParts 白名单/CS 不兼容、
  RaceMenu 滑块已知问题、"it's not a perfect plug-n-play mod" 原话、
  前置（RaceCompability；3BA 只取 SMP/CBCP 配置，缺则装 "CBBE 3BA Physics Config Reinstaller"；
  CBPC/FSMP/RaceMenu/XPMSSE）：
  LoversLab 官方发布帖（JohnyBungalow1，2023-04-20）
  `https://www.loverslab.com/topic/209371-skyrim-special-edition-male-dick-mod`
- **一手（Nexus 需求名与作者 credits）**："UBE 2.0 -- Ultimate Body Enhancer 2.0" 正式名、
  作者 JohnyBungalow1 与 lowresoutis：Nexus 92989 及多个依赖页
  （More Shields - UBE 174590、Zerofrost's Red Hood Armor - UBE 172883、
  UBE 2.0 RU/ES 翻译页 171450/186036、Elsa UBE Preset 115200）—— **一手（依赖页交叉一致）**
  `https://www.nexusmods.com/skyrimspecialedition/mods/92989`
- **一手（三套并行）**：`Additional Bodyslide files for 3BA, HIMBO and UBE`
  且三者均为 OPTIONAL：Iron Rose Armor 发布页 —— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/143045`
  （注意：该页是 Iron Rose Armor，**不是 UBE 本体**；早期版本的本条目曾误将其当作 UBE 源，已更正）
- **一手（标签体系）**：Nexus 存在 `UBE Bodybase` 标签，与 `CBBE Bodybase` /
  `UNP Bodybase` / `TBD Bodybase` 并列 —— **一手**
- **社区经验**：UBE Bodyslides + 预构建 zero-slider 网格 + UBE patch plugin
  配合 OBody NG 的分发模式：Nexus 转换页与整合包 BodySlide 说明
- **未确认**：UBE 2.0 当前版本号（Nexus 页在墙后；翻译页 U.0.7 为翻译版本）、
  Nexus 上传具体日期、许可证条款
