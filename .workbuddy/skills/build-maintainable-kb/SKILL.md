---
name: build-maintainable-kb
description: 将任意来源（wiki/文档/网页）整理为可维护、分层、版本化的 Markdown 资料库：每主题单文件 + 统一 frontmatter + 自动索引生成器（index.json / 离线可搜索 index.html，两栏布局 + 内联渲染后的 HTML 正文）。附通用脚本（MediaWiki 抓取 + 索引构建 + 索引页机械校验与交互回归测试 + aliases 清理 + 引用链接化）。适用于"整理并构建资料库/知识库/文档站"类请求。
agent_created: true
---

# 构建可维护资料库 (Build Maintainable Knowledge Base)

用户要求"整理并构建可维护的资料库/知识库"时，使用本技能产出一个**分层、单文件条目、元数据驱动、版本化、便于增删改查与协作**的 Markdown 仓库，并自动生成可离线双击浏览的索引页。

## 何时使用
- "根据某 URL / 文档 / 网页构建资料库"
- "整理成可长期维护的知识库"
- "做一个便于协作更新的文档结构 / 文档站"

## 核心设计原则
1. **分层清晰**：按读者意图分目录，目录名带序号前缀 `00-`、`01-` 便于排序。
2. **单文件条目**：每个主题一个 `.md`，互不耦合，便于单独修订、PR、删除。
3. **元数据驱动**：每文件顶部统一 YAML frontmatter，索引/搜索/过滤自动化。
4. **版本化**：`CHANGELOG.md` + 每条 `version` 字段，可追溯演进。
5. **协作友好**：约定明确 + 自动化索引，降低合并冲突与人工维护成本。
6. **离线可用**：索引页把数据内联进 `<script>`，双击 `index.html` 即可用（无需起服务器、无 CORS）。

## 标准产出结构

> **多库工作区**：一个工作区里可以有**多个**资料库（各自一个 `NN-` 或 `*-kb` 目录，
> 各自带 `manifest.json` + `scripts/`）。此时还应在**工作区根**放一份 `AGENTS.md`
> 作为 agent 入口契约（模板见 `references/agents-md-template.md`），
> 并用 `scripts/kb.py` 做跨库检索 —— 见下方"让 agent 用得起这个库"。

```
kb/
├── manifest.json        # 元数据 + 条目 schema + 分类定义 + 来源（索引页的分类中文名也取自这里）
├── index.json           # 自动生成的纯元数据索引（程序化消费，含内联正文 content）
├── index.html           # 自动生成的离线浏览器（两栏布局 + 内联渲染后的 HTML 正文，双击即用）
├── README.md            # 导航 + 使用 + 维护说明
├── CHANGELOG.md         # 版本化变更记录
├── CONTRIBUTING.md      # 协作规范（增删改查流程）
├── 00-overview/ 01-installation/ 02-features/ ...   # 分类目录（每主题单文件 .md）
├── _raw/                # （可选）抓取来的上游原文存档，便于后续同步，索引构建会忽略
└── scripts/
    ├── fetch_mediawiki.py  # 通用 MediaWiki 抓取器（见下方"抓取来源"）
    ├── gen_features.py     # （可选）脚手架：按模板**补缺**新建同类条目，默认不覆盖已有文件
    ├── build_index.py      # 扫描全部 frontmatter → index.json + index.html
    ├── validate_kb.py      # 机械校验：frontmatter / 索引一致性 / 别名规范 / 索引页模板
    ├── check_index_ui.py   # 索引页交互回归检查（Python 脚本；内部调 Node + DOM 桩，无需浏览器）
    ├── check_links.py      # 站内相对链接校验（+ 换行一致性提示）
    └── fix_links.py        # 按目标尾部路径反查实际文件，修正 ../ 深度错误
```

> ⚠️ **目录布局的两条硬约束**（都是踩过的坑）：
> 1. **条目必须放在带 `NN-` 前缀的分类子目录里**。`build_index.py` 会跳过库根层
>    （`if rel == "."`），条目写在库根会被**静默丢掉** —— 构建输出 `0 entries`
>    而**不报任何错**。库根只放 `manifest.json` / `index.*` / `README.md` / `AGENTS.md`。
> 2. 分类目录名**必须带 `NN-` 前缀**，且 `category` 字段与之**严格相等**（见下文）。

## 让 agent 用得起这个库（多库工作区的入口层）

**没被索引到的知识等于不存在。** 资料库建得再规整，如果 agent 开工时不知道它存在、
不知道怎么检索，这些条目就只是磁盘上的一堆文本。实测过的工作区里，5 个库 / 197 条目
却既无 `AGENTS.md` 也无检索脚本，agent 只能靠散文式记忆猜库的存在。

入口层由三件套构成：

1. **工作区根 `AGENTS.md`**（模板见 `references/agents-md-template.md`）：检索协议 +
   主题→库路由表 + 证据纪律 + 写回规则。这是 agent 每次都会读到的唯一位置。
