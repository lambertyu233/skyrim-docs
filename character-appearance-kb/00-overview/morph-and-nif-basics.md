---
id: morph-and-nif-basics
title: 底层机制：NIF、morph 与 .tri——滑块为什么能改变体型
category: 00-overview
kind: concept
version: 2.0.0
updated: 2026-10-25
tags: [总览, 机制, NIF, morph, tri, 原理]
aliases: [morph 原理, tri 文件, nif 格式, bodytri, 滑块原理, 网格机制, BSTriShape, BSDismemberSkinInstance, 顶点位移, conform, nif 是什么, morph 是什么, 为什么滑块能改体型, FaceGen 和 morph 区别]
source: https://github.com/ousnius/BodySlide-and-Outfit-Studio
summary: 讲清"滑块为什么能改变体型"这条唯一主线：NIF 网格容器与 BSTriShape、morph 的顶点位移数学、.tri 与 BODYTRI 的配合、RaceMenu 在运行时做了什么，以及 FaceGen 为什么是另一套；并补齐从 ECE 的 slot morph 到 skee/NiOverride 再到 Build Morphs 的演化。
---

# 底层机制：NIF、morph 与 .tri

不懂这一层，就只能"照着教程点"，出了偏差也不知道错在哪一步。本页是本库所有
"为什么我装了没反应"类问题的**最终解释层**。

## 速览

| 字段 | 内容 |
|---|---|
| 作用层 | **文件格式 + 变形机制**（不涉及某个具体 mod，但解释所有身形/捏脸现象） |
| 依赖 | BodySlide 产生数据；RaceMenu（`skee64.dll`）在运行时消费数据 |
| 影响范围 | 玩家体型、服装贴合、NPC 体型、部分皮肤-tone 与 overlay 效果 |
| 关键限制 | **运行时 morph 只影响玩家**；NPC 只能靠离线烘焙或分配工具 |
| 易混点 | FaceGen（预生成头数据）不是 morph；物理（骨骼模拟）不是 morph |
| 版本敏感性 | 中 —— NIF 解析本身受游戏版本影响（2026-08 起出现过 NIF 边界情况崩溃，见下） |

要点：

- **NIF 是容器**：身体、头、衣服都是 NIF，里面装着形状、着色器、骨骼绑定、物理信息。
- **morph 就是一组顶点位移向量**：滑块 = 权重，最终网格 = 基础网格 + Σ(morph × 权重)。
- **`.tri` 存 morph 目标，NIF 里的 `BODYTRI` 指向它** —— 两者都由 BodySlide 勾 `Build Morphs` 产出，缺一不可。
- **两条变形路径互不替代且叠加**：离线烘焙决定"起点"，运行时 morph 往起点上叠加。**起点不一致 = 穿模。**
- **FaceGen 是引擎另一套预生成机制**，NPC 的脸永远来自它 —— 这是很多"为什么不影响 NPC"类问题的答案。
- **装备不是套在身体外的布，而是替换裸体网格** —— 这一条决定了整个身型问题的唯一判据。

## 前世今生

这套机制是**三条线索汇合**的结果，把它们分别看，很多今天的怪现象才有解释。

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 时代 | NIF（NetImmerse Format）作为 Bethesda 的 3D 容器；身体形状节点为 **`NiTriShape` + `NiTriShapeData`**（几何数据分离） | 网格可以被工具读写，替换身形=替换 nif |
| 2012-03-15 | **ECE（Enhanced Character Edit）** 在 Nexus 发布 | 靠 `characterMakingExtender` 插件 + **slot 存档**（`CME_save` 目录、"Slot Load" 滑块）实现捏脸保存 —— 这是"morph 式捏脸"的雏形，但**只在脚本层、槽位有限** |
| LE 中期 | BodySlide 出现（Fallout 4 页更早，2015-12-24；SE 页 2016-11-02） | "把滑块烘进网格"成为标准做法 |
| LE 中后期 | **NiOverride / CharGen**（expired6978）出现，把 morph 与 tint 叠加做成**运行时 API** | 从"烘进去"进化到"运行时叠上去"；后来这两个组件随 RaceMenu 一同进入 SE |
| 2016-10 | SE 发布，形状节点改为 **`BSTriShape`**（形状与几何数据合并成单块） | 所有 LE 资产需要转换；也是今天"LE 网格不能直接用"的根因 |
| 2018-08-05 | **RaceMenu SE 页面首传**（含 `skee64.dll`，内含 NiOverride 与 CharGen） | SE 终于有了统一的运行时 morph 能力；其发布页 credits 明确致谢 ECE Team 的 ECE Morphs |
| 2018-02-20 / 11-25 | BodySlide 与 Outfit Studio 拆成两个可执行文件（配置分离）；随后"记住 `Build Morphs` 勾选状态"进入配置 | `Build Morphs` 从临时选项变成常规工作流的一部分 |
| 2026-04 | RaceMenu 0.4.20.0 加入 **Head part 标签系统**（`Data/SKSE/Plugins/CharGen/Tags/<MODNAME>/parts.json` 等） | 运行时能力继续扩展到 **metadata 层**（不再只是顶点） |
| 2026-08 | **BodySlide 5.9.0** 起写入**单一一条 BODYTRI**（清掉错误路径的残留）；**5.9.1** 进一步为锁定法线的形状写入 `LOCKEDNORM`，防止 RaceMenu 在不应重算的地方重算法线 | 侧证了"`BODYTRI` 只能有一条、且路径必须对"这条机制至今仍在被打磨 |
| 2026-08 | Bethesda 的 1.7.x 改坏了 NIF 解析的一个边界情况：**含 `NiTriShape` 但没有 `NiTriShapeData` 的网格会崩**，而 RaceMenu 的 overlay nif 恰好全是这种 | 说明"文件格式细节"至今仍能直接影响能否进游戏 |

