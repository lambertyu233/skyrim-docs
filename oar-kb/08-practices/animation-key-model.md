---
id: animation-key-model
title: 替换的心智模型：文件名的权威来源与 hkx 判定
category: 08-practices
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 心智模型, 文件名, hkx, 行为文件, 排错]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: OAR 替换的键是"路径+文件名"；想知道游戏请求哪个文件名，要读 vanilla 行为文件、交叉验证专业动画包的分包方式，或直接看 OAR 日志；hkx 位宽不能看标签，只能与已知可用的 SSE 文件逐字节比对。
---

# 替换的心智模型：文件名的权威来源与 hkx 判定

## 一、三条铁律（本工作区实测总结）

| # | 铁律 | 推论 |
| --- | --- | --- |
| 1 | **想让某个状态换成你的动画，文件名必须等于「那个状态下游戏请求的原始文件名」。** | 文件名错 = 永远不生效，且**不会有任何报错** |
| 2 | **「换不到」优先怀疑文件名，而不是条件。** | 条件写错最多是不命中；文件名写错是根本不会被问 |
| 3 | **一个事件名 = 一个文件，不是「一段动作」。** | 你以为的「一整套拉弓动作」，底层是 4 个互不相干的文件；你只换 idle，一移动就会掉回原版——因为移动是**另一个文件** |

### 举例：弓的动画不是「一套」，是三套

从 vanilla 行为文件里直接读出来的字符串：

| 状态 | 拉弓 | 瞄准待机 | 放箭 | 拉弓状态下**移动** |
| --- | --- | --- | --- | --- |
| **站姿** | `Bow_DrawLight` / `Bow_DrawHeavy` | `Bow_IdleDrawn` | `Bow_Release` | `BowDrawn_WalkForward/Left/Right/Backward`、`BowDrawn_TurnLeft/Right60/180` |
| **潜行** | `SneakBow_DrawLight` | `SneakBow_IdleDrawn` | `SneakBow_Release` | **`SneakWalk_*` / `SneakRun_*`**（通用潜行移动）+ `Sneak_Turn*`、`SneakMTIdle` |

三条结论：

1. **潜行时游戏根本不请求 `Bow_*`**，它请求的是 `SneakBow_*`。所以"把站姿动画的文件名原封不动留着，只加一条 `IsSneaking` 条件"是**彻底无效**的。
2. **「拉弓后移动」换的是另一套动画**。站姿走 `BowDrawn_Walk*`，潜行走**通用的** `SneakWalk_*` / `SneakRun_*`——潜行拉弓一移动，游戏请求的根本不是任何 `bow` 文件。
3. **潜行弓没有自己的移动动画**。vanilla 里只有 `SneakBow_DrawLight / IdleDrawn / Release` 三个文件。所以"潜行拉弓移动"只能靠**抢占通用潜行移动文件**实现。

> 旁证：整合里专业动画包 `女性动作补充包Gunslicer OAR Animations Pack` 的 `Bow_Sneak` 子模块，正是把 `sneakbow_*`（3 个）+ `sneakwalk_*` / `sneakrun_*` / `sneak_turn*` / `sneakmtidle`（21 个）**放在同一个 submod、同一套条件下**。**专业作者的打包方式和 vanilla 的行为结构完全对得上。**

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`。

## 二、怎么查「游戏到底请求哪个文件名」

三条路，从权威到省事：

### 2.1 权威：读 vanilla 行为文件

行为文件是「事件 → 动画路径」映射的**唯一定义处**。整合里通常有几份副本：

| 文件 | 能查到什么 |
| --- | --- |
| `…\characters\defaultmale.hkx` | **剪辑生成器 + 完整动画路径列表**（最全的"有哪些动画名"） |
| `…\behaviors\0_master.hkx` | 状态机、**行为图变量名**（如 `bBowDrawn`） |
| `…\behaviors\bow_direction_behavior.hkx` | **方向/移动分支**（含潜行分支，能看出"潜行拉弓移动走哪套"） |

**读法**：hkx 是二进制，但这些路径都是明文字符串。用 Python 提 ASCII 串即可：

```python
import re
data = open(path, 'rb').read()
for s in sorted(set(m.group().decode('ascii') for m in re.finditer(rb'[\x20-\x7e]{6,}', data))):
    if 'Animation' in s:
        print(s)