2. **`scripts/kb.py`**：跨库检索入口。子命令 `list / toc / find / grep / show / read / check`，
   零依赖、单文件，数据源**永远是各条目的 frontmatter**（不新增需要同步的清单文件）。
   - `find` 只回「路径 + 别名 + 摘要」，实测 **1.7KB** vs 读 `index.json` **296KB**，约 174× 差距；
   - `show` 返回**元数据 + 标题大纲**而非正文，把"读不读、读哪段"的决定权交回 agent；
   - `check` 校验 `AGENTS.md` 是否覆盖了所有库目录 —— **新增库后漏写入口文件会报错**。
3. **跨库索引条目**（可选但强烈建议）：文档按主题组织，用户提问按症状组织。
   建一个 `01-navigation/` 库放「症状 → 条目路径 + 最易误判分叉点」的对照表，
   是检索命中最直接的提升。它是**索引不是正文**，不要复制正文进来。

> 权衡量：三件套的收益是让"库存在"这件事对 agent 可见；成本是必须保持
> `AGENTS.md` 与实际库目录同步 —— 这个成本由 `kb.py check` 机械化兜住。

## frontmatter schema（统一）
必填：`id`(小写连字符唯一，与文件名一致) `title` `category`(=分类目录名，索引据此过滤) `version` `updated`(YYYY-MM-DD) `tags`(数组) `source`(URL) `summary`(一句话)
可选：`kind`(concept|reference|tutorial|tool)

### 可选字段 `aliases`（检索别名，提升 agent 命中率的杠杆）
`tags` 回答"这篇属于什么主题"，`aliases` 回答"**别人会用什么词来找它**"：
英文术语、俗称、常见错拼、上级概念词。**不要与 tags / id 重复**。

```yaml
tags: [OAR, 条件, 清单, 速查, 版本]
aliases: [conditions, conditions list, 条件列表, 条件速查表, AttackState, IsAttacking]
```

- 不填完全合法（字段可选，`build_index.py` / `kb.py` 都按可选处理）。
- 填了就要干净：必须是 `[]` 数组、无重复、≤16 项 —— `validate_kb.py` 会报错；
  与 tags 重叠会以 NOTE 提示（不阻断）。
- `kb.py find` 的加权：id 精确 100 > **别名精确 60** > tag 精确 40 >
  别名模糊 26 > tag 模糊 22 > 标题 20 > 摘要 8 > 正文 3×出现次数。
- 实测价值：条目标题是「条件全清单」，用英文提 `conditions list` 原本基本淹没，
  加别名后直接排第一。
- 界面上，`index.html` 会在搜索时于卡片上标出**命中原因**（别名/标签/标题/摘要/正文），
  详情页把别名以弱化 chip 单独列出。

**怎么写才真的有用**（2026-09-21 全库 198 条实战后总结）：

- 一条别名 ≈「一个别人真会敲进去的**短查询**」，**不要写整句话**。
  反例（实测无效且占名额）：`怎么让动画随机播`；正例：`随机动画`、`多个动画轮换`。
- 优先写：英文术语 / 缩写 / 俗称 / 常见错拼 / 上级概念词。
  SKILL 的固有盲点是"库里的规范名 ≠ 用户嘴里的说法"，别名就是补这个缝。
- **别抄 tags**：tags 已经单独计 40 分，重复写等于白占一项（`validate_kb.py` 会以 NOTE 提示）。
  写完后自检一遍"删掉与 tags 同名的项，是否每条还剩 ≥3 个"。

**搜索端的三条归一化（决定别名该怎么写）**：

- **空格不敏感**：`kb.py find` 会先去掉查询与别名中的所有空白再比对，
  `怎么装mod` 与 `怎么装 mod` 等价。**同一个说法不必为空格写两条。**
- **大小写不敏感**：`find` 对查询与别名都做 `.lower()`。
  **所以绝对不要为了兼容小写查询而同时写 `DynDOLOD` 与 `dyndolod`** ——
  这类变体在 `find` 端完全冗余，而在 `validate_kb.py` 端会被判为
  「aliases 有重复项」**直接报 ERROR**（`skyrim-tools-kb` 初稿因此报 8 个 ERROR）。
  即"大小写变体既没用、又有害"。同理不要写 `Base Object Swapper` + `base object swapper`。
- **中文长串反向包含**：查询是无空格的中文长串（≥4 字）时，会拿库里**较短的**别名去反向匹配。
  所以中文别名应写**更短的核心说法**（`光太多闪烁`），而不是把用户可能说的整句都列上去
  —— 长句既切不中，又挤占 16 项上限。

> ⚠️ 批量补别名时，务必用"**按 tags 行锚点插入**"的脚本一次性写回，并满足三条：
> ① 写前探针确认每个文件的 `tags:` 行唯一（否则锚点歧义）；
> ② 用 `newline=""` 读写，避免 Windows 文本模式把 `\n` 静默转成 `\r\n`；
> ③ 写前备份到 `_raw/pre-aliases-<date>/`，写后逐个断言 frontmatter 仍闭合、正文逐字节未变。
> 不要手工一个个改 200 个文件。

