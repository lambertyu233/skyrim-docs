---
id: primary-sources
title: 一手来源清单
category: 08-sources
kind: reference
version: 2.0.0
updated: 2026-10-25
tags: [来源, 一手, 清单, 出典]
aliases: [来源清单, 一手来源, sources, 出处, 官方来源, 哪些来源可信, 可信来源, 证据纪律, primary sources, 怎么核实版本, 版本去哪查, Nexus 发布页, changelog 在哪看, 作者原帖]
source: https://github.com/ousnius/BodySlide-and-Outfit-Studio
summary: 本资料库所有条目的出处总册：按"Nexus 发布页 / GitHub 仓库 / 官方 wiki / 作者本人说明 / 社区"五类列出全部一手来源，每条写明能回答什么问题、判据是什么，是复核与更新本库的第一入口。
---

# 一手来源清单

> **这一页是全库的"证据总册"**：任何条目里的结论，都应该能沿这里的链接回到原始出处。
> 查"某个说法对不对"去[不可信来源与未确认事项](unreliable-and-unconfirmed.md)，
> 查"这个结论从哪来"来这里。

## 速览

| 项 | 内容 |
|---|---|
| 作用 | 汇总本库全部条目的**可信出处**，并说明每个来源能回答什么 |
| 分级 | **一手**（发版者本人材料）· **社区经验** · **未确认** · **本工作区实测** |
| 五类来源 | A. Nexus 发布页 · B. GitHub 仓库 · C. 官方 wiki · D. 作者本人说明 · E. 社区 |
| 核心判据 | 有版本号？有文件路径？有指向发版者的链接？三条都答不上来就不用 |
| 维护规则 | 上游更新时**先改本页的来源状态**，再同步到具体条目 |

要点：

- **Nexus 发布页 + Files 页 changelog 是第一权威**：作者、当前版本、前置、权限条款都以它为准。
- **GitHub 仓库管"机制与许可证"**：源码、README、提交记录、LICENSE 是一手中的一手。
- **官方 wiki（SKSE 站 / UESP / ck.uesp.net）管"引擎与文件格式"**，不含任何 mod 的版本信息。
- **作者本人帖（Nexus Posts / Patreon / 博客）管"动机、计划与取舍"**，比发布页更细但更零散。
- **社区只作旁证**：引用时必须标"社区经验"，多帖一致时注明"多帖一致"。

## 它解决什么问题

这个领域的**转述失真**极其严重：版本号在搬运中被"顺手改新"，依赖清单被加上其实不需要的
前置，作者名被联想成另一个知名作者。因此本库要求**每条结论落到出处**，并把出处集中登记
在一处，达到三个目的：

1. **复核**：别人质疑某条结论时，沿链接回到原文，而不是靠记忆吵架；
2. **更新**：上游发新版时，知道该去哪个 URL 看变化，而不是重新全网搜；
3. **防再犯**：被内容农场骗过的域名与说法进黑名单，不再碰第二次
   （见 [unreliable-and-unconfirmed.md](unreliable-and-unconfirmed.md)）。

## 引用规范（本库怎么写出处）

| 层级 | 什么时候用 | 写法 |
|---|---|---|
| **一手** | Nexus 发布页描述 / Files 页 changelog、GitHub README/源码、官方 wiki、作者本人帖 | 直接采信，附 URL |
| **社区经验** | 论坛帖、reddit、指南站、他人 config | 标"社区经验"，多帖一致时注明 |
| **未确认** | 检索不到可靠出处 | **必须显式写"未确认"**，不当现状陈述 |
| **本工作区实测** | 本机实际访问/比对得出的结论 | 标"本工作区实测"并记日期 |

## 前世今生

这份清单的重心随生态演进发生过一次明显迁移：

| 时间 | 事件 | 意义 |
|---|---|---|
| 2011-2015 | Skyrim Nexus（LE）一家独大 | 发布页描述几乎是唯一权威 |
| 2016-2018 | SE 发布；BodySlide、HDT-SMP 等把源码放上 GitHub | "机制与许可证"有了独立于 Nexus 的权威 |
| 2018-08 | RaceMenu SE 页（19080）建立（一手：Nexus 文件信息） | 本库核心条目的一手源定型 |
| 2020-02 | Address Library 发布（meh321） | Files 页**文件名自带面向版本**成为核对手艺 |
| 2026-08 | Bethesda 发布 1.7.x | Files 页 changelog 成为"谁支持 1.7.x"的正面战场 |
| 2026-10 | 本轮扩写 | 逐条补全"每个来源能回答什么" |

