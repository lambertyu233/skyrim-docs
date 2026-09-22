# CHANGELOG

本文件记录本资料库的结构与内容变更。条目自身的版本号见各自 frontmatter 的 `version` 字段。

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