> 关键：`category` 必须**严格等于目录名**（如 `02-features`），索引聚合分类与查标签都依赖它。**不要**写成省略 `NN-` 前缀的短名（`features`）、也不要写别的 —— `build_index.py` 是拿 frontmatter 的值去 `CAT_LABELS` 里查中文标签的，写成 `features` 就查不到 `02-features` 的标签，页面上该条目的分类标签会变空、按分类过滤也找不到对应按钮，而且**只表现为「空标签」，不会报错**，很容易长期潜伏。

## 抓取来源（重要实战经验）
很多资料库源是 **MediaWiki**（如 `ck.uesp.net`、`modding.wiki`）：
- ❌ 直接用 WebFetch 抓这类页面，往往**只返回标题**，正文抽不到。
- ❌ 用 `urllib` 默认 User-Agent 访问会被 **403**。
- ✅ 走 MediaWiki API：`action=parse&prop=wikitext` 取 wikitext，或 `list=categorymembers` 列分类成员；UA 设为浏览器串即可正常抓取。
- 本技能附带 `scripts/fetch_mediawiki.py`（通用，支持单页 / 分类成员 / 出链三种模式），用法：
  ```bash
  python scripts/fetch_mediawiki.py --api https://ck.uesp.net/w/api.php "Main_Page"
  python scripts/fetch_mediawiki.py --api https://ck.uesp.net/w/api.php --cat "Category:Papyrus"
  python scripts/fetch_mediawiki.py --api https://ck.uesp.net/w/api.php --links "Papyrus"
  ```
- 抓来的原文存到 `_raw/`，阅读后据此写条目；**条目里的关键数值（版本号/路径/参数）务必对照原文，勿凭记忆改写**。

## 离线浏览器设计（最新效果参考 behaviour-engine-kb）
> **单一真相源**：`index.html` 的外观与交互**全部写在技能 stock 版 `scripts/build_index.py` 的
> `HTML_TEMPLATE` 字符串里**。新建库时把这个脚本复制过去，就自动继承当前 UI（含下面说的两个半圆把手）；
> 要改 UI 就改这一处，然后 `sync_scripts.py` 推送到各库、再逐库重建。
> **永远不要手改任何 `index.html`**（它是产物，下次重建即丢），也不要在某个库里单独改副本
> （下次同步就被 stock 覆盖）—— 已经在库里改过的那份，先把它并回技能再同步。

`build_index.py` 产出的 `index.html` 采用：
- **渐变页眉 + 统计胶囊**：标题 + 各分类计数。
- **两栏布局**：左侧分类侧栏（中文标签来自 `manifest.json`），右侧工具栏（搜索/排序）+ 卡片网格。
- **卡片 → 详情**：点卡片在页面内弹出详情面板，**整篇正文渲染为排版好的 HTML 内联展示**（`.article` 容器，标题/列表/表格/代码块/引用/行内均正常显示），并保留「打开本地 .md」「官方来源」按钮。
- **分类中文标签**：由 `manifest.json` 的 `categories[].title` 自动读取，UI 与资料库定义一致。
- **分类过滤可收起（收起 = 侧栏整条消失）**：**收起把手与展开把手共用同一个 `.navfab` 外形**（26×58、右半圆 `border-radius:0 30px 30px 0`、白底蓝字、hover 变实心蓝、`position:fixed;top:50%` 垂直居中）——
  - **展开态**：`#navtoggle`（`‹`）贴在**侧栏右缘**（`left:230px`，即 `aside` 的固定宽度），点它 → `aside.collapsed{display:none}` 使侧栏**整条让位**（早期版本只收窄到 78px 窄条，已废弃）；
  - **收起态**：`#navfab`（`›`）出现在**视口左缘**（`left:0`），`.navfab.show` 才 `display:flex`，点它重新展开。
  - ⚠️ **`#navtoggle` 必须留在 `<aside>` 的 DOM 子树里**（只用 `fixed` 把它挪到侧栏右缘，不要移到 `</aside>` 之外）：① 侧栏收起时它随 `aside{display:none}` **自动隐藏**，不需要额外 JS；② `check_index_ui.py` 只静态解析 `<aside>` 内的按钮，移到外面就取不到、断言会假失败。
  - `aside.collapsed + main{padding-left:44px}` 给正文让位，避免把手压住首列。状态存 `localStorage`。
  **以后新增筛选分组（如状态过滤）时，要把整组一起放进 `#navbox`**，收起才会一并生效。
- **安全**：内联 JSON 对 `</` 做 `</`→`<\/` 转义，避免 `</script>` 提前闭合。

> **正文默认即为排版好的文章**：构建期用纯标准库极简 `md_to_html()` 渲染器（覆盖标题 / 有序·无序列表 / 嵌套列表 / 表格含对齐 / 代码块 / 引用 / 行内粗体·斜体·代码·链接）把 `.md` 正文转成 HTML 内联进详情面板——**零依赖、完全离线、可移植**，无需任何前端 JS 库或网络。

