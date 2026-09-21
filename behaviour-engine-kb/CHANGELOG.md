# 变更记录（CHANGELOG）

本资料库遵循[语义化版本](https://semver.org/lang/zh-CN/)。每条目自身也有 `version` 字段。

## [1.1.0] - 2026-09-21

### 新增（脚本）

- 新增 `scripts/check_links.py`：扫描全部条目的 Markdown **站内相对链接**，报告解析不到实际文件的失效链接，并附带**换行一致性提示**。
  此前没有任何脚本覆盖正文链接 —— `validate_kb.py` 只查 frontmatter 与索引，所以坏链可以长期潜伏、构建一路绿灯。
- 新增 `scripts/fix_links.py`：**不信人写的 `../` 层数** —— 把目标路径的前导 `../` 剥掉得到「尾部路径」，在本库根目录反查实际文件，
  再用 `os.path.relpath` 反算正确的相对路径，因此不论条目在几层深都成立。
- 两者与 `build-maintainable-kb` 技能的 stock 版**逐字节一致**；至此本库五个脚本（`build_index.py` / `validate_kb.py` /
  `check_index_ui.py` / `check_links.py` / `fix_links.py`）全部与技能同步。

### 修复（站内链接）

- 修正 **1 处**失效链接：`00-overview/what-is-behaviour-engine.md` 引用同一级分类目录下的条目时漏了 `../`
  （`patcher-vs-replacer.md` → `../01-principles/patcher-vs-replacer.md`）。
- 这类错误**不会让构建失败**，只会在 `index.html` 里点不开，属于此前工具链的盲区。

### 变更（文档）

- `manifest.json`：`tooling` 补录 `check_index_ui.py`（此前遗漏）、`check_links.py`、`fix_links.py`；
  `version` 由 `1.0.0` 修正为 **1.1.0** —— 此前未随 1.0.1 / 1.0.2 递增，一直落后于本 CHANGELOG。
- `README.md`：`scripts/` 目录树展开为逐脚本说明；「怎么维护」补上三项校验命令。
- `CONTRIBUTING.md`：新增条目流程与「四、自检清单」加入 `check_index_ui.py` 与 `check_links.py`。

### 验证

- `validate_kb.py` → **0 错误**；`check_index_ui.py` → **20 项断言全过**；`check_links.py` → **97 条站内链接全部有效**、换行全部 LF。
- 28 个条目、8 个分类未增删，**条目正文一字未改**。

## [1.0.2] - 2026-09-21

### 变更（脚本对齐）

- `scripts/build_index.py` 对齐到 `build-maintainable-kb` 技能的 stock 版：此前 `renderNav()` 的函数定义位置与技能不同（功能等价，仅结构分叉），分类按钮也不再输出多余的 `type="button"`。
- 至此**四个资料库**（本库 / community-shaders-kb / creation-kit-kb / mo2-usvfs-kb）的 `build_index.py` / `validate_kb.py` / `check_index_ui.py` 与技能 stock 版**逐字节一致**。
- 条目与页面产物无实质变化；已重建并跑通双校验（结构校验 0 错误、交互回归 20/20）。

## [1.0.1] - 2026-09-21

### 修复（index.html 交互）

- **修复分类过滤无法切回「全部」**：`全部` 按钮此前写在 HTML 里但未绑定点击事件（只有 `#catnav` 内的分类按钮被绑定），选中任一分类后无法回到全部条目。
- **新增分类过滤的收起/展开**：侧栏顶部加「‹ 收起 / 展开 ›」按钮，收起后隐藏分类列表并把侧栏收窄，正文区自动变宽；状态写入 `localStorage`，下次打开保持上次选择。
- **条目详情底部**：去掉「正文已渲染为排版好的文章（标题/列表/表格/代码块正常显示）」这句冗余说明，只保留源文件路径。

### 说明

- 以上改动落在 `scripts/build_index.py` 的页面模板中，已重新生成 `index.html` / `index.json`（28 条目，校验 0 错误）。

## [1.0.0] - 2026-09-21

### 新增（初版）

- **概览（00-overview）**
  - 动作引擎是什么：它到底在解决什么问题
  - 三引擎脉络：FNIS → Nemesis → Pandora
  - 官方三引擎对比表（附解读）
- **原理（01-principles）**
  - Havok Behavior 是什么：FSM 与 hkx 包文件
  - hkx 其实有两种：行为文件 ≠ 动画文件（fore 一手帖）
  - 行为补丁器原理：读补丁 → 合并 → 输出
  - 动画数据库与事件名（scorrp10 解释）
  - Patcher 与 Replacer 的区别：FNIS/Nemesis/Pandora vs DAR/OAR
- **FNIS（02-fnis）**
  - FNIS 概览：第一代动作引擎（fore，7.6，已停更）
  - FNIS 的动画注册机制：AnimList 与生成器
  - FNIS 兼容性与淘汰原因
- **Nemesis（03-nemesis）**
  - Nemesis 概览：第二代动作引擎（模板化 + 开源）
  - Nemesis 复杂度分级（Basic → Master）
  - Nemesis 的局限：文档缺失、大列表崩溃、更新停滞
- **Pandora（04-pandora）**
  - Pandora 概览：第三代动作引擎
  - Pandora 架构与性能设计：为什么它"更快"
  - Pandora 补丁格式（作者向）
  - Pandora 安装指南（MO2 / Vortex）
  - Pandora 排错：Engine.log 与常见故障
- **生态（05-ecosystem）**
  - OAR / DAR 是什么，与动作引擎的关系
  - AMR 动画运动革命
  - 相关工具链
- **实战（06-practices）**
  - 如何选择引擎：决策指南
  - 标准刷补丁流程（跨引擎通用）
  - 常见报错与故障（跨引擎）
- **来源（07-sources）**
  - 官方来源清单（按阅读优先级）
  - 社区与讨论来源
  - 不可信来源警示

### 说明

- 所有原理性定义与版本号均标注官方出处；社区说法单独标注"（社区）"。
- `index.html` 首次由 `scripts/build_index.py` 生成。