## A. Nexus 发布页（描述正文与 Files 页）

**能回答什么**：作者与维护者、当前版本与最后更新日期、完整 changelog、官方前置与依赖、
权限/许可证条款、FOMOD 选项说明、作者自述的动机与警告。

**判据**：**看描述正文拿定位与依赖，看 Files 页拿版本与要求。** 作者通常把
"REQUIRES SKSE64 … and Game Version …" 写在**文件说明**里，而论坛帖里混杂着别人的
二手经验——**遇到版本问题，先看 Files 页而不是 Posts 页**
（本库 [version-matrix.md](../00-overview/version-matrix.md) 的"去哪里核"一节即此法）。

| 主题 | URL |
|---|---|
| RaceMenu（SE） | `https://www.nexusmods.com/skyrimspecialedition/mods/19080` |
| RaceMenu（LE） | `https://www.nexusmods.com/skyrim/mods/29624` |
| CBBE（SE） | `https://www.nexusmods.com/skyrimspecialedition/mods/198` |
| CBBE 3BA | `https://www.nexusmods.com/skyrimspecialedition/mods/30174` |
| BHUNP（SE） | `https://www.nexusmods.com/skyrimspecialedition/mods/31126`（LE：`mods/100306`） |
| Legacy UUNP | `https://www.nexusmods.com/skyrimspecialedition/mods/43773` |
| UNP Female Body Renewal | `https://www.nexusmods.com/skyrimspecialedition/mods/1699` |
| HIMBO | `https://www.nexusmods.com/skyrimspecialedition/mods/46311` |
| UBE 2.0 | `https://www.nexusmods.com/skyrimspecialedition/mods/92989` |
| BodySlide and Outfit Studio（SE） | `https://www.nexusmods.com/skyrimspecialedition/mods/201` |
| XP32 Maximum Skeleton Special Extended | `https://www.nexusmods.com/skyrimspecialedition/mods/1988` |
| HDT-SMP | `https://www.nexusmods.com/skyrimspecialedition/mods/30872` |
| HDT-PE（LE） | `https://www.nexusmods.com/skyrim/mods/53996` |
| Faster HDT-SMP | `https://www.nexusmods.com/skyrimspecialedition/mods/57339` |
| CBPC | `https://www.nexusmods.com/skyrimspecialedition/mods/21224` |
| Face Discoloration Fix | `https://www.nexusmods.com/skyrimspecialedition/mods/42441` |
| EFM / EFA-M / EFA-F | `mods/35785` / `mods/19532` / `mods/19181` |
| The Eyes of Beauty SSE | `https://www.nexusmods.com/skyrimspecialedition/mods/16185` |
| Brows / Beards | `https://www.nexusmods.com/skyrimspecialedition/mods/1062` / `mods/1067` |
| KS Hairdos SSE | `https://www.nexusmods.com/skyrimspecialedition/mods/6817` |
| ApachiiSkyHair SSE | `https://www.nexusmods.com/skyrimspecialedition/mods/2014` |
| Face Light | `https://www.nexusmods.com/skyrimspecialedition/mods/5965` |
| OBody NG | `https://www.nexusmods.com/skyrimspecialedition/mods/77016` |
| OBody（原版） | `https://www.nexusmods.com/skyrimspecialedition/mods/51084` |
| AutoBody | `https://www.nexusmods.com/skyrimspecialedition/mods/61321` |
| SKSE64 | `https://www.nexusmods.com/skyrimspecialedition/mods/30379` |
| Address Library | `https://www.nexusmods.com/skyrimspecialedition/mods/32444` |
| PapyrusUtil SE | `https://www.nexusmods.com/skyrimspecialedition/mods/13048` |
| JContainers SE | `https://www.nexusmods.com/skyrimspecialedition/mods/16495` |
| MCM Helper | `https://www.nexusmods.com/skyrimspecialedition/mods/53000` |
| po3's Papyrus Extender | `https://www.nexusmods.com/skyrimspecialedition/mods/22854` |
| SkyUI | `https://www.nexusmods.com/skyrimspecialedition/mods/12604` |
| UIExtensions | `https://www.nexusmods.com/skyrimspecialedition/mods/17561` |
| Fair Skin Complexion | `https://www.nexusmods.com/skyrimspecialedition/mods/798` |