## 关键脚本
### scripts/build_index.py
- 递归扫描目录，正则 `^---\s*$(.*?)^---\s*$`(DOTALL|MULTILINE) 解析 frontmatter；`key: value` 行，值若为 `[a, b]` 解析为数组。
- 抽取 frontmatter 之后的正文，用 `md_to_html()` 渲染为排版好的 HTML 后存为 `content` 字段，内联进浏览器详情面板。
- 忽略 `scripts/`、`_raw/` 与约定文件名（README/CHANGELOG/CONTRIBUTING/manifest/index 等）。
- 从 `manifest.json` 读分类中文名；输出 `index.json`（含元数据+正文）与 `index.html`（内联 `ENTRIES`/`CATS`/`CAT_LABELS` JSON 到 `<script>`）。
- 标题/副标题从 `manifest.json` 的 `kb.name`/`kb.description` 注入，已通用化。
  - ⚠️ **manifest 必须写成嵌套的 `"kb": { "name": ..., "description": ..., "source_name": ... }`**。脚本读的是 `mdata["kb"]["name"]`；若只在顶层写 `"name"`/`"description"`，`kb` 取到空字典，页面标题会静默退化为默认值「资料库」（`<title>资料库</title>`），且不报错。检查方法：构建后 grep `index.html` 的 `<title>` 是否等于你期望的资料库名。
- 用 `__ENTRIES__` 等占位符注入，避免 file:// 的 fetch CORS 问题。
- ⚠️ **侧栏筛选按钮的绑定铁律（历史 bug 就出在这）**：`全部` 按钮与各分类按钮必须由 `renderNav()` 里**同一行**统一绑定 ——
  `document.querySelectorAll('#navbox .navbtn[data-cat]')`。选择器**必须带 `[data-cat]`**，否则会把同处 `#navbox` 内的状态过滤按钮也绑成分类按钮。
  曾经的反面写法：把 `全部` 按钮直接写死在 HTML 里、只给 `#catnav` 内的按钮绑事件 —— 结果是「选进任一分类后点『全部』毫无反应」。
  **新按钮一律写在 `#navbox` 内、靠这一行统一绑定，不要再手写内联 `onclick`。** 改完必跑 `check_index_ui.py`，它第一条断言就是这个。

### scripts/validate_kb.py
- 机械校验，0 错误才算过：`id == 文件名`；**`category` 与目录名严格相等**；必填字段非空；`updated` 形如 `YYYY-MM-DD`；
  **每个有条目的目录都在 `manifest.categories[].dir` 里声明过**（否则页面分类标签渲染成空）；`index.json` 条目数与磁盘一致（若该库内联正文，则每条 `content` 非空）；`index.html` 无残留占位符；
  `<title>` 与 `manifest.kb.name` 一致；**索引页含 `#navbox` / `#navtoggle` / `#navfab`，且 `data-cat="all"` 的按钮确实落在 `#navbox` 内**（模板被改坏的哨兵）；少 `#navfab` 说明回退到了「收起只收窄、没有唤出按钮」的旧版模板。
- **兼容旧库**：按 `index.json` 里实际存在的字段决定检查范围（早期库是 `meta + entries` 且不内联正文），不会对旧库误报一堆假错误。
  ⚠️ 但「`category` 允许省略 `NN-` 前缀」这条宽容已在 2026-09-21 取消 —— 它放过了某库 47 个条目 `category: features` 的真实错误（页面一片空标签却一路绿灯）。宽容校验比没有校验更危险。
- 用法：`python scripts/validate_kb.py`，退出码 0 / 1。

### scripts/check_index_ui.py
- **索引页交互回归检查：不需要浏览器、不下载 Chromium**（agent-browser 要下几百 MB，为一个按钮的修复不值当）。
- 做法：抽出 `index.html` 内联的 `<script>`，套一层最小 DOM 桩（`El` 实现 `classList` / `innerHTML` / `querySelectorAll` / `dataset`；
  `document` 只支持用到的那几个选择器；`localStorage` 用内存对象），在 Node 里**真实执行页面脚本**，再模拟点击，断言：
  「全部」按钮已绑定 onclick、所有分类按钮已绑定、点某分类只显示该分类且点「全部」恢复全部、
  收起/展开的类名（`#navbox.hidden` / `aside.collapsed` / `#navfab.show`）·`localStorage`、页面不含已删除的冗余文案。
  ⚠️ 收起按钮与半圆悬浮按钮的**顶层变量名不能重名**：`check_index_ui.py` 会把页面 `<script>` 与断言段拼成**同一个文件**执行，
  同名 `const` 会直接 `SyntaxError`（页面里绑定 `#navfab` 因此用 IIFE 包住局部变量）。
- 用法：`python scripts/check_index_ui.py [库目录]`，退出码 0 / 1；环境里没有可用的 node 时打印 `SKIPPED` 并以 0 退出（不误报为失败）。
- ⚠️ **这个脚本用 `python` 跑，不是用 `node` 跑**（它内部才去调 Node 执行 DOM 桩）。若误用
  `node scripts/check_index_ui.py`，Node 会读到第 2 行的 `# -*- coding: utf-8 -*-` 而报
  `SyntaxError: Invalid or unexpected token` 并退出码 1 —— **这个报错会把人误导成「文件编码坏了」**，
  实际只是解释器用错了。同理 `check_links.py` / `validate_kb.py` / `build_index.py` 全部是 Python 脚本。
- 写这类 DOM 桩的坑：`innerHTML` 重写时必须**把旧子元素从全局注册表里摘掉**，否则条目计数会累加，测试会假失败。

