# CHANGELOG

## 1.0.0 — 2026-09-22

首次发布。

- 新建 `skyrim-tools-kb`，13 个分类、67 个条目。
- 来源限定为**一手来源**：官方文档站（LOOT / xEdit / Wrye Bash / DynDOLOD / Wabbajack /
  Nexus Mods Wiki / UESP / CK wiki）、官方代码仓库 README 与 Releases、
  Nexus 发布页描述正文、作者本人渠道。
  **明确排除 CSDN、toolify 类内容农场与镜像站**，并在 `12-sources/` 逐条记录判据。
- 分类与条数：
  - `00-overview` 3 · `01-frameworks` 10 · `02-distribution` 3 · `03-managers` 4
  - `04-loadorder` 7 · `05-assets` 5 · `06-lod` 4 · `07-behaviour` 2
  - `08-creation` 6 · `09-diagnostics` 12 · `10-audio` 5 · `11-config` 3
  - `12-sources` 3
- 全部条目补齐 `aliases`（检索别名，写"别人会敲的短查询"，不与 `tags` 重复）。
- 建立了与既有 6 个库的交叉索引：`01-frameworks` ↔ `oar-kb` / `behaviour-engine-kb`，
  `03-managers` ↔ `mo2-usvfs-kb`，`08-creation` ↔ `creation-kit-kb`，
  `09-diagnostics` ↔ 各库排错条目。
- 重要辨析产出：`12-sources/common-misconceptions.md` 列出 **18 条常见错误认知**
  （SKSE 启动方式、LOOT 的能力边界、zMerge 已停更、CAO 的真实能力范围、
  lip 是文本驱动而非波形驱动等），每条给出正解与出处条目路径。
- 证据分级：正文中区分**一手源 / 社区经验 / 本机实测**；
  版本号与日期均标注"可能已过期，请核对发布页"。
