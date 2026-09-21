# 上古卷轴5 OAR 资料库（Open Animation Replacer）

可维护 · 分层 · 版本化 · 协作更新 —— 围绕 **OAR（Open Animation Replacer）** 整理的结构化 Markdown 资料库。

- 打开 **[`index.html`](index.html)** 即可离线浏览（两栏布局、全文检索、内联渲染正文，双击即用，无需起服务器）。
- 程序化消费请读 **[`index.json`](index.json)**。

## 这是什么 / 解决什么问题

**OAR** 是一个 SKSE 框架插件：在游戏请求某个已有动画时，**按可配置条件改播另一个 hkx 文件**。它取代并继承了 DAR，内置游戏内编辑器，可被其他 SKSE 插件扩展。

它最反文档的一点是：**没有 wiki**。最权威的内容散在 Nexus 描述页、作者 Patreon 开发日志、源码注释和几篇中文教程里。本库把这些合并成一条可检索的知识基线，回答五类问题：

1. **定位**：OAR 到底替代什么？和 FNIS / Nemesis / Pandora 是什么关系？
2. **怎么写**：目录怎么放、`config.json` 什么字段、条件有哪些、怎么调优先级。
3. **怎么调**：游戏内编辑器怎么用、动画日志怎么读、出问题怎么定位。
4. **怎么扩展**：插件 API 与 Detection / Math / IED 等扩展。
5. **怎么迁移与实战**：DAR 老 mod 怎么迁，别人的动作包怎么改成自己想要的样子。

## 目录结构

```
oar-kb/
├── manifest.json          # 元数据 + schema + 分类定义 + 来源
├── index.json / index.html# 自动生成的索引（离线浏览器）
├── README.md              # 本文件
├── CHANGELOG.md           # 版本化变更记录
├── CONTRIBUTING.md        # 协作规范（增删改查流程）
├── 00-overview/           # 概览：定位、与 DAR/FNIS 的关系、版本史
├── 01-installation/       # 安装：前置、支持版本、ini、兼容性 FAQ
├── 02-structure/          # 结构：目录、config.json、优先级、变体、预设
├── 03-conditions/         # 条件：总览、全清单、容器、DAR 对照
├── 04-functions/          # 函数：OnTrigger 函数与 OAR 事件
├── 05-editor/             # 编辑器：三模式、动画日志、排错表
├── 06-plugins/            # 插件：API 与 Detection / Math / IED
├── 07-migration/          # 迁移：手动流程与转换工具
├── 08-practices/          # 实战：心智模型、改造方法、编辑器工作流、坑
├── 09-sources/            # 来源：官方、社区、不可信来源警示
├── _raw/                  # 抓取的上游原文存档（不参与索引）
└── scripts/
    ├── fetch_sources.py  # 抓取一手来源到 _raw/
    ├── build_index.py    # 扫描全部 frontmatter → index.json + index.html
    ├── validate_kb.py    # 结构 + 索引 + 索引页模板的机械校验
    ├── check_index_ui.py # 索引页交互回归（Node + DOM 桩，不需要浏览器）
    ├── check_links.py    # 站内相对链接 lint（附带换行一致性提示）
    ├── fix_links.py      # 修复链接深度错误（按目标尾部路径反查，不靠手写 ../ ）
    └── fetch_mediawiki.py# 通用 MediaWiki 抓取器（留作后续同步）
```

## 怎么用

**人读**：双击 `index.html` → 左栏选分类 → 点卡片看全文（内联渲染）。
**机读**：`index.json` 含 `entries[]`（含 `content` 字段为渲染后的 HTML）。

## 怎么维护

1. 在对应分类目录新建/修改 `.md`，**保持 frontmatter 的 `category` 等于目录名**。
2. 跑 `python scripts/build_index.py` 重新生成索引。
3. 跑三项校验，都过才算完成：`python scripts/validate_kb.py`（结构）、`python scripts/check_index_ui.py`（索引页交互回归）、`python scripts/check_links.py`（站内相对链接）。
4. 按 [`CONTRIBUTING.md`](CONTRIBUTING.md) 的检查清单自检。

## 来源与版权

- 官方口径来自 **OAR 源码仓库**与 **Nexus 发布页**；历史与技术细节来自作者 **Ersh 的 Patreon 开发日志**；社区经验来自 Nexus 论坛、巴哈姆特与 LoversLab。
- OAR 本体为 **GPL-3.0-or-later**（含 Modding Exception / Linking Exception）；各扩展插件版权归各自作者。本库为结构化整理，仅供学习与协作维护。
- 每页正文内以 `> 来源：…` 标注出处，**关键数值（版本号 / 枚举值 / 条件名 / 路径）均按原页或源码核对，不凭记忆改写**。

## 关于本库的定位提醒

- 本库**不是教程搬运**，而是"官方口径 + 源码事实 + 社区经验 + 来源辨析"的**知识基线**。
- 涉及**版本号 / 条件名 / 枚举值**时，务必回官方页面或源码复核（见 [`09-sources/unreliable-sources.md`](09-sources/unreliable-sources.md)）。
- 本工作区另有一份**面向本机实操的改造记录**（`OAR/` 目录的教程与补充文档），本库是它的"上游口径"支撑；两者互补，不重复。
