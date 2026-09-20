# Changelog

本文件记录资料库的版本化演进。版本号采用 `主.次.补` 形式：
- **主版本**：结构/分类/ schema 重大调整；
- **次版本**：新增分类或一批条目、重要内容扩充；
- **补版本**：条目修订、修正、小补充。

---

## [1.0.0] - 2026-09-20

### 初始版本

- 建立分层目录结构：`00-overview` / `01-installation` / `02-features` / `03-reference` / `04-development` / `05-tools`。
- 整理并收录官方核心内容：
  - 概览：什么是 CS、架构与缓存系统。
  - 安装：系统需求、安装指南、Vanilla 设置指南、ENB 迁移指南。
  - 功能：28 个核心特性 + 19 个附加特性（每特性独立条目，带元数据）。
  - 参考：不兼容 MOD 清单、完整 FAQ（安装/兼容/配置/开发/错误/性能/排查）。
  - 开发：True PBR 美术师与开发者指南、贡献指南。
  - 工具：Light Placer、PGPatcher。
- 建立元数据与版本化机制：
  - `manifest.json`：资料库元数据 + 条目 schema + 分类定义。
  - `index.json` / `index.html`：由 `scripts/build_index.py` 自动生成的索引与离线浏览器。
  - `scripts/gen_features.py`：功能条目生成器（数据驱动，便于增删改）。
  - 本 CHANGELOG 与 `CONTRIBUTING.md` 协作规范。

### 已知基线

- 内容基线对应官方文档 CS **1.8.4** 已知问题说明；部分附加特性标注为 TBA（开发中）。

---

## 待办 / 后续可补充

- [ ] 补全各功能的独立深度页面（目前多为摘要级，SSGI / Skylighting / Upscaling / Effects 11 已有交叉引用）。
- [ ] 收录官方各功能子页的完整参数与截图。
- [ ] 增加「推荐 MOD 列表 / 负载顺序示例」实战章节。
- [ ] 接入 CI：提交时自动运行 `build_index.py` 校验索引一致性。
