---
id: glossary
title: 术语表——捏脸与身形领域的行话词典
category: 00-overview
kind: reference
version: 2.0.0
updated: 2026-10-25
tags: [总览, 术语, 速查, 缩写]
aliases: [名词解释, 3BA 是什么, SMP 是什么, 什么叫 morph, CBPC 是什么, XPMSE 是什么, bodyslide 是什么, tri 文件是什么, jslot, skeleton, UV, physics 是什么, BODYTRI, facegen 是什么, presets 是什么]
source: https://www.loverslab.com/blogs/entry/16040-glossary
summary: 捏脸与身形领域的缩写、俗称与易混词按主题分组逐条对齐，每条给出"它到底指什么"、"常见的误解是什么"与"该去读哪一篇"，是本资料库的检索入口。
---

# 术语表

这一页是**整个 `character-appearance-kb` 的检索入口**：不认识的词先来这里查，
查到词之后顺着最后一列的链接往下读。每个词条都按同一格式给出：

> **是什么**（一句话定义） → **常见误解**（别人最容易理解错的地方） → **详见**（链接到具体条目）

## 速览

| 字段 | 内容 |
|---|---|
| 作用层 | 名词 / 缩写 / 俗称的**对齐层**（不涉及安装动作） |
| 覆盖范围 | 身形 · 物理 · 机制 · 前置 · 文件格式 · 分配预设 · 症状俗称，共七组 |
| 依赖 | 无 |
| 影响范围 | 读懂其余 47 篇条目的前提；也可当作"俗称表"反查（右上/文中检索会命中别名） |
| 关键限制 | 本页只负责**定义与消歧**，具体机制一律抛出到下属条目 |
| 版本敏感性 | 术语本身稳定，但 mod 版本状况请配合 [`version-matrix.md`](version-matrix.md) 查看 |

要点：

- **身形家族只有两组 UV**：CBBE 系与 UNP 系，这决定了皮肤与服装能不能通用。
- **物理只有两条技术路线**：CBPC（球体近似）与 SMP/FSMP（逐顶点 + Bullet）。它们不是新旧关系。
- **机制只有两条变形路径**：运行时 morph（只影响玩家）与离线烘焙（影响所有使用该网格的人）。
- **`Build Morphs` 是整套东西的开关**：不勾它，就没有 `.tri`，也就没有身形滑块。
- **2026-10 的现实**：`RaceMenu` 停在 0.4.20.0（面向 1.6.1170），1.7.x 未发布正式版，见 [`game-version-1-7-x.md`](game-version-1-7-x.md)。

## 前世今生

这套词汇不是一次设计的，而是**三个时代叠出来的**：

| 时代 | 留下的词 | 为什么会留下 |
|---|---|---|
| **LE 时代（2011~2015）** | CBBE、Dimonized UNP、UNPB、HGEC（Oblivion 遗产）、TBBP/BBP、ECE、slot | 那时"身形"就是替换 `femalebody_0/1.nif`；"物理"就是给身体加几根骨骼（BBP/TBBP）；"捏脸"就是 ECE 的 slot 保存/读取 |
| **SE 移植期（2016~2019）** | UUNP、Legacy UUNP、XPMSSE、RaceMenu、`skee64.dll`、NiOverride、BSTriShape | SE 换了网格格式并引入 64 位 SKSE，一切都要重写；"运行时 morph"这个概念随 RaceMenu 进入本区词汇表 |
| **AE 成熟期（2020 至今）** | 3BBB / 3BA、BHUNP、FSMP（HDT-SMP 的现代 fork）、OBody NG、CommonLibSSE-NG、Address Library v13 | 身形进入"3 乳骨 + 物理 + BodySlide 三合一"的形态；插件层有了跨版本通用的工程方案 |

