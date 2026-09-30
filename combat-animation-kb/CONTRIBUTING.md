# CONTRIBUTING

## 增删改查流程

1. **新增条目**：放对应 `NN-` 分类目录，文件名 = `id`（小写连字符）。frontmatter 必填 `id / title / category / version / updated / tags / source / summary`，`category` 必须与目录名**严格相等**（写短名页面标签会静默变空）。
2. **aliases**：写"别人会敲进去的短查询"（英文术语、俗称、上级概念词），不要写整句、不要与 tags 重复、不要写大小写变体（`DynDOLOD` + `dyndolod` 会被 validate 报 ERROR）。写完自检：删掉与 tags 同名的项后每条还剩 ≥3 个。
3. **版本敏感**：结论绑定上游版本（BFCO 3.100.x / MCO 1.6.0.6 等）。修改已有时 `version` 递增、`updated` 改当天。
4. **证据纪律**：结论分三级标注——一手源（GitHub README / Nexus 发布页正文 / 作者回帖）、社区经验（论坛帖、镜像站）、未核实。转述时不要混同。"不兼容"结论尽量引官方 description 原文并给链接。
5. **交叉引用**：一律写 markdown 相对链接（同库 `../NN-cat/x.md`，跨库 `../../other-kb/NN-cat/x.md`）。反引号纯文本引用是 `check_links.py` 的盲区。
6. **不重复已有库**：行为引擎机制去 `behaviour-engine-kb`，OAR 去去 `oar-kb`。本库只留选型结论与指针。

## 自检（改动后必跑）

```bash
python scripts/build_index.py
python scripts/validate_kb.py
python scripts/check_index_ui.py
python scripts/check_links.py
```

脚本为技能 stock 版副本，勿单库修改；要改行为去 `.workbuddy/skills/build-maintainable-kb/scripts/` 改后跑工作区 `scripts/sync_scripts.py`。
