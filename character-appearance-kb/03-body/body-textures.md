---
id: body-textures
title: 身体皮肤材质——与身形家族同族的硬规则
category: 03-body
kind: reference
version: 2.0.0
updated: 2026-10-25
tags: [身形, 皮肤, 材质, 贴图, UV]
aliases: [身体皮肤, 皮肤材质, skin, 男性皮肤, cbbe 皮肤, unp 皮肤, 皮肤接缝, 皮肤错位, 皮肤推荐, fair skin, tempered skins, vitruvia, bnp, 皮肤 uv, 皮肤与身形]
source: https://www.nexusmods.com/skyrimspecialedition/mods/798
summary: 皮肤必须与身形家族同族（CBBE 系 / UNP 系 / UBE 自成一系 / 男性 SOS 系各自独立 UV）——盘点女性与男性两条独立链上的常见皮肤 mod，给出换皮肤后出现接缝的排查顺序，以及与脖缝、黑脸条目的交叉。
---

# 身体皮肤材质

> **一句话**：皮肤贴图不是"换个图片"那么简单——**每套身形有自己的 UV 映射**，
> 皮肤必须与身形家族同族，否则手 / 颈 / 脚接缝、纹理错位是必然结果。
> 选身形 = 同时选定皮肤的可用范围。

## 速览

| 项 | 内容 |
|---|---|
| 条目性质 | 资源类（皮肤 / 纹理包） |
| 核心规则 | **皮肤必须与身形家族同族**；错配的表现是手 / 颈 / 脚接缝、纹理错位 |
| 女性链 | CBBE 系（自有 UV）与 UNP 系（共用原版 UV）**二选一**；UBE 又自成一系 |
| 男性链 | 独立的一条：HIMBO / SOS 型 UV（v4.0+ 互通），皮肤要下 **SOS-Lite / SOS 版** |
| 代表 mod | 女性：Fair Skin Complexion（798）、BnP - Female Skin（65274）；男性：Vitruvia（9112）、Tempered Skins（7902）、BnP - Male Skin（65402） |
| 是否需补丁 | 多数即装即用；RSV / RBT 类按种族分发需额外配置 |
| 关键限制 | 两套 UV 之间**没有转换补丁**，只能换皮肤文件本身 |

要点：

- **UV 分族是硬约束**：CBBE 与 UNP 用不同的 UV 映射，贴图无法互换；
  UBE 的 UV 与任何现存身形都不同；男性 SOS 系是第四条线。
- **Fair Skin Complexion（798）**是史上最通用的"默认皮肤"——同时提供
  CBBE 与 UNP 两种选项，装完 CBBE 后的常见推荐。
- **男性皮肤的反直觉经验**：即使不装 SOS，也要下 SOS-Lite / SOS 版纹理
  （详见 [himbo.md](himbo.md)）。
- 接缝问题的根因多数在"不同源"，**脖缝修补 mod 是创可贴，不解决根因**。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 原版时代 | 游戏自带低分辨率皮肤；早期皮肤 mod（Mature、Leyenda 等）直接替换原版贴图 | "给原版身体换皮"，一个 mod 服务所有身形 |
| 2011-2012 | **CBBE 与 UNP 分家**，各自建立独立 UV | 皮肤开始分族；UNP 系保留原版 UV，CBBE 自成一族 |
| SE 早期 | **Fair Skin Complexion**（Nexus 798）同时提供 CBBE / UNP 两选项 | 成为跨身形事实标准，"默认皮肤"地位延续至今 |
| 2018 前后 | **Vitruvia**（SE 9112）等男性专用皮肤成型；Tempered Skins（SE 7902）提供 nude / dressed / SOS 多版本 | 男性链从"蹭女性皮肤"走向独立生态 |
| 2021-2022 | **BnP** 系列登场：Female Skin（65274）/ Male Skin（65402），半写实、4K BC7、支持 RSV/RBT | "写实派"取代"娃娃皮"成为新主流审美 |
| 2023 起 | **UBE 2.0** 生态出现 Diamond Skin (UBE)、Freyna、Jada 8.1 等专用皮肤 | 第四条 UV 线诞生；UBE 角色必须用 UBE 皮肤 |

### 它从哪来

皮肤 mod 的历史就是**身形分家的历史**。原版时代一套贴图走天下；
CBBE / UNP 各自重做了 UV 之后，皮肤 mod 被迫二选一——
这也是"皮肤必须与身形同族"这条规则的来历。