> ⚠️ 部分 Nexus 页（尤其 CBBE / 3BA / BHUNP / HIMBO / CBPC / UBE）在**成人内容墙**后，
> 抓取受限。本资料库对这些条目标注了"经转述 / 经转载"，并以多个转载页交叉验证。

### 重点发布页：各自能拿到什么

| 来源 | 能拿到什么 | 判据与注意 |
|---|---|---|
| **RaceMenu 19080 + Files changelog** | 作者 expired6978；credits（ECE Team：tktk / RAN46 / kaeper；ousnius；schlangster）；SE 首发 2018-08-06；当前 0.4.20.0（2026-04）；**前置只列 SKSE64**；0.4.13 起 `skee` 命令族；0.4.19.11 `bEnableEarlyRegistration`（原文 "use this for OBODY"）；0.4.19.13 支持 1.6.640 / GOG 1.6.659；0.4.19.16 支持 1.6.1170；0.4.20.0 部件标签 + GOG 1.6.1179（作者标 untested） | 主文件原文 "REQUIRES SKSE64 Anniversary Edition 2.2.6 or greater and Game Version 1.6.1170"；VR 是独立文件 0.4.14；详见 [racemenu.md](../02-face/racemenu.md) |
| **CBBE 198** | 作者栏 "Ousnius - Caliente - Jeir"；顶点数、UV 自成一族、需 BodySlide 构建；**原名 Caliente's Big Bottom Edition → 改名 Beautiful Bodies**（作者访谈） | 墙后；访谈为 Nexus 官方新闻转载（原载 skyrimromance.com），标"一手（转载）" |
| **CBBE 3BA 30174** | 3BBB / 3BA 定位；前置链（含 CBPC 1.5.1+、"CBPC only" 档位）；游戏内 SMP / CBPC 切换 | 墙后；描述经 3DMGAME 转载，见 [cbbe-3ba.md](../03-body/cbbe-3ba.md) |
| **BHUNP 31126** | 作者 Bakafactory / BakaHaeun；官方全称 "BHUNP (UUNP Next Generation) SSE"（见多个依赖页 Requirements）；硬依赖（BodySlide / CBPC / HDT-SMP / SKSE64 / XPMSSE 4.67+）；LE 官方文件页可见 1.41V | 墙后；LE 官方文件页在 LoversLab 可直读，见 [unp-bhunp.md](../03-body/unp-bhunp.md) |
| **HIMBO 46311** | 作者 Kreiste（与 Novelyst）；权限栏 CC-BY-SA-4.0（允许上 Bethesda.net 但不改名字）；滑块清单；前置列表 | 墙后；描述经转载，权限栏经 Bethesda.net 移植页转引，见 [himbo.md](../03-body/himbo.md) |
| **UBE 2.0 92989** | 作者 JohnyBungalow1 与 lowresOutis；**新增独立种族**而非身体替换器；前置（RaceCompability 等） | 墙后；作者一手说明在 LoversLab 官方发布帖，见 [ube.md](../03-body/ube.md) |
| **HDT-SMP 30872** | 作者 hydrogensaysHDT；MIT；现为社区修复合并 fork（credits：ousnius 修复与更新）；SMP = Skinned Mesh Physics、Bullet；addon 列表（`CBBE SMP (3BBB)` / `CBBE 3BBB (3BA)` / `BHUNP SE`） | 仓库名是 `hdt-skyrimse-mods`；`hdt-skyrim-smp` 实测 404，见 [hdt-smp.md](../04-physics/hdt-smp.md) |
| **XPMSSE 1988** | Team XPMSE；v5.06（2024-02-11）；FOMOD 首屏选 Physics Extensions 其余 None；"不要删除 `skeleton_female.hkx`" 警告 | changelog 经镜像转载；v5.06 后是否停更**未确认**，见 [xpmse-skeleton.md](../04-physics/xpmse-skeleton.md) |
| **CBPC 21224** | 作者 Shizof；基于 polygonhell 的 CBP Physics（MIT）；"not Pre-Calculated or Fake Physics…uses spheres instead of vertices"；v1.6.1；FOMOD SSE / VR 分档 | 墙后；v1.6.1 描述经镜像转载，见 [cbpc.md](../04-physics/cbpc.md) |
| **SKSE64 30379 + Address Library 32444** | SKSE 各档版本对应（changelog 逐条 "support for X"）；Address Library v13 = "All in One (1.7.104.0)"（2026-08-27） | 版本核对的正面战场，见 [version-matrix.md](../00-overview/version-matrix.md) |