### scripts/check_links.py
- **站内相对链接 lint**。填的是 `validate_kb.py` 的盲区：它只查 frontmatter 与索引，**完全不看正文链接**，所以坏链可以长期潜伏、构建一路绿灯。
- 相对链接的 `../` 层数由**目录深度**决定（`02-features/core/x.md` 引根目录要 `../../`，`01-installation/x.md` 只要 `../`），手写必错，尤其在新增深层目录或批量写条目之后。
- 只检查站内相对链接（跳过 `http(s)` / `mailto` / 纯锚点）；目标可以是文件也可以是**目录**（`../02-features/core` 合法）。
- 附带报告**非 LF 换行的文件**（MIXED / CRLF），仅提示、不计入退出码。
- 用法：`python scripts/check_links.py`，退出码 0 / 1。
- ⚠️ **它只认 markdown 链接 `](...)`**。把交叉引用写成反引号纯文本
  （`` `09-diagnostics/x.md` ``）**不会被校验**，而且渲染出来不可点击 ——
  等于"自认为在做交叉引用，实际是一段死文本"。实测 `skyrim-tools-kb` 初稿 352 处全写成反引号，
  `check_links` 报"检查站内相对链接: 0 / 链接全部有效"，看起来像通过，其实是**空跑**。
  写条目时一律用 `[条目标题](../NN-cat/x.md)`；已有纯文本引用用 `linkify_refs.py` 批量转换。

### scripts/fix_links.py
- `check_links.py` 的修理工。**不信人写的层数**：把目标路径的前导 `../` 全部剥掉得到"尾部路径"，在库根目录下反查实际文件，再用 `os.path.relpath` 反算正确相对路径——所以条目在几层深都成立。
- 反查不到实际文件时**不猜**，原样保留并交回 `check_links.py` 报告。
- **换行必须原样保留**：以 `open(..., encoding="utf-8", newline="")` 读写（读写都不做换行翻译）。若写成"通用换行读入 + `newline=""` 写出"，会**静默把 CRLF 全变成 LF**，修一个链接却炸出整文件级 diff。
- 依然遵循"先全量校验、再统一写盘"的纪律：只有 `new_text != text` 才落盘。
- 用法：`python scripts/fix_links.py`，退出码 0 / 1。

### scripts/linkify_refs.py（把反引号纯文本引用批量转成 markdown 链接）
- 适用场景：条目初稿把交叉引用写成 `` `NN-cat/x.md` `` 纯文本 —— 不可点击，且是 `check_links.py` 的盲区。
- 解析策略（**命中即用，解析不到就不动**）：按序尝试 `entry_dir/../<token>`（同库）→
  `entry_dir/../../<token>`（工作区根 / 其它库）→ `entry_dir/<token>`（同目录）。
  解析不到实际文件/目录的 token 原样保留，所以 `github.com/xxx`、`x.osmenoga.com/xxx` 这类
  **URL 片段不会被误转成链接**。
- 链接文字自动取目标条目 frontmatter 的 `title`；目标是目录时取所属库 `manifest.json` 里该分类的 title。
- **安全设计（血泪）**：必须**按围栏代码块切段**，只对代码块外的片段做替换。
  第一版用"等长占位盖住围栏 + 替换后按位还原"，结果替换本身改变长度、按位还原失效——
  脚本自己断言到长度变化而中止（这个断言救了场）。**不要用等长占位方案。**
- 每文件断言：行数不变、反引号总数恰减少 2×替换数、围栏数量不变；读写用 `newline=""`。
- 用法：`python scripts/linkify_refs.py <kb-dir>`（dry-run）→ `--apply` 实际写盘。
  转换后**必须重跑 `build_index.py` 并用条目数做端到端校验**，再跑 `check_links.py`。

### scripts/fix_aliases.py（清理 aliases 冗余项）
- 一次性清掉三类**冗余且有害**的别名，判定键统一为 `re.sub(r"\s+", "", s.lower())`：
  ① 归一化后重复的项（**这是 `validate_kb.py` 的 ERROR 来源**，如 `DynDOLOD`+`dyndolod`）；
  ② 与 `tags` 归一化后相同的项（tags 已单独计 40 分）；
  ③ 与自身 `id` 相同的项（id 精确命中已计 100 分）。
- 只改 `aliases:` 那一行；每文件断言"恰好 1 行发生变化"（用 `old.split("\n")` 与 `new.split("\n")` 逐行 diff 计数），
  读写 `newline=""`。
- 会打印清理后 **<3 条别名**的条目，供人工补写。
- 用法：`python scripts/fix_aliases.py <kb-dir>`。写完重跑 `validate_kb.py`（须 0 ERROR / 0 NOTE）与 `build_index.py`。

