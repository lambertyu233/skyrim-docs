---
id: editor-workflow-weapon
title: 实战：给特定武器绑特定动作（不改原 mod 文件）
category: 08-practices
kind: tutorial
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 实战, 武器, Legacy, User 模式, IsEquipped, 巴哈姆特]
source: https://m.gamer.com.tw/forum/C.php?bsn=2526&snA=45432
summary: 巴哈姆特「武器or動作關鍵字替換」教程：用 User 模式 + Legacy 编号定位目标动画，通过 IsEquipped 在原有 OR 内添加武器条件，让某把武器单独用某套动作，全程不动原 mod。
---

# 实战：给特定武器绑特定动作（不改原 mod 文件）

> **素材来源**：巴哈姆特《【心得】Open Animation Replacer(OAR)的簡單應用 - 武器or動作關鍵字替換》
> <https://m.gamer.com.tw/forum/C.php?bsn=2526&snA=45432>
> 面向新手的一篇，比 [高跟鞋那篇](editor-workflow-idle.md) 简单，但**示范了"在已有 OR 里加条件"这个关键动作**。

## 课题

想把 `ADXP I MCO ER Mixed Scythe` 的**镰刀动画**用在自己整合里的 `Immersive Weapon` **龙钢镰刀**上。

传统做法（照原作者教学改）会**动到 mod 原文件**；OAR 则：

> OAR 会帮你建一个在 **overwrite** 内，而且是**直接在游戏内更改条件**不用特地关游戏，省去来回开关游戏的动作。

## 为什么需要这个功能

那套镰刀动画原本绑的是**原作者推荐的配套 mod 的关键字**。如果你没装那个 mod，就享受不到；而你想让你自己的某把武器用上它——最干净的办法就是**在 OAR 里给那条 DAR 规则补一个"我的武器"条件**。

## 完整步骤（原文归纳）

### Step A · 先记住动作编号

> 先记住该动作的编号，以上面举例的镰刀动画，该编号是 **`2800000`**。

### Step B · 进游戏查武器 FormID

> 进游戏把你要改的武器拿出来，开控制台查 **FormID**。

### Step C · 叫出 OAR 编辑器，选 user mod → 展开 Legacy

> **先不要关控制台**，按 **`Shift+O`** 叫出 OAR 的编辑选单，选择 **user mod**，点开 **`Legacy`** 下拉选单。

> 注意"先不要关控制台"——因为你需要控制台里那个 FormID，而且求值目标还挂着。

### Step D · 按编号找到目标，展开 Conditions

> 你会看到一堆编号，找到 **`2800000`** 的编号打开，点开 **conditions**。
> 你会看到 mod 作者已经设定好他原本推荐你装的配套 mod 的关键字。

### Step E · 加条件（⚠️ 必须加在原来的 OR 里面）

这是本页**最有价值的一条**：

> 这里用 **`IsEquipped`**，这是指定装备特定武器。因为镰刀在没有其他 mod 辅助的情况下并没有分配到武器关键字，需要特别注意的是**作者使用了 `or`**，所以**你不能另开 add new conditions，你只能在 `or` 的条件内点选 add new conditions**。
> 之后在框内照着控制台打入该 mod 全称与 FormID 后 4 码。

> 「当你输入正确就会显示武器，否则是 **Not Found**。另外中文会显示 `?????`，不是输错。」

### Step F · 保存

> 记得储存，点 **Save User Config**，玩你的动作吧。假如弄错也不要紧张，回来删掉或更改就行。

作者结尾很直白：

> 你的 `Immersive Weapon` 龙钢镰刀**再也不是大剑动作了**。

## 三个可复用的知识点

### 1. **"必须加在原有 OR 内"的通用规律**

这跟 LoversLab 那边得到的回答是同一条规律，只是方向相反：

| 场景 | 正确做法 |
| --- | --- |
| 你想**新增一个并列选项**（"我的武器也用它"） | 在**已有的 `OR` 里面**加（本页） |
| 你想**组合两个条件** | **先建 `OR`（或 `AND`）**，再把条件挂进去当子条件（[LoversLab 案例](../03-conditions/condition-containers.md)） |

**统一规律**：**只有容器条件（`OR`/`AND`/`XOR`/`TARGET`/`PLAYER`/`MOUNT`）才有子条件槽。** 普通条件是叶子节点，既不能挂子条件，也不能被"塞进"另一个叶子条件里。

### 2. **输入正确性的即时反馈**

- 正确 → **显示武器名**；
- 错误 → **`Not Found`**；
- **中文显示 `?????`** —— 这是字体问题，**不是输错**。

这条很实用：省得你在"是不是输错了"上纠结。

### 3. **全程改动落在 overwrite / `user.json`**

- 不碰 mod 原文件；
- 弄错了直接回来删掉或改；
- 效果与"改原 mod"一样，但可回退。

## 原文列的常用条件速查

作者顺手列了几个新手最常用的：

> - **`OR`** —— 任一条件达成就用
> - **`AND`** —— 全部条件达成才用
> - **`IsEquipped`** —— 装备特定武器
> - **`IsEquippedType`** —— 装备什么类型的武器（EX：双手空拳、单手锤等）
> - **`IsEquippedHasKeyword`** —— 装备的武器是否有特定关键字
> - **`IsRace`** —— 检测种族
> - **`IsWornHasKeyword`** —— 你全身装备了什么关键字的装备
> - **`IsFemale`** —— 男 or 女

完整清单见 [条件全清单](../03-conditions/conditions-list.md)。

## 与另一个常见需求的对照

| 需求 | 首选条件 |
| --- | --- |
| 某把**具体武器**用某套动作 | `IsEquipped`（指定 form）+ **在已有 OR 内加** |
| 某**类武器**用某套动作 | `IsEquippedType`（类型）+ **左右手各写一条 OR**（见 [容器条件](../03-conditions/condition-containers.md)） |
| 带某**关键字**的武器用某套动作 | `IsEquippedHasKeyword`（关键字可用 `editorID`） |
| 按**装备挂在哪里**决定拔收武器动画 | 用 [IED Conditions](../06-plugins/ied-conditions.md) |

## 相关

- [实战：靠编辑器做条件分流](editor-workflow-idle.md)
- [容器条件与子条件的挂载规则](../03-conditions/condition-containers.md)
- [IED Conditions（按装备位置分流）](../06-plugins/ied-conditions.md)
- [条件全清单](../03-conditions/conditions-list.md)
