# 上古卷轴5 捏脸与身形资料库

Skyrim SE/AE 的**人物外貌改造**知识库：把"捏脸"和"身形/身型"这条链
拆成五层（前置框架 → 脸 → 身形 → 骨骼与物理 → 分配），逐层整理、标出处、可长期维护。

- **44 个条目 / 9 个分类**
- 每个条目一个 Markdown + 统一 frontmatter
- 双击 `index.html` 即可离线浏览与搜索（无需服务器）

---

## 怎么读

### 用离线浏览器（推荐给人看）

直接双击 **`index.html`**：左侧分类过滤、右上搜索框、点卡片出详情（整篇正文已渲染）。
分类标签、页头标题都从 `manifest.json` 读取。

### 用检索脚本（推荐给 agent）

本工作区根目录有 `AGENTS.md` 作为 agent 入口契约，并提供跨库检索脚本：

```bash
KB="C:/Users/laptopyu/.workbuddy/binaries/python/versions/3.13.12/python.exe scripts/kb.py"
$KB list                          # 有哪些库
$KB toc character-appearance-kb   # 本库的分类地图
$KB find AttackState 条件          # 检索（返回路径 + 别名 + 摘要）
$KB show racemenu                 # 元数据 + 标题大纲
$KB read racemenu                 # 正文
```

> ❌ **不要读 `index.json` / `index.html`** —— 它们内联了每条正文的渲染 HTML，
> 一次读入等于把整个库塞进上下文。

### 按需求走（不想读全部）

| 你的情况 | 从这里开始 |
|---|---|
| 刚接触，不知从哪下手 | `00-overview/learning-path.md` |
| 名词看不懂 | `00-overview/glossary.md` |
| 版本对不上（SKSE/RaceMenu 报错） | `00-overview/version-matrix.md` |
| 只想捏脸 | `02-face/racemenu.md` |
| 想改身形 | `03-body/` 下的 `cbbe.md` / `unp-bhunp.md` / `cbbe-3ba.md` |
| 镜像/身形滑块不生效 | `03-body/bodyslide-outfit-studio.md` |
| 拖滑块衣服跟着变、换预设就穿模（原理） | `03-body/morph-runtime-vs-bake.md` |
| 想做物理 | `04-physics/physics-overview.md` |
| 想让 NPC 有不同身材 | `05-distribution/` |
| **已经出故障了** | `06-troubleshooting/` |
| 想知道该装什么顺序 | `07-workflow/install-order.md` |

---

## 分类

| 目录 | 主题 | 条目数 |
|---|---|---|
| `00-overview` | 总览：生态地图、术语表、版本对照、学习路径、NIF/morph 机制 | 5 |
| `01-prerequisites` | 前置：SKSE64 / Address Library、SKSE 插件框架 | 2 |
| `02-face` | 捏脸：RaceMenu、预设、高模头、EFM/EFA、FaceGen、眼眉发须、补光、皮肤 | 8 |
| `03-body` | 身形：CBBE、UNP/BHUNP、3BA、BodySlide、预设、身体皮肤、**运行时 morph vs 离线烘焙** | 7 |
| `04-physics` | 骨骼与物理：总览选型、XPMSE、HDT-SMP、FSMP、CBPC、头发衣物物理 | 6 |
| `05-distribution` | NPC 分配：BodyGen、OBody NG、AutoBody | 3 |
| `06-troubleshooting` | 排错：黑脸、脖缝、穿模、物理失效、滑块缺失、预设不生效 | 6 |
| `07-workflow` | 安装实务：次序、MO2 覆盖、Wabbajack、中文整合包、教程评估 | 5 |
| `08-sources` | 来源：一手来源清单、不可信来源与未确认事项 | 2 |

---

## 证据纪律（本库的硬规矩）

条目里的结论分四类，**转述时不要混同**：

| 标记 | 含义 |
|---|---|
| **一手** | 发版者本人维护的材料：Nexus 发布页描述、GitHub README/源码、官方 wiki、作者帖 |
| **社区经验** | 论坛帖、reddit、指南站；多帖一致时会注明 |
| **未确认** | 检索未取得可靠来源，**不可当作现状陈述** |
| **本工作区实测** | 撰写时实际访问/比对得出的结论 |

**不使用** CSDN、toolify、AI 聚合站、内容农场作为事实来源。
判据见 `08-sources/unreliable-and-unconfirmed.md`（含已知错误知识清单与未确认事项清单）。

---

## 维护

### 自检四连

```bash
PY="C:/Users/laptopyu/.workbuddy/binaries/python/versions/3.13.12/python.exe"
$PY scripts/build_index.py     # 重建 index.json / index.html
$PY scripts/validate_kb.py     # 结构 + 索引 + 别名 + 模板校验（0 错误才过）
$PY scripts/check_index_ui.py  # 索引页交互回归（内部调 Node，无需浏览器）
$PY scripts/check_links.py     # 站内相对链接 lint
```

改过目录或移动过文件后，**必须**再跑 `check_links.py`（坏链不会让构建失败）。
动过 `scripts/` 里的脚本后，在**工作区根**跑 `scripts/sync_scripts.py` 同步到所有库。

### 硬约束（踩过的坑）

1. **条目必须放在带 `NN-` 前缀的分类子目录**。`build_index.py` 会跳过库根层，
   条目写在库根会被**静默丢掉**（输出 `0 entries` 却不报错）。库根只放
   `manifest.json` / `index.*` / `README.md` / `CHANGELOG.md` / `CONTRIBUTING.md`。
2. **`category` 字段必须与所在目录名严格相等**。写成短名（`face` 而非 `02-face`）
   只会让页面分类标签变空，**不报错**。
3. **改页面一律改 `scripts/build_index.py` 的模板再重建**，不要手改 `index.html`。
4. 文件一律 **LF** 换行。

### 新增一个条目

1. 在对应分类目录新建 `<id>.md`（`id` 与文件名一致，小写连字符）；
2. 写 frontmatter（必填 `id` / `title` / `category` / `version` / `updated` /
   `tags` / `source` / `summary`）；
3. **补 `aliases`**：写"别人真会敲进去的**短查询**"，别写整句，别抄 `tags`
   （`tags` 说"属于什么主题"，`aliases` 说"别人会用什么词来找"）；
4. 结论标可信层级，**引用落到 URL 或条目路径**；
5. 跑上面的自检四连。

---

## 版权

各 mod、工具、贴图与文字版权归各自作者所有
（BodySlide 为 GPLv3+、HDT-SMP 为 MIT、Face Discoloration Fix 为 MIT）。
本资料库为**结构化整理与出处汇编**，关键数值均标注来源，仅供学习与协作维护。
