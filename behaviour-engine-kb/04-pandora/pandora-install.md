---
id: pandora-install
title: Pandora 安装指南（MO2 / Vortex）
category: 04-pandora
kind: tutorial
version: 1.0.0
updated: 2026-09-21
tags: [Pandora, 安装, MO2, Vortex, 输出文件夹, 教程]
source: https://www.nexusmods.com/skyrimspecialedition/articles/12319
summary: 按官方 README 与 Nexus「Extremely Detailed Pandora Install Guide」整理的 MO2/Vortex 双平台安装步骤，含输出文件夹与 -o 参数要点。
---

# Pandora 安装指南（MO2 / Vortex）

## 前置

- **.NET 7 Desktop Runtime**（或更新的 Desktop Runtime）。README 的 Quickstart 明确要求："Install .NET 7 Desktop Runtime if you do not have it installed."
- 一个**专用输出 mod**（强烈建议，见下）。

> ⚠️ 像任何 mod 一样，**不建议把 Pandora 直接装进 Data 文件夹**——mod 可能检测不到，且它产生的输出会让 Data 目录不干净。

## 通用要点：为什么要有"输出 mod"

Pandora 生成的行为文件**必须集中放在一个位置**，且这个位置**要作为 mod 保持启用**。官方推荐在 mod 管理器里建一个空 mod 作为输出（如 `Pandora Output`），并用启动参数指定它。

## MO2 步骤

1. 把 Pandora 作为 **mod 安装**（或装在 mods 文件夹外）。然后把它**添加为 MO2 的应用程序**。
2. 用主面板右上角的 **Tools → Create empty mod** 建一个空 mod，命名 **Pandora Output**。
3. 在该可执行文件的 **Arguments** 字段填 `-o "路径"`，把 `路径` 换成 Pandora Output 的绝对路径。
   - 取绝对路径：在 MO2 里右键 Pandora Output → **Open In Explorer** → 复制地址栏 URI。
4. 从 MO2 运行 Pandora，**勾选**需要的补丁，点 **Launch**。

> 官方提示：**推荐用启动参数 `-o` 指定输出 mod**，而**不要**用 MO2 的 "Create files in mod instead of overwrite"。原因：用 MO2 VFS 时，Pandora 产生的文件会**覆盖其在原处的现存文件**，哪怕那文件属于另一个 mod。

## Vortex 步骤

1. 在 **mods 文件夹之外**安装 Pandora，并把它加入 tools dashboard。
2. 在 **Command Line** 字段填 `-o "路径"`（指向你的 Pandora Output 文件夹）。
3. 确认 **Start In** 字段指向 Skyrim 的 **Data** 目录。
4. 运行 Pandora，勾选补丁，点 Launch。

> ⚠️ **Pandora Output** 文件夹需要**打包并作为 mod 通过 Vortex 安装**。

## Nexus 文章版步骤（流程细节）

来源：Nexus Article #12319「Extremely Detailed Pandora Install Guide」。要点：

- **Vortex**：把 Pandora.exe 加入 Tools dashboard（Target = exe 路径，Start In = Skyrim\Data）；在 Staging Mods 文件夹里建 `PandoraOutput`；在 Pandora **设置齿轮**里设 Data Path 与 Output Path；运行后**完全重启 Vortex** 并**启用 PandoraOutput mod**，在 "Manage File Conflicts" 里**确保 PandoraOutput 胜出（排在所有冲突之后）**。
  - 每次改动动画 mod：**Deploy → 重跑 Pandora → 再 Deploy**；若弹出"用哪个版本文件"一律选 **Use Newer File**。
- **MO2**：把 Pandora 作为 mod 或手动装（exe 在 Skyrim\Data）；建空 mod `Pandora Output` 并启用；用齿轮图标 → Modify Executables → Add from File 添加 exe，Start in 设为 Skyrim\Data，**不要勾** "Create files in mod instead of overwrite"；运行 Pandora，在 **Paths** 菜单设 Game/Data Path 与 Output Path；点底部三角形按钮 **Run**。
  - 推荐用 Pandora 自身的 **Paths → Output** 指定输出，而**不要**用 MO2 的 "Create files in mod instead of overwrite"（后者会让文件复制覆盖其他 mod 里的同名文件）。

> ⚠️ 启用一个你**没有安装**的动画补丁**会导致问题**。FNIS 动画**只会出现在右侧 Log 面板里**。

## 启动参数速查（README）

| 参数 | 作用 |
| --- | --- |
| `--auto_run` | 用上次成功运行缓存的同批 mod 直接运行 |
| `--auto_close` | 单次运行完成后自动关闭引擎 |
| `--skyrim_debug64` | 输出调试 xml（仅限懂行的作者） |
| `--output`（或 `-o`） | 自定义输出路径，例：`-o "C:\path\Pandora Output"` |
| `--tesv` | 指定**游戏根目录**（含 .exe 的那层，不是 Data）。用于 Wabbajack "Stock Game" 或多版本安装 |
| `--tesv:"path"` | Wabbajack 场景：指向 Stock Game 安装（如 `--tesv:"C:/Path/To/MO2/Stock Game"`） |

> 多个启动参数之间用**空格**分隔。

## 缓存

Pandora 在成功完成一轮打补丁后，会把启用的 mod 保存到外部缓存（`Pandora_Engine/ActiveMods.json`）。加载缓存时，所有启用 mod 显示在顶部，其相对优先级得以保留。**清除缓存**：删除 `Pandora_Engine/ActiveMods.json`。

> 来源：Pandora 仓库 README / Nexus Article #12319
> https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/blob/main/README.md
> https://www.nexusmods.com/skyrimspecialedition/articles/12319

## 相关

- [Pandora 排错](pandora-troubleshooting.md)
- [标准刷补丁流程](../06-practices/install-workflow.md)
