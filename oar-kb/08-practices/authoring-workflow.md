---
id: authoring-workflow
title: 实战：改造别人的动作包（六步法）
category: 08-practices
kind: tutorial
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 实战, 改造, 六步法, DAR, 优先级]
aliases: [改造别人动画包, 怎么改 mod 动画, workflow, 替换动画步骤]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 把一个 DAR 格式的动画包改成 OAR 原生结构的完整流程：备份→判 hkx→查事件名→搭目录改名→写 config.json→移走旧 DAR 结构→静态校验；含"按攻击阶段拆分移动接管"的进阶技巧。
---

# 实战：改造别人的动作包（六步法）

> 本页的流程与本工作区的一次真实改造（把一个 DAR 格式的站姿弓动作包改成"潜行专用 + 移动保持姿势"）一一对应，所有结论都在 Skyrim SE + MO2 + OAR 环境下实测或对照 vanilla 行为文件核实。

## 心智模型回顾

动手前请先读完 [替换的心智模型](animation-key-model.md)。一句话：**替换的键是「路径 + 文件名」；文件名错 = 永不生效且不报错。**

## Step 0 · 备份

```bash
cp "…/_conditions.txt" "…/obito定制拉弓动作-原_conditions.txt.bak"
```

改造过程一定会反复比对，原件是唯一的回退手段。

## Step 1 · 判 hkx 版本（不是 SE 格式就白干）

**看标签判不出位宽。** 与整合内一个**确定能正常播放**的 SSE 动画做**头部逐字节比对**，看 `0x0C` 是否为 `08 00 00 00`。

