# 变更记录（CHANGELOG）

本文件记录资料库整体与各条目的版本化演进。条目级 `version` 字段随内容变更递增。

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