### scripts/kb.py（多库工作区：agent 检索入口）
- 跨库检索入口，零依赖单文件。子命令：`list` / `toc <kb>` / `find <kw>` / `grep <正则>` / `show <id>` / `read <id>` / `check`，均支持 `--json`。
- **数据源永远是各条目的 frontmatter**，不维护额外清单 —— 这是它不会过期的原因。
- `show` 只给「元数据 + `##`/`###` 大纲」，把"读不读、读哪段"交回调用方；`find` 只给「路径 + 别名 + 摘要」。
- `check` 校验工作区根的 `AGENTS.md` 是否覆盖了所有含 `manifest.json` 的库目录，**新增库后漏写会以非零退出码报出**。
- 库发现规则：工作区下任一含 `manifest.json` 的一级目录（**不按 `*-kb` 后缀判断** —— 库可能叫 `01-navigation`，用命名巧合当判据会静默漏掉）。
- 用法：`kb.py list`、`kb.py find 拉弓 移动 -n 6`、`kb.py show authoring-workflow`。

### scripts/sync_scripts.py（多库工作区：防止脚本分叉）
- 五件套脚本在技能与每个库中各有一份副本。副本一多，只改一处就会变成"技能是这个行为、库里是那个行为"的**隐性分叉**，排查极费时间。
- 按**字节**（sha256）比较，把不一致的库内副本用技能 stock 版覆盖，覆盖前备份到 `_raw/pre-sync-<日期>/`；打印每个脚本的指纹，**指纹数为 1 才算真正统一**。
- 用法：`python scripts/sync_scripts.py`（同步）、`--check`（只检查，退出码非 0 表示有分叉）、`--kb <name>`（单个库）。
- 纪律：**改完技能里的任何 stock 脚本，必须跑一次同步**，否则下一次构建就会产生分叉。

### scripts/selftest_new_kb.py（自检：新建库是否继承当前索引页 UI）
- **"新库自动带上当前 UI"的唯一途径是从技能 `scripts/` 复制五件套**，而这件事没有任何默认报错：
  新库里若另写或从旧库抄了一份 `build_index.py`，构建成功、校验通过，**UI 却是旧样子**，静默得很。
- 本脚本把这条变成可执行断言：在**系统 temp 目录**造一个最小库（manifest + 1 条目 + 复制来的五件套），
  依次跑 `build_index` / `validate_kb` / `check_index_ui`，再对产物断言「含 `#navtoggle` 与 `#navfab`、
  两者都带 `.navfab` 类、无已废弃的 `.navtoggle{}` 与 `78px` 窄条、产物全 LF」，
  **跑完即删临时目录，不碰任何真实资料库**。
- 用法：`python <skill>/scripts/selftest_new_kb.py`。**新建资料库后、或改过索引页模板后跑一次。**
- 给索引页加新 UI 特性时**顺手在这里补一条断言** —— 它是"新库会不会继承"的唯一自动化保障。

> 💡 注意 `build_index.py` / `validate_kb.py` 的**根因**都在本目录的 `scripts/` 下（stock 版），
> 各库里的是副本。要改行为就改技能里的，再同步 —— 直接改库里的那份，下次同步就被覆盖。

### scripts/gen_features.py（同类条目多时）
- 把同类条目（如功能列表）定义为数据数组，循环写文件，保证格式一致；编辑数组后重跑即刷新。
- **必须做成"脚手架"而不是"真相来源"**：默认**跳过已存在的文件**，只在显式 `--force` 时才按数组重写。
- 原因：条目一旦被手工精修（补上工作原理、参数、需求、兼容性、贡献者等深度内容），生成器里的摘要数组**必然落后于正文**。此时若默认覆盖，一次误跑就会把精修内容全部打回模板——而且脚本会打印"Generated N entries"，看起来完全正常。**静默的破坏比报错危险得多。**

## 工作流
1. 用 `fetch_mediawiki.py`（或 WebFetch）**并行**抓取来源内容，存 `_raw/`。
2. 先建目录结构与 `manifest.json`（分类 dir + 中文 title + 来源信息）。
   **目录名一律带 `NN-` 前缀，条目全部放进分类子目录**（见"标准产出结构"里的硬约束）。
   同时**从技能 `scripts/` 复制五件套**到新库的 `scripts/` —— 这是"新库自动带上当前索引页 UI"
   的唯一途径（索引页模板就在 `build_index.py` 的 `HTML_TEMPLATE` 里），**不要另写一份副本**：
   ```bash
   cp <skill>/scripts/{build_index,validate_kb,check_index_ui,check_links,fix_links}.py <new-kb>/scripts/
   ```
3. 写内容页（概览/安装/参考/开发/工具），功能类用生成器。给每个条目补 `aliases`。
4. 写 `README.md` / `CHANGELOG.md` / `CONTRIBUTING.md`。
5. 生成与校验：跑 `build_index.py` 生成 `index.json` / `index.html`，再依次跑 `validate_kb.py`（结构 + 索引 + 模板）与
   `check_index_ui.py`（交互回归）—— **两个都过才算完成**。改索引页模板后必须重建；**不要手改 `index.html`，下次重建就丢**。
   若本步新增/移动过条目或分类目录，**再跑一次 `check_links.py`**（坏链不报错、构建照样过，只有这个脚本能发现）。
   若是**新建的库**（或刚改过索引页模板），再跑一次技能的 `selftest_new_kb.py`，
   确认新库确实继承了当前索引页 UI —— 它只在系统 temp 目录里造临时库，不会碰你的资料库。
