# 协作规范

## 一、目录布局（硬约束）

```
character-appearance-kb/
├── manifest.json          # 元数据 + 条目 schema + 分类定义（页面标题/分类中文名取自这里）
├── index.json             # 自动生成：纯元数据索引（含内容）
├── index.html             # 自动生成：离线浏览器
├── README.md / CHANGELOG.md / CONTRIBUTING.md
├── 00-overview/ ... 08-sources/     # 分类目录（每主题单文件 .md）
├── _raw/                  # 抓取来的上游原文存档（构建会忽略）
└── scripts/               # 五件套 + fetch_mediawiki.py
```

两条必须遵守的规则：

1. **条目必须放进 `NN-` 前缀的分类子目录**。
   `build_index.py` 会跳过库根层，条目写在根目录会被**静默丢掉**
   （构建输出 `0 entries` 却不报错）。库根只放 manifest / index / 三个说明文档。
2. **`category` 字段必须与所在目录名严格相等**（写 `02-face`，不要写 `face`）。
   写成短名只表现为"页面分类标签变空"，**不报错**，极易长期潜伏。

## 二、条目的 frontmatter

```yaml
---
id: racemenu                     # 小写连字符，必须与文件名一致
title: RaceMenu（捏脸核心）
category: 02-face                # 必须与目录名严格相等
kind: tool                       # concept | reference | tutorial | tool（可选）
version: 1.0.0                   # 内容变更时递增
updated: 2026-09-22              # YYYY-MM-DD
tags: [捏脸, RaceMenu, 滑块]      # "属于什么主题"
aliases: [racemenu, rm, 捏脸工具] # "别人会用什么词来找"（可选但强烈建议）
source: https://...              # 主要来源 URL
summary: 一句话摘要
---
```

### `aliases` 怎么写（检索质量的杠杆）

- 一条别名 ≈「一个别人真会敲进去的**短查询**」，**不要写整句话**。
  - 反例：`怎么让滑块显示出来` → 正例：`没有滑块`、`滑块缺失`
- 优先写：英文术语 / 缩写 / 俗称 / 常见错拼 / 上级概念词。
- **别抄 `tags`**（tags 单独计分，重复等于白占名额）。
- 中文别名写**更短的核心说法**（检索端对中文长串会做反向包含，
  短的更容易命中）。
- 上限 16 项，不能重复；`validate_kb.py` 会检查。

## 三、证据纪律

**每一条结论都要能落到出处。** 四种可信层级：

| 标记 | 什么时候用 |
|---|---|
| **一手** | Nexus 发布页描述、GitHub README/源码、官方 wiki、作者本人的帖 |
| **社区经验** | 论坛帖、reddit、指南站（多帖一致时注明"多帖一致"） |
| **未确认** | 检索不到可靠来源 —— **必须显式写"未确认"，不要猜版本号/作者名/路径** |
| **本工作区实测** | 你实际访问、比对得出的结论 |

**禁止**：拿 CSDN、toolify、AI 聚合站、内容农场当事实来源。
判据（三条）：有版本号吗？有文件路径吗？有指向发版者的链接吗？

如果发现新的"错误知识"或某条未确认事项已被确认，
**更新 `08-sources/unreliable-and-unconfirmed.md`** 并递增它的 `version`，
而不是在别处悄悄写一个不同的说法。

## 四、改东西的流程

### 改条目内容

1. 先完整读一遍该条目（避免覆盖别人的新增）；
2. 改正文；frontmatter 的 `version` 递增、`updated` 改成当天；
3. 跑自检（见下）。

### 改索引页 / 加入新功能

**不要手改 `index.html`** —— 它是生成物，下次重建就丢。

正确做法：改 `scripts/build_index.py` 里的模板 → 重建 → 跑 `validate_kb.py`
与 `check_index_ui.py`。

> 改 `scripts/` 下的任何脚本后，都要在**工作区根**跑
> `scripts/sync_scripts.py`，把这些脚本同步到其他资料库。
> 只改一处会造成"技能一个行为、库另一个行为"的隐性分叉。

### 新增条目

1. 在对应分类目录新建 `<id>.md`；
2. 写 frontmatter（含 `aliases`）；
3. 正文按"结论 + 分点 + 表格 + 来源"的结构写；
4. 跑自检四连。

## 五、自检

```bash
PY="C:/Users/laptopyu/.workbuddy/binaries/python/versions/3.13.12/python.exe"
$PY scripts/build_index.py     # 重建索引（输出条目数要与你预期相符）
$PY scripts/validate_kb.py     # 结构 + 索引 + 别名 + 模板（0 错误才过）
$PY scripts/check_index_ui.py  # 索引页交互回归
$PY scripts/check_links.py     # 站内相对链接 lint
```

- **动过目录结构或批量写条目** → 必须跑 `check_links.py`（坏链不会让构建失败）。
- 相对链接的 `../` 层数由**目录深度**决定，手写极易错；
  修链用 `fix_links.py`，不要手改层数。
- 全文一律 **LF** 换行（`check_links.py` 会提示非 LF 文件）。

## 六、写作风格

- **分开写"官方说的"和"玩家经验"**，不要把两者混成一句陈述。
- 遇到机制性问题（"为什么不生效"），**优先讲清机制**，再给操作步骤 ——
  否则读者只会照抄，不会迁移。
- 写"坑"的时候把**判据**一起写上（"如果看到 X，说明是 Y"），
  这比"要注意 Z"有用得多。
- 不要写"最新版是 X.Y" 这类会过期的陈述而不标注日期与来源；
  版本敏感的内容务必带 `updated` 与来源链接。
