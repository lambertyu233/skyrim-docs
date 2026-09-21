---
id: function-reference
title: 函数参考（Functions）
category: 04-scripting
version: 1.0.0
updated: 2026-09-20
tags: [papyrus, functions, native, global, self, reference]
aliases: [函数参考, Papyrus 函数, 函数用法]
source: https://ck.uesp.net/wiki/Function_Reference
summary: 函数是可复用的工作单元，含定义、参数、返回值；支持 global/native 修饰，通过 Self 作用于实例。
status: stable
kind: reference
---

# 函数参考（Functions）

**Function（函数）** 是比单条表达式更大的工作单元，可带参数并返回值给调用者。完整函数列表见 [List of Papyrus Functions](https://ck.uesp.net/wiki/List_of_Papyrus_Functions)。

## 函数定义

```papyrus
<返回类型> Function <名称>(<参数列表>) ('global' | 'native')* <flags>*
    <函数体>
EndFunction
```

- 函数头后必须跟函数体与 `EndFunction` 关键字，**native 函数除外**（由游戏实现，无函数体）。
- 函数名不能与同脚本其它函数冲突；若与父脚本同名，返回类型与参数须一致（即覆盖）。
- **Global**：不作用于具体实例，无 `Self`。
- **Native**：无函数体，由引擎实现；若引用引擎未暴露的函数，编译不报错但运行报错。同一修饰符不可重复。

## 参数

```
<参数> ::= <类型> <标识符> ['=' <常量>]
```

- 逗号分隔的参数列表。
- 参数可带默认值（常量）；一旦某参数有默认值，**其后所有参数都必须有默认值**。

## Self 与面向对象

- 所有函数最终都通过 `this/Self` 指针解析——函数作用于调用它的对象实例。
- 例如 `car1.Ram(car2)` 中，`Ram` 内部可用 `Self` 指代 `car1`，从而排除 `car2 == Self` 的自我伤害。
- 比较 `newObject != Self` 可避免「悬空指针」式错误。

## 示例

```papyrus
Function Ram(ObjectReference someVehicle)
    if someVehicle == Self
        return
    else
        Self.MoveTo(someVehicle)
    endIf
EndFunction
```

## 相关条目

- [事件参考](events-reference.md)
- [Papyrus 语言要素](papyrus-language.md)
- [常用脚本对象](script-object-actor.md)

> 来源：[UESP Function Reference](https://ck.uesp.net/wiki/Function_Reference)
