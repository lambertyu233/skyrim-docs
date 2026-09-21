---
id: compiling-scripts
title: 编译脚本（Papyrus Compiler）
category: 04-scripting
version: 1.0.0
updated: 2026-09-20
tags: [papyrus, compiler, compile, psc, pex, flags]
aliases: [Papyrus 编译, 编译脚本, 脚本编译失败]
source: https://ck.uesp.net/wiki/Compiling_Papyrus_Scripts
summary: Papyrus 源码（.psc）经编译器生成字节码（.pex）；可通过 CK 或命令行 PapyrusCompiler 编译。
status: stable
kind: reference
---

# 编译脚本（Papyrus Compiler）

Papyrus 脚本需要先**编译**为字节码，游戏才能运行。

## 两种源码形态

- **`.psc`**：可读的 Papyrus 源脚本（你编写与维护的文件）。
- **`.pex`**：编译后的字节码，由游戏加载执行。

## 编译方式

### 1. 通过 Creation Kit

在 CK 的脚本编辑器中保存即触发编译，错误会显示在消息窗口。

### 2. 命令行编译器

使用随 CK 提供的 `PapyrusCompiler.exe`，典型调用：

```bat
PapyrusCompiler.exe MyScript.psc ^
  -i="Source\Scripts" ^
  -o="Source\Scripts\Compiled" ^
  -f="MyFlags.flg" ^
  -debug ^
  -optimize ^
  -quiet
```

常用参数：

| 参数 | 作用 |
| --- | --- |
| `-i` | 源码（含导入脚本）搜索目录 |
| `-o` | 输出 `.pex` 的目录 |
| `-f` | 指定 `.flg` 标志文件（定义编译开关） |
| `-debug` | 保留调试信息（便于 `Debug.Trace`） |
| `-optimize` | 输出优化后的字节码 |
| `-quiet` | 减少命令行输出 |

## 排错

- **编译错误**：语法、类型不匹配、未声明属性等，见 [Papyrus Compiler Errors](https://ck.uesp.net/wiki/Papyrus_Compiler_Errors)。
- **运行时错误**：如调用引擎未暴露的 native 函数，见 [Papyrus Runtime Errors](https://ck.uesp.net/wiki/Papyrus_Runtime_Errors)。
- 脚本不生效时，先查 [My Script Doesn't Work! FAQ](https://ck.uesp.net/wiki/FAQ:_My_Script_Doesn%27t_Work!)。

## 相关条目

- [Papyrus 语言要素](papyrus-language.md)
- [常用脚本对象（Actor / ObjectReference / Game / Debug）](script-object-actor.md)

> 来源：[UESP Compiling Papyrus Scripts](https://ck.uesp.net/wiki/Compiling_Papyrus_Scripts)
