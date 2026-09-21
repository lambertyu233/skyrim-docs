---
id: faq
title: 常见问题（FAQ）
category: 06-reference
version: 1.0.0
updated: 2026-09-20
tags: [参考, FAQ, 排错]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 关于 VFS/USVFS 的高频疑问：mod 不显示、profile 崩溃、与符号链接区别等。
kind: reference
---

# 常见问题（FAQ）

## mod 在游戏里不显示 / LOOT、xEdit、Wrye Bash 看不到？

- 确认你是**通过 MO2 启动**游戏或工具（直接双击 exe 看不到虚拟视图）。
- 确认 mod 已勾选启用、且顺序正确（见 [冲突解决](../05-usage/conflict-resolution.md)）。
- 检查是否被安全软件拦截（见 [VFS 排错](troubleshooting-vfs.md)）。

## 为什么游戏目录里找不到我的 mod 文件？

- 正常。mod 物理上在 `mods\`，通过 VFS 只在被注入的进程内"可见"（见 [进程级可见](../01-mechanism/process-local-links.md)）。资源管理器看到的是真实目录。

## 这和 NTFS 符号链接有什么不同？

- 见 [USVFS vs NTFS 符号链接](../02-features/vs-ntfs-symlink.md)：进程级/会话级/免权限/跨文件系统/可叠加可隐藏。

## 切换 profile 时 MO2 崩溃？

- 见排错：禁用杀软、检查 Windows Event Log 服务、重启（而非关机）。

## 会不会有性能影响？

- 会有少量内存/CPU 开销（见 [USVFS 的代价与风险](../02-features/usvfs-drawbacks.md)），通常可忽略。

## 关闭 MO2 后 mod 还在吗？

- 虚拟链接随会话消失；mod 文件本身仍在 `mods\`，下次启动照常生效。
