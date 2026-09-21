# Changelog

本文件记录资料库的版本化演进。版本号采用 `主.次.补` 形式：
- **主版本**：结构/分类/ schema 重大调整；
- **次版本**：新增分类或一批条目、重要内容扩充；
- **补版本**：条目修订、修正、小补充。

---

## [2.1.0] - 2026-09-21

**内容扩充版**：把整理范围从「官方用户 wiki 一份来源」扩展到 **官方用户 wiki + 官方仓库 README + 官方 GitHub Developer Wiki + Nexus 发布页与各附加特性 MOD 页**，并修正了一批与上游不一致的陈述。

### 新增分类

- **`06-community`（社区）**——原 6 个分类都是「官方文档的结构化」，没有承载实战经验与信息源甄别的位置。

### 新增条目（5）

| 条目 | 说明 | 主要来源 |
|------|------|---------|
| `00-overview/feature-matrix.md` | **官方 CS / ENB / CS VR / ENB VR 全功能对照矩阵**（约 60 项）+ 官方承认的潜在功能依赖图 | GitHub Developer Wiki |
| `00-overview/version-and-support.md` | 版本号现状（稳定 1.8.x / 开发 1.9.0）、受支持游戏版本、VR 与 Linux 现状、官方构建政策、**功能并入核心时间线**、团队署名 | Nexus 发布页 + 官方 wiki |
| `04-development/testing-and-debugging.md` | **A/B 对比测试（Test Interval）**、`TESTCUBEMAP`、Shader Defines、`LLFDEBUG` 灯光可视化、Light Editor、抓帧与性能分析 | GitHub Developer Wiki + 各功能页 |
| `06-community/common-pitfalls.md` | 「现象 → 原因 → 处理」式实战清单（启动/缓存/兼容/画面/性能/平台六类） | 官方 wiki + FAQ + Nexus 页 + 社区反馈 |
| `06-community/community-resources.md` | 官方与可信社区渠道分级，以及**识别内容农场 / AI 聚合站**的判据 | 官方渠道 + 本次调研观察 |

### 内容扩充（官方深度内容）

- **14 个核心特性条目 + 2 个附加特性条目**由摘要级存根升级为完整条目，补入：工作原理与算法、游戏内参数与调试开关、需求与前置 MOD、兼容性注意事项、相关条目交叉引用、贡献者。涉及：cloud-shadows、dynamic-cubemaps、extended-materials、extended-translucency、grass-collision、grass-lighting、inverse-square-lighting、light-limit-fix、screen-space-shadows、sky-sync、subsurface-scattering、terrain-shadows、water-effects、skylighting、upscaling。
- `01-installation/vanilla-setup.md`（**1.0.0 → 2.0.0**）：按官方 Vanilla 设置指南补全**推荐 MOD 清单**——照明方案（True Light / Lux CS / 通用型清单）、天气 MOD 清单、Window Shadows Ultimate、CS Particle Patch、DIAL、Seamless Dynamic Cubemaps、PBR 纹理包（Faultier's / Skyland / Cathedral / Vanaheimer）、Asset Doctor 与网格修复。这补齐了 README 里挂了很久的「推荐 MOD 列表」待办。
- `01-installation/requirements.md`：补入官方 Nexus 页的**「强烈推荐」**项（Crash Logger PDB 版、Assorted Mesh Fixes）与新手入门指南指引。
- `01-installation/installation-guide.md`：补入**官方 Vortex 合集一键安装**（Collections `62eesj`）与整体更新规则。
- `03-reference/incompatible-mods.md`：新增**「照明 MOD 之间的互斥规则」**（一室内+一室外、一天气、EVLaS、MLO2 >1.3.6、WSU / Lux CS 的冲突矩阵）。
- `03-reference/faq.md`、`00-overview/what-is-cs.md`：更新版本基线与结论性表述；`what-is-cs` 的对比表加入 VR、性能、强项领域等维度。

### 修正