### 中间经历了什么

两条线索：**女性侧**从"娃娃皮"（Fair Skin、The Pure、Demoniac）
走向半写实（BnP：毛孔、皱纹、痣、毫发细节，4K BC7）；
**男性侧**从长期蹭女性资产，到 Vitruvia / Tempered Skins / BnP Male Skin
三足鼎立，且全部要提供 SOS 版（因为 HIMBO/SOS 的 UV 与裸男体型绑定）。

### 现状

皮肤选择完全以身形为前提：装 CBBE 3BA 就在 CBBE 皮肤里挑，
玩男性角色就在 SOS 系男性皮肤里挑，用 UBE 只能用 UBE 专用皮肤。
**先定身形，再挑皮肤**，顺序反了必然返工。

## 它解决什么问题

**没有它之前（的问题）**：原版皮肤低分辨率、无细节；
而随手装一个"高清热门皮肤"到错误的身形上，得到的是
手/颈/脚一圈错位接缝——玩家往往误以为"皮肤 mod 有 bug"。

**正确姿势**：把皮肤选择变成两步决策——

1. **先确认身形家族**（CBBE / UNP / UBE / 男性 SOS 系）；
2. **再在该家族内挑皮肤**，并确认 FOMOD 选项与身形一致。

## 核心规则：皮肤必须与身形家族同族

| 身形家族 | UV | 可用皮肤 |
|---|---|---|
| **CBBE / 3BA** | CBBE 自有 UV | 仅 CBBE 系皮肤（Fair Skin 的 CBBE 选项、BnP 的 CBBE 文件等） |
| **UNP / UUNP / BHUNP** | 全系共用**原版 UV** | UNP 系皮肤 + 大量原版皮肤（Fair Skin 的 UNP 选项、Bijin Skin 等） |
| **UBE 2.0** | UBE 自有 UV（与任何现存身形不同） | 仅 UBE 专用：Diamond Skin (UBE)、Freyna Skin、Jada 8.1 Skin 等 |
| **HIMBO / SOS 系男性** | SOS 型 UV（HIMBO v4.0+ 互通） | 仅 SOS-Lite / SOS 版男性皮肤（Vitruvia、Tempered Skins、BnP Male Skin） |
| **TNG** | 与 SOS Full retextures 兼容 | SOS Full 系 retextures |

> **UNP 系是全族共用原版 UV**，所以 vanilla 皮肤可直接用于 UNP 系，
> 但不能用于 CBBE——这是 UNP 系"皮肤库存大"的结构性原因
> （见 [unp-bhunp.md](unp-bhunp.md)、[cbbe.md](cbbe.md)）。

## 常见皮肤 mod

### 女性链

| mod | Nexus | 覆盖 | 备注 |
|---|---|---|---|
| **Fair Skin Complexion** | **798** | 脸 + 身 | 提供 **CBBE 与 UNP 两种选项**；CBBE 装完后的常见推荐 |
| **BnP - Female Skin** | **65274** | 脸 + 身 | 半写实；支持 CBBE / UNP / COCO + RSV；4K / 2K BC7 |
| Bijin Skin | LE 91953 | 脸 + 身 | 社区点名较多的 NPC 美化向皮肤 |
| Demoniac | LE 70834 | 女性 | 社区推荐（浅肤色、8K） |
| Mature / Leyenda / Diamond / The Pure | 未确认 | 女性为主 | 社区点名较多；清单随时期变化 |

### 男性链（与女性完全独立）

| mod | Nexus | 覆盖 | 备注 |
|---|---|---|---|
| **Vitruvia - Skin texture overhaul for males** | **SE 9112** / LE 82948 | 人类男性 | mandragorasprouts；有 SOS 与 SOS Lite 版、多毛/无毛胸选项 |
| **Tempered Skins for Males - Vanilla and SOS versions** | **SE 7902** | 非兽族男性 | traa108；nude（来自 Better Males）/ dressed / SOS 版；含 complexions、雪精灵、吸血鬼 |
| **BnP - Male Skin** | **65402** | 男性全种族 | 基于 Vobla 的 Svein skin；**全面支持 SOS full / HIMBO / SOS light / TNG / SAM light**；15 种皮肤、13 种肌肉、7 种吸血鬼脸 |
| Masculine Khajiit Textures (Grey Cat and Leopard) | **SE 186** | 虎人男性 | MONSTERaider（Grey Cat 原为 mrLenski）；有 SOS-LITE 2K 版 |
| Masculine Argonian Textures (Chameleon and Lizard) | LE 70164；SE ID 未确认 | 亚龙人男性 | MONSTERaider；有 SOS-LITE 2K 版 |
| SkySight Skins | ID 未确认 | 男性 | fadingsignal；Norse 神系审美，社区报告与 SOS 不兼容需补丁 |

