---
id: in-game-editor
title: 游戏内编辑器：三种模式与实用功能
category: 05-editor
kind: guide
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 编辑器, Shift+O, Author, User, 附加设置]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 默认 Shift+O 打开游戏内 UI；Inspect 只读、Author 写 config.json、User 写 user.json；支持按优先级查看替换列表、条件状态图标与当前值、拖放排序、右键复制粘贴。
---

# 游戏内编辑器：三种模式与实用功能

## 打开方式

默认按 **`Shift + O`** 打开游戏内 UI，检视并编辑所有已安装的 replacer mod。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 三种模式

| 模式 | 写到哪里 | 用途 |
| --- | --- | --- |
| **Inspect（检视）** | 不写 | **只读**，编辑功能全部禁用 |
| **Author（作者）** | **`config.json`** | 随 replacer mod 一起分发的**主配置文件**，面向 mod 作者 |
| **User（用户）** | **`user.json`** | 覆盖 `config.json` 里**除 submod 名称与描述之外的一切**；改优先级/条件/禁用动画而**不动原文件**；**可安全删除** |

官方原文（User 模式）：

> **User 模式**会生成一个 `user.json`，它会覆盖 `config.json` 里除 submod 名称与描述之外的一切。这个模式让用户能做**个性化调整**——改优先级、改条件、禁用动画——而不影响原始文件。用户配置文件可以安全删除，删掉后会改用原来的 `config.json`。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

**选择口诀**：改 mod 本身 → Author；给自己做个性化 → User；只想看 → Inspect。

## 实用功能（官方）

- **选取求值目标**：用**控制台选中某个 actor**，或在编辑器**左上角直接输入其 FormID**，即设为"当前求值目标"。
- **条件状态图标**：选中目标后，每个条件都会显示一个**图标**，实时指示其要求当前是否满足；**部分条件还会额外显示"当前被检查的值"**。
- **复制 / 粘贴**：**右键**条件即可复制/粘贴单个条件，或整个条件集。
- **拖放排序**：可以**拖放**条件来**重新排序**。
- **替换列表标签页**：额外标签页按**优先级**列出某个动画的**所有替换**，仅供检视、不可编辑（因为一个 submod 内所有替换动画共享同一套配置，这个视图看不出它们之间的关系）。
- **预览动画**：可以在编辑器里**预览**任何替换动画。
- **设置菜单**：包含实验性功能开关。
- **警告 / 错误栏**：
  - 多个 submod **优先级相同** → 显示**警告**
  - 某个 submod 的条件**需要其他插件或更高版本** → 显示**错误**
  - **点击编辑器底部的错误栏**可查看详细信息。
- **动画日志**与**动画事件日志**的开关（见 [动画日志与调试](animation-log-and-debugging.md)）。
- **注释**（3.1.0+）：右键条件/函数 → "Edit comment"，给自己的配置写备注。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## ⚠️ 社区实测补充：预览按钮要先选中目标

官方描述里提到"可以预览"，但**没说清前置条件**。论坛里有玩家花了数周才搞明白：

> 教程里和帖子里都说可以预览动画，但我怎么都调不出预览按钮…… 昨天我才发现，**要让预览按钮出现，你必须先把自己选为目标（`prid 14`）**。

> 来源：<https://forums.nexusmods.com/topic/13487504-for-animations-what-is-the-difference-between-fnisnemesis-and-oar/>

**结论**：进编辑器第一件事，先用控制台点自己（或 `prid 14`）把求值目标设成玩家。条件图标、当前值、预览按钮**全都依赖它**。

## 子模组附加设置（Additional Settings）

| 设置 | 作用 |
| --- | --- |
| **Constant polling**（`interruptible`） | 动画播放期间**持续轮询**所需条件，情况一变就**立即替换**，并在新旧动画间做正确混合 |
| **循环时保留随机结果** | 动画**循环**时保留随机条件的结果。移动类 mod 很有用——避免每走几步就换动画 |
| **共享随机结果** | 在整个 submod 内**共享**随机结果，让整套动画一起随机 |
| **自定义混合时间** | 动画被打断替换时的混合（blend）时长 |
| **忽略 No Triggers 标记** | 原版某些动画剪辑带此标记，会**忽略**带触发器的注释事件；开启后该标记被忽略，注释中的动画事件即可正常触发 |
| **必需项目名称** | 指定行为项目名（如 `DefaultMale` / `DefaultFemale`），让该 submod 只在该项目下加载——这些动画**不计入**该项目的动画数量上限 |
| **动画文件夹覆盖** | 指定存放动画的文件夹名，让多个 submod **共用同一批动画而不必重复复制** |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（Features / additional settings）与 <https://bakemono.app/p/patreon/25643772/81916525>（动画文件夹覆盖的引入动机）

### ⚠️ 关于 `interruptible` 的性能提醒（官方原话）

> 考虑给你的 submod 用上 **"Interruptible"** 设置——对任何需要特定条件的**循环动画**都很好用，因为条件变化时它会**立刻被替换**（例如 EVG Conditional Idles 的盾牌掩护 idle 会在你卸下盾牌的瞬间停止）。
> **但不要给不需要它的 submod 打开**——它带来潜在的性能开销（察觉不到，但在多个角色 × 大量替换动画上可能累积），因为这个设置会导致动画播放期间**条件被持续求值**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（miscellaneous notes）

## 编辑的保存语义（重要）

- **Author 模式**：点保存 → 写 `config.json`。
- **User 模式**：点保存 → 生成 `user.json`。
- **User 模式下每个动作的编辑状态**（社区教程观察到的 UI 约定）：
  - 左上角动作名旁出现**橙色 `*`** → 有未保存的修改；
  - 出现**黄色 `(User)`** 标记 → 这条在 User 模式被编辑过，保存后会生成干净的用户配置档；
  - 按左下角 **Save user config** 后橙色 `*` 消失 → 修改已落盘。

> 来源：<https://forum.gamer.com.tw/Co.php?bsn=2526&sn=154942>

**记住这点能少走弯路**：编辑器里改了没按保存，等于没改。

## 相关

- [动画日志与调试](animation-log-and-debugging.md)
- [排错对照表](troubleshooting.md)
- [函数系统与 OAR 自定义动画事件](../04-functions/functions-and-events.md)
- [编辑器驱动的实战工作流](../08-practices/editor-workflow-idle.md)
