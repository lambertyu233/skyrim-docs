# 上古卷轴5 工具集资料库

Skyrim SE/AE 模改**工具链**的结构化知识库：从"让脚本 mod 能跑起来"的前置框架，
到排序、清理、打补丁、生成远景、诊断崩溃的整条流水线，
每题一条目、统一 frontmatter、可离线浏览与检索。

## 目录结构

| 目录 | 内容 |
|---|---|
| `00-overview/` | 工具链全景、按任务选工具、术语表 |
| `01-frameworks/` | SKSE64、Address Library、CommonLibSSE-NG、Papyrus 工具族、SkyUI / MCM |
| `02-distribution/` | SPID / KID / BOS（免冲突的运行时分发） |
| `03-managers/` | MO2、Vortex、Wrye Bash、Wabbajack |
| `04-loadorder/` | LOOT、xEdit、脏编辑清理、Bash Patch、Synthesis、zMerge、ESL 化 |
| `05-assets/` | NifSkope、Cathedral Assets Optimizer、BSA 工具、Blender/PyNifly、DDS 与贴图 |
| `06-lod/` | xLODGen、DynDOLOD、TexGen、遮挡生成 |
| `07-behaviour/` | 动画工具链总览、hkx 文件工具 |
| `08-creation/` | Creation Kit、Papyrus 编译/反编译、xEdit 脚本、编辑器插件、翻译工具 |
| `09-diagnostics/` | Crash Logger、Crash Log Analyzer、Engine Fixes、Scrambled Bugs、Papyrus/显示调优、FallrimTools |
| `10-audio/` | xVASynth、xVATrainer、FaceFXWrapper、Yakitori、配音链路 |
| `11-config/` | BethINI、PrivateProfileRedirector、配置文件体系 |
| `12-sources/` | 一手来源清单、不可信来源警示、常见错误认知 |

## 怎么用

**离线浏览**：双击 `index.html`（数据内联，无需服务器、无需联网）。
左侧按分类筛选，顶部可搜索；点卡片在页内展开全文。

**命令行检索**（推荐给 agent）：

```bash
KB="C:/Users/laptopyu/.workbuddy/binaries/python/versions/3.13.12/python.exe ../../scripts/kb.py"
$KB find 崩溃日志          # 找该读哪篇（返回路径 + 别名 + 摘要）
$KB show crash-logger-sse  # 元数据 + 标题大纲
$KB read crash-logger-sse  # 正文
```

跨库检索入口在工作区根的 `scripts/kb.py`；
手上有"症状"时优先读 `01-navigation/troubleshooting-index.md`。

## 内容边界

本库只覆盖**工具**这一层。以下主题在各自独立的库里，本库只做交叉索引：

- OAR 条件与 submod → `oar-kb`
- FNIS / Nemesis / Pandora → `behaviour-engine-kb`
- Community Shaders → `community-shaders-kb`
- Creation Kit 编辑器与 Papyrus 语言 → `creation-kit-kb`
- MO2 / USVFS 机制 → `mo2-usvfs-kb`
- 捏脸 / 身形 / 骨骼物理 → `character-appearance-kb`

## 维护

```bash
python scripts/build_index.py     # 重建 index.json / index.html
python scripts/validate_kb.py     # 结构 + 索引 + 别名 + 模板校验
python scripts/check_index_ui.py  # 索引页交互回归
python scripts/check_links.py     # 站内相对链接
```

改条目请**保持 frontmatter 字段完整**并递增 `version`；
新增条目请一并写 `aliases`（见 `CONTRIBUTING.md`）。
`scripts/` 下的五件套是技能 `build-maintainable-kb` 的副本，
**不要在本库内单独改**，改完技能要跑 `scripts/sync_scripts.py` 同步。

## 来源与版权

条目来源为**官方 wiki / 官方文档 / 官方仓库 README / Nexus 发布页描述正文 / 作者本人说明**，
逐条在 `source` 字段标注。各工具与文字版权归各自作者所有；
本库是结构化整理与出处汇编，关键数值均标注来源，仅供学习与协作维护。
