---
id: papyrus-logging
title: Papyrus 日志与脚本排错
category: 09-diagnostics
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [诊断, Papyrus, 日志, 排错, 调试]
aliases: [papyrus log, 脚本日志, Papyrus.0.log, 脚本报错, 开日志, 调试脚本]
source: https://ck.uesp.net/wiki/Papyrus_Log
summary: 怎么打开脚本日志、日志里哪些行才值得看、以及「日志很大 ≠ 有问题」这条最容易被误读的常识。
---

# Papyrus 日志与脚本排错

## 打开日志（改 INI）

在 `文档\My Games\Skyrim Special Edition\Skyrim.ini` 的 `[Papyrus]` 段：

```ini
[Papyrus]
bEnableLogging=1
bEnableTrace=1
bLoadDebugInformation=1
```

日志落在 `文档\My Games\Skyrim Special Edition\Logs\Script\`（文件名形如 `Papyrus.0.log`）。

> **排查完请立刻关掉**：日志对性能有实际影响，且会持续增长。
> `bEnableTrace` 尤其啰嗦——只在需要细节时开。

## 怎么读（比"有没有错误"更重要）

日志里绝大多数行是**良性噪音**：

| 行类型 | 要不要管 |
|---|---|
| `error: ... cannot be ... because ... is not ...`（偶发一次） | 通常不用 |
| 同一脚本**反复**报同一错误 | 要看 |
| 引用了**已卸载 mod** 的脚本名 | 要看（存档残留 → [FallrimTools / ReSaver（存档清理）](../09-diagnostics/fallrimtools-resaver.md)） |
| **栈耗尽 / stack dump** | 要看（脚本风暴） |
| 大量 `VM is freezing / thawing` | 正常，是 VM 在重整 |

**判据是"重复与聚集"，不是"存在"**。一个正常的 400 mod 存档每天都会写进几条 error。

## 提高信噪比

- **Logger Tweaks**：`Papyrus Tweaks NG`（v4.0+）提供了专门的日志侧调整项
  （可开 doc strings、debug information、栈 dump 摘要等）
  → [Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md)
- 用支持**过滤/高亮**的编辑器打开，而不是全文搜索
  → [编辑器插件（写脚本/配置的外围工具）](../08-creation/editor-plugins.md)
- 排错时可以配合 [More Informative Console](../09-diagnostics/more-informative-console.md) 在游戏内确认对象来源。

## 常见结论与对应动作

| 观察 | 动作 |
|---|---|
| 反复报某 mod 的脚本错误 | 检查该 mod 与前置的版本匹配；必要时卸掉并清存档残留 |
| 卸载 mod 后仍报它的脚本 | 存档残留 → ReSaver 清未附着实例 |
| 脚本风暴（连续 stack dump） | 先 Papyrus Tweaks NG 调优；根因通常是某个脚本在自旋 |
| 延迟尖峰但无明显错误 | 属调度问题，不是 bug → Papyrus Tweaks NG |

## 相关

- [Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md)
- [FallrimTools / ReSaver（存档清理）](../09-diagnostics/fallrimtools-resaver.md)
- [Crash Log Analyzer（崩溃日志解读）](../09-diagnostics/crash-log-analyzer.md)（崩溃侧）
- [Debug 脚本对象](../../creation-kit-kb/04-scripting/script-object-debug.md)（`Debug` 脚本对象）
