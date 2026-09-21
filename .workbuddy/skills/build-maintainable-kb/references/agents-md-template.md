---
id: agents-template
title: AGENTS.md 模板（工作区入口契约）
category: _template
kind: template
version: 1.0.0
updated: 2026-09-21
tags: [模板, 入口, agent, AGENTS.md, 契约]
aliases: [agents md template, 入口契约模板, agent 入口模板]
source: 本工作区实践（2026-09-21 建立 six-kb 工作区时总结）
summary: 供技能在新工作区生成 AGENTS.md 的模板：把"库在哪、怎么检索、什么不该读、结论要多可靠、怎么写回"写成一份 agent 每次都会读到的契约。
---

# AGENTS.md 模板

## 为什么必须有这个文件

**没被索引到的知识等于不存在。** 资料库建得再规整，如果 agent 每次开工时
不知道它存在、不知道它怎么检索，这些条目就只是磁盘上的一堆文本。

实测症状：某工作区已有 5 个资料库 / 197 条目，但根目录既无 `AGENTS.md`
也无检索脚本，agent 只能靠散文式记忆猜测库的存在，且面对"想先了解全貌"的
冲动去读 `index.json`（单个 296KB，内联了全部正文 HTML）——一次吃掉整个上下文预算。

## 模板（复制后按实际库名替换）

````markdown
# AGENTS.md — <工作区名>

本工作区是一个**结构化知识库**（不是代码仓库）：N 个资料库 + 入口索引，
共 X 条目，全部为「每主题一个 Markdown + 统一 frontmatter」。
本文件是 agent 的入口契约：**先看这里，再决定读什么。**

## 零、先试这条路（最省事）
（如果有跨库索引，把它的路径放在最前面。症状导向的入口优先于主题导向的。）

## 一、检索协议
```bash
KB="<托管 python 绝对路径> scripts/kb.py"
$KB list / toc <kb> / find <kw> / grep <正则> / show <id> / read <id>
```
**别做的事**：
- ❌ 不要读 `index.json` / `index.html`（内联正文 HTML，单个可达数百 KB）
- ❌ 不要为了"了解全貌"通读整个库
- ✅ 找具体事实用 `grep`，找该读哪篇用 `find`

## 二、路由表（问题 → 库）
| 你在处理什么 | 去哪个库 | 常见入口 |
（每库一行。跨库问题要显式提醒"两个库都要查"。）

## 三、证据纪律
1. 引用落到条目路径（如 `kb/03-x/y.md`），没写清出处 = 结论不可用
2. 区分可信层级：一手源 / 社区经验 / 本机实测，转述时不要混同
3. 先查"不可信来源"条目，踩过的坑不要踩第二遍
4. 版本敏感：结论绑定上游版本，条目 `updated` 久远时明说"可能已过期"

## 四、写回
| 学到的东西 | 写到 |
（条目正文 / 索引页 / aliases / 日志 / MEMORY.md / 用户级 MEMORY.md）

## 五、维护自检
```bash
$KB check                              # 入口文件是否覆盖全部库
python scripts/sync_scripts.py --check # 各库脚本是否还有分叉
python <kb>/scripts/validate_kb.py     # 条目结构 + 别名规范
python <kb>/scripts/check_links.py     # 站内相对链接
```
````

## 三条设计铁律

1. **可发现性优先于检索质量**。路由信息必须躺在 agent 每次都会加载的位置
   （工作区根 `AGENTS.md`），而不是藏在某个库的 README 里。
2. **返回指针，不返回正文**。让 agent 自己决定读不读、读哪一段。
3. **不新增手工同步面**。路由集中在 `AGENTS.md` 一处，每库详情由 frontmatter
   现算（`kb.py toc`）。一旦给每个库都手写一份路由卡，你就会得到 N 个迟早过期的文件。

## 目录布局约束（踩过坑，必须写进契约）

- **条目必须放在带 `NN-` 前缀的分类子目录里**。`build_index.py` 的
  `if rel == "."` 会跳过库根层，条目写在库根会被**静默丢掉**——
  构建输出 `0 entries` 却不报错。
- 库根只放 `manifest.json` / `index.json` / `index.html` / `README.md` / `AGENTS.md`。
- 分类目录名**必须带 `NN-` 前缀**；`category` 字段与目录名**严格相等**。
  写成短名（`features` 而非 `02-features`）只会表现为"页面标签变空"，
  不报错、极易长期潜伏 —— 宽容校验比没有校验更危险。
