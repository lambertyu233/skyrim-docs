---
id: events-reference
title: 事件参考（Events）
category: 04-scripting
version: 1.0.0
updated: 2026-09-20
tags: [papyrus, events, onactivate, onhit, ondeath, reference]
source: https://ck.uesp.net/wiki/Events_Reference
summary: 事件是游戏运行时触发、脚本可响应的信号；常见如 OnInit、OnLoad、OnActivate、OnHit、OnDeath。
status: stable
kind: reference
---

# 事件参考（Events）

**Event（事件）** 是游戏运行时在特定时机**自动触发**的信号，脚本可定义对应的事件处理函数来响应。事件属于「游戏调用你的代码」，而函数属于「你的代码调用游戏」。

## 机制要点

- 事件处理函数以 `Event <Name>(<params>)` 开头，以 `EndEvent` 结束。
- 事件由引擎在特定对象上触发；若你关心某对象的事件，需在该对象的脚本里实现。
- 事件可带参数（如 `OnHit` 会传入攻击者、武器、伤害等）。

## 常用事件（节选）

| 事件 | 触发时机 | 典型用途 |
| --- | --- | --- |
| `OnInit` | 脚本/对象初始化完成时 | 初始化变量、注册状态 |
| `OnLoad` | 对象被加载进游戏世界时 | 一次性设置 |
| `OnActivate` | 对象被激活（玩家/AI 互动） | 开门、触发机关、给物品 |
| `OnHit` | 受到攻击时 | 反伤、特效、剧情触发 |
| `OnDeath` | Actor 死亡时 | 任务推进、掉落 |
| `OnEquipped` | 物品被装备时 | 套装效果、buff |
| `OnContainerChanged` | 物品进出容器时 | 任务物品追踪 |
| `OnCellAttach` / `OnCellDetach` | 单元格载入/卸载时 | 资源管理 |

> 上表为高频事件示例；完整事件集与签名以官方 [Events Reference](https://ck.uesp.net/wiki/Events_Reference) 为准。

## 示例

```papyrus
Event OnActivate(ObjectReference akActionRef)
    Debug.Notification("你激活了 " + Self.GetDisplayName())
EndEvent
```

## 相关条目

- [函数参考](function-reference.md)
- [Papyrus 语言要素](papyrus-language.md)
- [Debug 脚本对象](script-object-debug.md)

> 来源：[UESP Events Reference](https://ck.uesp.net/wiki/Events_Reference)