### 一句话演化脉络

> **ECE 的 slot morph（脚本层/有限槽位） → skee / NiOverride 的运行时叠加（原生、可作用任意网格） →
> BodySlide 的 `Build Morphs`（把 morph 数据从" menu 里临时调"变成"落盘给运行时用"）。**

今天的完整链路就是这三段接起来的：**BodySlide 产出数据 → NIF 用 `BODYTRI` 指过去 →
RaceMenu 在运行时读 `.tri` 并按滑块权重叠加到顶点上。**

## 它解决什么问题

- **"为什么我装了身形 mod 却还是原版身材"** → 因为"装"不等于"用了"："装"只是把 nif 放进去，
  **滑块的产生需要构建**（`.tri` + `BODYTRI`）。
- **"为什么拖滑块身体和衣服一起变"** → 因为两者**共用同一套 morph 名字**（conform 带来的），
  NiOverride 遍历身上所有含同名 morph 的网格一起施加位移。
- **"为什么换了预设就穿模"** → 因为 Build 是**离线烘焙**，它改写的是 nif 的顶点坐标（起点），
  而你只重烘了身体没重烘衣服。
- **"为什么调好的身材 NPC 没有"** → 因为运行时 morph 只作用于玩家。

## 配置与使用

这一节是"怎么用手验证本页讲的东西"：

1. **检查某个网格有没有 morph 入口**：用 NifSkope 打开 `femalebody_0.nif`，找 NIF 根节点上的
   extra data 是否有一条 **`BODYTRI`**，看它指向的 `.tri` 路径是否存在。
   *没有 `BODYTRI` ⇒ 引擎找不到 morph ⇒ 那一栏滑块不会出现。*
2. **让 morph 出现**：BodySlide 里勾选 **`Build Morphs`** 后 Batch Build。
   （Group Filter 记得勾 `Unassigned`，很多服装默认在这个组。）
3. **确认 RaceMenu 侧的开关**：`SKSE\Plugins\skee64` 下的配置里 `bEnableBodyMorph=1`；
   `bEnableBodyGen` 是另一回事（随机分配，**与本页的 morph 不是一回事**）。
4. **验证**：进游戏打开捏脸界面，找到那一栏身形滑块；拖动时身体**与衣服一起**变化即为成功。
5. **检查 morph 是否被保存**：morph 状态存在 SKSE co-save 里，换 mod 后旧存档的 morph 可能对不上 ——
   排查时用一个新档对比是最省事的二分法。