6. **多库工作区**：在工作区根写 `AGENTS.md`（模板 `references/agents-md-template.md`），
   放 `scripts/kb.py` 与 `scripts/sync_scripts.py`，跑一次 `kb.py check` 确认入口覆盖全部库，
   跑 `sync_scripts.py` 让各库脚本与 stock 一致。
7. 交付：`present_files` 展示 `index.html`（实时预览）+ `README.md`。

## 环境坑（实战踩过）
- **Bash 环境 PATH 可能损坏**（`ls`/`dirname`/`head` 等 not found）：文件操作用 `Read`/`Write`/`Edit` 工具，网络/计算用**托管 Python 绝对路径**（见运行环境），不要依赖裸 `python`/`ls`。
- **同一文件不要并行发多个 Edit**：并发编辑会互相覆盖或报 `EBUSY`，且工具可能返回"Success"但实际未落盘。要改同一文件多处时，用**单次 Python 脚本做字符串替换**（`.replace()` + 断言复核），或严格串行逐个 Edit；改完立刻 `Read` 复核是否真的生效。
  - 已实测的失败姿势：**在同一条消息里对同一个文件发两个 Edit**，第一个先落盘，第二个仍按旧内容匹配、同样返回"成功"，最终只有一处生效、另一处被静默丢掉。（2026-09-21 实测踩到。）
  - 用脚本批量替换时**先全部校验、再统一写盘**：每处断言"恰好命中 1 次"，任何一处不中就整体中止且不写任何文件，避免留下改到一半的半成品。
- Windows 路径用正斜杠或在 Python 里 `replace("\\","/")`；`os.walk` 跨平台可用。
- **同一批条目可能混用换行符**（实测某库 47 个生成出来的条目是 CRLF、其余 15 个是 LF）。批量改 frontmatter 时**必须按字节处理并保留原换行符**：用 `io.open(p,"rb")` + `raw.split(sep)`/`sep.join()`，`sep = b"\r\n" if b"\r\n" in raw else b"\n"`；用文本模式 `open(..., "w")` 会把 CRLF 统一成 LF，产生整文件级 diff。
- **批量改写 frontmatter 的纪律**：先逐文件断言锚点「恰好命中 1 次」，再**逐行比对**证明只有目标行变化、行数不变、字节增量等于替换差值，**全部通过才统一写盘**；写完再复核一遍并统计异常数。任一文件不中就整体中止、不写任何文件。
- **⚠️ 切片陷阱（2026-09-22 实测翻车，静默破坏 33 个条目）**：用正则定位 frontmatter 时，
  `m.start()` 指向的是**含 `---` 分隔符**的整体匹配起点，而 `m.group(1)` **不含**分隔符。
  写成下面这样就会**丢掉开头的 `---\n`**，并把原 `raw` 的末 4 个字符挤到 `summary` 行末尾：
  ```python
  m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
  raw = m.group(1)
  new_text = text[:m.start()] + new_raw + text[m.start() + len(raw):]   # ✗ 错
  ```
  正确写法是**拼回完整的 frontmatter 块**，不要去算 group 的偏移：
  ```python
  new_text = "---\n" + new_raw + "\n---\n" + text[m.end():]            # ✓ 对
  ```
  后果：条目数从 43 掉到 10（正好是没被改的那批），报「缺少 frontmatter」。
  **修复**：被吞的恰是分隔符的 4 个字符，所以确定性地剥掉结束分隔符前的末 4 个字符
  （用「每行都必须是合法 `key: value`」做断言确认），再补回 `---\n`。
- **⚠️ 校验别只查「关键字段是否存在」**：上例中追加到**同一行末尾**的垃圾，
  行首检查与"字段存在"检查**全都抓不到**（第一版修复脚本因此误判成"已经是干净的"）。
  要断言**每个非空行都匹配 `^[A-Za-z_]+:`**，或用 `build_index.py` 的**条目数**做端到端校验
  —— 数量对不上是最早、最可靠的报警信号。
- **⚠️ 不要用「等长占位」屏蔽不需要改的区域**（2026-09-22 实测翻车）：把围栏代码块用等长占位
  盖住、替换完再按位还原 —— 这个方案**必然失效**，因为**替换本身会改变字符串长度**，
  后续位置全部错位、按位还原也就错位。正确做法是**按区域切段**：用
  `re.finditer(r"^```.*?^```\s*$", re.S|re.M)` 切出「代码段 / 围栏段」交替的片段，
  只对代码段做替换，围栏段原样 append 拼回。同理，**任何"先遮蔽、后还原"的批量改写都该被怀疑**。
- **⚠️ 批量改写必须自带断言，让错误自己暴露**：即使只改 1 行也要断言（行数不变、
  「恰好 1 行变化」、「语法记号减少量 == 替换数」、「围栏数量不变」）。
  上面那次翻车就是**被脚本自己的长度断言拦下的** —— 没有断言就会静默写坏一批文件。
- **PowerShell 的 `Add-Type` 可能被本机安全策略禁止**（"compiles and loads .NET code at runtime"）：
  需要调 Win32 API（如走回收站的 `shell32.SHFileOperationW`）时改用**托管 Python + ctypes**。
  ⚠️ 且沙箱下 `SHFileOperationW` 可能返回非 0、`C:\$Recycle.Bin` 里也查不到条目 ——
  **动用户目录的文件，备份必须自己做，别把回收站当保险。**