于是形成了今天这些容易撞脸的说法：同一个部位在 LE 叫 TBBP、在 SE 叫 3BBB/3BA；
同一个 morph 需求在 LE 靠 ECE slot、在 SE 靠 RaceMenu + `.tri`；
同一个 "skee" 既指 `skee64.dll`（RaceMenu 的 dll），也指它内部的 NiOverride / CharGen 两套机制的统称。
**看到旧词时先问它属于哪个时代**，多数困惑就消了。

## 它解决什么问题

- **同一个东西两个名字**：例如 "3BBB" 与 "3BA" 混用、"HDT-SMP" 与 "FSMP" 混用。
- **两个东西一个名字**：例如 "CBP"（旧的无碰撞版）与 "CBPC"（带碰撞的后继）；
  "BodySlide 预设" 与 "RaceMenu 预设" 都叫"预设"，但**完全不能互通**。
- **缩写没有展开**：例如 SMP = Skinned Mesh Physics，XPMSE = XP32 Maximum Skeleton Special Extended。
- **看不懂别人给的解决方案**：教程里说"在 BodySlide 里勾 Build Morphs 重新构建"，不认识其中的词等于无法执行。

## 配置与使用

用法很简单：**先在下面对应的分组里找词 → 看"常见误解"确定是不是你要的那个 → 点最后一列进具体条目。**
如果你手上只有一句"症状/口语说法"，直接跳到最后的"## 症状俗称 → 条目对照"。

下面是**常见英文提问词 → 本库条目**的对照（用的多数是大家在搜索引擎里会敲的词）：

| 你会搜的词 | 对应本库的什么 | 进去 |
|---|---|---|
| body slider / body morphs not showing | 身形滑块缺失（缺 `.tri` 或 `BODYTRI`） | [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md) |
| black face bug | 黑脸 | [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md) |
| seam / neck gap | UV 不同族造成的接缝 | [`../06-troubleshooting/neck-seam.md`](../06-troubleshooting/neck-seam.md) |
| clipping / boobs clipping armor | 穿模 | [`../06-troubleshooting/clipping.md`](../06-troubleshooting/clipping.md) |
| physics not working / no bounce | 物理不生效 | [`../06-troubleshooting/physics-not-working.md`](../06-troubleshooting/physics-not-working.md) |
| preset have no effect | 预设未生效 | [`../06-troubleshooting/preset-not-applied.md`](../06-troubleshooting/preset-not-applied.md) |
| crash after update | 大版本更新后的崩溃（含 1.7.x） | [`game-version-1-7-x.md`](game-version-1-7-x.md) |
| bodytype / tofu body | 缺少身形 mod，使用了原版体型 | [`../03-body/cbbe.md`](../03-body/cbbe.md) |

---

### 一、身形（body）

