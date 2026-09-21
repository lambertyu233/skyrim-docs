# 上古卷轴5 动作引擎资料库（FNIS / Nemesis / Pandora）

可维护 · 分层 · 版本化 · 协作更新 —— 围绕**行为引擎（Behaviour Engine）**整理的结构化 Markdown 资料库。

- 打开 **[`index.html`](index.html)** 即可离线浏览（两栏布局、全文检索、内联渲染正文，双击即用，无需起服务器）。
- 程序化消费请读 **[`index.json`](index.json)**。

## 这是什么 / 解决什么问题

"动作引擎"不是动画包，而是**按你的 modlist 现场生成一份行为文件（.hkx）的补丁工具**。本库回答四类问题：

1. **原理**：Havok Behavior 是什么？hkx 为什么"有两种"？补丁器到底在做什么？
2. **对比**：FNIS / Nemesis / Pandora 三代的官方对比与真实差异。
3. **操作**：怎么装、怎么刷、输出放哪、遇到报错怎么办。
4. **辨析**：哪些来源可信、哪些在编造。

## 目录结构

```
behaviour-engine-kb/
├── manifest.json          # 元数据 + schema + 分类定义 + 来源
├── index.json / index.html# 自动生成的索引（离线浏览器）
├── README.md              # 本文件
├── CHANGELOG.md           # 版本化变更记录
├── CONTRIBUTING.md        # 协作规范（增删改查流程）
├── 00-overview/           # 概览：定位、三引擎脉络、官方对比表
├── 01-principles/         # 原理：Havok Behavior、hkx、补丁器、动画数据库、Patcher vs Replacer
├── 02-fnis/               # FNIS：机制、兼容性、淘汰原因
├── 03-nemesis/            # Nemesis：模板化、复杂度分级、局限
├── 04-pandora/            # Pandora：架构、补丁格式、安装、排错
├── 05-ecosystem/          # 生态：OAR/DAR、AMR、工具链
├── 06-practices/          # 实战：选型、刷补丁流程、常见报错
├── 07-sources/            # 来源：官方清单、社区来源、不可信来源警示
├── _raw/                  # 抓取的上游原文存档（不参与索引）
└── scripts/               # 索引构建脚本
```

## 怎么用

**人读**：双击 `index.html` → 左栏选分类 → 点卡片看全文（内联渲染）。
**机读**：`index.json` 含 `entries[]`（含 `content` 字段为渲染后的 HTML）。

## 怎么维护

1. 在对应分类目录新建/修改 `.md`，**保持 frontmatter 的 `category` 等于目录名**。
2. 跑 `python scripts/build_index.py` 重新生成索引。
3. 按 [`CONTRIBUTING.md`](CONTRIBUTING.md) 的检查清单自检。

## 来源与版权

- 官方原理与数据来自 **Pandora 官方 Wiki / README**、**FNIS / Nemesis Nexus 页面**等（见 [`07-sources/official-sources.md`](07-sources/official-sources.md)）。
- Pandora、Nemesis 为 **GPLv3**，FNIS 闭源；版权归各原作者。本库为结构化整理，仅供学习与协作维护。
- 每页正文内以 `> 来源：…` 标注出处，**关键数值均按原页核对，不凭记忆改写**。

## 关于本库的定位提醒

- 本库**不是**教程搬运，而是"官方口径 + 社区经验 + 来源辨析"的**知识基线**。
- 涉及**版本号/路径**时，务必回官方页面复核（见 [`07-sources/unreliable-sources.md`](07-sources/unreliable-sources.md)）。