## B. GitHub 仓库（源码与 README）

**能回答什么**：机制实现、许可证、依赖链、提交历史（可精确回答"某功能哪一年加的"）、
fork 链、构建方式、作者自述的已知问题。

**判据**：README 管定位与依赖；**LICENSE 文件是许可证的唯一权威**（Nexus 权限栏可能滞后）；
提交记录管"何时变的"。

| 项目 | 仓库 |
|---|---|
| RaceMenu / skee64 | `https://github.com/expired6978/SKSE64Plugins` |
| BodySlide and Outfit Studio | `https://github.com/ousnius/BodySlide-and-Outfit-Studio` |
| HDT-SMP（原始） | `https://github.com/HydrogensaysHDT/hdt-skyrimse-mods` |
| Faster HDT-SMP | `https://github.com/DaymareOn/hdtSMP64` |
| OBody NG / OBody | `https://github.com/Aietos/OBody-NG`、`https://github.com/Aietos/OBody` |
| AutoBody | `https://github.com/napmouse/autoBodyAE` |
| Face Discoloration Fix | `https://github.com/Exit-9B/Face-Discoloration-Fix` |
| Wabbajack | `https://github.com/halgari/wabbajack` |

各仓库能拿到什么：

- **`expired6978/SKSE64Plugins`（skee64）**：`skee64.dll` 源码——**NiOverride 与 CharGen
  两个模块都在里面**（这是"RaceMenu 不依赖 PapyrusUtil"的根源）；`skee` 控制台命令族、
  `skee64.ini` 字段（`bEnableBodyMorph` / `bEnableEarlyRegistration` 等）的实现出处。
- **`ousnius/BodySlide-and-Outfit-Studio`**：作者与致谢（**jonwd7** 的 NIF 帮助、
  **degenerated1123** 的 shader 帮助、**NifTools** 团队）、**GPL-3.0**、**2,040+ 提交**
  且 2026 年仍活跃（Starfield cloth、CS/ENB Complex Material、BSA/BA2 测试等）、
  依赖库清单（nifly / wxWidgets / OpenGL / GLI / TinyXML-2 / Bullet 等）、
  **官方 wiki 的 CLI 参数表**（"`-o` / `-m` 不存在"的纠错依据）、
  `Build Morphs` → `.tri` + `BODYTRI` 的提交记录、2018-02 拆分两个 exe 的提交。
  本库 [bodyslide-outfit-studio.md](../03-body/bodyslide-outfit-studio.md) 的机制依据基本都在这里。
- **`HydrogensaysHDT/hdt-skyrimse-mods`**：HDT-SMP 原始源码与 **MIT** 许可、
  SMP 配置 XML 格式（`hdtSkinnedMeshConfigs` / `defaultBBPs.xml`）、
  "只对 XPMSE human 骨骼生效"等 changelog 要点的原文。
- **`DaymareOn/hdtSMP64`**：FSMP 源码（**GPL-3.0**）、fork 链
  （HydrogensaysHDT → aers → Karonar1 → DaymareOn）、构建档位
  （`vs2022-windows-{nocuda,cuda}-{avx,avx2,avx512}`）、`smp` 命令、维护者自述的已知问题，
  见 [faster-hdt-smp.md](../04-physics/faster-hdt-smp.md)。
- **`Aietos/OBody` 与 `Aietos/OBody-NG`**：OBody NG 源码、**GPL-3 与仓库明示的 AI 使用政策**、
  语义化版本号、CommonLibSSE NG 构建链、"5.0 起支持 Skyrim 1.7.x" 的提交记录，
  见 [obody-ng.md](../05-distribution/obody-ng.md)。