| 词 | 是什么 | 常见误解 | 详见 |
|---|---|---|---|
| **CBBE** | Caliente's Beautiful Bodies Enhancer，女性身形网格，自成一族 UV | 误解成"软件"。它是**网格 + 贴图资源**，不是工具 | [`../03-body/cbbe.md`](../03-body/cbbe.md) |
| **Caliente's Big Bottom Edition** | CBBE 的原名，因初始比例夸张而得名，后改名 Beautiful Bodies | 以为是另一个 mod | 同上 |
| **UNP / Dimonized UNP** | dimon99 的 LE 女性身形，UNP 家族源头 | 以为 UNP = 一个固定形状（它其实是一族；各变体共用原版 UV） | [`../03-body/unp-bhunp.md`](../03-body/unp-bhunp.md) |
| **UNPB** | UNP Blessed Body，UNP 的丰胸丰臀重制变体 | 以为是独立家族（它属 UNP 家，皮肤通用） | 同上 |
| **UUNP** | Unified UNP，LE 时代把 UNP 变体统一并做成 BodySlide 可构建形态 | 以为 SE 上仍受官方支持（**并非如此**，SE 靠 Legacy UUNP 过渡） | 同上 |
| **Legacy UUNP** | 供 LE→SE 转换的过渡版本（Nexus 43773） | 以为是要长期使用的日常身形 | 同上 |
| **BHUNP** | "UUNP Next Generation" 的 SE 版，作者 Bakafactory / Haeun，支持物理与 BodySlide，3BBB | 以为和 UUNP 是一回事（两者骨头结构不同） | 同上 |
| **3BBB** | 3 Breast Bones Body —— 每侧乳房 3 根骨骼 | 以为是某个文件名或某个 mod 的缩写（它是**通用术语**） | [`../03-body/cbbe-3ba.md`](../03-body/cbbe-3ba.md) |
| **3BA** | CBBE 3BBB Advanced，CBBE 的扩展，基底网格仍同 CBBE | 以为是"CBBE 的替代品"（其实**同基底**，可叠加） | 同上 |
| **CBBE SMP (3BBB)** | HDT-SMP 官方页列出的 CBBE SE **官方 SMP 身体与配置预设** | 与 3BA 混为一谈（后者是**编辑过**的版本） | [`../04-physics/hdt-smp.md`](../04-physics/hdt-smp.md) |
| **HIMBO** | Highly Improved Male Body Overhaul，作者 Kreiste，男性身形 | 以为和 CBBE 属于同一条链（男性其实是**另一条独立的链**） | [`../03-body/himbo.md`](../03-body/himbo.md) |
| **UBE** | Ultimate Body Enhancer 2.0，"Bungalow Body and Face" | 以为是身体替换器（它其实是**新增独立种族**） | [`../03-body/ube.md`](../03-body/ube.md) |
| **UV / UV 家族** | 网格表面到贴图的映射关系。CBBE 自有 UV；UNP 系共用原版 UV | 以为"换个皮肤贴图无所谓" —— **错配必在手/颈/脚出现接缝** | [`../03-body/body-textures.md`](../03-body/body-textures.md)、[`../06-troubleshooting/neck-seam.md`](../06-troubleshooting/neck-seam.md) |
| **high poly head（HPH）** | 高模头部网格替换 | 以为装了就完事（还需要配套的 head part 资源与 morph 支持） | [`../02-face/high-poly-head.md`](../02-face/high-poly-head.md) |

### 二、物理（physics）

| 词 | 是什么 | 常见误解 | 详见 |
|---|---|---|---|
| **BBP / TBBP** | LE 时代的骨骼驱动方案（Better/TJBP breasts & butt physics） | 以为 SE 上还能原样使用（需 XPMSE 骨骼支持，且已被 CBPC / SMP 取代） | [`../04-physics/physics-overview.md`](../04-physics/physics-overview.md) |
| **HDT-PE** | HDT Physics Extensions，用游戏内建 Havok 做**骨骼级**碰撞的旧方案 | 以为和 HDT-SMP 是同一个东西的升级版（它们是**不同实现**） | 同上 |
| **HDT-SMP** | Skinned Mesh Physics，用 Bullet 做**逐顶点蒙皮网格**物理 | 以为 SMP 只管身体（它才是做**头发与衣物**物理的那一个） | [`../04-physics/hdt-smp.md`](../04-physics/hdt-smp.md) |
| **FSMP** | Faster HDT-SMP（Nexus 57339），SMP 的现代维护 fork，作者 DaydreamingDay | 以为可以和原版 SMP 同时装（**不要两个都装**） | [`../04-physics/faster-hdt-smp.md`](../04-physics/faster-hdt-smp.md) |
| **CBPC** | CBP Physics with Collisions，作者 Shizof，用**球体近似**做碰撞 | 以为它能管头发和衣服（**不能**）；但它轻量、对 CPU 友好 | [`../04-physics/cbpc.md`](../04-physics/cbpc.md) |
| **CBP** | polygonhell 的早期无碰撞版本，MIT 释出源码 | 与 CBPC 混为一谈（**名字像但不是同一个**） | 同上 |
| **physics 变体** | 身形 FOMOD 里带物理节点的那个选项 | 以为装了物理 DLL 就会自动有物理节点（**钩子 + 骨骼 + 网格三者缺一不可**） | [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md) |