- 索引构建与抓取都要用 UTF-8 读写，避免中文乱码。
- **`md_to_html()` 的代码围栏必须顶格**：`re.match(r"^```(\w*)\s*$", line)` 允许零个前导空格，所以**缩进在列表项里的 ``` 块不会被识别**（会当普通段落渲染）。但把围栏顶格又会打断列表，使后续 `ol` 重新从 1 编号。因此：**列表项内的配置/代码片段一律用行内 `` `code` `` 表达**，需要整块围栏代码时放到列表之外。
- **新增/改完条目后做一次机械校验**：直接跑 `scripts/validate_kb.py`（已断言 `id == 文件名`、`category` 与目录名相符、必填字段非空、`index.json` 条目数与正文非空）；必要时再抽查 `<h2>` / `<table>` 计数。避免"写完了但没进索引/没渲染"这类静默失败。

## 注意事项
- 来源务必指向官方页面，关键数值勿凭记忆改写。
- **条目放错层会被静默丢弃**：`build_index.py` 跳过库根层，条目必须进 `NN-` 前缀的分类子目录。
  构建输出 `0 entries` **不报错** —— 写完目录后扫一眼构建输出的条目数是否与预期相符。
- **改索引页模板等于改产品**：改完必须重建 + 跑 `validate_kb.py` + `check_index_ui.py`，否则很容易出现"新库少个功能、老库点不动"这类静默回归。
- **改完 stock 脚本必须同步**：`python scripts/sync_scripts.py`。只改技能或只改某个库，都会造成"技能一个行为、库另一个行为"的隐性分叉。
- **坏链是"不会报错的错误"**：新增/移动目录或批量写条目后，务必跑 `check_links.py`；用 `fix_links.py` 修，别手改 `../` 层数。
- **换行统一为 LF**：库内混用 LF/CRLF 会让 diff 噪音巨大。批量改动一律按字节处理并保留原换行（见"环境坑"），但从零新建的条目就写 LF；发现混用时用脚本一次性归一化并记进 CHANGELOG。
- **生成器脚本自身必须写 `newline=""`**：`open(p, "w", encoding="utf-8", newline="")`。
  默认文本模式在 Windows 上会把 `\n` **静默**翻译成 `\r\n`。
  **这一类 bug 已出现过两次**：先是 `gen_features.py` 产出 4 个 CRLF 条目；
  后是 **`build_index.py` 写 `index.json` / `index.html` 时漏传**，导致每次重建都往产物里灌 CRLF
  （stock 版 2026-09-21 已修正，六库已同步）。
  **只归一化产物而不修生成器，下次重跑又会被写回去** —— 修产物是治标，修生成器才是治本。
- **`check_links.py` 查不出这个问题**：它只 lint `.md`，不检查 `index.json` / `index.html` 的换行。
  怀疑产物换行异常时，直接按字节扫：
  `python -c` 不可靠，写成脚本：遍历目标目录，`open(p,"rb").read()` 后断言 `b"\r\n" not in raw`。
- **配合 git 用时必须加 `.gitattributes`**：本机常见 `core.autocrlf=true`，
  会在检出时把全库 LF 改写成 CRLF，与「全部为 LF」的约定直接冲突。
  工作区根放一行 `* text=auto eol=lf` 即可覆盖该设置（`eol=` 优先级高于 `core.autocrlf`）。
  ⚠️ 加了之后**别顺手跑 `git add --renormalize .`** —— 它会把工作区文件按新属性重新检出，
  可能一次性改掉大量文件的磁盘换行（实测一次刷出 13 个 CRLF 文件），
  确认索引本身已是 `i/lf` 就足够了（用 `git ls-files --eol <path>` 看）。
- 功能条目众多时优先数据驱动生成，避免手工 50+ 文件。
- 本技能产出"结构 + 内容"，上游版权保留出处（如 GPL-3.0 精神 / UESP 署名）。

## 参考文件
- `references/agents-md-template.md`：多库工作区的 agent 入口契约模板（含三条设计铁律与踩坑记录）。
- `scripts/kb.py`：跨库检索入口（可复制到工作区 `scripts/` 下直接用）。
- `scripts/sync_scripts.py`：把 stock 脚本同步到各库，防止副本分叉。
- `scripts/selftest_new_kb.py`：自检「从技能复制脚本新建的库是否继承当前索引页 UI」（temp 里造库、跑完即删）。
- `scripts/linkify_refs.py`：把条目里的反引号纯文本引用批量转成 markdown 链接（`check_links.py` 的盲区修补）。
- `scripts/fix_aliases.py`：清理 `aliases` 的重复项 / 与 tags 同名项 / 与 id 同名项（validate 报 ERROR 的根源）。

> 后两个是**技能级维护工具，不参与 `sync_scripts.py` 同步**（后者按显式 `SYNC_FILES` 列表工作），
> 因此不会影响各库脚本指纹的一致性。用法均为 `<script> <kb-dir> [--apply]`。
