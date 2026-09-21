# 变更记录（CHANGELOG）

本资料库遵循[语义化版本](https://semver.org/lang/zh-CN/)。每条目自身也有 `version` 字段。

## [1.0.0] - 2026-09-21

### 新增（初版）

- **概览（00-overview）**
  - 动作引擎是什么：它到底在解决什么问题
  - 三引擎脉络：FNIS → Nemesis → Pandora
  - 官方三引擎对比表（附解读）
- **原理（01-principles）**
  - Havok Behavior 是什么：FSM 与 hkx 包文件
  - hkx 其实有两种：行为文件 ≠ 动画文件（fore 一手帖）
  - 行为补丁器原理：读补丁 → 合并 → 输出
  - 动画数据库与事件名（scorrp10 解释）
  - Patcher 与 Replacer 的区别：FNIS/Nemesis/Pandora vs DAR/OAR
- **FNIS（02-fnis）**
  - FNIS 概览：第一代动作引擎（fore，7.6，已停更）
  - FNIS 的动画注册机制：AnimList 与生成器
  - FNIS 兼容性与淘汰原因
- **Nemesis（03-nemesis）**
  - Nemesis 概览：第二代动作引擎（模板化 + 开源）
  - Nemesis 复杂度分级（Basic → Master）
  - Nemesis 的局限：文档缺失、大列表崩溃、更新停滞
- **Pandora（04-pandora）**
  - Pandora 概览：第三代动作引擎
  - Pandora 架构与性能设计：为什么它"更快"
  - Pandora 补丁格式（作者向）
  - Pandora 安装指南（MO2 / Vortex）
  - Pandora 排错：Engine.log 与常见故障
- **生态（05-ecosystem）**
  - OAR / DAR 是什么，与动作引擎的关系
  - AMR 动画运动革命
  - 相关工具链
- **实战（06-practices）**
  - 如何选择引擎：决策指南
  - 标准刷补丁流程（跨引擎通用）
  - 常见报错与故障（跨引擎）
- **来源（07-sources）**
  - 官方来源清单（按阅读优先级）
  - 社区与讨论来源
  - 不可信来源警示

### 说明

- 所有原理性定义与版本号均标注官方出处；社区说法单独标注"（社区）"。
- `index.html` 首次由 `scripts/build_index.py` 生成。
