---
id: script-object-debug
title: Debug 脚本对象
category: 04-scripting
version: 1.0.0
updated: 2026-09-20
tags: [papyrus, script-object, debug, global, native]
source: https://ck.uesp.net/wiki/Debug_Script
summary: 开发与调试用的全局脚本对象，提供日志输出、相机定位、通知与测试辅助函数。
status: stable
kind: reference
---

# Debug 脚本对象

开发与调试用的全局脚本对象，提供日志输出、相机定位、通知与测试辅助函数。

> 来源：https://ck.uesp.net/wiki/Debug_Script

## 概述

本条目汇总该 Papyrus 脚本对象最常用的原生（native）函数。所有函数均来自游戏引擎暴露，无法在脚本中重写其实现。完整列表与参数请以官方页面为准。

## 常用函数

| 函数 | 说明 |
| --- | --- |
| `Trace - Debug` | 向脚本日志输出一条调试信息（最常用）。 |
| `Notification - Debug` | 在屏幕右下角弹出一条玩家可见通知。 |
| `MessageBox - Debug` | 弹出一个带确定的消息框。 |
| `CenterOnCell - Debug` | 将编辑器 / 游戏相机定位到指定单元格。 |
| `CenterOnCellAndWait - Debug` | 定位并等待相机到达目标。 |
| `OpenUserLog - Debug` | 打开 / 创建自定义用户日志文件。 |
| `CloseUserLog - Debug` | 关闭自定义用户日志。 |
| `DumpAliasData - Debug` | 将任务别名数据输出到日志，便于排查。 |
| `SendAnimationEvent - Debug` | 向引用发送动画事件（测试用）。 |

## 使用提示

- 脚本对象即「类」，运行于具体实例（如某个 Actor 或某个箱子）。
- `Self` 指向调用函数的当前实例；全局对象（Game / Debug）无 Self。
- 编译与连接请参见同板块的「编译脚本」条目。

