---
id: mo2-tool
title: Mod Organizer 2（工具视角）
category: 03-managers
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [管理器, MO2, 虚拟文件系统, 安装]
aliases: [Mod Organizer, Mod Organizer 2, mod管理器, 管理器选哪个, overwrite 目录]
source: https://github.com/ModOrganizer2/modorganizer
summary: 用 USVFS 把 mod 文件虚拟化进游戏进程的模组管理器：游戏目录保持干净、profile 可切换；深层机制与完整设置见 mo2-usvfs-kb。
---

# Mod Organizer 2（工具视角）

> 本条目只讲"它是哪一类工具、与别家的区别、日常操作要点"。
> **机制、源码架构、逐项设置说明在 `mo2-usvfs-kb`**（43 条），本文不重复。

## 它属于哪一类

**虚拟文件系统型**管理器：mod 文件存放在各自的独立目录里，
启动游戏时由 USVFS（用户态文件系统钩子）在**游戏进程内部**拼出一个虚拟 `Data\`。
因此**游戏目录始终是干净的**——这是与 Vortex 最本质的分野。

## 与 Vortex 的取舍

| 维度 | MO2 | Vortex |
|---|---|---|
| 落地方式 | 进程内虚拟化（USVFS） | 部署链接（硬链接/复制）到游戏目录 |
| 游戏目录 | 干净 | 含部署产物（可 Purge 清除） |
| 工具可见性 | **必须从 MO2 启动工具**（否则工具看不到 modlist） | 工具直接看游戏目录即可 |
| 覆盖排查 | 左侧顺序 + 冲突面板 | 规则（Rules）+ 加载顺序 |

> 上表最后一行是新手最常踩的一脚：**MO2 里跑 xEdit / DynDOLOD / Synthesis 必须登记为可执行程序并从 MO2 启动**，
> 直接双击 exe 会得到一个"什么都看不见"的空环境。参见 [Vortex（Nexus 官方管理器）](../03-managers/vortex.md)。

## 日常四个动作

1. **左侧排序** = 安装顺序（文件覆盖）：越靠下越优先。
2. **右侧排序** = 插件顺序（记录覆盖）：由 LOOT 决定。
3. **启用/禁用** 与 **部署** 是两回事——MO2 靠虚拟化，不存在"部署"这一步，
   但**必须从 MO2 启动游戏**。
4. **Overwrite 目录**：没有归属的产物（生成的 ini、日志、工具输出）都落这里。
   长期不清会掩盖问题；**每次跑完生成类工具就把它归位到对应的输出 mod**。

## 相关

- [使用与运维](../../mo2-usvfs-kb/05-usage/)：安装、冲突、profile、ini、工具配方（26 条）
- [源码级架构](../../mo2-usvfs-kb/03-architecture/)：USVFS 源码级机制
- [Vortex（Nexus 官方管理器）](../03-managers/vortex.md)、[Wrye Bash（管理器 + Bash Patch）](../03-managers/wrye-bash.md)、[Wabbajack（整合包一键安装）](../03-managers/wabbajack.md)
- [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)：从 MO2 启动的必要性
