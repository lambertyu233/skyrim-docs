# Mod Organizer 2 · USVFS 资料库

> 基于 [USVFS GitHub README](https://github.com/ModOrganizer2/usvfs)、[MO2 Debugging usvfs Wiki](https://github.com/ModOrganizer2/modorganizer/wiki/Debugging-usvfs)、[STEP Mod Organizer 指南](https://stepmodifications.org/wiki/Guide:Mod_Organizer)、[DeepWiki 源码解析](https://deepwiki.com/ModOrganizer2/modorganizer) 等官方/准官方来源整理的可维护、分层、版本化 **USVFS（Mod Organizer 2 虚拟文件系统）资料库**。
> 面向长期协作更新：每个条目独立成文件、带统一元数据，新增/删除/修改后一键刷新索引。

---

## 这是什么

[Mod Organizer 2（MO2）](https://stepmodifications.org/wiki/Guide:Mod_Organizer) 是开源 mod 管理工具，其"心脏"是 **USVFS（用户态虚拟文件系统）**——靠 API hooking 在运行时把分散的 mod 合并成游戏看到的目录，而不改动游戏真实文件。本资料库把分散的机制说明、特性对比、源码级架构、调试排错与使用运维，结构化为一个便于检索与维护的知识库。

## 目录结构（清晰分层）

```
mo2-usvfs-kb/
├── manifest.json          # 资料库元数据 + 条目 schema + 分类定义 + 来源
├── index.json             # 自动生成的纯元数据索引（便于程序化增删改查）
├── index.html             # 自动生成的离线可搜索/筛选浏览器（双击即用）
├── README.md              # 本文件
├── CHANGELOG.md           # 版本化变更记录
├── CONTRIBUTING.md        # 协作维护规范
├── 00-overview/           # 概览：MO2 与 USVFS 的定位、角色
├── 01-mechanism/          # 核心机制：hooking、进程可见、会话级、overlay、虚拟删除
├── 02-features/           # 特性对比：USVFS vs NTFS 符号链接、代价与风险
├── 03-architecture/       # 源码级架构：VFS 节点类、DirectoryRefresher、优先级、Connector、BSA
├── 04-debugging/          # 调试排错：hook 命名、usvfs 日志、Process Monitor
├── 05-usage/              # 使用与运维：运行时部署、隔离、profile、冲突、Overwrite
├── 06-reference/          # 参考：FAQ、VFS/USVFS 排错
├── _raw/                  # 上游来源抓取/摘要存档（索引构建忽略）
└── scripts/
    ├── build_index.py    # 扫描全部 frontmatter → index.json + index.html
    ├── validate_kb.py    # 结构 + 索引 + 索引页模板的机械校验
    ├── check_index_ui.py # 索引页交互回归（Node + DOM 桩，不需要浏览器）
    ├── check_links.py    # 站内相对链接 lint（附带换行一致性提示）
    ├── fix_links.py      # 修复链接深度错误（按目标尾部路径反查，不靠手写 ../ ）
    └── fetch_mediawiki.py# 通用 MediaWiki 抓取器（抓取 STEP 指南，存档于 _raw/）
```

## 快速使用

- **浏览**：双击 `index.html`（无需联网，内置全文搜索、分类过滤、排序；点卡片内联展示整篇正文，含"打开本地 .md""官方来源"按钮）。
- **程序化查询**：读取 `index.json`（含每条的 id/标题/分类/标签/来源/摘要/路径/正文）。
- **看原文**：每个条目 `source` 字段指向官方页面。

## 如何维护（增删改查）

1. 在对应分类目录新建 `your-id.md`，填写统一 `frontmatter`（字段见 `manifest.json → schema`）。
2. 运行 `scripts/build_index.py` 刷新索引。
3. 跑三项校验，都过再算完成：`python scripts/validate_kb.py`（结构）、`python scripts/check_index_ui.py`（索引页交互回归）、`python scripts/check_links.py`（站内相对链接）。
4. 任何内容变更：递增相关条目 `version`，并在 `CHANGELOG.md` 记录；资料库整体版本号维护在 `manifest.json` 与 `CHANGELOG.md`。

## 设计原则

1. **分层清晰**：按读者意图（概览→机制→特性→架构→调试→使用→参考）组织。
2. **单文件条目**：每个主题一个 Markdown，互不耦合，便于单独修订与 PR。
3. **元数据驱动**：统一 frontmatter 让索引、搜索、过滤自动化。
4. **版本化**：CHANGELOG + 每条目 version，可追溯演进。
5. **协作友好**：约定明确，自动化索引降低合并冲突与人工维护成本。

---

*资料库版本 1.2.0 · 生成于 2026-09-21 · 内容整理自 MO2 / USVFS 官方文档、[STEP 非官方 Mod Organizer 指南](https://stepmodifications.org/wiki/Guide:Mod_Organizer) 与 DeepWiki 源码解析（USVFS 当前 GPLv3）。*