> ⚠️ 上表中除标注 Nexus ID 的条目外，一批名字来自社区推荐清单
> （Nexus 论坛皮肤讨论、Kiseenaji 清单等）——**社区经验，且清单随时期变化**。
> 写文档或推荐时不要把它当成"权威排行"，引用请附日期。

### ⚠️ 男性皮肤要下 SOS-Lite 版（交叉）

男性链的铁律：**即使不装 SOS，纹理也要选 SOS-Lite / SOS 版**——
HIMBO v4.0+ 的 UV 与 SOS 型纹理互通，装原版（非 SOS）版本会出现接缝或错位。
完整论述见 [himbo.md](himbo.md) 的"男性皮肤生态"一节。

## 按种族分发：RSV / RBT（进阶）

现代皮肤包普遍带**按种族分配不同皮肤**的选项，代表是 BnP 系列的
**RBT**（Racial Body Textures）与 **RSV**（Racial Skin Variance）：

| 机制 | 做什么 | 代价 |
|---|---|---|
| **RBT** | 给每个种族（除兽族）独特身体纹理；**独特头部纹理只对玩家生效** | NPC 头要用 CK 导出才能吃到种族头纹理（mod 页描述） |
| **RSV** | 类似 RBT，且覆盖非玩家族（Dremora 等），可经 SPID 给 NPC 脸分配纹理 | 依赖 SPID；配置项多，调试成本高 |

> 这是"皮肤安装"里少见的**需要额外配置**的形态：不配 SPID / 不导 NPC 头，
> 装了也只有玩家生效（mod 页描述 + 社区经验）。求稳可只用标准 replacer 文件。

## 安装与配置

- 皮肤 mod 之间**抢同一路径**是常态（都写 `textures\actors\character\...`），
  同时装两个皮肤 = 看覆盖关系谁赢（规则见
  [mo2-override-rules.md](../07-workflow/mo2-override-rules.md)）；
- **FOMOD 选项要一次选全**：头 / 身 / 手 / 脚 / tintmask 不同档，
  会直接造成接缝（排查顺序第 2 步）；
- 换皮肤后进游戏**看不到变化**的常见原因是构建产物或 facegen 缓存，
  不是皮肤没装上——先按上面的顺序查，别急着重装。

## 两条独立链

- 女性身形（CBBE 系 / UNP 系）**二选一**，选完皮肤池就定了；
- 男性身形（[HIMBO](himbo.md)）是**另一条**链，可与女性身形**同时启用**；
- 男性皮肤（Tempered Skins for Males 等）**自成一套 UV**，
  与女性皮肤互不通用；
- [UBE](ube.md) 是第四条线：与 3BA/BHUNP 并存安装，但皮肤全线不兼容。

## 排查顺序：出现接缝时

按顺序查，**每一步都能单独排除一类根因**：

1. **性别链对不对？** 男性皮肤装给女性角色（或反之）是低级但高频的错误。
2. **头 / 手 / 身体是否来自同一套皮肤的同一种选项？**
   （一支 FOMOD 里的十几个选项要全选同一档——这是最常见的自伤。）
3. **皮肤与身形是否同族？** CBBE 皮肤贴 UNP 身上，必然错位。
4. **是否装了自定义头网格**（HPH / CITRUS 等）而没做配套？
   头部拓扑不同会连带动脖子附近的 UV。
5. **FaceGen 的 tint 是否与 CK 里 NPC 的 Face Tinting Color 一致？**
   （这条管"脸黑/脸花"，不管理想接缝。）
6. **最后**才考虑"脖缝修补 mod"——它是创可贴，不解决根因。

