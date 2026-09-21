---
id: troubleshooting-common
title: 常见报错与故障（跨引擎）
category: 06-practices
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [报错, 排错, A pose, 2006, 1210, 6001, T-pose]
source: https://magicskyrim.net/archives/23507
summary: 汇总 A-pose/T-pose、动画不生效、Nemesis 报错编号、hkx 不兼容等高频故障的成因与对策。
---

# 常见报错与故障（跨引擎）

## A-pose / T-pose（角色僵直摆大字）

**症状**：角色（含 NPC）保持 A 字或 T 字姿势，无任何动画。

**成因**：行为文件/动画注册没生效，或 OAR 没能加载动画包。

**对策**：

1. OAR 场景：**先查 OAR 日志**（`Documents\My Games\Skyrim Special Edition\SKSE\` 下），看它是否根本没读到动画；也有专门的"A Pose Bug Fix"补丁可解决。
2. 引擎场景：确认引擎跑完且输出 mod 启用、胜出冲突。
3. 检查 hkx 版本兼容（见下）。

> 案例来源：Nexus 论坛 https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/

## "not Skyrim SE compatible"（hkx 版本不兼容）

**症状**：FNIS/Nemesis 日志警告 `\character\behaviors\XXX.hkx not Skyrim SE compatible`。

**成因**：装了 **LE（Oldrim）** 版的动画/hkx。SE 的 hkx 二进制格式与 LE 略有不同，LE 文件直接丢进 SE 不工作。

**对策**：

1. 换 SE 版本（多数流行 mod 已有 SE 版——**首选**）；
2. 或自行转换（如 SSE NIF Optimizer / HKX to SE 转换工具），转换器要在**该 mod 所在文件夹**内运行才能生效；
3. 实在不行就弃用该 mod。

> 案例来源：LoversLab / Nexus 论坛多条 FNIS 警告帖

## Nemesis 报错编号（中文社区整理）

| 编号 | 对策 |
| --- | --- |
| **2006** | 去 Nexus 下载 **Creature Behaviour – WereWolf Addon** 装上后重刷 |
| **1210** | 在 mod 安装目录（管理器的 mods 文件夹）搜索所有 `werewolfbeast` 文件夹并删除；搜不到就装上面的 WereWolf Addon |
| **6001** / 攻击与移动莫名弯腰 | 使用社区修复版 Nemesis（0.84）——"6001 + 攻击弯腰修复版" |

另有：遇到 FNIS 报 `FNIS_XPMSE_List.txt` 相关问题时，删除 `XPMSE\FNIS_XPMSE_List.txt` 即可跑完（社区经验）。

> 来源：烽火 MOD 使用指南 https://magicskyrim.net/archives/23507 、巴哈姆特讨论串

## 动画不生效 / 0 animations added

- **引擎提示 0 animations added 或无输出**：以**管理员身份**运行，或把引擎移出受保护目录（如 `C:\Program Files`）。
- **改了 mod 没重刷**：重刷引擎。
- **overwrite 未清理**：清空 overwrite / 删除旧 Output 再重跑。
- **Pandora 输出只有 txt**：检查是否装了 **.NET 7 Desktop Runtime**，并查看 `Engine.log`。

## 移动施法等动作丢失（Pandora 特例）

- 方案 1（推荐）：用 **Pandora 4.1.2**，无需额外前置；
- 方案 2：最新版 Pandora + **Auto Skeleton Patch** 前置（不一定有效）。

## 读档 CTD（行为文件缺失）

**成因**：卸载了使用 FNIS/引擎的 mod 却**没重跑生成器**，行为文件缺失。

**对策**：恢复 mod 或重跑引擎；卸生物包要先执行对应卸载流程。

## 通用排查顺序

1. 读引擎日志（Pandora：`Engine.log`；FNIS：生成器输出；OAR：SKSE 目录下的 OAR 日志）；
2. 禁用可疑/报错 mod 再跑一次；
3. 检查文件名（事件名）、优先级、输出与冲突；
4. 检查 hkx 版本与引擎互斥（FNIS ↔ Nemesis/Pandora 不能共存）；
5. 极端情况考虑重装动画 mod（旧引擎污染的 hkx）。

## 相关

- [Pandora 排错](../04-pandora/pandora-troubleshooting.md)
- [标准刷补丁流程](install-workflow.md)
- [hkx 其实有两种](../01-principles/hkx-two-kinds.md)
