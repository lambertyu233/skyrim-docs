---
id: debugging-usvfs
title: 调试 usvfs：hook 命名与日志
category: 04-debugging
version: 1.0.0
updated: 2026-09-20
tags: [调试, hook, 日志, 重定向]
source: https://github.com/ModOrganizer2/modorganizer/wiki/Debugging-usvfs
summary: 开启 MO2 调试日志后即可看到 usvfs 的 hook 调用、原始路径与重定向后路径；附 spawn_delay 与 Process Monitor 用法。
kind: tutorial
---

# 调试 usvfs：hook 命名与日志

打开 MO2 的**调试日志（debug logs）**，usvfs 也会输出对应日志——这是看"重定向到底发生了什么"最直观的途径。

## 日志格式

大多形如：

```
timestamp <pid:tid> [L] message [param] [param]...
```

示例（来自官方 wiki）：

```
07:52:53.161 <19328:40984> [D] hook_GetFileAttributesW [lpFileName=\??\C:\skyrim\data\] [reroute.fileName()=C:\mo\overwrite] [res=10] [originalError=0] [fixedError=0]
```

## 字段含义

| 片段 | 含义 |
|------|------|
| `07:52:53.161` | 消息的本地时间 |
| `<19328:40984>` | 进程 ID 19328、线程 ID 40984（多个进程在 usvfs 下运行时，pid 很有用） |
| `hook_GetFileAttributesW` | **所有 usvfs hook 都以 `hook_` 开头，并包含原函数名** |
| `lpFileName=\??\C:\skyrim\data\` | 进程**原始请求**的路径 |
| `reroute.fileName()=C:\mo\overwrite` | usvfs **重定向后**实际使用的真实路径 |
| `res=10` | 底层 `GetFileAttributesW()` 的返回值（此处为属性位） |
| `originalError=0` | 调用后 `GetLastError()` 的结果 |
| `fixedError=0` | 同上，但部分错误被重映射（如 `ERROR_PATH_NOT_FOUND` → `ERROR_FILE_NOT_FOUND`） |

## 读懂"重定向"

- `lpFileName` → `reroute.fileName()` 这一对，就是"进程以为打开 A，实际打开 B"的铁证。
- 注意：部分调用**若最终未被重定向则不会打印**（例如 `DeleteFile()` 在未重定向时不打日志），以避免刷屏、但也因此可能掩盖某些问题。

## 辅助调试手段

- **spawn_delay（启动延迟）**：在 MO2 的 INI 中加
  ```ini
  [Settings]
  spawn_delay = X   # 单位：秒
  ```
  让 MO2 启动进程后先挂起若干秒，方便你 attach 调试器或重置 Process Monitor。
- **Process Monitor**（Sysinternals）：按目标进程加筛选、开启"Show File System Activity"，可看到每一次文件系统调用，作为日志的补充。
- **Visual Studio**：打开 usvfs 解决方案后可 attach 到 MO2 直接或间接启动的任意进程；配合 `spawn_delay` 更易下断点。调试会派生子进程时可用 Child Process Debugging Power Tool。

> 看到 hook 行为却仍不对？大概率是注入被安全软件挡了，见 [VFS/USVFS 常见排错](../06-reference/troubleshooting-vfs.md)。
