# 变更日志（CHANGELOG）

本文件记录资料库整体演进。条目级版本见各 `.md` 的 `version` / `updated` 字段。

## [2.1.0] - 2026-09-21

### 新增（脚本）

- 新增 `scripts/check_links.py`：扫描全部条目的 Markdown **站内相对链接**，报告解析不到实际文件的失效链接，并附带**换行一致性提示**。
  此前没有任何脚本覆盖正文链接 —— `validate_kb.py` 只查 frontmatter 与索引，坏链可长期潜伏而构建一路绿灯。
- 新增 `scripts/fix_links.py`：把目标路径的前导 `../` 剥掉得到「尾部路径」，在本库根目录反查实际文件，再用 `os.path.relpath`
  反算正确相对路径 —— **不信人写的 `../` 层数**。读写用 `newline=""`，修链接不会顺带改动 CRLF/LF。
- 两者与 `build-maintainable-kb` 技能的 stock 版**逐字节一致**。

### 修复（站内链接 29 处 / 15 个文件）

- **全部是同一类错误**：引用**同级或下级分类目录**下的条目时漏了 `../`。本库条目都在 `0X-分类/` 这一层深，正确写法几乎总是 `../0X-分类/xxx.md`。
  例：`02-features/archive-exe.md` → `../02-features/archive-exe.md`。
- 按文件分布：`06-tutorials/basic-quest-scripting.md` 4 处；`06-tutorials/ck-interface-tutorial.md` 3 处；
  `00-overview/creation-kit.md`、`01-installation/data-files.md`、`02-features/glossary.md`、`03-game-systems/quests.md`、
  `05-tools/blender-skyrim-art-tools.md`、`05-tools/skse-plugin-dev.md`、`05-tools/tes5edit.md`、
  `06-tutorials/ck-interface-cheat-sheet.md`、`06-tutorials/upload-steam-workshop.md` 各 2 处；
  `02-features/archive-exe.md`、`02-features/editor-interface.md`、`03-game-systems/packages.md`、`03-game-systems/radiant-story.md` 各 1 处。
- 这类错误**不会让构建失败**，只会在 `index.html` 里点不开。

### 修复（换行一致性）

- `04-scripting/script-object-{actor,debug,game,objectreference}.md` 4 个文件由 **CRLF 归一为 LF**（共 185 处）。
- **根因已修**：这 4 个是 `scripts/gen_features.py` 生成的，而它用文本模式 `open(path, "w", encoding="utf-8")` 写文件，
  Windows 上会把 `\n` 静默翻译成 `\r\n`。现已改为 `open(..., newline="\n")`；否则下次重跑生成器又会把 CRLF 写回来。

### 变更（文档）

- `manifest.json`：`tooling` 补录 `check_links.py` / `fix_links.py`，`gen_features.py` 说明补上「已改为写 LF」；`version` → 2.1.0。
- `README.md`：`scripts/` 目录树补两个脚本；「校验」步骤由两项改为三项。
- `CONTRIBUTING.md`：合并前校验由两项改为三项（加 `check_links.py`）。

### 验证

- `validate_kb.py` → **0 错误**；`check_index_ui.py` → **20 项断言全过**；`check_links.py` → **70 条站内链接全部有效**、换行全部 LF。
- 29 个条目、7 个分类未增删，**条目正文一字未改**（仅换行归一）。

## [2.0.0] - 2026-09-21

### 变更（结构对齐）

索引页模板与数据层**整体对齐到 `build-maintainable-kb` 技能的 stock 版**，与 `mo2-usvfs-kb` / `behaviour-engine-kb` / `community-shaders-kb` 四库统一。
**条目正文与 frontmatter 一字未改。**

- **`scripts/build_index.py` 换成 stock 版**（diff 确认与技能逐字节一致）：
  - 页头标题 / 副标题改为**从 `manifest.json` 的 `kb.name` / `kb.description` 注入**（此前硬编码在模板里，改 manifest 不生效）。
  - 新增 `_strip_leading_h1()`：详情面板已单独显示条目标题，因此正文开头的 `# H1` 会被剥掉，避免标题重复。
  - 移除 `statusBadge()`、`kind` / `status` 徽章与 `.b-*` 样式。
  - 移除侧栏「状态过滤」按钮组与 `curStatus` 筛选逻辑。
- **`manifest.json` 转为 stock 形状**：`kb.{name,description,locale}`；`entry_schema` → `schema`（含 `required` / `optional` 字段表）；`categories[].description` → `desc`；补充 `version` / `generated_at` / `maintainers` / `sources` / `license_note` / `index_files` / `tooling`。

### 保留

- frontmatter 的 `kind` / `status` **仍作为数据保留**（`index.json` 中照常输出），仅页面不再呈现徽章。
- `scripts/gen_features.py`、`scripts/fetch_ck.py` 作为生成器与上游同步工具保留。

### 验证

- `validate_kb.py` → **0 错误**（29 条目、id 与目录严格一致、无残留占位符）；`check_index_ui.py` → **20 项断言全过**。
- 7 个分类的 `CAT_LABELS` 全部解析成功（无空标签）。
- 替换前的脚本与 manifest 备份于 `_raw/legacy-creation-kit-2026-09-21/`。

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

### 新增
- 初始资料库骨架：manifest.json / README.md / CONTRIBUTING.md / CHANGELOG.md。
- 七大分类目录：`00-overview`、`01-installation`、`02-features`、`03-game-systems`、`04-scripting`、`05-tools`、`06-tutorials`。
- 概览板块：Creation Kit 概述、导航枢纽。
- 安装板块：获取与启动、INI 文件体系、Data 目录与插件格式。
- 编辑器功能：编辑器界面、快捷键映射、术语表、Archive.exe（BSA 打包）。
- 游戏系统：任务、对话、AI 包、Radiant Story（故事管理器）。
- Papyrus 脚本：语言概览、语言要素、编译、事件参考、函数参考，以及 4 个常用脚本对象（Actor / ObjectReference / Game / Debug，由 `gen_features.py` 生成）。
- 工具链：SKSE 插件开发、TES5Edit 清理、Blender 天际美术工具。
- 教程：Creation Kit 界面教程、界面速查表、基础任务脚本、上传 Steam 创意工坊。
- 自动化：`scripts/fetch_ck.py`（抓取）、`scripts/gen_features.py`（生成脚本对象）、`scripts/build_index.py`（构建索引与离线浏览器）。
- 生成 `index.json` 与 `index.html`（离线可搜索）。

### 来源
- 内容整理自 UESP Creation Kit Wiki：https://ck.uesp.net/wiki
- Creation Kit 当前版本：**1.9.32.0**
