---
id: unreliable-and-unconfirmed
title: 不可信来源与未确认事项
category: 08-sources
kind: reference
version: 3.0.0
updated: 2026-10-25
tags: [来源, 辨析, 不可信, 未确认, 内容农场, 1.7]
aliases: [不可信来源, csdn, 假信息, 别信, ai 生成, csdn 能信吗, 错误知识, 讹传, 未确认事项, 这个说法对不对, 网传, 勘误]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: 别人来查"这个说法对不对"时唯一该看的一页：不做事实来源的站点类型与三条判据、本领域已知错误知识清单（讹传勘误）、以及本轮扩写汇总的全部未确认事项。
---

# 不可信来源与未确认事项

> **这一页的定位**：有人（包括 agent）拿着一个"网上都说"的说法来问对不对时，
> **先来这里**——第二节是已核实的讹传勘误，第三节是未确认事项。
> 两头都没有的，按第一节的判据自己去核，核完回来更新本页。
> 反过来的"哪些来源可信、去哪核版本"见 [primary-sources.md](primary-sources.md)。

## 速览

| 项 | 内容 |
|---|---|
| 作用 | 黑名单 + 判据 + 讹传勘误 + 未确认事项，一本查完 |
| 三节结构 | 一、不可信的站点类型 / 二、已知错误知识 / 三、未确认事项 |
| 判据 | 有版本号？有文件路径？有指向发版者的链接？ |
| 维护规则 | 新讹传或已确认项**只更新本页**（递增 version），不在别处另写一套说法 |
| 可信来源 | 反过来在 [primary-sources.md](primary-sources.md) |

要点：

- **CSDN / toolify / AI 聚合站 / 内容农场一律不作事实来源**，写得多漂亮都不用。
- **"未确认"不是"不存在"**：它只是还没找到可靠出处，条目里禁止当现状陈述。
- 版本号是最容易被搬运改新的字段——**二手版本号默认降级**。
- 作者名会被"就近联想"（KouLeifoh → Kalilies 是真实案例）。
- 依赖清单会被加上其实不需要的前置（PapyrusUtil → RaceMenu 是真实案例）。

## 一、不做事实来源的站点类型

本工作区有一条硬纪律：**不用 CSDN、toolify、AI 聚合站、内容农场**。

### 已识别并排除的域名（部分）

```
tsight.io        "深度解析"类文章，结构工整但无可核验的版本号/路径
gifpow.com       "2026 完整指南"，含夸张断言（"全光追"式表述）
2023game.com     "梦里 / Dreamlike 整合包" 等无实证内容
maoxu.com / bajiujiu.com / 233leyuan.com
jingyan.baidu.com
部分门户的转载号（搜狐等，常见"整合包十大排行"式文章）
```

### 内容农场的四种典型模式

1. **三无**：无版本号、无文件路径、无发版者链接——结构再工整也是空的；
2. **夸张断言**："全光追""16K 视差""一键搞定"这类超出引擎常识的表述；
3. **聚合排行**："十大整合包""2026 完整指南"式标题，内容是多站拼贴；
4. **AI 生成痕迹**：条目齐全但每条都浅、术语混用、把不同 mod 的功能张冠李戴。

### 判据（三条，很好用）