### 三、机制（mechanics）

| 词 | 是什么 | 常见误解 | 详见 |
|---|---|---|---|
| **morph** | **一组顶点位移向量**；运行时网格 = 基础网格 + Σ(morph × 权重) | 以为滑块会改文件（运行时 morph **不改文件**，详见下一条"两条路径"） | [`morph-and-nif-basics.md`](morph-and-nif-basics.md) |
| **运行时 morph** | RaceMenu / NiOverride 在游戏运行中施加的形变，**只影响玩家** | 以为调好的身材会自动作用于 NPC（**不会**） | [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md) |
| **离线烘焙** | BodySlide 的 Build：把预设数值**写进 `.nif` 顶点坐标**，影响所有使用该网格的人（含 NPC） | 以为 Build 只是"预览一下" | 同上 |
| **conform** | Outfit Studio 里把身体的滑块形变数据复制到衣服顶点的操作 | 以为"拖滑块衣服跟着变"是巧合（正因为 conform 后两者**共用同一套 morph 名字**） | [`../03-body/bodyslide-outfit-studio.md`](../03-body/bodyslide-outfit-studio.md) |
| **Zeroed Sliders** | 滑块归零的基准构建（起点统一到零） | 以为里面的 100% 项是 bug（**部分 100% 是有意设计，不要改**） | [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md) |
| **NiOverride** | RaceMenu 的运行时叠加机制（位于 `skee64.dll` 内），负责应用 morph / overlay / tint | 以为是一个可以单独下载的独立 mod（它随 RaceMenu 发布） | [`../02-face/racemenu.md`](../02-face/racemenu.md) |
| **CharGen** | RaceMenu 的角色创建模块（滑块界面） | 以为是可选组件（**早已并入本体**） | 同上 |
| **FaceGen** | 引擎的**头部预生成数据**：头网格 `.nif` + 色调 `.dds`，由 CK 的 `Ctrl+F4` 导出 | 以为 NPC 的脸也是实时 morph 生成的（**不是，NPC 脸永远是预生成的**） | [`../02-face/facegen-pipeline.md`](../02-face/facegen-pipeline.md) |
| **tint mask** | 脸部着色遮罩（唇色/腮红/眼线/肤色…），在 RACE 与 NPC 记录里逐层定义 | 以为是贴图本体 | [`../02-face/face-textures.md`](../02-face/face-textures.md) |
| **head part / HDPT** | 面部部件数据对象（头发、眼、胡须、疤痕、眉毛…） | 以为发型就是"一根 nif"（它是一条 HDPT 记录，可被多个 mod 同时提供并相互覆盖） | [`../02-face/face-headparts-resources.md`](../02-face/face-headparts-resources.md) |
| **overlay** | RaceMenu 的贴图叠加层（身体/脸/手/脚各自一个 nif） | 2026-08 起这些 nif 在 1.7.x 上会直接崩游戏，见最后一组 | [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md) |

### 四、前置（frameworks）

