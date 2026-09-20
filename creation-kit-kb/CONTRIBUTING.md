# 协作规范（CONTRIBUTING）

本资料库以「单文件条目 + 元数据驱动 + 自动化索引」为核心，目标是让多人长期协作时**低冲突、易审查、可追溯**。

---

## 1. 新增条目（Create）

1. 在合适的分类目录下新建 `<id>.md`，文件名使用小写连字符（如 `script-object-actor.md`）。
2. 顶部填写完整 frontmatter（字段见 `manifest.json` 的 `entry_schema`）：
   - `id` 与文件名一致；`category` 等于所在目录名（如 `04-scripting`）。
   - `version` 从 `1.0.0` 起；`updated` 写当天日期 `YYYY-MM-DD`。
   - `source` 必须指向官方页面 URL。
3. 正文用中文撰写，保留英文术语（Papyrus、ObjectReference 等）。
4. 运行 `python scripts/build_index.py` 重新生成索引。
5. 在 `CHANGELOG.md` 记录本次新增。

> 同类条目（如 Papyrus 脚本对象）优先用 `scripts/gen_features.py` 数据驱动生成，保证格式一致。

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
- 新条目默认 `draft`，经复核后改为 `stable`。
- PR/合并前请确保 `python scripts/build_index.py` 无报错、无残留占位符。

---

## 5. 版本化

- 每个条目自带 `version` + `updated`，可追溯单条演进。
- `CHANGELOG.md` 记录资料库整体的重要变更（新增板块、批量生成、结构变动等）。

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
