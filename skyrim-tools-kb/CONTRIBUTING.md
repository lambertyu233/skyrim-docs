# CONTRIBUTING

## 硬约束（违反了不报错，但会静默失效）

1. **条目必须放在带 `NN-` 前缀的分类子目录里**。
   写在库根会被 `build_index.py` **静默跳过**（输出 `0 entries` 而不报错）。
2. **`category` 必须与所在目录名严格相等**（如 `04-loadorder`）。
   写成短名（`loadorder`）只表现为"页面分类标签变空"，同样不报错。
3. 新建分类目录后，**必须在 `manifest.json` 的 `categories[]` 里声明**
   （`dir` + `title` + `desc`），否则页面标签渲染为空。

## 条目模板

```markdown
---
id: kebab-case-id          # 必须与文件名（不含 .md）一致
title: 中文标题
category: 04-loadorder     # 与目录名严格相等
kind: tool                 # concept | reference | tutorial | tool（可选）
version: 1.0.0             # 内容变更时递增
updated: 2026-09-22        # YYYY-MM-DD
tags: [标签, 数组]          # 与 aliases 不重复
aliases: [英文术语, 俗称]    # 见下
source: https://...        # 主要来源（一手源优先）
summary: 一句话摘要，说清「它是什么 + 解决什么问题」
---

# 标题（与 frontmatter 的 title 呼应）

正文……
```

## `aliases` 怎么写

`tags` 说"这篇属于什么主题"，`aliases` 说"**别人会用什么词来找它**"。

- 一条别名 ≈「一个别人真会敲进去的**短查询**」，**不要写整句**。
  - ✗ `怎么让崩溃日志更好读` → ✓ `崩溃日志`、`读日志`、`crash log`
- 优先写：**英文术语 / 缩写 / 俗称 / 常见错拼 / 上级概念词**。
- **别抄 `tags`**（`validate_kb.py` 会以 NOTE 提示）。
- 写完自检："删掉与 tags 同名的项，是否还剩 ≥3 个"。
- 搜索端两条归一化（决定怎么写）：
  1. **空格不敏感** —— 同一个说法不必为空格写两条；
  2. **中文长串会做反向包含** —— 中文别名写**更短的核心说法**比写长句有效。
- 形式上必须是 `[]` 数组、无重复、≤16 项（`validate_kb.py` 会报错）。

## 证据纪律

1. **结论要落到条目路径**，格式如 `04-loadorder/xedit.md`。没写出处 = 结论不可用。
2. **区分核实层级**，转述时不要混同：
   - **一手源**（官方文档 / 官方仓库 README / Releases / 发布页描述正文 / 作者渠道）→ 可采信；
   - **社区经验**（论坛帖、社区 wiki、他人整理）→ 必须标注"社区经验"；
   - **本机实测** → 标"本机实测"。
3. **不要引用** CSDN、toolify 类内容农场、镜像/重托管站、
   以及"看起来像 GitHub 但不是"的域名。判据见 `12-sources/unreliable-sources.md`。
4. **版本敏感**：涉及版本号、路径、命令行开关的陈述必须可回溯到一手源；
   回不去的就写成"未确认"或干脆不写。条目里给出的版本号请注明
   "可能已过期，请核对发布页"。
5. 作者署名拿不准时**宁可留空并注明"以发布页为准"**，不要猜。

## 提交前自检

```bash
python scripts/build_index.py     # 看输出的条目数是否与预期一致
python scripts/validate_kb.py     # 必须 0 错误
python scripts/check_index_ui.py  # 索引页交互
python scripts/check_links.py     # 动过目录结构才需要
```

## 不要做的事

- **不要手改 `index.html` / `index.json`**（产物，下次重建即丢）。
- **不要在本库内单独改 `scripts/` 下的五件套**：
  它们是技能 `build-maintainable-kb` 的副本，
  改完技能要跑 `scripts/sync_scripts.py` 推送到全部库。
- **不要用文本模式写文件**：Windows 会把 `\n` 静默转成 `\r\n`。
  批量脚本请用 `open(p, "w", encoding="utf-8", newline="")`。
- **不要在同一条消息里对同一个文件发多个 Edit**（会静默丢写入）。