| 词 | 是什么 | 常见误解 | 详见 |
|---|---|---|---|
| **SKSE64** | Skyrim Script Extender（Skyrim SE/AE 版），版本**必须与游戏版本精确对应** | 以为"装了最新版就好"（它只支持 Steam/GOG 最新版，其他版本需对应档） | [`../01-prerequisites/skse64.md`](../01-prerequisites/skse64.md) |
| **Address Library** | meh321 的地址数据库，让 SKSE DLL 插件跨 1.6.x 小版本通用 | 以为 SE(1.5.x) 与 AE(1.6.x) 的 bin 通用（**不通用**）；SKSE 自身**不使用**它 | [`../01-prerequisites/skse-plugin-frameworks.md`](../01-prerequisites/skse-plugin-frameworks.md) |
| **CommonLibSSE / NG** | 插件开发用的上层库（含偏移数据库）；RaceMenu 正在向 NG 版移植 | 以为它能让任意老插件免重编生效（**不能**，插件本身要改代码） | [`game-version-1-7-x.md`](game-version-1-7-x.md) |
| **XPMSE / XPMSSE** | XP32 Maximum Skeleton Special Extended（Nexus 1988），Team XPMSE 出品，骨骼扩展 | 以为 "XPMSSE" 和 "XPMSE" 是两个 mod（前者是 SE/AE 重制版） | [`../04-physics/xpmse-skeleton.md`](../04-physics/xpmse-skeleton.md) |
| **PapyrusUtil / JContainers / MCM Helper** | 数据存取（StorageUtil/JsonUtil）、JSON 容器、配置菜单 | 以为"可装可不装"（多个分配/物理工具明列为前置） | [`../01-prerequisites/skse-plugin-frameworks.md`](../01-prerequisites/skse-plugin-frameworks.md) |

### 五、文件格式（formats）

