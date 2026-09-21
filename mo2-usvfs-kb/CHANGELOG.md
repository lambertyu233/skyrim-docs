# 变更记录（CHANGELOG）

本文件记录资料库整体与各条目的版本化演进。条目级 `version` 字段随内容变更递增。

## [1.2.0] - 2026-09-21

### 新增（脚本）

- 新增 `scripts/check_links.py`：扫描全部条目的 Markdown **站内相对链接**，报告解析不到实际文件的失效链接，并附带**换行一致性提示**。
  此前没有任何脚本覆盖正文链接 —— `validate_kb.py` 只查 frontmatter 与索引，坏链可长期潜伏而构建一路绿灯。
- 新增 `scripts/fix_links.py`：把目标路径的前导 `../` 剥掉得到「尾部路径」，在本库根目录反查实际文件，再用 `os.path.relpath`
  反算正确相对路径 —— **不信人写的 `../` 层数**。读写用 `newline=""`，修链接不会顺带改动 CRLF/LF。
- 两者与 `build-maintainable-kb` 技能的 stock 版**逐字节一致**。

### 修复（站内链接 31 处 / 19 个文件）

- **全部是同一类错误**：引用**同级或下级分类目录**下的条目时漏了 `../`。本库条目都在 `0X-分类/` 这一层深，正确写法几乎总是 `../0X-分类/xxx.md`。
  例：`01-mechanism/api-hooking.md` → `../01-mechanism/api-hooking.md`。
- 按分类分布：`05-usage/` 5 文件 8 处、`01-mechanism/` 5 文件 7 处、`06-reference/` 2 文件 5 处、`03-architecture/` 3 文件 5 处、
  `00-overview/` 2 文件 4 处、`02-features/` 与 `04-debugging/` 各 1 文件 1 处。单文件最多的是 `06-reference/faq.md`（4 处）。
- 这类错误**不会让构建失败**，只会在 `index.html` 里点不开。

### 修复（换行一致性）

- **22 个条目由 CRLF 归一为 LF**（共 714 处），与另外三个资料库及「统一 LF」的约定一致。
  此前不影响 `index.html` / `index.json` 的渲染，但混用换行会让未来 diff 噪音变大。

### 变更（文档）

- `manifest.json`：`tooling` 此前**只登记了 `build_index.py` 一项**，而 `scripts/` 下实有 6 个脚本 —— 现补全
  `fetch_mediawiki.py`、`validate_kb.py`、`check_index_ui.py`、`check_links.py`、`fix_links.py`；
  `version` → 1.2.0（此前停在 1.1.0，落后于本 CHANGELOG 的 1.1.1）。
- `README.md`：`scripts/` 目录树展开为逐脚本说明；「如何维护」补上构建 + 三项校验的完整流程；页脚版本号同步。
- `CONTRIBUTING.md`：把「每次增删改后运行 build_index」扩为「构建 + 三项校验」。

### 验证

- `validate_kb.py` → **0 错误**；`check_index_ui.py` → **20 项断言全过**；`check_links.py` → **144 条站内链接全部有效**、换行全部 LF。
- 43 个条目、7 个分类未增删，**条目正文一字未改**（仅换行归一）。

## [1.1.1] - 2026-09-21

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

## [1.1.0] - 2026-09-20

### 新增（05-usage「使用与运维」大幅补全）

依据 [STEP 非官方 Mod Organizer 指南](https://stepmodifications.org/wiki/Guide:Mod_Organizer)（通过 MediaWiki API 抓取 wikitext 存档于 `_raw/Guide_Mod_Organizer.wiki.txt`）补齐了此前缺失的**操作层面**知识，新增 21 个条目：

- **入门与安装**：安装与首次启动设置、便携安装 vs 实例安装。
- **界面**：界面总览（工具栏/左窗格/右窗格/Flags 图例）、筛选/分组与冲突高亮、自定义 mod 分类。
- **mod 生命周期**：安装 mod（四种途径 + Mod Exists + Simple/BAIN/FOMOD/手动安装）、更新合并与卸载、启用 mod 与激活插件（含插件备份恢复、Sort、Lock load order）、下载管理与 Nexus 集成（meta/Query Info/nxmhandler）。
- **工具与程序**：配置第三方程序与快捷方式（含 profile 专属快捷方式）、常用工具配置配方（LOOT/xEdit/Wrye Bash/FNIS/SkyProc/SKSE/CK/BodySlide/SBW/FCXE）、插件体系（extensions/installers/tools/黑名单）。
- **文件与资源**：文件树、隐藏文件（`.mohidden`）与冲突面板、BSA 管理与解包（Unmanaged、Archive Invalidation）。
- **运维**：存档查看与 Fix Mods、备份与恢复、警告面板与潜在 mod 顺序问题、游戏 INI 与 ini tweaks、设置页参考、加载机制与 Steam App ID、使用类常见问答。

### 修复
- `manifest.json` 增补 `kb` 块（`name` / `description` / `source_name`）。此前索引脚本读取 `kb.*` 而 manifest 只有顶层同名字段，导致 `index.html` 的标题退化为默认值「资料库」；现已正确注入「Mod Organizer 2 · USVFS 资料库」及副标题。

### 变更
- `manifest.json` 版本 1.0.0 → 1.1.0；来源名补充 STEP 指南；`05-usage` 分类描述更新。
- `README.md` 目录结构说明与版本号同步。

### 来源
- [STEP 非官方 Mod Organizer 指南](https://stepmodifications.org/wiki/Guide:Mod_Organizer)（新增，主来源）

## [1.0.0] - 2026-09-20

### 新增
- 初版发布，共 22 个条目，覆盖 7 个分类。
- **00-overview**：什么是 MO2、USVFS 在 MO2 中的角色。
- **01-mechanism**：API Hooking、进程级可见链接、会话级/免管理员/跨文件系统、多目录叠加、虚拟删除。
- **02-features**：USVFS vs NTFS 符号链接对比、USVFS 的代价与风险。
- **03-architecture**：VFS 节点类（DirectoryEntry/FileEntry/FilesOrigin/FileRegister/VirtualFileTree）、DirectoryRefresher、FileEntry 优先级冲突、UsvfsConnector、BSA 优先级解析。
- **04-debugging**：调试 usvfs（hook_ 命名、日志格式与字段、spawn_delay、Process Monitor、Visual Studio）。
- **05-usage**：运行时部署、mod 隔离、profile 切换、冲突解决与优先级、Overwrite 目录维护。
- **06-reference**：FAQ、VFS/USVFS 常见排错（杀软、HVCI/Core Isolation、Windows Event Log 服务、系统日志被清）。

### 来源
- USVFS GitHub README
- MO2 Wiki - Debugging usvfs
- STEP Mod Organizer 参考指南
- DeepWiki - ModOrganizer2/modorganizer
- MO2 Wiki - Troubleshooting / HVCI