```

> 环境备注：本机没有 `strings` 二进制，用上面的 Python 方案替代。

### 2.2 交叉验证：看专业动画包怎么分包

**比读二进制更直观的一招**：找一个整合里**已知能用**的专业 OAR 动画包，看它的文件夹划分。

**专业包的分包方式 = vanilla 行为结构的镜像。** 这是最好的教科书。

### 2.3 省事：直接读 OAR 日志

**跑一次游戏**，然后看日志。日志会列出**所有被识别为"有人要替换"的原始动画路径**——等于让 OAR 告诉你"哪些文件名是有效的替换目标"。日志还会标注该动画是否会被当作 `interruptible`，这能直接印证你的 submod 有没有被扫描到。

详见 [动画日志与调试](../05-editor/animation-log-and-debugging.md)。

### 2.4 官方补一条：对话 idle 是怎么选到动画的（社区问答）

Nexus 论坛里有人问"怎么让 NPC 在对话的某一句话说某句台词时挠头"。得到的回答把整条链路讲通了：

> **OAR 里的 R 是 Replacer。** 也就是说，这个情境下 NPC 必须**先执行某个** idle 动画，然后 OAR 里要有一条规则**把那个动画替换成另一个**。
> 比如你为这个特定 NPC 写一条规则，把"耸肩"替换成"挠头"，然后在对话里指示一个"耸肩" idle。

更具体的走法（同帖的详解）：

> 在 Creation Kit 里做对话时，TopicInfo 窗口里编辑某句回应时，**Edit Response 窗口可以给说话者和/或听者选一个 idle 动画播放**。
> CK 的 Gameplay 菜单里，Animations → 展开 `Actors\Character\Behaviors\` 树，**最后有个 LOOSE 分类**——那里面的动画就是你能在 Edit Response 窗口里选的。例如 `IdleCiceroDance1`。
> Animations 窗口会告诉你 `IdleCiceroDance1` 这个 idle 实际用的是 `IdleCiceroDance1` 这个**动画事件**。
> 在 `meshes\actors\character\behaviors` 里 grep（我用 Nemesis，所以有 `Nemesis_*.xml`），能查到 `CiceroDance1` 对应 `Animations\Special_CiceroDance3.HKX`。
> **所以，走 OAR 路线的话，你可以在 OAR 里替换那个具体的 `.hkx` 文件，并加一条规则让它只对这个 NPC 生效。**
>
> 另一条路是把这个挠头动画文件加进你的 mod，并配上 FNIS/Nemesis 的行为文件——那就变成**新增动画事件**了。

> 来源：<https://forums.nexusmods.com/topic/13506665-need-answer-with-oar-how-it-actually-works/>

**这段的价值**：它示范了"**从 CK 看到的 idle 名 → 行为文件里的动画事件 → 具体 hkx 路径**"这条完整追查链。这是把"我想要某句台词配某动作"落到 OAR 条件上的正确姿势。

### 2.5 社区补充：一个 LoversLab 上的"反向验证"

有人想把一套 idle 改成 `mt_idle.hkx`，得到的最靠谱的回答是：

> 如果它已经是 `.hkx` 格式，你只需要**把它改名为 `mt_idle.hkx`**，然后放到 OAR（或 DAR）用来加载它们的文件夹里。

> 来源：<https://www.loverslab.com/topic/229457-making-an-idle-animation>

**注意**：这条"只改文件名就行"的说法**只在文件名本来就是游戏请求的那个时才成立**——它和铁律 1 完全一致，不是矛盾。文件名对了内容随便，文件名错了内容再好也没人问。

## 三、hkx 文件的版本判定（最容易踩的坑）

**看标签是判不出 32/64 位的。**

`hkx` 文件头里那个 `hk_2010.2.0-r1` 标签，**Skyrim LE（32 位）和 SE（64 位）共用**。一个 LE 格式的动画丢进 SE，游戏**不会报错**，只会**加载失败**（角色摆 T-pose 或该动作不播放）。

**唯一可靠的判定方法：与本机已知可用的 SSE 动画做头部逐字节比对。**

```bash
# 待判定的文件
od -A x -t x1z -N 64 "待判定.hkx"
# 参照物：整合里随便一个确定能用的 OAR 动画
od -A x -t x1z -N 64 "已知可用.hkx"
```

本工作区实测的**可用 SSE 文件头**（两份来自不同 mod 的文件**完全一致**）：

```
000000 57 e0 e0 57 10 c0 c0 10 00 00 00 00 08 00 00 00   >W..W............<
000010 08 01 00 01 03 00 00 00 02 00 00 00 00 00 00 00   >................<
000020 00 00 00 00 4b 00 00 00 68 6b 5f 32 30 31 30 2e   >....K...hk_2010.<
000030 32 2e 30 2d 72 31 00 ff 00 00 00 00 ff ff ff ff   >2.0-r1..........<
```

逐段读它：

| 偏移 | 值 | 含义 |
| --- | --- | --- |
| `0x00` | `57 E0 E0 57` | hkx magic #1 |
| `0x04` | `10 C0 C0 10` | hkx magic #2 |
| `0x08` | `00 00 00 00` | userTag（通常为 0） |
| `0x0C` | **`08 00 00 00`** | **指针宽度 = 8 → 64 位（SE）** |
| `0x10` | `08 01 00 01` | layout rules |
| `0x28` | `hk_2010.2.0-r1` | 版本标签（**LE/SE 共用，不能用来判位宽**） |

**判定就看 `0x0C` 那个 4 字节**：`08 00 00 00` = 64 位。32 位（LE）文件此处按社区通行说法是 `04 00 00 00`——**但这一条未在本机实测**。所以最稳的判定永远是：

> 拿一个**你确定游戏能正常播放**的 SSE 动画当基准，两份文件逐字节比对；一致就能用。

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`。

**旁证**：社区里那位 A-pose 玩家提到的 FNIS 报错 `"32bit Animations incompatible with the current version of the game"` 就是位宽不对的典型信号。
> 来源：<https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/>

## 四、被替换动画的"代价"（副产物）

替换是**换文件**，不是改逻辑。所以：

1. **被替换掉的动画，其内嵌事件一起消失。** 原版移动动画里带的 `FootLeft`/`FootRight` 脚步声事件随替换没了。对潜行通常是好事，但要知道。
2. **会盖掉同文件名的其他 mod。**
3. **移动会"滑行"**（如果替换的是个静态姿势）——见 [坑与代价](pitfalls-and-costs.md)。

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`。

## 相关

- [实战：改造别人的动作包](authoring-workflow.md)
- [坑与代价](pitfalls-and-costs.md)
- [动画日志与调试](../05-editor/animation-log-and-debugging.md)