| 词 | 是什么 | 常见误解 | 详见 |
|---|---|---|---|
| **NIF** | NetImmerse Format，Creation Engine 的 3D 资产容器（身体/头/服装都是 NIF） | 以为它只存网格（还包括着色器、骨骼、动画、物理信息） | [`morph-and-nif-basics.md`](morph-and-nif-basics.md) |
| **BSTriShape** | SE/AE 的形状节点，**形状与几何数据合并成单块**（LE 是 `NiTriShape` + `NiTriShapeData`） | 以为 LE 的网格式能直接用于 SE（**不能直接通用**） | 同上 |
| **`BSDismemberSkinInstance`** | 蒙皮网格的皮肤实例，含**顶点权重**与**身体分区（partitions）** | 以为"分区号随便填"（分区号与 ARMO/ARMA 的 biped 槽不一致则该部分**不显示**） | 同上 |
| **`.tri`** | morph 目标文件；BodySlide 勾 `Build Morphs` 时生成，并被 RaceMenu 读取 | 以为有了 `.tri` 就够了（还得 NIF 里有 `BODYTRI` 指过去） | [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md) |
| **BODYTRI** | NIF 里的 extra data，**指向对应的 `.tri`** | 以为一个 NIF 可以保留多份 BODYTRI（新版 BodySlide 只写一条，正是为了清掉路径错的残留） | 同上 |
| **`.jslot`** | RaceMenu 预设文件，**JSON 文本**格式 | 以为能被 BodySlide 直接读取（**两套预设体系不通用**） | [`../02-face/racemenu-presets.md`](../02-face/racemenu-presets.md) |
| **`.slot`（旧）** | RaceMenu 的旧二进制格式；旧的仍可被读取，但**不再被写出** | 以为新版本还能写出 `.slot` | 同上 |
| **`.xml`（SliderPresets）** | BodySlide 预设文件，位于 `Data\CalienteTools\BodySlide\SliderPresets\`；**每个滑块存体重 0 与 100 两个值** | 以为它和 `.jslot` 是同一件事的两种后缀 | [`../03-body/bodyslide-presets.md`](../03-body/bodyslide-presets.md) |
| **`.osp` / `.osd`** | Outfit Studio 项目文件（`.osp` 是**纯文本 XML**）与滑块数据（`.osd` 是**二进制**） | 以为两者都能手改（`.osd` 不能） | [`../03-body/bodyslide-outfit-studio.md`](../03-body/bodyslide-outfit-studio.md) |
| **CK `Ctrl+F4`** | Creation Kit 导出 FaceGen 头网格与色调数据的快捷键 | 以为导出一次就永久有效（换任何影响脸的 mod 都要重导） | [`../02-face/facegen-pipeline.md`](../02-face/facegen-pipeline.md) |

### 六、分配与预设（distribution）

| 词 | 是什么 | 常见误解 | 详见 |
|---|---|---|---|
| **BodyGen** | RaceMenu 内置的随机身形分配；数据目录 `meshes/actors/character/BodyGenData/<MOD_FILENAME_WITH_EXT>/` | 以为 ini 末尾要不要空行无所谓（**必须留空行**） | [`../05-distribution/racemenu-bodygen.md`](../05-distribution/racemenu-bodygen.md) |
| **OBody（原版）** | OStim 团队出品，**BodyGen 的完全重写** | 以为它自带身形（它只消费你已有的 BodySlide `.xml` 预设库） | [`../05-distribution/obody-ng.md`](../05-distribution/obody-ng.md) |
| **OBody NG** | Aietos 用 CommonLibSSE NG 编译的续作，单 dll 通吃多个游戏版本，GPL-3 | 以为是同一个作者（**作者不同**：前者为 OStim 团队，后者为 Aietos） | 同上 |
| **AutoBody** | napmouse 的 AE 版身形分发 | 以为和 OBody NG 用法一样（两者都对 Zeroed Sliders 基础有要求） | [`../05-distribution/autobody.md`](../05-distribution/autobody.md) |
| **ORefit** | OBody 的穿衣状态下重算体型功能 | 以为开启后会拖慢很多才生效 | [`../05-distribution/obody-ng.md`](../05-distribution/obody-ng.md) |

### 七、症状俗称 → 条目对照

| 口语说法 | 它在本库叫什么 | 直接进去 |
|---|---|---|
| 黑脸 | FaceGen 数据不匹配 / 脸 nif 或 tint 层被覆盖 | [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md) |
| 脖子缝 / 身体两截色 | UV 不同族导致的 seam | [`../06-troubleshooting/neck-seam.md`](../06-troubleshooting/neck-seam.md) |
| 穿模 / 破皮 | 起点形状不一致（只 Build 了身体没 Batch Build 衣服） | [`../06-troubleshooting/clipping.md`](../06-troubleshooting/clipping.md) |
| 不抖 / 物理没反应 | 物理 DLL 未加载 / 非 physics 变体 / FOMOD 版本档错 | [`../06-troubleshooting/physics-not-working.md`](../06-troubleshooting/physics-not-working.md) |
| 滑块没了 | 缺 `.tri` 或 `BODYTRI`，或被其他 nif 覆盖 | [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md) |
| 预设导进去脸还是不对 | `.jslot` / head nif 的搭配与加载顺序问题 | [`../06-troubleshooting/preset-not-applied.md`](../06-troubleshooting/preset-not-applied.md) |
| 一进捏脸就崩 / 更新后启动崩 | 版本错配；2026-08 起还要查 overlay nif | [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md)、[`version-matrix.md`](version-matrix.md) |

## 高频辨析（最容易搞混的四组）

### 3BBB vs 3BA

**3BBB 是术语**（每侧乳房 3 根骨骼），**3BA 是 CBBE 家族里那个具体的实现**（CBBE 3BBB Advanced）。
HDT-SMP 官方页同时列出 `CBBE SMP (3BBB)`（官方 SMP 身体）与 `CBBE 3BBB (3BA)`（**编辑过**的版本）。
骨骼节点越多 → 可控性与效果上限越高，但最终效果仍取决于 XML 配置质量与网格比例。

### BodySlide 预设 vs RaceMenu 预设

两者**都不能互相导入**。前者是 `.xml`、每个滑块存体重 0/100 两个值、在 Build 时烘焙进 nif；
后者是 `.jslot`、在 `bodyMorphs` 段存浮点值、在游戏运行时施加。详见
[`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

### HDT-SMP vs CBPC