1. **有没有版本号？** 真文档会说"BodySlide 5.8.2""SKSE 2.2.6"。
2. **有没有文件路径？** 真文档会说 `Data\SKSE\Plugins\CharGen\Presets\`。
3. **有没有指向发版者的链接？** 真文档会链到 Nexus mod ID 或 GitHub 仓库。

三条都答不上来的，**无论写得多漂亮都不用**。

## 二、本领域已知的"错误知识"清单

以下说法在本库调研中被判定为**错误或被误传**，请勿采信：

| 说法 | 实际情况 |
|---|---|
| **RaceMenu 需要 PapyrusUtil** | **不需要**。RaceMenu 只要求 SKSE64，`skee64.dll` 自带 NiOverride 与 CharGen |
| **RaceMenu 的 morph 滑块范围是 -1 到 +1** | **不准确**。`.jslot` 里存的是浮点（实测样例 `0.50000`）；滑块上限由 `RaceMenuMorphs*.psc` 的 `OnSliderRequest` 中 `Float factor` 决定（社区记录默认 `2.0`）。**以实际界面为准** |
| **BodySlide 预设可以直接当 RaceMenu 预设用** | **不能**。`.xml`（0~100，每个滑块存体重 0 与 100 两个值）与 `.jslot`（浮点 `bodyMorphs`）格式、刻度、生效方式都不同，只能逐滑块手工换算 |
| **手动拖 RaceMenu 滑块能改变 NPC 身材** | **不能**。运行时 morph 只作用于玩家。NPC 要靠 BodyGen / OBody NG / AutoBody 分配，或给单个 NPC 做专属裸体网格 |
| **BodySlide CLI 有 `-o` / `-m` 参数** | **不存在**。现行参数是 `--groupbuild` / `--build` / `--filter` / `--targetdir` / `--preset` / `--trimorphs` 等 |
| **HPH 的作者是 Kalilies** | **不是**。是 **KouLeifoh（KLF）** |
| **`modding.wiki` 是 STEP 的 Skyrim SE 指南** | **不是**，该域名相关页面 404；STEP 官方 wiki 是 `stepmodifications.org` |
| **HDT-SMP 的仓库是 `hydrogensaysHDT/hdt-skyrim-smp`** | **错**，实测 404；正确是 **`hdt-skyrimse-mods`** |
| **Skyrim Outfit System 是"给 NPC 分配身形"的工具** | **不是**。它是外观/换装系统。分配身形的是 **BodyGen / OBody NG / AutoBody** |
| **SPID 的 Outfit Distribution 能分配身形** | **不能**，它分配的是**服装** |
| **The Eyes of Beauty SE 的版本是 10.x** | **10.x 是 LE 的版本号体系**；SE 官方移植是 **1.2** |
| **CBPC 可以做头发/衣服物理** | **不能**。头发与衣物必须用 HDT-SMP / FSMP |
| **"九大猫 / 醉梦 / 陶德"是整合包** | 检索后**均未确认存在**（详见 [`../07-workflow/chinese-modpacks.md`](../07-workflow/chinese-modpacks.md)） |
| **1.6.1130 对应 SKSE64 2.2.6** | **错**。PapyrusUtil 官方 changelog 明写 4.5 = "SKSE64 **2.2.4** & Skyrim **1.6.1130**"，2.2.6 对应的是 **1.6.1170**（4.6）。**本库旧版对照表曾误写，2026-09-30 已修正** |
| **1.6.640 对应 SKSE64 2.2.2** | **错**，应为 **2.2.3**。**本库旧版对照表曾误写，2026-09-30 已修正** |
| **"1.6.1170 是当前 AE 版本"** | **已过时**。2026-08 起 Bethesda 发布 1.7.x，当前 Steam AE 为 **1.7.104（SKSE 2.3.1）**；1.6.1170 退为"上一代稳定版"。但**捏脸生态仍建议留在 1.6.1170** |
| **"UBE 取代了 3BA"** | **未获证据支持**。新 mod 是同时发 3BA / HIMBO / UBE 三套文件，见 [`../03-body/ube.md`](../03-body/ube.md) |
| **CBBE 一开始就叫 Beautiful Bodies** | **原名是 Caliente's Big Bottom Edition**（因初始比例夸张得名），后改名 **Beautiful Bodies**（一手：作者访谈，Nexus 官方新闻转载，原载 skyrimromance.com） |
| **"UNP 就是一具身体"** | **是一条谱系**：**Dimonized UNP**（dimon99）→ **UUNP**（统一变体 + BodySlide 可构建）→ SE 时代 **Legacy UUNP**（Nexus 43773）与 **UNP Female Body Renewal**（Nexus 1699，不支持 BodySlide）→ **BHUNP**（Nexus 31126）。UNP / UNPB / UUNP / BHUNP 共用原版 UV，与 CBBE 不通用 |
| **"HDT-SMP 与 HDT-PE 是并存的两代，任选其一"** | **不是并存**。HDT-SMP 是 **HDT-PE（HDT Physics Extensions）的继任者**：PE 用游戏内建 Havok 逐骨方案，SMP 用 Bullet + 蒙皮网格逐顶点，才能做头发与身体/地面碰撞 |
| **"CBPC 是从零写的独立物理引擎"** | **不是**。它**基于 polygonhell 的 CBP Physics**（作者原话致谢 polygonhell，"which allowed me to create this mod"；该源码以 MIT 释出） |
| **"BodySlide 和 Outfit Studio 是两个不同的 mod"** | **同一项目**（`ousnius/BodySlide-and-Outfit-Studio`）；2018-02 起才拆成两个 exe、配置文件分开 |
| **"MCM Helper 是 SkyUI 自带的功能"** | **不是**。SkyUI 提供 MCM 框架本身，MCM Helper（作者 Parapets，MIT）是让作者用 JSON 定义菜单的第三方框架 |
| **"po3 Papyrus Extender 就是 powerofthree's Tweaks"** | **不是**。同作者的不同 mod：Tweaks 管引擎修复与调整，Extender 补 Papyrus 原生函数 |
| **"EFM 的表情 morph 对 NPC 也生效"** | **只影响玩家**（作者明示）。NPC 的脸是预生成网格，不实时生成 |
| **"OBody NG 是 OBody 原版作者的后续版本"** | **不是同一作者**。原版作者 **Sairion350**（OStim 生态），OBody NG 作者 **Aietos**（credits 中 Sairion350 列为"原版"） |
| **"SKSE 需要 Address Library 才能运行"** | **不需要**。SKSE 本身**不使用** Address Library（skse.silverlock.org 明示）；Address Library 是给第三方 DLL 插件查地址用的 |
| **"UBE 2.0 是又一具身体替换器"** | **不是**。它是**新增独立种族**（自带身体/头部网格与纹理），可与 3BA / BHUNP 并存安装无冲突，但服装转换与 CBBE / UNP 皮肤纹理不通用，见 [`../03-body/ube.md`](../03-body/ube.md) |

> 本表是"尸检报告"：每条都已在对应条目写透机制。新增条目时若发现新的讹传，
> **加进本表**（递增本页 `version`），不要在正文里悄悄写一个不同的说法。

## 三、⭐ 未确认事项清单（明确标注，勿当现状）

以下各项在本轮扩写中**未能取得可靠来源**，各条目正文已相应标注，按主题分组。
**带 ✅ 的小节是扩写过程中已核实、从旧版未确认清单"毕业"的项。**

### 3.1 版本号类（当前最新版本未能直读/核实）

| 事项 | 状态 |
|---|---|
| **CBBE SE 当前最新版本** | 二手来源给出 1.6.1 与 1.6.2，**不一致**；Nexus 页在内容墙后 |
| **CBBE 3BA 当前最新版本** | 仅确认到 2.45 左右；存在 3BAv2 迭代；Nexus 上传日期**未确认** |
| **BHUNP SE 当前最新版本 / 维护状态** | **未确认**（LE 官方文件可见 1.41V） |
| **UBE 2.0 当前版本号与 Nexus 上传日期** | **未确认**（墙后；翻译页 U.0.7 为翻译版本号，非本体版本） |
| **HIMBO 当前版本号** | **未确认**（社区可见 5.8 / 2025-09；2026 年第三方仍有转载更新） |
| **CBPC v1.6.1 之后是否有新版** | **未确认**（v1.6.1 为社区可确认的最新版） |
| **XPMSSE v5.06（2024-02-11）之后是否有更新 / 是否停更** | **未确认**（Nexus Files 页本轮未能直读） |
| **XPMSSE v5.06 changelog 细节** | 来自镜像站转述，**非 Nexus 原文** |
| **SkyUI 当前最新版本号** | **未确认**（社区长期主流 5.2 SE，本库未逐版核实） |
| **po3 Papyrus Extender 函数/事件数当前精确值** | **未确认**（发布页口径 374+ 函数、37 事件，数字随版本增长，以发布页为准） |
| **OBody NG 当前 Files 页确切版本号** | **未确认**（社区文档引 4.4.3；仓库提交提及 5.0） |
| **AutoBody Nexus 61321 当前版本号** | **未确认** |
| **Wabbajack 确切首发日期与最新版本号** | **未确认**（GitHub 早期历史未逐条核实，以 Releases 页为准） |
| **BodySlide GitHub Releases 当前版本号** | **未确认**（SE 页 201 当前 5.9.1 / 2026-10-04 已确认；以 Releases 与 SE 页为准） |

### 3.2 日期类（首发/更新的精确日期）

| 事项 | 状态 |
|---|---|
| **OBody 原版（Nexus SE 51084）确切首发日期** | **未确认** |
| **CBBE LE 初版具体首发月份** | **未确认**（作者访谈只给出 2011-12-04 是"第一个配套服装 mod"） |
| **HIMBO Nexus 精确首发日** | **未确认**（社区证据：LoversLab 2021-02-28 帖宣布"刚发布到 Nexus"） |
| **EFA 男版（SE 19532）首发与最后更新日期** | **未确认** |
| **EFM SE 35785 页面精确 original upload / last updated** | **未确认**（本轮抓取被 Cloudflare 拦截；归档文件名时间戳换算 ≈ 2020-07-19） |
| **RaceMenu 0.4.9 ~ 0.4.19.11 各版本上传日期** | **未确认**（changelog 有内容但 Nexus 未给日期） |
| **HDT-PE（Nexus LE 53996）首发日期；BBP/TBBP 流行具体年份** | **未确认**（Nexus LE 旧页日期未能核实） |
| **BodySlide LE 时代首发具体日期** | **未确认** |
| **HPH 发布时间、1.0→1.4 各版本日期、1.4 之后是否有更新** | **未确认** |
| **ECE 首发日期与末版版本号** | **未确认**（末版社区可见 1.3 / 1.4 / 1.5 多种口径） |
| **整合包"污神 / 无心"的首发年份与作者** | **未确认**（来源缺失，见 [`../07-workflow/chinese-modpacks.md`](../07-workflow/chinese-modpacks.md)） |
| **STEP 指南具体创立年份与维护团队现状** | **未确认** |
| **GamerPoets 各教程视频的更新年份** | **未确认**（未逐一核对） |
| **MO1 确切首发日期、NMM EOL 公告原文与确切日期** | **未确认** |

### 3.3 归属与关系类

| 事项 | 状态 |
|---|---|
| **HPH 作者归属的早期细节**（"作者是 SAM Light 的作者"仅见 2019-12 社区搬运帖） | **未确认**，仅社区标注 |
| **"Vector Plexus 原域名失效"** | **社区传言，未确认**；稳妥来源是 Wabbajack 白名单 GD |
| **HPH 头部网格顶点数** | **未确认** |
| ***High Poly Heads AND Hair for All Vanilla NPCs*** 等 HPH 补丁的 Nexus ID 与维护状态 | **未确认** |
| **Facelight Plus 的 Nexus 发布状态、作者（社区站标注 Freya）、版本** | **未确认**（仅见社区指南站） |
| **Better Lighting for Face Light / Facelight Plus 的 Nexus ID** | **未确认** |
| **AutoBody 与 OBody NG 的先后/取代关系** | **社区说法不一致，未确认** |
| **OBody NG 5.x 是否仍硬性依赖 RaceMenu** | **未确认**（1.7.x 已支持而 RaceMenu 无 1.7.x 版，逻辑上应有变化；以 Nexus Requirements 为准） |
| **AutoBody 仓库迁至 RocketBun-OG 后的维护状态** | **未确认**：与 napmouse 的关系（账号变更或转移）、2022-09 之后是否有其他维护渠道 |
| **UBE 是否取代 3BA** | **未确认，且现有证据倾向"否"**（新 mod 同时发 3BA / HIMBO / UBE 三套文件） |
| **BnP 系列作者署名；Mature / Leyenda / Diamond / The Pure 等皮肤的 Nexus ID** | **未确认** |
| **各类头发资源（HG Hairdos、VHR、Hallgarth's 等）的 Nexus ID 与作者** | **未确认** |
| **LM's Dual Brows - HPH - Standalone（LeelooMinai）的 SE Nexus ID** | **未确认** |

### 3.4 1.7.x 适配状态类

| 事项 | 状态 |
|---|---|
| **FSMP 对 1.7.x 的支持状态** | **未确认**（本轮未见任何 1.7.x 档位信息；多份插件页反而直接写 "Not supported: 1.7.x"） |
| **FSMP 4.1.1（2026-08-27）面向的确切游戏版本** | **未确认**（Files 页日期一手；仓库 2026-08-23 有面向 1.7.99 的 commit；社区报告互相矛盾） |
| **CBPC 对 1.7.104 的兼容性** | **未确认**（有中文媒体报道称已兼容，但该来源不可信，本库不予采信） |
| **CBBE 在 1.7.x 下的兼容性** | **未确认** |
| **BodySlide 对 1.7.x 的兼容性** | **未确认** |
| **RaceMenu Patreon beta（"RaceMenu AE NG"）的可用性与发布状态** | **未确认**（非官方途径；Nexus 讨论区用户整理，强调装前必须删 8 个 overlay nif） |
| **modding.wiki 插件适配状态表的具体内容** | **未确认**（SKSE 置顶帖推荐该站为查询入口——一手；但本库未逐项核实其内容） |
| **"多数 Skyrim 整合包锁 1.6.1170"** | **本库基于 RaceMenu 1.7.x 现状的推断**；具体列表的版本要求以其 README 为准 |

### 3.5 文件、字段与机制类

| 事项 | 状态 |
|---|---|
| **RaceMenu morph 滑块的精确上下限** | 社区记录由 `OnSliderRequest` 的 `factor` 决定（默认 2.0），但该讨论针对 `RaceMenuMorphsUUNP.psc`，**未在 CBBE 版脚本上确认** |
| **「拖 morph 只对玩家与 EFF 随从直接生效」** | **未找到来源支持**。可确认的只有"只影响玩家"；给单个 NPC 固定身材的途径是"构建专属裸体网格 + ArmorAddon + 设为裸体皮肤"（社区经验） |
| **`skee64.ini` 与 `skee.ini` 的命名差异** | **未确认**（changelog 两种写法都出现过） |
| **`parts.json` / `tags.json` 除作者示例外的完整字段定义** | **未确认** |
| **`.jslot` 的完整字段清单** | **未确认**（本库列出的是多份实际文件与社区讨论中复现的字段） |
| **SKSE co-save 中 RaceMenu 运行时数据的具体格式** | **未确认** |
| **BodyGen 首次发布的版本与日期；是否支持 EditorID 键** | **未确认** |
| **CharGen Extension "2.5 起内置核心 / 2.7+ 完全并入本体"的版本号区间** | **二手记载，未确认** |
| **`BodySlide.xml` / `OutfitStudio.xml` 的运行时存放位置** | **未确认** |
| **Actor 的 `GetNthHeadPart` / `SetNthHeadPart` 函数页** | 仅见于 CK wiki **示例**，未单独确认 |
| **FaceGen 技术最初来源（是否某个商业中间件）** | **未确认** |
| **MO2 各版本对 BSA 加载顺序的精确算法细节** | **未确认**（本库未逐行核对源码） |
| **Wabbajack 官方 wiki 是否有独立的 System Requirements 专页** | **未确认**（.NET / VC++ / 空间要求引自 Troubleshooting FAQ） |
| **"把 Face Part 拉到 3"的具体档位** | 官方未给编号，**未确认**（中文社区帖） |
| **KS Hairdos 发型数量** | 983 与 883 两种口径，统一表述为"约 980+" |
| **Brows（Aesthetic）版本** | 4.0.1 与 4.1.0 两种记录，**未确认唯一最新值** |
| **EFM 与 EFA 是否有 1.0 / 1.7 / 1.21 之后的更新计划** | **未确认** |
| **某些整合包给 HPH 打的 "EFM patch" 究竟改了什么、是否让 morph 真正生效** | **未确认** |
| **CK 官方站（creationkit.com）停机** | 骨骼系统条目因此缺少一手官方引文，**待补**（镜像缺 Skeleton / Havok 专页） |

### 3.6 ✅ 已核实毕业项（原未确认，现已确认）

| 原未确认项 | 核实结果 |
|---|---|
| ~~**RaceMenu 的 1.7.99 / CommonLibSSE-NG 版本是否已发布**~~ | ✅ **已核实（2026-09-30）**：**未发布**。1.7.99 版已完成但被 SKSE 的 Papyrus 函数 bug 卡住；1.7.104 未开始；CLSSE-NG 移植进行中。作者帖 2026-08-23 为一手依据 |
| ~~**"BHUNP" 的正式展开式**~~ | ✅ **已核实（2026-10-25）**：官方展开式为 **UUNP Next Generation**（Nexus 依赖页 Requirements 标题，一手）；"Baka Haeun UNP"（源自作者名）、"UNP Bearer" 等均为**社区读法** |
| ~~**UBE 2.0 的作者与 Nexus ID**~~ | ✅ **已核实（2026-10-25）**：作者 **JohnyBungalow1 与 lowresOutis**，Nexus **92989** |
| ~~**HIMBO 的 Nexus ID / 作者**~~ | ✅ **已核实（2026-10-25）**：作者 **Kreiste**（与 Novelyst），Nexus **46311**；**当前版本号仍未确认**（见 3.1） |

## 四、怎么用这一条

1. 拿到一个说法 → **先查第二节**（错误知识清单）。命中 → 直接按"实际情况"回答，并给出来源链接；
2. 没命中 → **查第三节**（未确认事项）。命中 → 明确回答"本库未确认"，**不要替它下结论**；
3. 都没命中 → 按第一节三条判据自己核：Nexus Files 页 → GitHub → 官方 wiki → 作者本人帖
   （顺序见 [primary-sources.md](primary-sources.md) 的"取舍与建议"）；
4. 核出来了 → **回来更新本页**（错误知识 or 未确认事项，递增 `version`），再改对应条目。

**为什么值得这么做**：这个领域**转述失真**特别严重——

- 版本号在搬运过程中会被"顺手改新"；
- 一个 mod 的依赖清单会被加上它其实不需要的前置；
- 作者名会被就近联想成另一个知名作者（如 KouLeifoh → Kalilies）。

> **踩过的坑不要踩第二遍。** 新增条目时如果发现本清单里的某一项可以确认了，
> 请**直接更新本条目**（提升 `version`），而不是在别处悄悄写一个不同的说法。

## 来源

- 第二节"实际情况"列各项依据，均已写在各对应条目的"来源"节 ——
  请沿条目内的引用逐条复核（入口见 [primary-sources.md](primary-sources.md)）
- 排除域名清单与"三条判据"：**本工作区检索过程中识别（2026-09-22）/ 总结的方法论**
- 第三节各未确认项的检索范围与日期：**本工作区本轮调研（2026-10-25）**
- "1.6.1130 → 2.2.4、1.6.640 → 2.2.3"两条勘误的原始依据：PapyrusUtil 官方 changelog
  与 SKSE64 官方 Changelog —— **一手**（见 [`../00-overview/version-matrix.md`](../00-overview/version-matrix.md)）
