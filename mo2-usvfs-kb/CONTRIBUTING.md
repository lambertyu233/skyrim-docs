# 协作规范（CONTRIBUTING）

本资料库面向社区协作维护。请遵循以下约定，降低合并冲突、便于程序化索引。

## 条目文件约定

- **单文件单主题**：每个主题一个 `.md`，放在对应分类目录（`00-overview` ~ `06-reference`）。
- **`category` 必须等于目录名**（如 `01-mechanism`），索引据此过滤。
- **文件名 = `id`**：用小写连字符（如 `api-hooking.md`），与 frontmatter 的 `id` 一致。
- **统一 frontmatter**（必填：`id` `title` `category` `version` `updated` `tags` `source` `summary`；可选：`kind`）。字段含义见 `manifest.json → schema`。

## 内容约定

- 关键数值、路径、函数名（如 `hook_GetFileAttributesW`、源码路径）务必对照官方来源，勿凭记忆改写。
- 每个条目顶部 `source` 指向最贴切的官方页面；多条来源可在文内补充链接。
- 正文用标准 Markdown（标题/列表/表格/代码块/引用），索引页会内联渲染。
- 条目间可用相对路径互相链接（如 `01-mechanism/api-hooking.md`）。

## 增 / 改 / 删 流程

1. 新增：在对应目录建文件 → 填 frontmatter → 写正文。
2. 修改：编辑文件 → 递增该条目 `version` → 在 `CHANGELOG.md` 记录。
3. 删除：直接删文件（如有他处引用，一并更新链接）。
4. 每次增删改后运行：`python scripts/build_index.py`，确认 `index.json` / `index.html` 刷新无误。
5. 提交 PR（或合并）前跑三项校验，都过才算完成：`python scripts/validate_kb.py`（结构）、`python scripts/check_index_ui.py`（索引页交互回归，20 项断言）、`python scripts/check_links.py`（站内相对链接；**新增/移动条目后必跑**——`validate_kb.py` 不查正文链接）。
6. 再确认 `index.html` 无残留占位符、分类统计正确。

## 版本化

- 条目 `version` 语义化（1.0.0 起），内容变动即递增。
- 资料库整体版本维护在 `manifest.json` 与 `CHANGELOG.md`。

## 来源与版权

- 上游：MO2 / USVFS 官方文档（USVFS 当前 GPLv3）及 DeepWiki 解析。
- 本资料库仅做结构化整理，便于学习与协作维护；如有上游更新，请同步到对应条目并注明 `updated` 日期。