不是新旧关系，而是**两条不同技术路线**：CBPC 用球体近似、每帧计算、轻量但对 CPU 友好且
管不了头发衣物；SMP/FSMP 用 Bullet 做逐顶点、能吃 cpu 但能做头发与衣物。详见
[`../04-physics/physics-overview.md`](../04-physics/physics-overview.md)。

### UUNP vs BHUNP

UUNP 是 LE 时代的统一 UNP，**在 SE 上处于不受支持状态**（转换靠 Legacy UUNP）；
BHUNP 是它的 SE 后继（Bakafactory / Haeun），同时支持物理与 BodySlide，且是 3BBB 体系。
两者 toolkit 不通用。详见 [`../03-body/unp-bhunp.md`](../03-body/unp-bhunp.md)。

## 排错

| 症状 | 判据（说明你把词认错了） | 处理 |
|---|---|---|
| 按教程搜不到某个 mod | 用了 LE 时代的行话（如 TBBP、slot）去找 SE 的东西 | 回到"前世今生"表判断属于哪个时代，换当代同义词再搜 |
| 装的是身形，却期待物理效果 | 把"身形"当成了"物理"（两者分属 L2 / L3） | 看 [`ecosystem-map.md`](ecosystem-map.md) 分层 |
| 想用 OBody 却发现没有可选预设 | 以为它自带预设；它消费的是你的 BodySlide `SliderPresets` | 先完成 Zeroed Sliders + Build Morphs 基础构建 |
| 换了 XPMSE 之后某件衣服消失 | 分区号与 ARMO/ARMA 的 biped 槽不一致 | 查 `.nif` 的 `BSDismemberSkinInstance` 分区设置 |

## 取舍与建议

- **查到词之后，一定要顺着链接进具体条目。** 本页只解决"这个词指什么"，不解决"怎么装"。
- **把同义词记 ARCHIVE 成一个家族** —— CBBE 系 / UNP 系 / 物理两条路线 —— 比逐个记词条有效得多。
- **遇到community 教程里的陌生词，先怀疑它是不是 LE 时代遗留下来的说法**，再决定要不要照做。
- **给疑虑留条后路**：本页标注为"社区一致"或"未确认"的项，请到
  [`../08-sources/unreliable-and-unconfirmed.md`](../08-sources/unreliable-and-unconfirmed.md) 看是否为已知讹传。

## 来源

- LoversLab 术语表（社区整理）：`https://www.loverslab.com/blogs/entry/16040-glossary` —— **社区经验**
- **Nexus 发布页描述与 Files 页（一手）**：RaceMenu `https://www.nexusmods.com/skyrimspecialedition/mods/19080`
  （`NiOverride` / `CharGen` / 版本要求由此确认）、BodySlide `https://www.nexusmods.com/skyrimspecialedition/mods/201`
  （5.9.1 起 "Write only a single BODYTRI extra data when building"）、
  FSMP `https://www.nexusmods.com/skyrimspecialedition/mods/57339`（作者与 fork 链、最后基于 SKSE 的版本）
- **GitHub README / 源码（一手）**：`https://github.com/ousnius/BodySlide-and-Outfit-Studio`（GPLv3+、2018-02 拆分 BS/OS）、
  `https://github.com/DaymareOn/hdtSMP64`（fork 链 HydrogensaysHDT → aers → Karonar1 → DaymareOn；GPL-3.0）
- **HDT-SMP 官方页把 `CBBE SMP (3BBB)` 与 `CBBE 3BBB (3BA)` 并列为可选 addon** —— **一手（发布页描述）**
- **3BA 作者归属为 Acro**：社区多源一致（含第三方 mod 的 credits 列表），
  但**本轮未在 Nexus 页面正文直接核实署名** → 标注为**待核实**
- **ECE / slot 时代的机制、 `.slot` 与 `CME_save` 的说法**：社区装机文档与 namu wiki —— **二手**
- **UBE 的 "Bungalow Body and Face" 俗称与"新增独立种族"定位**：Nexus UBE 发布页 —— **一手**
