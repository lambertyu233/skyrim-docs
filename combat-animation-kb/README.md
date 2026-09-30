# 上古卷轴5 动作系统资料库

Skyrim SE/AE 动作（战斗）系统生态的结构化知识库。

## 内容分层

| 分类 | 管什么 |
|---|---|
| `00-overview` | 五层生态地图 + 攻击框架选型（现在是 BFCO 的时代） |
| `01-frameworks` | 攻击动作框架：SkySA/ABR（一代）→ MCO（二代）→ BFCO（三代） |
| `02-foundations` | 行为引擎与运行时插件：Pandora/Nemesis 选型、OAR 生态、Payload Interpreter、Key Utils/DMK、BDI、AMR/AMF |
| `03-dodge` | 闪避：TK Dodge 家族、DMCO、IFrame Generator RE |
| `04-poise` | 韧性与硬直：MaxsuPoise、Modern Stagger Lock、Valhalla、POISE |
| `05-block-parry` | 格挡与弹反：Elden Parry/Counter、MaxsuBlockOverhaul、双持格挡、Inpa Sekiro |
| `06-ai-camera` | 战斗 AI、碰撞与视角：SCAR、Precision、TDM、SmoothCam |
| `07-movesets` | 动作包（招式库）：Elden Rim、For Honor in Skyrim、Stances 等 |
| `08-compatibility` | BFCO 不兼容清单、版本地雷、装完动作包的刷新流程 |
| `09-sources` | 常见错误说法与未核实项 |

## 与工作区其它库的分工

- 行为引擎本体（FNIS/Nemesis/Pandora 的机制、格式、排错）在 `behaviour-engine-kb`，本库只留**选型结论**与指针。
- OAR 条件/结构/编辑器在 `oar-kb`，本库只把 OAR 当作"框架生态里的一个成员"引用。
- 装哪个工具、版本对不对在 `skyrim-tools-kb`。

## 来源纪律

条目结论分三级标注：**一手源**（GitHub README / Nexus 发布页正文 / 作者回帖）、**社区经验**（论坛帖、镜像站）、**未核实**。所有"不兼容"结论都尽量引自官方 description 原文。检索用工作区根的 `scripts/kb.py`。

## 维护

新增条目放对应 `NN-` 分类目录，frontmatter 照现有条目抄（`category` 必须与目录名严格相等，`aliases` 写"别人会敲的短查询"）。改完跑 `scripts/build_index.py` → `validate_kb.py` → `check_index_ui.py` → `check_links.py`。