- **`napmouse/autoBodyAE`**：AutoBody 源码、GPL-3.0、`morphs.ini` 语法、
  ORefit 重实现、credits（Sairion350 / Ryan-rsm-McKenzie / Scrab / alandtse）；
  **仓库现解析到 `RocketBun-OG/autoBodyAE`**（账号变更/迁移，维护状态未确认，
  见 [autobody.md](../05-distribution/autobody.md)）。
- **`Exit-9B/Face-Discoloration-Fix`**：作者 Parapets、**MIT**、运行时阻止 tint 丢失的机制
  （0.2 ms vs 30–70 ms/NPC 的代价对比来自其 README），见 [dark-face.md](../06-troubleshooting/dark-face.md)。
- **`halgari/wabbajack`**：Wabbajack 源码、GPL-3、manifest 机制，见 [wabbajack.md](../07-workflow/wabbajack.md)。

## C. 官方 wiki

**能回答什么**：引擎行为、文件格式、官方流程——**不含任何 mod 的版本信息**。

| wiki | 用途 |
|---|---|
| **SKSE 官方站**（`skse.silverlock.org`） | 当前各档版本（AE 2.3.1 = 1.7.104、GOG 2.2.6 = 1.6.1179、SE 2.0.20 = 1.5.97）、1.7.x 更新警告、不支持 MS Store / Game Pass 与 Epic 版、**SKSE 本身不使用 Address Library** |
| **Wabbajack wiki**（`wiki.wabbajack.org`） | 安装与排错（.NET 8 / VC++ 运行时、hash 不匹配 = 空间不足）、modlist 许可纪律 |
| **UESP**（`en.uesp.net/wiki/Skyrim_Mod:Mod_File_Format/...`） | `RACE` / `NPC` / `HDPT` 记录格式、`TINP` 枚举 |
| **Creation Kit wiki**（`ck.uesp.net`） | `HeadPart`、`HeadPart Script`、`Dark Face Bug` |
| **Beyond Skyrim Arcane University**（`wiki.beyondskyrim.org`） | NIF 技术细节（社区权威技术文档） |

> ⚠️ `creationkit.com`（CK 官方站）在本轮检索时处于**后端维护停机**；
> `ck.uesp.net` 是它的镜像。`Skeleton` / `Havok` 专页在镜像上缺页
> —— 因此本资料库的"骨骼系统"条目只能靠**原作者描述 + 引擎常识**支撑，
> 已在相应条目标注。**CK wiki 恢复后建议回头补一手引文。**

具体引用位置：

- `https://skse.silverlock.org/` —— 版本档位与更新警告（[version-matrix.md](../00-overview/version-matrix.md)
  与 [game-version-1-7-x.md](../00-overview/game-version-1-7-x.md) 的第一依据）
- `https://wiki.wabbajack.org/` —— 安装 / 排错（[wabbajack.md](../07-workflow/wabbajack.md)）
- `https://en.uesp.net/wiki/Skyrim_Mod:Mod_File_Format/RACE`（同系列 `/HDPT`、`/NPC`）——
  FaceGen 与头部部件记录的字段依据（[facegen-pipeline.md](../02-face/facegen-pipeline.md)、
  [dark-face.md](../06-troubleshooting/dark-face.md)）
- `https://ck.uesp.net/wiki/HeadPart`（及 `HeadPart_Script`）—— HeadPart 记录字段与黑脸 bug

## D. 作者本人说明

**能回答什么**：动机、设计取舍、未来计划、坑的官方口径——发布页装不下的细节都在这里。

| 内容 | 位置 |
|---|---|
| RaceMenu 作者关于 overlay NIF 与 1.7.99 的帖 | Nexus RaceMenu Posts 区 |
| BodySlide 作者解释 `.osp` / `.osd` | LoversLab 帖 |
| FSMP 作者的取代声明与 `smp report` | GitHub README |
| HPH 作者归属 | Alternate High Poly Head 的 credits |
| BHUNP 作者 Bakafactory 的物理科普（HDT-PE / SMP / 3BBB 的关系） | `https://babofactory.blogspot.com/2019/10/what-is-hdt-pe-hdt-smp-bbp-tbbp-3bbb.html` |
| OBody 原版作者（Sairion350）的设计自述（"a total rewrite of Racemenu's semi-obscure bodygen feature"） | Patreon 帖 |
| UBE 2.0 作者（JohnyBungalow1）的发布说明 | LoversLab 官方发布帖 |

