# CONTRIBUTING — 资料库协作维护规范

本规范用于**长期协作维护** Community Shaders 资料库。目标是让任何人都能安全、低冲突地增删改查内容。

## 1. 条目格式（必须遵守）

每个条目是一个 Markdown 文件，顶部带 YAML `frontmatter`：

```markdown
---
id: unique-id            # 小写连字符，唯一，用于索引与链接
title: 中文标题
category: 02-features    # 必须是分类目录名（索引据此过滤）
kind: core               # 仅功能条目：core / additional
status: released         # released / TBA
version: 1.0.0           # 语义化；内容变更时递增
updated: 2026-09-20      # YYYY-MM-DD
tags: [光照, 性能]        # 便于检索
source: https://...      # 官方来源 URL
summary: 一句话摘要
---

# 标题
正文……
```

字段定义见 `manifest.json → schema`。

## 2. 增（Create）

- **普通条目**：在对应分类目录新建文件，填好 frontmatter 与正文。
- **功能条目**：编辑 `scripts/gen_features.py` 的 `FEATURES` 列表后运行生成（推荐，保证格式一致）；也可直接新建/编辑 `02-features/*/*.md`。

## 3. 删（Delete）

- 直接删除对应 `.md` 文件；功能条目也可从 `FEATURES` 列表移除后重新生成。
- 若有其它条目通过相对链接引用它，需同步更新引用。

## 4. 改（Update）

- 编辑文件正文与 frontmatter。
- **必须**：递增该条目 `version`，更新 `updated` 日期。
- **必须**：在 `CHANGELOG.md` 记录本次变更摘要。
- 若涉及结构/分类调整，递增资料库整体版本（`manifest.json` 与 `CHANGELOG.md`）。

## 5. 查（Query）

- 人工：双击 `index.html` 使用搜索 / 分类 / 状态过滤。
- 程序化：读取 `index.json`（每条含 id、标题、分类、标签、来源、摘要、路径）。

## 6. 提交前必做

运行索引生成器，确保索引与条目一致：

```bash
python scripts/build_index.py
```

（功能条目变更还需先 `python scripts/gen_features.py`。）

## 7. 协作约定

- 一个 PR 聚焦一个主题，便于审阅。
- 不篡改他人条目的 `id`（会导致链接失效）。
- 来源务必指向官方页面；勿凭记忆改写关键数值（版本号、路径、参数）。
- 内容基线跟踪官方文档版本（当前 CS 1.8.4），重大上游变更应在 PR 说明中标注。
- 遵循上游 [GPL-3.0](https://github.com/community-shaders/skyrim-community-shaders#license) 精神，仅做结构化整理与翻译，保留出处。
