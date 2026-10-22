# 上古卷轴5 环境美化资料库

Skyrim SE/AE 环境美化（画质/材质/地形/植被/水体/天气光照）生态的结构化知识库。

## 内容分层

| 分类 | 管什么 |
|---|---|
| `00-overview` | 六层生态地图、选型总纲、收录边界 |
| `01-principles` | 视差与 Complex Material、DDS 压缩格式、VRAM 与 ENBoost、LOD 层级原理 |
| `02-textures` | SMIM、Skyland AIO、Skyrim 202X、Noble、aMidianBorn、RUSTIC、Vivid Landscapes、选型原则 |
| `03-landscape` | Majestic Mountains、Blended Roads、Terrain LOD Redone、Cathedral Landscapes、Skyrim 3D Landscapes |
| `04-flora` | 树木 overhaul（HLT/Aspens/NOTWL/SFO）、草类生态、草地 INI、NGIO、Landscape Fixes |
| `05-water` | Realistic Water Two、Water for ENB、Pure Waters |
| `06-weather-lighting` | 天气 mod 生态、Obsidian、Cathedral Weathers、ELFX、Lux 系、Embers XD |
| `07-mesh-tools` | SSE NIF Optimizer、Cathedral Assets Optimizer、xLODGen、DynDOLOD |
| `08-practices` | 安装顺序与冲突、LOD 生成流程、INI 设置、ENB 预设与 CS 衔接、性能预算 |
| `09-troubleshooting` | 视差异常、白块 glitch、水缝与 LOD 条纹、VRAM 耗尽、草地异常 |
| `10-sources` | 作者归属勘误、不可信来源、过时与改名页面 |

## 与工作区其它库的分工

- 渲染框架本体（Community Shaders 功能/安装/版本）在 `community-shaders-kb`，本库只讲"选哪个 ENB 预设 / 何时迁 CS"。
- 角色外观（捏脸/身形/骨骼）在 `character-appearance-kb`。
- MO2/Vortex 覆盖机制、USVFS 在 `mo2-usvfs-kb`，本库只引结论。
- SKSE/Address Library/Engine Fixes 版本对应在 `skyrim-tools-kb`。
- 动画/战斗框架在 `combat-animation-kb` / `behaviour-engine-kb`。

## 来源纪律

条目结论分三级标注：**一手源**（Nexus 发布页/文件页/日志、作者回帖、官方仓库、官方站）、**社区经验**（STEP/Nolvus/sinitar 等指南、论坛）、**未核实/存疑**。**不用 CSDN、toolify 一类内容农场与 AI 聚合站**；镜像站的转录只用于定位，事实一律回 Nexus 文件信息页。建库时已逐条核实作者与 Nexus ID，勘误表见 `10-sources/author-attribution-corrections.md`。

## 维护

新增条目放对应 `NN-` 分类目录，frontmatter 照现有条目抄（`category` 必须与目录名严格相等，`aliases` 写"别人会敲的短查询"）。改完跑：

```bash
python scripts/build_index.py      # 重建索引
python scripts/validate_kb.py      # 结构 + 索引 + 别名规范
python scripts/check_index_ui.py   # 索引页交互回归
python scripts/check_links.py      # 站内链接（新增/移动条目后必跑）
```

工作区级入口：根目录 `AGENTS.md` + `scripts/kb.py`（list/toc/find/grep/show/read/check）。
