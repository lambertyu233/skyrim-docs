---
id: troubleshooting-vfs
title: VFS/USVFS 常见排错
category: 06-reference
version: 1.0.0
updated: 2026-09-20
tags: [参考, 排错, 杀软, HVCI, 事件日志]
source: https://github.com/ModOrganizer2/modorganizer/wiki/Troubleshooting
summary: 注入被拦、HVCI/Core Isolation 阻止受保护 exe、Windows 事件日志服务异常、系统日志被清等排查。
kind: reference
---

# VFS/USVFS 常见排错

usvfs 靠**注入**工作，所以很多"怪问题"其实是注入没成功或被干扰。

## 1. 杀软 / 反恶意软件拦截注入

- usvfs 的 hook 技术与部分恶意软件相似，易被拦截且**常常毫无提示**。
- **把整个 MO2 安装目录**（不只是 exe）加入排除/例外项；顽固者可能需彻底卸载。
- 已知会干扰的（非穷举）：Acronis（含反勒索模块）、Avast、Bitdefender、Malwarebytes、VIPRE、Windows Defender。

## 2. HVCI / Core Isolation（硬件强制栈保护）阻止受保护 exe

- Windows 的 **Hardware-enforced Stack Protection（需 Intel CET / AMD Shadow Stack 硬件）** 可能阻止受保护的可执行文件通过 usvfs 运行。
- 用户侧解决：Windows 安全中心 → 应用和浏览器控制 → 漏洞利用保护设置 → 程序设置 → 添加该程序 → 找到 exe → 关闭"硬件强制栈保护"（Override system settings → Off）。
- 开发者侧：用 `/CETCOMPAT:NO` 编译，或 .NET 项目设 `<CETCompat>false</CETCompat>`。

## 3. Windows Event Log 服务异常

- 未知原因下，该服务对正确 hook 像 LOOT/Wrye Bash/xEdit 这类程序**至关重要**。MO2 2.1.4+ 会在运行可执行文件时警告服务异常。
- 检查"Windows Event Log"服务状态应为"正在运行"、启动类型"自动"；若拒绝启动，可能是 Windows 日志损坏（超出本 wiki 范围）。

## 4. 清空了 Windows 系统日志

- 系统日志被清（手动或 CCleaner 的"Windows Event Logs"）后，必须**重启**（用"重启"而非"关机"）MO2 才能恢复正常。CCleaner 可关闭该项避免。

## 5. 通用排查顺序

- 在 MO2 之外测试该程序是否正常。
- 新建**空白 profile**（选 DefaultGameSettings）测试。
- 确认游戏目录/Data 里没有残留 mod。
- 确认脚本扩展器（SKSE 等）版本匹配且为最新。
- 关闭杀软、完成 Windows 更新、真正"重启"电脑。

> 想确认 usvfs 到底有没有在重定向，开 [调试 usvfs](04-debugging/debugging-usvfs.md) 看日志。
