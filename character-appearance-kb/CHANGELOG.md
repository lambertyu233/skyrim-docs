# CHANGELOG

本文件记录本资料库的结构与内容变更。条目自身的版本号见各自 frontmatter 的 `version` 字段。

## 2.1.0 — 2026-10-25

**新增条目 `04-physics/body-physics-tuning.md`（身体物理调参完全指南），全库 48 → 49 条。**

- 定位为**操作层手册**：引擎选型看 [physics-overview](04-physics/physics-overview.md)、
  mod 本身看 [cbpc](04-physics/cbpc.md)，本卷专讲"装好之后怎么调"。
- 内容：配置文件全家福（8 类文件逐一说明）、全局参数表（官方注释中译 + 调节方向）、
  3BA 逐骨骼参数族、幅度文件、主控映射（ConfigMap / MalePhysics / `< >` 链式排序）、
  碰撞球（球/胶囊格式、权重插值、Nifskope 拟合）、System.ini 性能项、
  条件配置（Conditions/Priority 语义与空壳校验）、Tuning.rate 实时调参工作流、
  "把乳摇调大"的目标→参数处方与乘数实例、Physics Editor 游戏内手段、排错表。

### 本轮新核实的一手材料（已写入该条目）

- **源码定案（CBPC 1.5 系 MIT 源码，Discrim0/CBPC-1.5-AE-AS）**：
  - `CBPConfig_3b.txt` 的**双值格式 = 体重 100 值 + 体重 0 值**，
    运行时 `GetPercentageValue(v0, v100, actorWeight)` 按体重线性插值——
    **纠正了"参考值+生效值"的流传误解**（只改第一个数 = 只改体重 100 的角色）；
  - 文件加载规则：`SKSE\Plugins\` 下所有 `CBPConfig` 前缀 + `.txt/.ini` 都被加载；
  - Conditions **先拆 AND 再拆 OR**（AND 绑定更紧）+ NOT 前缀；
    Priority 降序、同级 AND 项多者优先、先匹配先得；
  - 1.5.0 空壳校验（`IsConfigActuallyAllocated`）：条件配置未设
    stiffness/stiffness2/damping 或未移离 ±100 的 collision*offset 会被静默忽略；
  - `MalePhysics=0` 时男性自动跳过 breast/butt/belly/pelvis 及含
    breast/thigh/calf 的节点；`< >` 链式顺序执行的并行/抖动权衡。
- **Physics Editor（Nexus 186341，2026-07-25 首发）**：iMode 0/1/2/3、
  Hybrid 分部位组、`physicseditor actor <mode>`、bFitColliders 运行时拟合碰撞球、
  GUI 依赖 FLICK（Nexus 181603；mod 自带 ini 注释拼作 FUCK，系笔误）。
- **Tuning 周期重载 + 3BA gravityBias/gravityCorrection → 胸部抽搐重置**
  （LoversLab CBBE 3BBB 帖，多人确认；解法：调完关 Tuning.rate/TuningMode）。
- 自检四连全过：build_index 49 条 / validate 0 错误 / check_index_ui 34 项 /
  check_links 767 条全有效（全 LF）；工作区索引重建为 408 条。

## 2.0.0 — 2026-10-25

**全库 48 条目百科化改写：从「要点笔记」升级为「百科全书式条目」。**

### 改写标准

每个条目统一采用九段骨架：`速览（信息卡 + 要点）` → `前世今生` → `它解决什么问题`
→ `安装` → `使用与配置` → `兼容与冲突` → `排错` → `取舍与建议` → `来源`。
排错类条目改用 `速览 / 前世今生 / 成因（按频率）/ 排查顺序 / 修法 / 判断分叉点（别误诊）/ 来源`。
要求读者打开任一篇，即可看懂这个 mod 或这套机制的**来龙去脉**与**装用方法**。

### 规模

- 48 条目全部重写，总行数 **4336 → 12000+**；每条 `aliases` 补齐至 12~16 项（共约 400 项），
  交叉引用全部改为 markdown 相对链接（751 条，`check_links.py` 全通）。
- 所有条目 `version` 递增、`updated` 统一为 2026-10-25。

### 本轮新核实的一手材料（已写入对应条目）

- **RaceMenu**：Nexus Files 页完整 changelog（0.4.12→0.4.20.0），
  含 0.4.13 首加 `skee` 命令、0.4.19.11 为 OBody 加 `bEnableEarlyRegistration`、
  0.4.19.13 支持 1.6.640/GOG 1.6.659、0.4.19.16 支持 1.6.1170、0.4.20.0 部件标签 + GOG（untested）；
  credits 中 ECE Team（tktk / RAN46 / kaeper）与 ousnius 的角色；作者 2026-08-23 原帖（1.7.x 现状与 overlay NIF 崩溃根因）。
- **CBBE**：原名 **Caliente's Big Bottom Edition**、2011-12-04 首个配套服装、
  后由 Jeir 与 Ousnius 接手维护（作者访谈转载，标社区经验）。
- **UNP 家族**：Dimonized UNP（dimon99）→ UUNP → SE 时代 BodySlide 弃支持 →
  Legacy UUNP（43773）→ UNP Female Body Renewal（1699）→ BHUNP（31126，Bakafactory/BakaHaeun）。
- **HIMBO**：全称 Highly Improved Male Body Overhaul，作者 Kreiste，Nexus 46311，
  主体网格 CC-BY-SA-4.0，四枚全身滑块 Hugh/Hassan/Hideo/Hector。
- **UBE 2.0**：JohnyBungalow1 + lowresOutis，Nexus 92989（原条目误链 143045，已修正），
  "新种族"而非身体替换、全部服装需 .esp 补丁 + Outfit Studio 转换。
- **BodySlide**：仓库 2k+ 提交、GPL-3.0、2018-02 起拆分两个 exe、2026 年仍在活跃开发。
- **HDT-SMP / FSMP / CBPC / XPMSSE**：HDT-PE→SMP 继任关系、MIT 释源、
  FSMP 的 fork 链（HydrogensaysHDT→aers→Karonar1→DaymareOn）与 `smp` 命令组、
  CBPC 基于 polygonhell 的 CBP Physics（MIT）、XPMSE 5.00→5.06 完整 changelog。
- **OBody NG**：Aietos、CommonLibSSE NG 单 dll 通吃全版本、GPL-3、AI 使用政策；
  原版 OBody 是 RaceMenu BodyGen 的完全重写。

### 未确认事项

集中在 `08-sources/unreliable-and-unconfirmed.md` 第三节，按
「版本号 / 日期 / 归属 / 1.7.x 适配 / 文件字段」五类汇总 **68 项**；
其中 4 项本轮毕业（BHUNP 展开式、UBE 真实来源、HIMBO 作者 ID、RaceMenu 1.7.x 现状）。

### 结构维护

- 修 2 处失效相对链接（`face-headparts-resources` 误链 04-physics、
  `physics-overview` 误链同目录 cbbe-3ba）。
- 重建 `index.json` / `index.html`（48 条目）与工作区根 `index.html`（10 库 / 407 条）。
- `validate_kb.py` 0 错误、`check_index_ui.py` 34 项全过、`sync_scripts.py --check` 无分叉。

## 1.1.0 — 2026-09-22

**新增「运行时 morph 与离线烘焙」条目，并把该机制反向接入相关条目。**

### 新增

- `03-body/morph-runtime-vs-bake.md`（本库第 44 条目）：解释捏脸菜单里身形那一栏的**三层来源**、
  为什么拖滑块衣服会跟着变、为什么换 BodySlide 预设就穿模，以及
  `Zeroed Sliders` + `Build Morphs` + `Batch Build` 的正解工作流；
  并给出两套预设体系（`.xml` 0~100 / `.jslot` 浮点）不可互换的对照表。

### 修改

- `00-overview/morph-and-nif-basics.md`：新增「装备网格替换裸体网格」一节，写出两条变形路径。
- `03-body/bodyslide-presets.md`：补 `.xml` 每个滑块存体重 0/100 两值，以及与 `.jslot` 不通用的提示。
- `03-body/cbbe-3ba.md`：补它提供 `RaceMenuMorphs*.esp`（滑块名字的定义者）。
- `06-troubleshooting/clipping.md`：新增「根因：构建是烘焙，滑块是运行时」与「正解：Zeroed Sliders」两节。
- `05-distribution/obody-ng.md`：写清 Zeroed Sliders 基础构建是**前提条件**，且它读取 `SliderPresets`。
- `08-sources/unreliable-and-unconfirmed.md`：错误知识 10 条 → **13 条**；未确认事项 15 项 → **17 项**。
- `01-navigation/troubleshooting-index.md`（工作区入口索引）：新增「六、捏脸与身形」症状表（8 行）。

### 本条新增纠正的错误知识

11. **「RaceMenu 的 morph 滑块范围是 -1 到 +1」不准确** —— `.jslot` 存浮点（实测样例 `0.50000`），
    上限由 `RaceMenuMorphs*.psc` 的 `OnSliderRequest` 中 `Float factor` 决定（社区记录默认 `2.0`）。
12. **「BodySlide 预设可以直接当 RaceMenu 预设用」不成立** —— `.xml` 与 `.jslot`
    的格式、刻度、生效方式都不同，只能逐滑块手工换算。
13. **「手动拖 RaceMenu 滑块能改 NPC 身材」不成立** —— 运行时 morph 只作用于玩家。

## 1.0.0 — 2026-09-22

**首次建立。**

### 结构

- 新建资料库 `character-appearance-kb`，共 **43 条目 / 9 分类**：
  `00-overview`(5) / `01-prerequisites`(2) / `02-face`(8) / `03-body`(6) /
  `04-physics`(6) / `05-distribution`(3) / `06-troubleshooting`(6) /
  `07-workflow`(5) / `08-sources`(2)。
- 五件套脚本（`build_index.py` / `validate_kb.py` / `check_index_ui.py` /
  `check_links.py` / `fix_links.py`）从技能 stock 版逐字节复制；另附
  `fetch_mediawiki.py`（用于后续同步 UESP / CK wiki）。
- 生成 `index.json` 与 `index.html`（离线可搜索浏览器）。

### 内容要点

- **总览层**给出"五层结构"（前置框架 / 脸 / 身形 / 骨骼与物理 / 分配）与依赖方向，
  并写出两条互斥红线（女性身形只能一个；SMP 与 CBPC 争 body 插槽）。
- **版本对照表**以游戏版本为主键串起 SKSE64 / RaceMenu / Faster HDT-SMP。
- **脸部**覆盖 RaceMenu（含 CharGen / NiOverride / Sculpt / `skee` 命令）、
  `.jslot` 预设、High Poly Head、EFM 与 EFA、FaceGen 管线与 head parts、
  眼眉发须资源、Facelight、皮肤纹理。
- **身形**覆盖 CBBE、UNP 家族与 BHUNP、CBBE 3BA、BodySlide 与 Outfit Studio
  （含 `.osp` / `.osd` / SliderPresets 与官方 CLI 参数）、身形预设、身体皮肤。
- **物理**覆盖 HDT-PE / HDT-SMP / FSMP / CBPC 的原理差异、XPMSE 四类骨骼节点前缀、
  头发与衣物物理的机制限制。
- **分配**覆盖 RaceMenu BodyGen、OBody NG、AutoBody。
- **排错**六条：黑脸、脖缝、穿模、物理不生效、RaceMenu 滑块缺失、预设不生效。
- **安装实务**覆盖安装次序、MO2 左栏/右栏覆盖规则、Wabbajack、中文整合包现状、教程评估。

### 来源

一手来源为 Nexus 发布页描述正文、GitHub 官方仓库（BodySlide / hdtSMP64 /
Face-Discoloration-Fix / OBody-NG / autoBodyAE / SKSE64Plugins）、
UESP 与 Creation Kit wiki（经 MediaWiki API 抓取）。
社区经验来源为 Nexus 论坛、LoversLab、巴哈姆特、NGA、3DM，均在条目内标注。

### 本次明确纠正的错误知识（10 条）

1. RaceMenu **不依赖** PapyrusUtil（只要求 SKSE64）。
2. BodySlide CLI **不存在** `-o` / `-m` 参数。
3. High Poly Head 作者是 **KouLeifoh (KLF)**，不是 Kalilies。
4. `modding.wiki` **不托管** STEP 的 Skyrim SE 指南（应为 `stepmodifications.org`）。
5. HDT-SMP 的正确仓库是 **`hdt-skyrimse-mods`**（`hdt-skyrim-smp` 返回 404）。
6. **Skyrim Outfit System 不是身形分配工具**（是外观/换装系统）。
7. **SPID 的 Outfit Distribution 分配的是服装**，不是身形。
8. The Eyes of Beauty 的 **10.x 是 LE 版本号体系**，SE 官方移植是 1.2。
9. **CBPC 无法处理头发/衣服物理**，必须用 HDT-SMP / FSMP。
10. **"九大猫 / 醉梦 / 陶德"作为整合包名查无实据**，已在条目中标注未确认。

### 未确认事项

集中在 `08-sources/unreliable-and-unconfirmed.md` 第三节，共 15 项，
包括 CBBE / BHUNP / 3BA / CBPC 的当前最新版本、Brows 与 KS Hairdos 的版本口径、
Facelight Plus 的发布状态、AutoBody 与 OBody NG 的先后关系、CK 官方站停机导致
骨骼系统条目缺少一手官方引文等。

> **后续建议**：CK 官方 wiki 恢复后回补骨骼系统的一手引文；
> 在能访问 Nexus 文件页时复核各 mod 的最新版本号并把对应条目 `version` 递增。
