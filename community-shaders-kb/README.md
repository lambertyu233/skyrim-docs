# Community Shaders 资料库

> 基于 [modding.wiki 官方文档](https://modding.wiki/en/skyrim/developers/community-shaders) 整理的可维护、分层、版本化 **Community Shaders 资料库**。
> 面向长期协作更新：每个条目独立成文件、带统一元数据，新增/删除/修改后一键刷新索引。

---

## 这是什么

[Community Shaders (CS)](https://modding.wiki/en/skyrim/developers/community-shaders) 是开源、模块化的 Skyrim 图形增强框架，提供先进光照、材质与视觉特效。本资料库把分散的官方页面（安装、功能、FAQ、PBR 开发、工具）结构化为一个便于检索与维护的知识库。

## 目录结构（清晰分层）

```
community-shaders-kb/
├── manifest.json          # 资料库元数据 + 条目 schema + 分类定义
├── index.json             # 自动生成的索引：元数据 + 内联渲染后的正文（便于程序化增删改查与外部工具消费）
├── index.html             # 自动生成的离线可搜索/筛选浏览器（双击即用）
├── README.md              # 本文件
├── CHANGELOG.md           # 版本化变更记录
├── CONTRIBUTING.md        # 协作维护规范
├── 00-overview/           # 概览：定位、架构与缓存
├── 01-installation/       # 安装：需求、安装指南、Vanilla 设置、ENB 迁移
├── 02-features/           # 功能：core/ 与 additional/ 每特性一文件
├── 03-reference/          # 参考：不兼容 MOD、FAQ
├── 04-development/        # 开发：PBR 美术师指南、贡献
├── 05-tools/              # 工具：Light Placer、PGPatcher
├── _raw/                  # 上游原文存档 / 历史备份（索引构建会忽略）
└── scripts/               # build_index.py + validate_kb.py + check_index_ui.py（gen_features.py 为遗留生成器）
```

## 快速使用

- **浏览**：双击 `index.html`（无需联网，内置全文搜索、分类过滤、排序）。
- **程序化查询**：读取 `index.json`（含每条的 id/标题/分类/标签/来源/摘要，以及渲染好的正文 `content` 与相对路径 `_file`）。
- **看原文**：每个条目 `source` 字段指向官方页面。

## 如何维护（增删改查）

### 新增一个普通条目
1. 在对应分类目录新建 `your-id.md`，填写统一 `frontmatter`（字段见 `manifest.json → schema`）。
2. 运行 `scripts/build_index.py` 刷新索引。

### 新增 / 修改 / 删除功能条目
- 功能条目由 `scripts/gen_features.py` 的 `FEATURES` 列表统一生成。
- 编辑该列表后运行 `python scripts/gen_features.py`，再运行 `build_index.py`。
- 也可直接编辑已生成的 `02-features/*/*.md`（手动微调个别条目）。

### 版本化
- 任何内容变更：递增相关条目 `version`，并在 `CHANGELOG.md` 记录。
- 资料库整体版本号维护在 `manifest.json` 与 `CHANGELOG.md`。

## 设计原则

1. **分层清晰**：按读者意图（概览→安装→功能→参考→开发→工具）组织。
2. **单文件条目**：每个主题一个 Markdown，互不耦合，便于单独修订与 PR。
3. **元数据驱动**：统一 frontmatter 让索引、搜索、过滤自动化。
4. **版本化**：CHANGELOG + 每条目 version，可追溯演进。
5. **协作友好**：约定明确，自动化索引降低合并冲突与人工维护成本。

---
*资料库版本 2.0.0 · 生成于 2026-09-21 · 内容整理自 Community Shaders 社区官方文档（GPL-3.0）。*
