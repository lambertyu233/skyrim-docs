---
id: pandora-patch-format
title: Pandora 补丁格式（作者向）
category: 04-pandora
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [Pandora, 补丁格式, xml, 作者, 文件定位, AnimData]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/blob/main/README.md
summary: Pandora 作者向补丁格式速查：单一 xml patch、四类编辑操作、文件定位规则、AnimData/AnimSetData 与图注入。
---

# Pandora 补丁格式（作者向）

> 本节面向行为 mod 作者，说明 Pandora 的补丁写法。普通玩家无需阅读。内容整理自 Pandora 仓库 README「For Mod Authors」。

## 1. 补丁格式总览

除了兼容**几乎全部 Nemesis 补丁格式**，Pandora 用自己的格式——更高效、更容错。**每个行为图只用单个 xml 文件**（而不是 Nemesis 那样多个文本文件），所有编辑自包含其中：

```xml
<patch>
  <replace>
    <edit path="#xxxx\...\..."><!-- content --></edit>
  </replace>
  <insert>
    <edit path="#xxxx\...\..."><!-- content --></edit>
  </insert>
  <append>
    <edit path="#xxxx\...\..."><!-- content --></edit>
  </append>
  <loose>
    <edit path="#xxxx\...\..."><!-- content --></edit>
  </loose>
</patch>
```

四类操作：**replace（替换）/ insert（插入）/ append（追加）/ loose**。单条编辑的格式：

```xml
<edit path="#xxxx\...\..."><!-- XText xor XElement --></edit>
```

一个真实补丁示例：

```xml
<patch>
  <replace>
    <edit path="#0885/legs/Element0/maxAnkleHeightMS">
      <hkparam name="maxAnkleHeightMS">0.700000</hkparam>
    </edit>
    <edit path="#0885/legs/Element0/hipIndex">
      <hkparam name="hipIndex">12</hkparam>
    </edit>
    <edit path="#0885/legs/Element0/kneeIndex">
      <hkparam name="kneeIndex">13</hkparam>
    </edit>
    <edit path="#0885/legs/Element0/ankleIndex">
      <hkparam name="ankleIndex">14</hkparam>
    </edit>
    <edit path="#0885/legs/Element0/isPlantedMS">
      <hkparam name="isPlantedMS">false</hkparam>
    </edit>
  </replace>
</patch>
```

## 2. 文件定位（File Targeting）

### 唯一标识符（Unique Identifiers）

Pandora 支持与 Nemesis 相同的补丁文件格式，但**扩展了文件夹系统**以提供生物兼容性。补丁文件夹可用**短名**或**完整唯一名**被引擎识别。

完整标识名格式为 `[ProjectName]~[FileName]`。例如：

- `0_master` 也识别为 `defaultmale~0_master`；
  - `_1stperson~0_master` 指向第一人称工程里的另一个同名文件。
- `horsebehavior` 也识别为 `defaultmale~horsebehavior`；
  - `horseproject~horsebehavior` 指向马工程里的同名文件。

注意：使用完整名**不会**把各工程本就共享的文件分开，它只用于解决命名冲突。

### 间接标识符（Indirect Identifiers）

骨骼与角色文件可用短名或全名，也可用：

- `[ProjectName]_character` —— 定位该工程的**角色文件**；
- `[ProjectName]_skeleton` —— 定位该工程的**骨骼文件**。

## 3. AnimData（让动画有位移）

mod 若想让动画带位移（motion），需**手动注册 clip generator**：

- 建名为 `animdata` 的文件夹；
- 在里面建 `[ProjectName].txt`，**每行一个 clip generator 名**；
- 重复项会被自动去重（**区分大小写**）。

自 **v0.3.0-alpha** 起，Pandora 能为既有 Nemesis 格式的 animsingledata 文件生成兼容格式。

## 4. AnimSetData（配对动画等边缘场景）

AnimSetData **不会自动生成**——并非所有新动画都需要它，全量自动生成是浪费。只有**添加配对动画**等边缘场景才需要，目前 Pandora 仅支持"为配对动画添加动画信息"。

写法：按下面的目录结构把动画路径写进独立文件。

```
[ModFolder]\animationsetdatasinglefile\[ProjectName]\[SetName].txt
```

或者直接 `[ModFolder]\animationsetdatasinglefile\[ProjectName].txt`——后者会**自动加到该工程下所有 set**，省去大量复制粘贴。

文件内容每行一个**相对 Data 目录**的动画路径，例如：

```
meshes\actors\character\animations\killmove1.hkx
meshes\actors\character\animations\killmove2.hkx
meshes\actors\character\animations\killmove3.hkx
```

这些动画会被解析、按正确格式编码并加入 animsetdata。

> 过去作者得自己编码文件与路径，并在两个注释标记之间手工插入；现在只需在新文件里写一行。

## 5. 图注入（Graph Injection，实验性）

**图注入**是把 mod 图里的属性注入到原版行为图的过程。（"图"是专用于行为、含节点图的 hkx。）

- FNIS 在通过 `GenerateFNISforModders.exe` 生成 mod 行为时，读 animlist 生成自定义图；
- 先把自定义图解包成可读 xml：**64 位（SE/AE）** 用 hkxconv，**32 位（LE）** 用 hkxcmd；
- 要注入某个图，在其**标识文件夹**下建子文件夹 `inject`，再在其中建一个**与目标 `hkbStateMachine` 同名**的文件夹，把自定义图放进去；
- 要把自定义图的动画（从所有 `hkbClipGenerator` 中提取）注入某个角色文件，在其标识文件夹下建 `inject`，把自定义图放进去。

**注意：图注入是实验性功能，只应由清楚自己在做什么的作者使用。**

## 6. 日志格式（排错用）

日志在 `Engine.log`，格式大致为：`[Severity]: [Component] > [Data] > [Operation] > [Input] > [Status]`。

- **Severity**：`INFO`（提示）/ `WARN`（意外但可能有问题）/ `ERROR`（阻碍了部分工作，多半是真问题）/ `FATAL`（引擎彻底失败，通常发生在导出，应**立即上报**）。
- **Component**：`Assembler`（解析补丁求操作，如 `Nemesis Assembler`）、`Dispatcher`（保存并应用编辑）、`Validator`（编辑后校验）。
- **Input**：通常是 xml 路径，指出编辑失败的位置。

README 给了一个自查示例：路径 `#2521/event/Element0/id` 失败，正确答案应是 `#2521/contactEvent/Element0/id`——**作者需修正，或用户需报给作者**。

> 来源：Pandora 仓库 README「For Mod Authors」
> https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/blob/main/README.md

## 相关

- [Pandora 概览](pandora-overview.md)
- [Pandora 架构与性能设计](pandora-architecture.md)
