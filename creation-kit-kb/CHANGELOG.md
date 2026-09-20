# 变更日志（CHANGELOG）

本文件记录资料库整体演进。条目级版本见各 `.md` 的 `version` / `updated` 字段。

## [1.0.0] - 2026-09-20

### 新增
- 初始资料库骨架：manifest.json / README.md / CONTRIBUTING.md / CHANGELOG.md。
- 七大分类目录：`00-overview`、`01-installation`、`02-features`、`03-game-systems`、`04-scripting`、`05-tools`、`06-tutorials`。
- 概览板块：Creation Kit 概述、导航枢纽。
- 安装板块：获取与启动、INI 文件体系、Data 目录与插件格式。
- 编辑器功能：编辑器界面、快捷键映射、术语表、Archive.exe（BSA 打包）。
- 游戏系统：任务、对话、AI 包、Radiant Story（故事管理器）。
- Papyrus 脚本：语言概览、语言要素、编译、事件参考、函数参考，以及 4 个常用脚本对象（Actor / ObjectReference / Game / Debug，由 `gen_features.py` 生成）。
- 工具链：SKSE 插件开发、TES5Edit 清理、Blender 天际美术工具。
- 教程：Creation Kit 界面教程、界面速查表、基础任务脚本、上传 Steam 创意工坊。
- 自动化：`scripts/fetch_ck.py`（抓取）、`scripts/gen_features.py`（生成脚本对象）、`scripts/build_index.py`（构建索引与离线浏览器）。
- 生成 `index.json` 与 `index.html`（离线可搜索）。

### 来源
- 内容整理自 UESP Creation Kit Wiki：https://ck.uesp.net/wiki
- Creation Kit 当前版本：**1.9.32.0**
