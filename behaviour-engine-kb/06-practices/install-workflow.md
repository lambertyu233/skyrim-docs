---
id: install-workflow
title: 标准刷补丁流程（跨引擎通用）
category: 06-practices
kind: tutorial
version: 1.0.0
updated: 2026-09-21
tags: [流程, 刷补丁, 标准操作, MO2, Vortex]
source: https://www.nexusmods.com/skyrimspecialedition/articles/12319
summary: 把三份官方/半官方安装文档抽象成一套"任何时候都适用"的刷补丁标准流程，并标出最容易被忽略的三个坑。
---

# 标准刷补丁流程（跨引擎通用）

无论用哪个引擎，本质流程一致：

## 前置准备（一次性）

1. 装好引擎本体（Nemesis 作为 mod；Pandora 作为 mod 或装在 mods 文件夹外）。
2. 在 mod 管理器里建一个**专用输出 mod**（`Nemesis Output` / `Pandora Output`）。
3. 把引擎添加为管理器的**可执行程序**，`Start In` 指向 Skyrim 的 **Data** 目录。
4. 让输出指向那个专用输出 mod（Pandora 用 `-o "路径"` 或 Paths 菜单；Nemesis 在配置里设）。

## 每次改动动画/行为 mod 后

1. **排序**：用 LOOT 排好插件顺序，确认所有插件已勾选。
2. **确认启用**：在引擎界面勾选所有需要的补丁。
   - ⚠️ **绝不勾选你没有安装的 mod 的补丁**——会导致问题。
   - Nemesis/Pandora 都支持**拖动调整优先级**（后者优先级覆盖前者）。
3. **运行引擎**：点 Launch/Run，等它完成（Pandora 通常秒级到数十秒；Nemesis 通常 30 秒–2 分钟）。
4. **处理输出**：
   - Pandora：确认输出落在 Output mod；在管理器里确保 **Output 胜出所有文件冲突**（Vortex 场景）。
   - Nemesis：输出默认进 **overwrite**，需手动移入 `Nemesis Output` mod。
5. **部署**（Vortex）：Deploy → 重跑引擎 → 再 Deploy；若问用哪个版本文件，选 **Use Newer File**。
6. **进游戏验收**。

## 三个最容易被忽略的坑

### 坑 1：改了 mod 不重刷引擎

**只要动了会改行为文件的 mod，就必须重刷。** 否则新动画/新行为不会生效。

### 坑 2：切换引擎不重装动画 mod

FNIS 与 Nemesis 会**直接改写各 mod 目录里的 .hkx**（不只在 overwrite）。所以在 FNIS ↔ Nemesis ↔ Pandora 之间迁移时：

> 切换动画补丁器（FNIS↔Nemesis 等）前，**务必先备份所有动画 mod**；否则要重装所有动画 mod，因为它们的 .hkx 行为文件可能已被旧引擎改过。

社区经验（烽火 MOD 指南）：

- **每次运行 Nemesis 前清空 overwrite**；**卸载 Nemesis 后也清空 overwrite** 并重装整合包，否则动作不生效。

### 坑 3：忘了清理旧输出

反复重刷时残留的旧输出会造成混乱。Pandora 会自动跟踪并清理旧输出；Nemesis 则需**手动删除 Output 文件夹**再重跑（社区通行做法）。

## 验收清单

- [ ] 引擎界面里目标 mod 已勾选
- [ ] 优先级顺序正确（尤其是框架类 mod）
- [ ] 引擎日志无 FATAL，warning 可接受
- [ ] 输出 mod 已启用且**胜出文件冲突**
- [ ] 进游戏后新动画/新系统表现正常

## 相关

- [Pandora 安装指南](../04-pandora/pandora-install.md)
- [常见报错](troubleshooting-common.md)
- [如何选择引擎](choosing-engine.md)