完整排查见 [neck-seam.md](../06-troubleshooting/neck-seam.md)（脖缝）与
[dark-face.md](../06-troubleshooting/dark-face.md)（黑脸/脸花）。

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 换皮肤后手 / 颈 / 脚一圈接缝 | 皮肤与身形不同族 | 换同族皮肤；UNP 系可沿用原版皮肤，CBBE 必须 CBBE 系 |
| 纹理整体错位 / 花色 | UV 族不对（如 CBBE 皮肤贴 UNP） | 同上；别试图用补丁"救"UV |
| 同一套皮肤只有脖子一圈分界 | 头 / 身来自不同选项或不同 mod | FOMOD 全选同一档；检查覆盖关系 |
| 男性皮肤装上没效果 / 错位 | 下的是非 SOS 系 UV 版本 | 改下 SOS-Lite / SOS 版（见 [himbo.md](himbo.md)） |
| UBE 角色皮肤贴不上 | CBBE/UNP 皮肤 UV 与 UBE 不同 | 换 UBE 专用皮肤（Diamond / Freyna / Jada 等） |
| 两个皮肤 mod 互相"抽风" | 抢同一路径，覆盖关系不稳定 | 只保留一个；规则见 [mo2-override-rules.md](../07-workflow/mo2-override-rules.md) |
| NPC 脸黑 / 脸不变 | 与皮肤无关，是 facegen / 覆盖问题 | [dark-face.md](../06-troubleshooting/dark-face.md) |
| RSV / RBT 按种族分发不生效 | 没配 SPID / 没导 NPC 头 | 按 mod 页说明补配置；或退回标准 replacer 文件 |
| 4K 皮肤显存吃紧 / 加载变慢 | 分辨率与压缩格式选太高 | NPC 密集场景用 2K；BC7 是有损下的高质选项（社区经验） |

## 取舍与建议

**给女性角色挑皮肤**：

- 求稳、求生态：Fair Skin Complexion（798）——两族通吃；
- 求写实：BnP - Female Skin（65274），4K BC7，注意与 RSV/RBT 的搭配成本。

**给男性角色挑皮肤**：

- Vitruvia（光滑审美）/ Tempered Skins（肌肉现实向）/ BnP Male Skin（写实派），
  三者都下 **SOS-Lite / SOS 版**；
- 虎人 / 亚龙人用 MONSTERaider 系列，同样下 SOS-LITE 版。

**通用纪律**：

- **先定身形再挑皮肤**；换身形 = 换全套皮肤，沉没成本很高；
- 皮肤是"全身资产"（脸+身+手+脚+tintmask），别只装一半；
- 分辨率不是越高越好：4K BC7 的显存与加载成本真实存在，
  NPC 遍布的世界里尤其敏感（社区经验）。

## 来源

- **一手（Nexus 页）**：Fair Skin Complexion 提供 CBBE 与 UNP 两种选项：
  `https://www.nexusmods.com/skyrimspecialedition/mods/798`
- **一手（Nexus 页，经转载）**：Tempered Skins for Males（traa108，SE 7902）
  "High quality non-beast male face and body texture replacement… Nude (from
  Better Males) and dressed (Vanilla based) bodies, SOS versions also available"
- **一手（Nexus 页，经转载）**：Vitruvia（mandragorasprouts，SE 9112 / LE 82948）
  的 SOS / SOS Lite 版与多毛/无毛选项；BnP - Male Skin（65402）基于 Svein skin
  （Vobla）且全面支持 SOS full / HIMBO / SOS light / TNG / SAM light
- **一手（Nexus 页交叉）**：Masculine Khajiit Textures 为 Nexus SE 186：
  LoversLab 补丁页引用
- **社区经验**：CBBE / UNP 的 UV 不通用（Nexus 发布页描述 + 社区一致确认）；
  "男性皮肤下 SOS-Lite 版"（Return to Skyrim 指南，Nexus 58414）；
  皮肤清单（Bijin Skin、Demoniac、Mature、Leyenda、Diamond、The Pure、SkySight）
  来自社区推荐清单，随时期变化；接缝排查顺序综合 Nexus 论坛 / LoversLab
  脖子接缝帖归纳
- **一手（Nexus 页，经转载）**：RBT / RSV 的机制描述（RBT 独特头纹理仅玩家生效、
  需 CK 导出 NPC 头；RSV 经 SPID 分配 NPC 脸）：BnP - Male Skin 发布页描述
- **未确认**：BnP 系列作者署名、Mature/Leyenda/Diamond/The Pure 的 Nexus ID、
  Masculine Argonian SE ID、SkySight Skins 的 Nexus ID、各皮肤当前版本号