- **`Upscaling` 不支持 XeSS**——条目标题下的摘要原为「DLSS 4.5/FSR 3.1」，易被读成含 XeSS；现明确写出 **XeSS 不受支持**并附作者原因，同时标注 DLSS 版本在官方两处页面上的表述差异（Nexus 页 DLSS 4 / 用户 wiki DLSS 4.5）。
- **补上帧生成的硬性条件**：仅 **≥120 Hz 刷新率**生效、需 Windowed / Borderless Windowed、建议配 SSE Display Tweaks。
- **修复坏链**：
  - `03-reference/incompatible-mods.md` 中 Sky Sync 链接指向不存在的 `02-features/additional/sky-sync.md` → 改为 `02-features/core/sky-sync.md`；
  - `03-reference/faq.md` 中两处 `../../01-installation/installation-guide.md` 上跳过头 → 改为 `../01-installation/...`；
  - `00-overview/what-is-cs.md` 中三处 `01-installation/...` 缺 `../` → 修正。
- **`manifest.json`**：版本 2.0.0 → **2.1.0**；`sources` 补入 GitHub Developer Wiki；新增 `06-community` 分类声明；`tooling.gen_features.py` 说明同步为「脚手架」语义。

### 工具链

- **`scripts/gen_features.py` 降级为脚手架**：默认**跳过已存在的文件**，不再覆盖手工精修内容；仅在显式 `--force` 时按 `FEATURES` 重写。脚本头新增醒目的「已降级」说明，避免后来者误跑而把 15 个精修条目打回模板。
- **新增 `scripts/check_links.py`**：扫描全部条目的 Markdown **站内相对链接**，报告解析不到实际文件的失效链接。此前没有任何脚本覆盖正文链接——`validate_kb.py` 只查 frontmatter 与索引，所以坏链可以长期潜伏。
- **新增 `scripts/fix_links.py`**：按「目标尾部路径在根目录反查实际文件」的策略反算正确相对路径，不依赖人写的 `../` 层数。本次一次性修复了 32 处（14 处为本版新增条目引入，18 处为历史遗留）。

### 一致性

- **全部 Markdown 统一为 LF 换行**（此前 LF 与 CRLF 混用，共 35 个文件被归一化）。资料库无版本控制，统一换行可消除未来 diff 噪音；`build_index.py` / 校验脚本均按通用换行处理，不受影响。

### 验证

- `validate_kb.py` → **0 错误**；`check_index_ui.py` → **20 项断言全过**；`check_links.py` → **132 条站内链接全部有效**；`gen_features.py` → **跳过 47 个已存在条目、新建 0 个**（脚手架保护生效）。

### 备份

- 本版未改动 `_raw/legacy-community-2026-09-21/`（上一版的脚本与 manifest 存档保持原样）。

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

- [x] ~~补全各功能的独立深度页面~~ —— 2.1.0 已完成 **15 个**（13 核心 + Skylighting、Upscaling）。
- [ ] **继续精修其余 32 个摘要级功能条目**：
  - 核心（15）：cs-editor、image-based-lighting、interior-sun、lod-blending、nrd、performance-overlay、remote-control、renderdoc、scene-manager、screenshot、true-pbr、unified-water、vanilla-fresnel、volumetric-lighting、volumetric-shadows
  - 附加（17）：advanced-skin、effects-11、exponential-height-fog、grass-optimizations、hair-specular、hdr-display、horizon-fix、linear-lighting、order-independent-transparency、post-processing、screen-space-reflections、snow-deformation、ssgi、terrain-blending、terrain-helper、terrain-variation、wetness-effects

  > 这 32 个里，官方只在功能总览页给了**一句话描述**（没有独立子页），Nexus 上对应 MOD 页则各有较丰富的说明与需求——**下一轮应从 Nexus 各附加特性 MOD 页取材**，而不是硬凑内容。
- [x] ~~增加「推荐 MOD 列表 / 负载顺序示例」实战章节~~ —— 2.1.0 以 `01-installation/vanilla-setup.md` 的官方推荐清单落地。**负载顺序示例**仍缺（官方未给统一负载顺序，只给了互斥规则）。
- [ ] 收录官方各功能子页的完整参数截图（官方页面配图均为 Nexus 外链，本库不宜镜像）。
- [ ] `03-reference/incompatible-mods.md` 与官方 FAQ 的「不兼容 MOD」条目做一次逐条对齐（本版只补了照明/天气互斥）。
- [ ] 接入 CI：提交时自动运行 `build_index.py` 校验索引一致性。
