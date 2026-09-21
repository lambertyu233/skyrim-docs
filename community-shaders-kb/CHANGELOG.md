# Changelog

本文件记录资料库的版本化演进。版本号采用 `主.次.补` 形式：
- **主版本**：结构/分类/ schema 重大调整；
- **次版本**：新增分类或一批条目、重要内容扩充；
- **补版本**：条目修订、修正、小补充。

---

## [2.0.0] - 2026-09-21

**与 `build-maintainable-kb` 技能模板完全对齐**：不再维护本库的私有构建分支。**知识内容（各条目的标题、正文、摘要、标签、来源）一字未改。**

### 重大变更（索引数据结构）

- `index.json` 顶层由 `{meta:{...}, entries:[...]}` 改为扁平结构 `{generated, total, by_category, entries}`。
- `by_category` 的键由**中文标签**（`"功能": 47`）改为**分类目录名**（`"02-features": 47`）。
- 条目改用内联渲染后的正文 `content`，并新增 `_file`（相对路径）与 `_chars`；移除 `category_label` 与 `path`
  （页面改为用目录名现查中文标签）。`index.json` 由约 34 KB 增至约 112 KB。
- `generated` 改为构建当天日期。此前是**硬编码的 `2026-09-20`**，重建也不会更新。

### 修复（数据）

- **修正 47 个功能条目的 frontmatter**：`02-features/core`（28 个）与 `02-features/additional`（19 个）下的条目
  此前写的是 `category: features`，与所在目录名 `02-features` 不一致。旧构建脚本用目录名兜底，所以这个错一直没暴露；
  新脚本按 frontmatter 取值，该值在分类标签表里查不到 → 页面上这些条目的分类标签会渲染成空。
  现已全部改为 `category: 02-features`。改动经逐行比对确认**每个文件只有这一行变化**，CRLF 换行与其余内容原样保留。

### 变更（工具链）

- `scripts/build_index.py` 替换为技能 stock 版（与技能副本逐字节一致），本库的私有页面分支作废。
- `manifest.json` 改为新结构：`name` / `description` → 嵌套 `kb.name` / `kb.description`；
  `categories[].key` / `label` → `dir` / `title`；`tooling` 补录两个校验脚本；schema 字段说明同步更新。

### 移除（按维护者要求，换取与新版结构一致）

- 侧栏「状态过滤」按钮组（全部状态 / 已发布 / 开发中）及对应筛选逻辑；
- 条目卡片与详情页的 `kind`（核心 / 附加）、`status`（TBA）徽章，及 `.b-core` / `.b-add` / `.b-tba` 样式；
- 索引字段 `category_label` 与 `path`。

> frontmatter 里的 `kind` / `status` **保留不删**（数据仍在，只是页面不再呈现）。
> `scripts/gen_features.py` 也保留（它是这 47 个条目的生成源），但已属遗留工具——它原本写出的 `category: features`
> 已在本版修正，之后再用它新增条目请手动确认该字段为完整目录名。

### 验证

- `validate_kb.py` → **0 错误**（此前针对旧结构打印的 2 条 NOTE 已随之消失）；`check_index_ui.py` → **20 项断言全过**。
- 另做**反向验证**：故意把 1 个条目改回 `category: features` → 校验器报错并退出 1；把 manifest 的某个目录声明删掉 →
  同样报错。测试后两份文件均逐字节还原。

### 备份

- 替换前的脚本与 manifest 存档于 `_raw/legacy-community-2026-09-21/`（本目录无版本控制，留作回滚）。

## [1.0.1] - 2026-09-21

### 修复（离线浏览器 index.html）

- **修复分类过滤无法切回「全部」**：`全部` 按钮此前写死在 HTML 里、**没有绑定点击事件**（事件只绑给了 `#catnav` 内的分类按钮），
  所以在侧栏选中任一分类后就再也回不到全部条目。现在「全部」与各分类按钮一起放进 `#navbox`，由 `renderNav()` 统一绑定
  （选择器为 `#navbox .navbtn[data-cat]`，只认分类按钮，不会误绑同处的状态过滤按钮）。
- **新增分类过滤收起 / 展开**：侧栏顶部加「‹ 收起 / 展开 ›」按钮，收起后隐藏筛选列表并把侧栏收窄、正文区变宽；
  状态写入 `localStorage`，下次打开保持上次选择。
- **详情页底部**：去掉「正文已渲染为排版好的文章（标题/列表/表格/代码块正常显示）」这句冗余说明，只保留源文件路径。

### 维护

- 新增 `scripts/validate_kb.py`：结构 + 索引 + 索引页模板的机械校验（兼容本库已有的 index.json 结构，不会误报）。
- 新增 `scripts/check_index_ui.py`：索引页**交互回归检查**（抽出内联 `<script>` 套 DOM 桩在 Node 里跑，无需浏览器）。
- 以上改动全部落在 `scripts/build_index.py` 的页面模板中，已重新生成 `index.html` / `index.json`。

### 验证

- `validate_kb.py` → **0 错误**；`check_index_ui.py` → **20 项断言全过**。

## [1.0.0] - 2026-09-20

### 初始版本

- 建立分层目录结构：`00-overview` / `01-installation` / `02-features` / `03-reference` / `04-development` / `05-tools`。
- 整理并收录官方核心内容：
  - 概览：什么是 CS、架构与缓存系统。
  - 安装：系统需求、安装指南、Vanilla 设置指南、ENB 迁移指南。
  - 功能：28 个核心特性 + 19 个附加特性（每特性独立条目，带元数据）。
  - 参考：不兼容 MOD 清单、完整 FAQ（安装/兼容/配置/开发/错误/性能/排查）。
  - 开发：True PBR 美术师与开发者指南、贡献指南。
  - 工具：Light Placer、PGPatcher。
- 建立元数据与版本化机制：
  - `manifest.json`：资料库元数据 + 条目 schema + 分类定义。
  - `index.json` / `index.html`：由 `scripts/build_index.py` 自动生成的索引与离线浏览器。
  - `scripts/gen_features.py`：功能条目生成器（数据驱动，便于增删改）。
  - 本 CHANGELOG 与 `CONTRIBUTING.md` 协作规范。

### 已知基线

- 内容基线对应官方文档 CS **1.8.4** 已知问题说明；部分附加特性标注为 TBA（开发中）。

---

## 待办 / 后续可补充

- [ ] 补全各功能的独立深度页面（目前多为摘要级，SSGI / Skylighting / Upscaling / Effects 11 已有交叉引用）。
- [ ] 收录官方各功能子页的完整参数与截图。
- [ ] 增加「推荐 MOD 列表 / 负载顺序示例」实战章节。
- [ ] 接入 CI：提交时自动运行 `build_index.py` 校验索引一致性。
