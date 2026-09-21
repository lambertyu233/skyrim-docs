---
id: contributing
title: 参与贡献
category: 04-development
version: 1.0.0
updated: 2026-09-20
tags: [贡献, 开发, 社区, GitHub, Discord]
source: https://modding.wiki/en/skyrim/developers/community-shaders#contributing
summary: 如何参与 Community Shaders 的代码、文档、测试与着色器贡献。
---

# 参与贡献

Community Shaders 是社区驱动项目，欢迎对**代码、文档、测试、着色器**的贡献。

## 入口

- **GitHub 仓库**：[community-shaders/skyrim-community-shaders](https://github.com/community-shaders/skyrim-community-shaders)
- **Discord**：[discord.gg/nkrQybAsyy](https://discord.gg/nkrQybAsyy)
- **贡献指南**：`CONTRIBUTING.md`（dev 分支）

## 方式

- **功能请求**：Discord `#cs-feature-request` 频道（勿直接发 GitHub Issues，除非开发者要求）。
- **加入开发**：Fork / PR，阅读官方 CONTRIBUTING；可加入 `#cs-development-discussion`。AI 辅助可行，未经验证的 vibe coding 不行。
- **测试开发中功能**：Discord `#cs-testing`（测试构建不提供常规支持，常为 AIO，须卸旧 CS/功能且无冲突；反馈回原线程）。
- **文档**：本资料库即社区文档成果之一——见根目录 [CONTRIBUTING.md](../CONTRIBUTING.md) 了解如何协同维护。

## 本资料库的贡献约定

- 每个条目独立成 `.md` 文件，带统一 `frontmatter`（见 [manifest.json](../manifest.json) 的 schema）。
- 新增/删除条目后运行 `scripts/build_index.py` 刷新 `index.json` 与 `index.html`。
- 功能类条目统一由 `scripts/gen_features.py` 的 `FEATURES` 列表生成，编辑该列表后重跑。
- 任何内容变更须在 [CHANGELOG.md](../CHANGELOG.md) 记录版本与摘要，并递增版本号。
