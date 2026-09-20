# Creation Kit 资料库

> 基于 [UESP Creation Kit Wiki](https://ck.uesp.net/wiki) 整理的可维护、分层、版本化资料库。
> 覆盖 Creation Kit 的 **概览 / 安装 / 编辑器功能 / 游戏系统 / Papyrus 脚本 / 工具 / 教程** 七大板块。

本资料库面向《上古卷轴 V：天际》（The Elder Scrolls V: Skyrim）MOD 开发者，结构清晰、单文件条目、元数据驱动，便于长期协作与增删改查。

---

## 目录结构

```
creation-kit-kb/
├── manifest.json        # 元数据 + 条目 schema + 分类定义 + 来源
├── index.json           # 自动生成的纯元数据索引（程序化消费）
├── index.html           # 自动生成的离线可搜索浏览器（双击即用）
├── README.md            # 本文件：导航与使用说明
├── CHANGELOG.md         # 版本化变更记录
├── CONTRIBUTING.md      # 协作规范（增删改查流程）
├── 00-overview/         # 概览
├── 01-installation/     # 安装与配置
├── 02-features/         # 编辑器功能
├── 03-game-systems/     # 游戏系统
├── 04-scripting/        # Papyrus 脚本
├── 05-tools/            # 工具链
├── 06-tutorials/        # 教程
└── scripts/
    ├── fetch_ck.py      # 从 UESP API 抓取原始 wikitext 到 _raw/
    ├── gen_features.py  # 数据驱动生成 04-scripting 下的脚本对象条目
    └── build_index.py   # 扫描全部 frontmatter → index.json + index.html
```

分类目录名带 `00-`~`06-` 序号前缀，便于排序；每个条目一个 `.md` 文件，互不耦合。

---

## 快速开始

1. **浏览资料库**：双击 `index.html`（离线可用，支持搜索 / 分类 / 状态过滤 / 排序）。
2. **查看条目**：在 `index.html` 中点击「查看条目」，或直接打开对应分类目录下的 `.md` 文件。
3. **重新生成索引**（修改或新增条目后务必执行）：
   ```bash
   python scripts/build_index.py
   ```
4. **抓取最新原文**（可选，用于同步上游）：
   ```bash
   python scripts/fetch_ck.py --quiet <PageTitle> ...
   python scripts/fetch_ck.py --cat <CategoryName>
   ```

---

## 条目规范

每个 `.md` 文件顶部统一 frontmatter：

```yaml
---
id: creation-kit
title: Creation Kit 概述
category: 00-overview        # 必须等于所属目录名
version: 1.0.0
updated: 2026-09-20
tags: [creation-kit, overview, skyrim]
source: https://ck.uesp.net/wiki/Creation_Kit
summary: Creation Kit 是天际的内容编辑器，当前版本 1.9.32.0。
status: stable
kind: concept
---
```

- `category` 必须等于目录名，否则索引过滤会失效。
- `source` 指向官方页面，关键数值（版本号/路径/参数）以官方为准，勿凭记忆改写。
- 详细协作流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 来源与版权

- 内容整理自 **UESP Creation Kit Wiki**（社区维护），条目均保留原始 `source` 链接。
- 本资料库仅作结构化整理与中文导读，版权与署名遵循上游文档精神。
