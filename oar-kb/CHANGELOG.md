# 变更记录（CHANGELOG）

本库遵循 [语义化版本](https://semver.org/lang/zh-CN/)。条目自身的版本记录在各文件 frontmatter 的 `version` 字段。

## [1.0.0] - 2026-09-21

### 新增

- 首版发布，共 10 个分类、33 个条目。
- **00-overview**：OAR 定位、与 DAR 的关系、与 FNIS/Nemesis/Pandora 的分工、版本迭代史（含 Patreon 开发日志时间线）。
- **01-installation**：前置需求与支持版本、安装与 ini 配置、兼容性 FAQ。
- **02-structure**：目录结构与路径插入规则、`config.json` / `user.json` 与优先级、动画变体、条件预设。
- **03-conditions**：条件系统总览、条件全清单（按引入版本）、容器条件、DAR 旧条件改名/合并对照。
- **04-functions**：函数清单、OAR 自定义动画事件、OnTrigger 用法。
- **05-editor**：游戏内编辑器三模式、动画日志与 trace、排错对照表。
- **06-plugins**：SKSE 插件 API、Detection Plugin、Math Plugin、IED Conditions。
- **07-migration**：手动迁移流程、转换工具（单人 / 批量 / dar2oar）。
- **08-practices**：替换心智模型、改造别人动作包的六步法、两篇巴哈姆特编辑器工作流、坑与代价。
- **09-sources**：官方来源清单、社区来源清单、不可信来源警示。

### 说明

- 建立时对以下事实做了**源码级核对**（非二手转述）：
  - 从 `src/Conditions.h` 抽出 OAR 注册的**全部 125 个条件名**，确认官方清单完整、无遗漏；
  - 从 `src/API/OpenAnimationReplacer-ConditionTypes.h` 等确认插件 API 的形状；
  - 确认 **OAR 本体不注册 `IsPlayer` 条件**，Detection Plugin 也只注册 5 个条件 —— 因此 Detection 页面示例里的 `IsPlayer` 是**文档笔误**（详见 `06-plugins/detection-plugin.md`）。
- 抓取的上游原文存于 `_raw/`，不参与索引。