## E. 社区（标注为"社区经验"）

- **LoversLab**：体型术语表、BodyGen 非官方文档（引作者原话）、CBPC 配置与 SMP 共存、
  穿模与脖缝排查
- **Nexus 论坛**：黑脸成因与修法、RaceMenu 滑块缺失、预设问题、3BA 安装问答
- **巴哈姆特（home.gamer.com.tw）**：中文身材/物理教程
- **NGA**：中文现代打底包推荐
- **3DM**：LE 时代整合包发布帖

> 社区材料的用法：**标"社区经验"**；多帖一致时写"多帖一致"。
> 社区帖里出现的版本号**默认降级为二手**，除非它引用了发布页原文。
> 教程站的分级评估见 [tutorials-and-guides.md](../07-workflow/tutorials-and-guides.md)。

## 速查：想查什么，去哪里

| 想查什么 | 去哪里 | 判据 |
|---|---|---|
| 某 mod 的当前版本 / 最后更新 | Nexus **Files 页** | 文件说明里的版本串与日期 |
| 某插件支持哪个游戏版本 | Nexus Files 页文件说明 + SKSE 官网 | 找 "support for X" / "Last FSMP version for Skyrim X" |
| 许可证 / 能否搬运二改 | Nexus 权限栏 + GitHub **LICENSE** | 以 LICENSE 文件为最终权威 |
| 机制原理 / 文件格式 | GitHub 源码 + UESP / ck.uesp.net | 提交记录 + wiki 字段 |
| 作者计划（停更？支持 1.7.x？） | Nexus Posts 区 / Patreon / 博客 | 作者本人帖，注意日期 |
| 某个"说法"对不对 | [unreliable-and-unconfirmed.md](unreliable-and-unconfirmed.md) | 先查错误知识清单，再查未确认事项清单 |
| 整合包装了啥 / 版本要求 | 列表自己的 README 与 wiki | 列表作者的文档是一手 |

## 取舍与建议

- **引用优先级**：Nexus Files 页 changelog > GitHub README/源码 > 官方 wiki > 作者本人帖 >
  社区帖。冲突时按此顺序采信，并在条目里写明"以 X 为准"。
- **版本敏感结论必须带日期**：不写"最新版是 X.Y"而不标来源与日期（本库规矩，见 CONTRIBUTING）。
- **内容墙后的页面**（CBBE / 3BA / BHUNP / HIMBO / CBPC / UBE）：用转载页全文、
  标"经转载 / 经转述"，并**至少两个转载页交叉一致**才写入。
- **本页会过期**：任何版本决策之前，重新核 SKSE 官网首页、目标 mod 的 Files 页、
  Address Library 的 Files 页——这三处是版本信息的"现在时"。

## 来源

- 本页绝大部分内容**本身就是来源清单**，无需再引用。
- "哪些 Nexus 页在成人内容墙后"与"CK 官方站停机、镜像缺页"两条为
  **本工作区实测（2026-09-22）**。
- 各来源的逐条核实细节（作者、版本、日期、权限栏原文）写在对应条目的"来源"节：
  [racemenu.md](../02-face/racemenu.md) · [cbbe.md](../03-body/cbbe.md) ·
  [cbbe-3ba.md](../03-body/cbbe-3ba.md) · [unp-bhunp.md](../03-body/unp-bhunp.md) ·
  [himbo.md](../03-body/himbo.md) · [ube.md](../03-body/ube.md) ·
  [bodyslide-outfit-studio.md](../03-body/bodyslide-outfit-studio.md) ·
  [xpmse-skeleton.md](../04-physics/xpmse-skeleton.md) · [hdt-smp.md](../04-physics/hdt-smp.md) ·
  [faster-hdt-smp.md](../04-physics/faster-hdt-smp.md) · [cbpc.md](../04-physics/cbpc.md) ·
  [obody-ng.md](../05-distribution/obody-ng.md) · [autobody.md](../05-distribution/autobody.md) ·
  [skse-plugin-frameworks.md](../01-prerequisites/skse-plugin-frameworks.md) ·
  [wabbajack.md](../07-workflow/wabbajack.md)
