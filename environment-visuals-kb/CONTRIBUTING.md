# 协作规范（CONTRIBUTING）

## 增条目

1. 放进对应 `NN-` 前缀分类目录（**别放库根**——会被索引静默丢弃）。
2. frontmatter 九必填：`id`（=文件名，小写连字符）、`title`、`category`（**与目录名严格相等**）、`version`、`updated`（YYYY-MM-DD）、`tags`、`source`（一手 URL）、`summary`。
3. `aliases` 写"别人会敲的短查询"：英文术语/俗称/错拼/上级词；**不与 tags 重复、不写大小写变体**（validate 会报 ERROR）、不写整句。
4. 交叉引用一律写 **markdown 相对链接**（同库上一层目录，如指向 `02-textures/smim.md` 的路径；跨库再上两层），不要反引号纯文本（check_links 查不出纯文本）。
5. 关键数值（版本号/Nexus ID/文件大小/VRAM）照抄一手源；区分一手源/社区经验/未核实。

## 改条目

- 先读全文再改；`version` 递增、`updated` 更新。
- 批量改写用脚本（`newline=""`、逐文件断言），改完跑 `verify_linkify.py` 证语义等价。

## 删/移条目

- 删除后重建索引；移动目录必须跑 `check_links.py`（坏链不报错、构建照样过）。
- `../` 层数别手算，用 `fix_links.py` 反查修正。

## 自检（改完必跑）

```bash
python scripts/build_index.py && python scripts/validate_kb.py && python scripts/check_index_ui.py && python scripts/check_links.py
```

新增库或改索引页模板后，另跑技能里的 `selftest_new_kb.py`；动过 stock 脚本跑工作区根 `scripts/sync_scripts.py --check`。