> 如果想一次看懂"两条路径"的全部推论，直接读
> [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

## 工作原理

### 一、NIF 是网格容器

**NIF（NetImmerse Format）** 是 Creation Engine 的 3D 资产格式，可包含网格、着色器、骨骼、
动画与物理信息。**身体 / 头部 / 服装都是 NIF。**

关键差异：

| 游戏 | 身体网格的形状节点 |
|---|---|
| Skyrim LE | `NiTriShape` + 挂一个 `NiTriShapeData`（几何数据分开） |
| **Skyrim SE / AE** | **`BSTriShape`**（把形状与几何数据合并成单块） |

> 这个差异有实际后果。RaceMenu 作者记录过：某个游戏版本更新后，
> **`NiTriShape` 不带 `NiTriShapeData` 会导致崩溃**，因此新版 overlay NIF 被重新打包进 BSA。
> 也就是说，"网格格式的细节"是会直接影响能否进游戏的。

#### 蒙皮网格还要一个东西

可被骨骼摆动的网格（身体、衣服）额外挂 **`BSDismemberSkinInstance`**，它包含两件事：

1. **顶点权重**（每个顶点受哪些骨骼影响、权重多少）—— 这就是 "`Bone Weight Fix`" 在修的东西；
2. **Partitions（身体部位分区）**：裸体 = `SBP_32_Body`，手 = `33`，脚 = `37`。
   **分区号必须与 ARMO / ARMA 记录里的 biped 槽一致，否则该部分不显示。**

### 二、morph：滑块的数学本质

**morph 就是一组顶点位移向量。** 一个 morph 描述"当这个滑块 = 100 时，每个顶点要移动多少"。

```
运行时实际显示的网格 = 基础网格 + Σ(各 morph × 该滑块权重)
```

所以：

- 基础网格 + 滑块值 = 你最终看到的体型；
- **这也解释了为什么"手动把滑块拉到极限会破网格"** —— 位移是线性叠加的，超出设计范围就会自交。

### 三、`.tri` 与 BODYTRI：morph 怎么被游戏找到

| 环节 | 谁产生 | 谁消费 |
|---|---|---|
| `.tri` 文件（morph 目标数据） | **BodySlide**（勾 `Build Morphs` 时生成） | RaceMenu 的 NiOverride / 游戏引擎 |
| NIF 里的 **`BODYTRI` extra data** | **BodySlide**（同一次构建写入） | 引擎（据此找到对应 `.tri`） |

**因此**（三种失败模式，这是"滑块突然消失"的全部真相）：

- 不勾 `Build Morphs` → 没有 `.tri` → **RaceMenu 里看不到身形滑块**；
- 只生成了 `.tri` 但 NIF 没有 `BODYTRI` → 引擎找不到 → 同样无效；
- 构建被另一个 mod 的 NIF 覆盖 → 你的 `BODYTRI` 也没了（**第三条是最常见、也最难想到的**）。

BodySlide 的官方 Changelog 里有两条佐证：**5.9.0** 起 "Write only a single BODYTRI extra data
when building (removes leftovers with wrong paths)"；**5.9.1** 起还会为锁定法线的形状写入
`LOCKEDNORM`，"Prevents RaceMenu from regenerating normals where it should not"。

### 四、RaceMenu 在运行时做什么

RaceMenu 的核心是 **`skee64.dll`**，它内含 **NiOverride** 与 **CharGen** 两个模块：

- **NiOverride**：运行时往网格上叠加 morph / 纹理覆盖（overlay）/ 着色；
- **CharGen**：角色创建界面本身（也就是"滑块界面"）。

> 补充：二者的合并过程发生在更早的 PC 版 RaceMenu 上（社区记录提到 RaceMenu 2.5 起内置 CharGen
> 核心部分；本库早前的说法是 2.7+ 起完全并入本体）—— **版本号区间为二手记载，未确认**，
> 但对 SE 用户而言结论不变：**SE 的 RaceMenu 不需要任何额外组件。**

因为 NiOverride 能在**运行时**改网格，所以：

- 滑块能即时预览；
- 预设能在游戏内应用、能发给 NPC；
- **但也意味着 morph 状态是存在存档（SKSE co-save）里的** —— 换 mod 后旧档的 morph 可能对不上。

### 五、FaceGen 是另一套机制（别混）

脸不是靠 morph 实时生成的：

- **FaceGen** 是引擎**预生成**的头部数据，来自 Creation Kit 的 `Ctrl+F4` 导出；
- 玩家角色在 RaceMenu 里可以临时用 morph 调整并导出成 FaceGen；
- **NPC 的脸永远是预生成的**（这也是 EFM 只影响玩家、不影响 NPC 的根本原因）。

详见 [`../02-face/facegen-pipeline.md`](../02-face/facegen-pipeline.md)。

### 六、装备网格替换裸体网格

一条容易被忽略、但决定了整个身型问题的机制：

> **Skyrim 里「穿衣服」不是给身体套一层布，而是用装备网格直接替换裸体网格。**
> 装备本身就是「一具穿好衣服的身体」。

推论只有一个：**所有网格（裸体 + 每一件衣服）的顶点形状必须一致**。谁不一致，谁穿模。

而「形状」由两条互相独立的路径决定：

| 路径 | 何时算 | 改不改文件 | 影响谁 |
|---|---|---|---|
| **离线烘焙**（BodySlide Build） | 你点 Build 的那一刻 | **改**：数值写进 `.nif` 的顶点坐标，成静态模型 | 所有用这个网格的人（含全部 NPC） |
| **运行时 morph**（RaceMenu / NiOverride） | 游戏运行中 | 不改，只是临时形变 | **只影响玩家** |

**两者是叠加的**：先烘出一个「起点形状」，再在运行时往它上面叠 morph。
所以只要起点不一致，运行时怎么调都会错位 —— 这就是「换了预设衣服就穿模」的根源。

展开见 [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

## 排错

症状 → 判据 → 处理：

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 捏脸界面里根本没有身形滑块那一栏 | 缺 `.tri` 或 NIF 里缺 `BODYTRI` | BodySlide 勾 `Build Morphs` 重新 Batch Build；见 [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md) |
| 之前有滑块，装了某个服装/身形 mod 之后没了 | 该 mod 的 nif **覆盖**了你的构建产物（`BODYTRI` 丢失） | 提高自己构建产物的优先级，或重新构建；见 [`../07-workflow/mo2-override-rules.md`](../07-workflow/mo2-override-rules.md) |
| 拖滑块身体变了但衣服没变 | 这件衣服**没有同源 morph**（未做 conform / 属于别族身形） | 换同族服装或在 Outfit Studio 里 conform；见 [`../06-troubleshooting/clipping.md`](../06-troubleshooting/clipping.md) |
| 换 BodySlide 预设之后衣服穿模 | 只重烘了身体，没 Batch Build 全部服装 | Zeroed Sliders + `Build Morphs` + Batch Build 全套重做 |
| 装了身形但游戏里还是原版 | 从未 Build 过（只有 nif 没有 morph 数据，或 Base Shape 就没替换） | [`../03-body/bodyslide-outfit-studio.md`](../03-body/bodyslide-outfit-studio.md) |
| 玩家身材好看、NPC 千篇一律 | 运行时 morph 只作用于玩家（这是设计） | 走分配工具 [`../05-distribution/obody-ng.md`](../05-distribution/obody-ng.md) 或烘焙给 NPC |
| 更新到 1.7.x 后进游戏/进捏脸就崩 | 旧的 overlay nif 触发 NIF 解析边界崩溃 | 删除那 8 个残留文件；见 [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md) |
| 某件衣服穿上去有一部分不显示 | partition 分区号与 ARMO/ARMA 的 biped 槽不一致 | 检查 `BSDismemberSkinInstance` 的分区设置 |

## 取舍与建议

- **先把"两条路径"记住**：面对任何身型问题，第一句都该问"它落在哪条路径上"。
- **优先使用 Zeroed Sliders 起构建**：把起点统一到零，把所有形状交给运行时 morph —— 这是唯一
  能一劳永逸避开"换预设就穿模"的做法（代价是 `.tri` 文件占用空间变大）。
- **不要把 BodySlide 预设与 RaceMenu 预设当成同一种东西**：前者 `.xml`（体重 0/100 两个值、烘焙），
  后者 `.jslot`（浮点、运行时）。两者**不能互相导入**。
- **排查务必用新存档做对照**：morph 状态存在 co-save 里，旧档本身就是混淆源。
- **理解 FaceGen 的独立性**，能省掉大量无用功：想改 NPC 的脸，走 FaceGen/贴图路线；
  想改 NPC 的身体，走烘焙或分配路线。
- **不要指望 morph 解决物理**：morph 是顶点位移（静态/半静态），物理由骨骼与 DLL 模拟，两者完全独立。

## 来源

- **NIF / `BSTriShape` / `BSDismemberSkinInstance` / SBP 分区号**：Beyond Skyrim「Arcane University」NIF 技术文档 —— **社区权威技术文档**
  （原文另见：`https://wiki.beyondskyrim.org/wiki/Arcane_University:NetImmerse_Format`）
- **`.tri` + `BODYTRI` + `Build Morphs`、"单条 BODYTRI"、`LOCKEDNORM`**：
  BodySlide Nexus `Files`/`Changelogs` 页（5.9.0、5.9.1 条目）与 GitHub 仓库提交 —— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/201` · `https://github.com/ousnius/BodySlide-and-Outfit-Studio`
- **`NiTriShape` / `NiTriShapeData` 崩溃与 overlay NIF 需要重打包**：RaceMenu 作者 Nexus 置顶帖（2026-08-23）—— **一手（作者本人）**
- **NiOverride / CharGen 属于 `skee64.dll`；0.4.20.0 的 Head part 标签路径
  `Data/SKSE/Plugins/CharGen/Tags/<MODNAME>/parts.json`**：RaceMenu 发布页与帖子 —— **一手**
- **morph = 顶点位移、基础网格 + Σ(morph × 权重)**：由 BodySlide wiki 的滑块机制说明与 NiOverride 行为归纳 —— **一手机制 + 本工作区归纳**
- **NPC 脸是预生成、EFM 只影响玩家**：EFM Nexus 发布页描述 —— **一手**
- **ECE 的 slot 机制（`CME_save`、"Slot Load" 滑块）与其发布时间 2012-03-15**：modder 博客记载与社区装机文档 / namu wiki —— **二手**
- **CharGen Extension "2.5 起内置核心 / 2.7+ 完全并入本体" 的具体版本号**：社区记载 —— **未确认**
