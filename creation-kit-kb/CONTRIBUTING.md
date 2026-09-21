# 协作规范（CONTRIBUTING）

本资料库以「单文件条目 + 元数据驱动 + 自动化索引」为核心，目标是让多人长期协作时**低冲突、易审查、可追溯**。

---

## 1. 新增条目（Create）

1. 在合适的分类目录下新建 `<id>.md`，文件名使用小写连字符（如 `script-object-actor.md`）。
2. 顶部填写完整 frontmatter（字段见 `manifest.json` 的 `schema`）：
   - `id` 与文件名一致；`category` **严格等于**所在目录名（如 `04-scripting`）。
   - `version` 从 `1.0.0` 起；`updated` 写当天日期 `YYYY-MM-DD`。
   - `source` 必须指向官方页面 URL。
3. 正文用中文撰写，保留英文术语（Papyrus、ObjectReference 等）。
4. 运行 `python scripts/build_index.py` 重新生成索引。
5. 在 `CHANGELOG.md` 记录本次新增。

> 同类条目（如 Papyrus 脚本对象）优先用 `scripts/gen_features.py` 数据驱动生成，保证格式一致。

### 条目格式示例

```markdown
---
id: unique-id            # 小写连字符，唯一，用于索引与链接
title: 中文标题
category: 04-scripting   # 必须与所在目录名**严格相同**（写 scripting 会导致页面分类标签变空）
status: stable           # 【保留字段】stable / review / draft；页面已不呈现徽章
kind: reference          # 【保留字段】concept / reference / tutorial / tool；页面已不呈现徽章
version: 1.0.0           # 语义化；内容变更时递增
updated: 2026-09-21      # YYYY-MM-DD
tags: [papyrus, reference]
source: https://ck.uesp.net/wiki/Papyrus
summary: 一句话摘要
---

# 标题
正文……
```

字段定义见 `manifest.json → schema`。

---

## 2. 修改条目（Update）

1. 直接编辑对应 `.md` 文件。
2. **必须**同步更新 frontmatter：
   - `updated` → 当天日期；
   - `version` → 按语义版本递增（修复小错 `1.0.0`→`1.0.1`，内容增改 `1.0.1`→`1.1.0`，结构性重写 `1.1.0`→`2.0.0`）。
3. 若引用数值/路径有变更，核对官方 `source` 后再改。
4. 重新生成索引并登记 CHANGELOG。

---

## 3. 删除条目（Delete）

1. 删除对应 `.md` 文件。
2. 重新生成索引（该条目会自动从 `index.json` / `index.html` 移除）。
3. 在 CHANGELOG 注明「移除：<id> 及原因」。

---

## 4. 评审约定（Review）

- `status` 字段：`draft`（草稿）/ `review`（待审）/ `stable`（已发布）。
  **仅作为数据保留**（会写入 `index.json`），索引页**不再呈现状态徽章**。
- 新条目默认 `draft`，经复核后改为 `stable`。
- PR / 合并前必须重建索引并跑通两项校验：

  ```bash
  python scripts/build_index.py
  python scripts/validate_kb.py     # 结构校验，退出码 0 通过
  python scripts/check_index_ui.py  # 索引页交互回归，20 项断言
  ```

---

## 5. 版本化

- 每个条目自带 `version` + `updated`，可追溯单条演进。
- `CHANGELOG.md` 记录资料库整体的重要变更（新增板块、批量生成、结构变动等）。
- 资料库整体版本号维护在 `manifest.json` 与 `CHANGELOG.md`。

---

## 6. 与上游同步

上游 UESP Wiki 可能更新。同步流程：

```bash
# 抓取单页或整类原始 wikitext 到 _raw/
python scripts/fetch_ck.py --quiet <PageTitle>
python scripts/fetch_ck.py --cat <CategoryName>

# 比对 _raw/ 与现有条目，按需修订，再重建索引
python scripts/build_index.py
```

> 注意：`_raw/` 仅作抓取缓存，不计入索引（构建脚本自动忽略 `scripts/` 与 `_raw/`）。