方法见 [hkx 版本判定](animation-key-model.md#三hkx-文件的版本判定最容易踩的坑)。

> 实测结论示例：4 个源文件头部与整合内已知可用的 SSE 动画**逐字节一致**，是原生 64 位格式，**不需要任何转换**，可以直接改名使用。

## Step 2 · 搞清楚目标状态请求哪些文件名

**这是整个改造的成败所在。** 三条路（读行为文件 / 看专业包分包 / 读 OAR 日志）见 [2. 怎么查游戏请求哪个文件名](animation-key-model.md#二怎么查游戏到底请求哪个文件名)。

改造示例（站姿 → 潜行）的对照结果：

```
原来放的（站姿）      →  要改成（潜行）
Bow_DrawLight.HKX         sneakbow_drawlight.hkx
Bow_IdleDrawn.HKX         sneakbow_idledrawn.hkx
Bow_Release.HKX           sneakbow_release.hkx
bow_drawheavy.HKX         （潜行没有对应事件，废弃）
```

额外还要抢 20 个**移动/转身**文件，才能做到「移动时保持姿势」：

```
SneakWalk_Forward / FrwrdLeft / FrwrdRight / Left / Right /
          Bckward / BckwrdLeft / BckwrdRight          （8 个）
SneakRun_Forward / FrwrdLeft / FrwrdRight / Left / Right /
         Backward / BckwrdLeft / BckwrdRight          （8 个）
Sneak_TurnLeft60 / TurnLeft180 / TurnRight60 / TurnRight180   （4 个）
```

## Step 3 · 搭目录 + 复制重命名

**hkx 内容一字不改**，只是「换个名字放到对的位置」：

```bash
ROOT="$MOD/meshes/actors/character/animations/OpenAnimationReplacer/ObitoSneakBow"
mkdir -p "$ROOT/Pose" "$ROOT/HoldMove"

# 潜行三件套：改名即可
cp "$SRC/Bow_DrawLight.HKX" "$ROOT/Pose/sneakbow_drawlight.hkx"
cp "$SRC/Bow_IdleDrawn.HKX" "$ROOT/Pose/sneakbow_idledrawn.hkx"
cp "$SRC/Bow_Release.HKX"   "$ROOT/Pose/sneakbow_release.hkx"

# 移动保持姿势：把「瞄准姿势」这一个文件复制成 20 个移动事件名
for n in sneakwalk_forward sneakwalk_frwdleft … sneak_turnright180; do
  cp "$SRC/Bow_IdleDrawn.HKX" "$ROOT/HoldMove/$n.hkx"
done
```

> 💡 **「复制同一个文件成 N 份」是让某个姿势在多个事件下复用**的标准手法。代价见 [坑与代价](pitfalls-and-costs.md)。

## Step 4 · 写 `config.json`

拆成**多个 submod**，因为**一个 submod 内所有动画共享同一套条件**——条件不同就必须拆。

**`Pose/config.json`**（潜行时用这套动作）：

```json
{
    "name": "Sneak Bow Pose",
    "priority": 1750000000,
    "interruptible": true,
    "conditions": [
        { "condition": "IsActorBase", "requiredVersion": "1.0.0.0",
          "Actor base": { "pluginName": "Skyrim.esm", "formID": "7" } },
        { "condition": "IsSneaking", "requiredVersion": "1.0.0.0" }
    ]
}
```

**`HoldMove/config.json`**（移动时保持拉弓姿势）：

```json
{
    "name": "Sneak Bow - Hold Pose While Moving",
    "priority": 1750000010,
    "interruptible": true,
    "conditions": [
        { "condition": "IsActorBase", "requiredVersion": "1.0.0.0",
          "Actor base": { "pluginName": "Skyrim.esm", "formID": "7" } },
        { "condition": "IsSneaking", "requiredVersion": "1.0.0.0" },
        { "condition": "OR", "requiredVersion": "1.0.0.0",
          "Conditions": [
              { "condition": "IsEquippedType", "requiredVersion": "1.0.0.0",
                "Type": { "value": 7.0 }, "Left hand": true },
              { "condition": "IsEquippedType", "requiredVersion": "1.0.0.0",
              "Type": { "value": 7.0 }, "Left hand": false }
          ] },
        { "condition": "OR", "requiredVersion": "1.0.0.0",
          "Conditions": [
              { "condition": "AttackState", "requiredVersion": "1.3.0.0",
                "Comparison": "==", "Attack state": { "value": 9.0 } },
              { "condition": "AttackState", "requiredVersion": "1.3.0.0",
                "Comparison": "==", "Attack state": { "value": 10.0 } }
          ] }
    ]
}
```

**`HoldMove` 里那两组 OR 是这套方案的关键**：

- 第一组「手上有弓」——潜行移动事件会被**所有**潜行角色请求，条件必须把范围收窄；
- 第二组「弓已拉开」——**没有它，潜行持弓但没拉弦走路时姿势也会被冻住**。这是最典型的"条件太宽"事故。

字段写法要点（详见 [条件系统总览](../03-conditions/conditions-overview.md)）：`{"value": N}` 包数值、`Conditions` 大写、`negated` 取反、`formID` 不带 `0x`。

## Step 5 · 把旧 DAR 结构移出 `meshes`

```bash
mkdir -p "$MOD/_备份_原DAR结构"
mv "$MOD/meshes/actors/character/animations/DynamicAnimationReplacer" "$MOD/_备份_原DAR结构/"
```

**为什么必须移走**：`DynamicAnimationReplacer\` 是 OAR 的**合法入口**，留在 `meshes` 里会被当成 `Legacy` replacer mod 一起加载。不移走，新旧两套同时生效，行为不可预期。移到 `meshes` **之外**就不会被扫描。

## Step 6 · 静态校验

不给游戏跑之前，先在文件层面校验：

```python
import json, glob, os
base = r'…\ObitoSneakBow'
for p in glob.glob(base + r'\**\config.json', recursive=True):
    raw = open(p, 'rb').read()
    assert not raw.startswith(b'\xef\xbb\xbf'), 'BOM!'
    d = json.loads(raw.decode('utf-8'))
    print('OK', os.path.relpath(p, base), '| priority =', d.get('priority'))
```

要点：

- **不能有 UTF-8 BOM**（用 Python `json.load` 读二进制、断言开头不是 `EF BB BF`）；
- 文件数对得上；
- 顺手抽查文件头四个字节（Step 1）。

## 进阶技巧 · 让「移动」按动作阶段接管

**要解决的问题**：一个 submod 里所有移动事件只能配**同一个**动画文件。只要条件命中，「移动」期间就永远显示同一个姿势——拉弓拉到一半一移动，会**瞬间跳成拉满弓的姿势**。

**根因**：`IsAttacking` 在整个弓攻击过程（拉弓 → 瞄准 → 放箭）**都为真**。用它当「弓已拉开」的判据，等价于「只要在射箭且移动，就切到保持姿势」。

> ⚠️ **不要用 `IsAttacking` 判断「弓已拉开」**。它只说明「正在攻击」，不区分阶段。要精确到阶段，用 **`AttackState`**。

**解法**：把同一个动作的不同阶段，拆成多个 submod——它们**共用同一批移动文件名**，但分别放不同阶段的动画、配不同的 `AttackState` 条件，靠 `interruptible` 在阶段推进时**自动交接**。

| 阶段 | `AttackState` | 接管子模块 | 移动时播放 |
| --- | --- | --- | --- |
| 拉弓中 | `8` = Bow draw | `DrawMove` | 拉弓动画（**继续拉**） |
| 拉满瞄准 | `9` = Bow attached / `10` = Bow drawn | `HoldMove` | 拉满姿势（**保持**） |
| 放箭中 | `11`~`14` | `ReleaseMove` | 放箭动画（**继续放**） |

三条实现要点：

1. **`interruptible: true` 必须开**。阶段推进（8 → 9/10 → 11）时它才会重新求值并切换动画；否则一旦移动，整个过程中会一直停在进入时的那个动画上。
2. **条件尽量互斥，优先级再拉开做兜底**（本项目：`HoldMove` 0030 > `ReleaseMove` 0020 > `DrawMove` 0010）。
3. **状态值必须用游戏内实时值核对**。`Shift + O` 选中玩家 → 展开对应条件，那一行会显示**当前值**。

### `AttackState` 的弓专用枚举

```
8  = Bow draw          9  = Bow attached      10 = Bow drawn
11 = Bow releasing     12 = Bow released      13 = Bow next attack
14 = Bow follow through
```

`10 = Bow drawn` 就是**「弦已拉满、正在瞄准」**——想判定"玩家正持弓拉满"，这是最精确的一条。

**这套 8/9/10/11 是怎么定下来的**（本工作区的证据链，值得照抄思路）：

- `9`、`10` 由两条独立证据锁定：整合里**全部 9 个**用到 `AttackState` 的专业弓箭 mod 都恰好写 `9 OR 10`；且实测在**拉满弓**时确实生效。
- `8`（前一个）与 `11`（后一个）由 OAR 二进制里枚举名字的**排列顺序**确定：
  `… Bash, [Unused?], Bow draw, Bow attached, Bow drawn, Bow releasing, Bow released, Bow next attack, Bow follow through, Fire, Firing, Fired`
  ——锚定 `Bow attached / Bow drawn = 9 / 10` 后，前后邻居自然确定。

> 方法论价值：**"多个专业 mod 一致写同一个枚举值"是最强的交叉验证**；当需要枚举的相邻值时，**读二进制里的名字排列顺序**比猜可靠。

## 做完之后要接受的代价

见 [坑与代价](pitfalls-and-costs.md)。三条核心：移动会滑行、被替换动画的内嵌事件会丢、会盖掉同文件名的其他 mod。

**更省事的替代方案**：如果只是不想"跳到拉满姿势"，可以把 `HoldMove` 收窄成只判 `9/10`，**不做** `DrawMove` / `ReleaseMove`。这样拉弓/放箭途中移动时会**落到下一个同名的提供者**（例如整合里 Gunslicer 的潜行弓移动动画——一套"边走边持弓"的完整动作）。视觉上比滑行自然，代价是它不接续你原来的动作。

## 相关

- [替换的心智模型](animation-key-model.md)
- [坑与代价](pitfalls-and-costs.md)
- [手动迁移流程](../07-migration/manual-migration.md)
- [条件系统总览](../03-conditions/conditions-overview.md)
