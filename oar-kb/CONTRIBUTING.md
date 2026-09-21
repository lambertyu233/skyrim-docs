# 协作规范（CONTRIBUTING）

## 一、条目格式

每个 `.md` 条目**必须**以 YAML frontmatter 开头，字段如下：

```yaml
---
id: what-is-oar                   # 小写连字符，必须与文件名一致
title: OAR 是什么：它替换的到底是什么
category: 00-overview             # 必须等于所在目录名
kind: concept                     # concept | reference | tutorial | tool | guide
version: 1.0.0                    # 语义化版本，内容有实质变更时递增
updated: 2026-09-21               # YYYY-MM-DD
tags: [OAR, 入门, 定位]            # 数组
source: https://...               # 官方来源 URL
summary: 一句话摘要
---
```

### 硬性约束（构建脚本依赖）

1. `category` **必须等于目录名**（索引按目录过滤）。写成省略 `NN-` 前缀的短名会**静默**变成空标签、不报错。
2. `id` **必须等于文件名**（去 `.md`）。
3. 必填字段（`id/title/category/version/updated/tags/source/summary`）不得为空。
4. 正文首行若为 `# 标题`，详情面板会自动去掉 H1（避免与面板标题重复），无需删除。

## 二、增删改查流程

### 新增条目

1. 在对应分类目录新建 `小写连字符.md`；
2. 填 frontmatter（`category` = 目录名）；
3. 写正文，关键结论处用 `> 来源：…` 标注出处；
4. 运行构建：`python scripts/build_index.py`；
5. 运行校验（三项都过）：`python scripts/validate_kb.py`、`python scripts/check_index_ui.py`、`python scripts/check_links.py`；
6. 按"四、自检清单"核对。

### 修改条目

1. 直接改正文；若有实质内容变更，把 `version` 递增、`updated` 改为当天；
2. 重跑构建脚本。

### 删除条目

1. 删除 `.md` 文件；
2. 重跑构建脚本（索引会自动移除）。

### 新增分类

1. 建新目录（建议带序号前缀，如 `10-xxx`）；
2. 在 `manifest.json` 的 `categories[]` 增加一项：`{ "dir": "10-xxx", "title": "中文名", "desc": "..." }`；
3. 重跑构建脚本。

## 三、来源纪律（本库特有，务必遵守）

- **原理 / 版本 / 路径 / 枚举值 / 条件名**：以官方页面或**源码**为准，并在正文标注 `> 来源：URL`。
- **社区说法**：单独标注"（社区）"，不得与官方口径混写；社区案例要写清是**某个整合/某个版本下的现象**，不要当通则。
- **禁止**引用 CSDN / toolify 等内容农场、AI 聚合站的版本号与功能名。已实测这些站点会**编造**不存在的目录（`Data\OAR\`）、配置文件（`OAR.json`）、控制台命令（`oar list`）、文件格式（`.kf` / `.nif` / `.fbx`）与版本号（`OAR v5.0`）。详见 [`09-sources/unreliable-sources.md`](09-sources/unreliable-sources.md)。
- 抓来的上游原文放 `_raw/`，**不参与索引**。

## 四、自检清单（提交前）

- [ ] 每个条目 `id == 文件名`、`category == 目录名`、必填字段非空
- [ ] 已运行 `python scripts/build_index.py` 且无报错
- [ ] 已运行 `python scripts/validate_kb.py` 与 `python scripts/check_index_ui.py`，两项都过
- [ ] 已运行 `python scripts/check_links.py`，**0 条失效站内链接**（新增/移动条目后尤其必跑——`validate_kb.py` 不查正文链接）
- [ ] `index.json` 的 `by_category` 计数与目录内条目一致
- [ ] `index.html` 的 `<title>` 是本库名（非默认"资料库"）
- [ ] `index.html` 中无残留占位符（如 `__ENTRIES__`）
- [ ] 正文中的代码/配置块**围栏顶格**（列表项内用行内 `` `code` ``，不要缩进围栏）

## 五、环境备注

- 本机 Bash 的 PATH 可能损坏；文件操作优先用编辑器工具，脚本用托管 Python：
  `C:\Users\laptopyu\.workbuddy\binaries\python\versions\3.13.12\python.exe`
- 构建脚本零第三方依赖，纯标准库。
- **同一批条目必须统一 LF 换行**；批量改写 frontmatter 时按字节处理并保留原换行符。
