# OAR 补充文档 —— 从「看懂」到「改出来」

> **本文定位**：`OAR-教程.md` 是**官方文档的结构化整理**（条件清单、编辑器三模式、变体、预设、函数）。本文补的是它没有的那一半——**把别人的动画包改造成自己想要的样子**这条路怎么走。
>
> **素材来源**：本机对 `obito定制拉弓动作`（一个 DAR 格式的纯动画包）的完整改造过程，所有结论都在 Skyrim SE + MO2 + **OAR 2.3.6** 环境下实测/核对过。
>
> 阅读顺序建议：先看 `OAR-教程.md` 建立概念 → 再看本文动手。

---

## 目录

1. [先建立正确的心智模型：OAR 到底在替换什么](#一先建立正确的心智模型oar-到底在替换什么)
2. [目录与配置：DAR 旧格式 vs OAR 原生格式](#二目录与配置dar-旧格式-vs-oar-原生格式)
3. [优先级：三种来源与冲突排查](#三优先级三种来源与冲突排查)
4. [条件：文本语法 vs JSON 语法](#四条件文本语法-vs-json-语法)
5. [实操：把 DAR 动作包改造成 OAR 原生（六步法）](#五实操把-dar-动作包改造成-oar-原生六步法)
6. [怎么查「游戏到底请求哪个文件名」](#六怎么查游戏到底请求哪个文件名)
7. [hkx 文件的版本判定](#七hkx-文件的版本判定)
8. [验证与排错](#八验证与排错)
9. [案例复盘：一次「看起来对、实际无效」的改法](#九案例复盘一次看起来对实际无效的改法)
10. [经验清单（照抄即可）](#十经验清单照抄即可)
11. [附录：本次改造的完整配置](#附录本次改造的完整配置)

---

## 一、先建立正确的心智模型：OAR 到底在替换什么

**这是全文最重要的一节。** 绝大多数「改了没效果」的困惑，根子都在对 OAR 的粒度理解错了。

### 1.1 替换的键是「路径 + 文件名」，不是「动作」

游戏的行为图（behavior）里，写死了类似这样的一条条引用：

```
Animations\Bow_IdleDrawn.hkx
Animations\SneakBow_IdleDrawn.hkx
Animations\SneakWalk_Forward.hkx
```

当游戏要播放「持弓瞄准待机」时，它去请求 `Bow_IdleDrawn.hkx`。OAR 在这一步**拦截请求**，问一句：

> 在我扫描到的所有 submod 里，谁的目录下放着一个叫 `Bow_IdleDrawn.hkx` 的文件、且条件命中了？

然后挑**优先级最高**的那个，把请求重定向过去。

所以：

### 1.2 三条铁律

| # | 铁律 | 推论 |
| --- | --- | --- |
| 1 | **想让某个状态换成你的动画，你的文件名必须等于「那个状态下游戏请求的原始文件名」。** | 文件名错 = 永远不生效，且不会有任何报错。 |
| 2 | **「换不到」优先怀疑文件名，而不是条件。** | 条件写错最多是不命中；文件名写错是根本不会被问。 |
| 3 | **一个事件名 = 一个文件，不是「一段动作」。** | 你以为的「一整套拉弓动作」，底层是 4 个互不相干的文件；你只换其中的 idle，一旦移动就会掉回原版——因为移动是**另一个文件**。 |

**第 3 条是本次改造的核心收获**，值得单独举例。

### 1.3 举例：弓的动画不是「一套」，是三套

从 vanilla 行为文件里直接读出来的字符串：

| 状态 | 拉弓 | 瞄准待机 | 放箭 | 拉弓状态下**移动** |
| --- | --- | --- | --- | --- |
| **站姿** | `Bow_DrawLight`<br>`Bow_DrawHeavy` | `Bow_IdleDrawn` | `Bow_Release` | `BowDrawn_WalkForward/Left/Right/Backward`、`BowDrawn_TurnLeft/Right60/180` |
| **潜行** | `SneakBow_DrawLight` | `SneakBow_IdleDrawn` | `SneakBow_Release` | **`SneakWalk_*` / `SneakRun_*`**（通用潜行移动）+ `Sneak_Turn*`、`SneakMTIdle` |

三个必须记住的结论：

1. **潜行时游戏根本不请求 `Bow_*`**。它请求的是 `SneakBow_*`。所以「把站姿动画的文件名原封不动放着，只加一条 `IsSneaking` 条件」是彻底无效的。
2. **「拉弓后移动」换的是另一套动画**。站姿走 `BowDrawn_Walk*`，潜行走**通用的** `SneakWalk_*` / `SneakRun_*`——也就是说，潜行拉弓一移动，游戏请求的根本不是任何 `bow` 文件。
3. **潜行弓没有自己的移动动画**。vanilla 里只有 `SneakBow_DrawLight / IdleDrawn / Release` 三个文件，没有 `SneakBowDrawn_Walk*`。所以「潜行拉弓移动」这件事，只能靠**抢占通用潜行移动文件**来实现。

> **旁证**：整合里专业动画包 `女性动作补充包Gunslicer OAR Animations Pack` 的 `Bow_Sneak` 子模块，正是把 `sneakbow_*`（3 个）+ `sneakwalk_*` / `sneakrun_*` / `sneak_turn*` / `sneakmtidle`（21 个）**放在同一个 submod、同一套条件下**。专业作者的打包方式和 vanilla 的行为结构完全对得上——这是最好的教科书。

---

## 二、目录与配置：DAR 旧格式 vs OAR 原生格式

### 2.1 两种写法并排看

同一个需求（替换玩家的 `Bow_IdleDrawn`），两种格式：

**DAR 旧格式**（OAR 会把它读成 `Legacy` replacer mod）：

```
meshes\actors\character\animations\
└─ DynamicAnimationReplacer\
   └─ _CustomConditions\
      └─ 1750000000\              ← 文件夹名 = 优先级
         ├─ _conditions.txt       ← 文本条件
         └─ Bow_IdleDrawn.HKX     ← 文件名 = 被替换的事件
```

**OAR 原生格式**：

```
meshes\actors\character\animations\
└─ OpenAnimationReplacer\
   └─ ObitoSneakBow\              ← 「替换模组名」，随便起
      ├─ config.json              ← mod 级：只有 name / author / description
      └─ Pose\                    ← 「子模组」，随便起
         ├─ config.json           ← 子模组级：priority / conditions / interruptible
         └─ Bow_IdleDrawn.hkx
```

### 2.2 OAR 的路径规则：插在哪都行，但后半段不能动

自 OAR **2.0.0** 起，replacer mod 可以放在 `meshes` 下的**任意位置**。规则一句话：

> 把 `OpenAnimationReplacer\<Mod名>\<Submod名>\` 这一段，**插进原始动画路径的任意位置**，后面保留原始相对路径。

以 `male\mt_idle.hkx` 为例，以下都合法：

```
meshes\OpenAnimationReplacer\MyMod\MySub\actors\character\animations\male\mt_idle.hkx
meshes\actors\OpenAnimationReplacer\MyMod\MySub\character\animations\male\mt_idle.hkx
meshes\actors\character\OpenAnimationReplacer\MyMod\MySub\animations\male\mt_idle.hkx
```

**实际最省事的做法**：插在 `animations\` 这一层（本项目就是这么做的）——因为行为文件里的引用是以 `Animations\` 开头写的，动画文件本体也确实住在 `...\character\animations\` 下，这一层最不会记错。

### 2.3 谁是 submod？——config.json 的位置说了算

- **`config.json` 所在的那个文件夹，就是 submod 的根**；它覆盖该文件夹及其**所有子文件夹**里的 hkx。
- 如果某个子文件夹**自己又放了一份 `config.json`**，它就变成一个**独立的 submod**，与父级互不干扰。
- 这解释了为什么专业包（如 Gunslicer）是「两层 config.json」：顶层只写名字和描述，每个功能文件夹各写自己的条件和优先级。

> 这意味着你可以用**嵌套结构**做出一套动作的不同变体，且各自带独立条件——这是 DAR 那种「一个优先级文件夹一套条件」做不到的。

---

## 三、优先级：三种来源与冲突排查

### 3.1 优先级从哪来

| 来源 | 怎么定 | 备注 |
| --- | --- | --- |
| OAR 原生 submod | `config.json` 里的 `"priority"` 字段 | 数字，**越大越优先** |
| DAR 旧格式 | **文件夹名**就是优先级 | 必须是 `-2147483648 ~ 2147483647` 内不为 0 的整数 |
| DAR 的 ActorBase 派发目录 | 恒为 **0** | 即按「哪个 NPC 用哪套」分文件夹的那种写法 |

同名动画被多个 submod 命中时 → **取优先级最高的那个**。

### 3.2 什么时候会“顶掉”别人

这是实战里最容易出事故的地方。改造一个动画包之前，**先查一下这个文件名在整合里还有谁在提供**：

```bash
find "…\mods" -iname "bow_idledrawn.hkx" -printf "%10s  %p\n"
```

一眼就能看出：
- 有几个来源；
- 各自文件大小（**大小差异大 = 动画内容/骨骼绑定不同**，是判断“谁是专业包”的快速线索）。

一个刻意拉满的优先级（比如本项目的 `1750000000`）会**压制整合里所有同类动画包**。要不要压，取决于你的意图：

- **想让自己的改动赢** → 保持高优先级；
- **只想在别人没覆盖的状态下生效**（例如只想管潜行，不想影响站姿）→ 应该**收窄条件**，而不是靠优先级硬顶。

### 3.3 冲突排查的正确姿势

游戏内 `Shift + O` → 控制台选中目标 actor（或直接输 FormID）→ 找到那条动画 → **「替换列表」标签页**。

它会：
- 按**优先级**列出该动画的**所有**替换项；
- 高亮当前**实际胜出**的那个；
- 多个 submod **优先级相同**时，编辑器会给出**警告**（同优先级的结果不可预期，必须避免）。

---

## 四、条件：文本语法 vs JSON 语法

### 4.1 文本语法（DAR 旧格式的 `_conditions.txt`）

```
IsActorBase("Skyrim.esm" | 0x00000007)
```

格式是 `函数名("插件名" | 0xFormID)`，多个条件用 `AND` / `OR` / `NOT` **在同一行串联**：

```
IsActorBase("Skyrim.esm" | 0x00000007) AND IsSneaking()
```

**FormID 要丢掉代表加载顺序的前两位**：`0xAA123456` → `0x00123456`。

`Skyrim.esm` 的 `0x00000007` 是 **Player 这条 NPC_ 记录**——这是最常用的「只对玩家生效」写法。

### 4.2 JSON 语法（OAR 原生）

```json
{
    "name": "Sneak Bow Pose",
    "priority": 1750000000,
    "interruptible": true,
    "conditions": [
        {
            "condition": "IsActorBase",
            "requiredVersion": "1.0.0.0",
            "Actor base": { "pluginName": "Skyrim.esm", "formID": "7" }
        },
        { "condition": "IsSneaking", "requiredVersion": "1.0.0.0" }
    ]
}
```

几个反直觉的点：

- **字段名是英文可读名**（`"Actor base"`、`"Left hand"`、`"Attack state"`），不是变量名。
- **数值要包成对象**：`"Type": { "value": 7.0 }`，不是 `"Type": 7`。
- **顶层的 `conditions` 数组本身就是 AND**，不需要写 AND。
- **组合条件用条件的形式写**：`{"condition": "OR", "Conditions": [ … ]}`——注意子数组的键是**大写 `C` 的 `Conditions`**。
- `formID` 在 JSON 里写**插件内的 FormID**（本项目实测写成字符串 `"7"` 可用），不带 `0x` 前缀；对应文本语法的 `0x00000007`。

### 4.3 常用条件速查（本项目实测过的）

| 条件 | 用途 | 关键参数 |
| --- | --- | --- |
| **IsActorBase** | 限定某个角色（最常用：玩家） | `{pluginName, formID}`，玩家 = `Skyrim.esm` / `7` |
| **IsSneaking** | 潜行中 | — |
| **IsWeaponDrawn** | 已拔武器 | — |
| **IsEquippedType** | 手上是什么类型的武器 | `Type`：**7 = Bow**；左右手用 `"Left hand": true/false`；**左右手要各写一条 OR**（避免手位歧义） |
| **AttackState** | 攻击状态（**弓有专用枚举**） | 见下表 |
| **IsAttacking** | 正在攻击（**含拉弓保持阶段**） | — |
| **IsMovementDirection** | 朝某个方向移动 | 配 `MovementSpeed` 用 |

**`AttackState` 的弓专用枚举（重要）**：

```
8  = Bow draw          9  = Bow attached      10 = Bow drawn
11 = Bow releasing     12 = Bow released      13 = Bow next attack
14 = Bow follow through
```

`10 = Bow drawn` 就是**「弦已拉满、正在瞄准」**——想判定「玩家正持弓拉满」，这是最精确的一条。

### 4.4 两个必知的坑

**坑 1：`HasGraphVariable` 只能判断变量「存在」，不能读值。**

想要「读行为图变量的值」做判断，要用 **`CompareValues`**（它的取值来源支持行为图变量）或 OAR 专门的图变量条件，不能指望 `HasGraphVariable`。

**坑 2：抄别人的条件时要连 `requiredVersion` 一起抄。**

带版本号的条件（如 `AttackState` 是 `1.3.0.0`）如果没写 `requiredVersion`，或写的版本高于你的 OAR，编辑器会报「需要更高版本/缺少插件」。**最安全的做法**：别手写，直接在 `Shift + O` 的**作者模式**里加条件，编辑器会自动填好所有字段。

### 4.5 怎么学会 `config.json` 的字段名（推荐做法）

官方文档明确说过 *“不要手动编辑 .json”*——理由是容易写错。但改造场景下你迟早要手写。**最可靠的自学方法**：

1. 在 `Shift + O` 作者模式下，打开一个 submod；
2. 改一个设置（勾上 Constant polling、改优先级、加一条条件）；
3. 回到文件系统，**用 git diff / 对比工具看 `config.json` 多出了什么字段**。

字段名、值的格式（什么时候用 `{}`、什么时候用数组）全都一目了然，比查文档快且准。

---

## 五、实操：把 DAR 动作包改造成 OAR 原生（六步法）

以本项目为例：把 `obito定制拉弓动作`（4 个站姿弓动画 + 一行条件）改造成「**潜行专用 + 移动保持姿势**」。

### Step 0 · 备份

```bash
cp "…/_conditions.txt" "…/obito定制拉弓动作-原_conditions.txt.bak"
```

改造过程一定会反复比对，原件是唯一的回退手段。

### Step 1 · 判 hkx 版本（不是 SE 格式就白干）

见 [第七节](#七hkx-文件的版本判定)。

### Step 2 · 搞清楚目标状态请求哪些文件名

**这是整个改造的成败所在**，方法见 [第六节](#六怎么查游戏到底请求哪个文件名)。

本项目查出来的结果：

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

### Step 3 · 搭目录 + 复制重命名

**hkx 内容一字不改**，只是「换个名字放到对的位置」：

```bash
ROOT="$MOD/meshes/actors/character/animations/OpenAnimationReplacer/ObitoSneakBow"
mkdir -p "$ROOT/Pose" "$ROOT/HoldMove"

# 潜行三件套：改名即可
cp "$SRC/Bow_DrawLight.HKX" "$ROOT/Pose/sneakbow_drawlight.hkx"
cp "$SRC/Bow_IdleDrawn.HKX" "$ROOT/Pose/sneakbow_idledrawn.hkx"
cp "$SRC/Bow_Release.HKX"   "$ROOT/Pose/sneakbow_release.hkx"

# 移动保持姿势：把「瞄准姿势」这一个文件复制成 20 个移动事件名
for n in sneakwalk_forward sneakwalk_frwrdleft … sneak_turnright180; do
  cp "$SRC/Bow_IdleDrawn.HKX" "$ROOT/HoldMove/$n.hkx"
done
```

> 💡 **「复制同一个文件成 N 份」是让某个姿势在多个事件下复用**的标准手法。代价见 Step 5 之后的注意事项。

### Step 4 · 写 config.json

拆成**两个 submod**，因为两组的条件不同：

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
                "Comparison": "==", "Attack state": { "value": 10.0 } },
              { "condition": "IsAttacking", "requiredVersion": "1.0.0.0" }
          ] }
    ]
}
```

**`HoldMove` 里那两组 OR 是这套方案的关键**：

- 第一组「手上有弓」——防止对没拿弓的潜行角色误触发（虽然潜行移动事件会被所有潜行角色请求，但条件把范围收窄了）；
- 第二组「弓已拉开」——**没有它，潜行持弓但没拉弦走路时姿势也会被冻住**。这是最典型的“条件太宽”事故。

### Step 5 · 把旧 DAR 结构移出 `meshes`

```bash
mkdir -p "$MOD/_备份_原DAR结构"
mv "$MOD/meshes/actors/character/animations/DynamicAnimationReplacer" "$MOD/_备份_原DAR结构/"
```

**为什么必须移走**：`DynamicAnimationReplacer\` 是 OAR 的**合法入口**，留在 `meshes` 里会被当成 `Legacy` replacer mod 一起加载。不移走，新旧两套同时生效，行为不可预期。移到 **`meshes` 之外**（哪怕是 mod 根目录下的 `_备份\`）就不会被扫描。

### Step 6 · 静态校验

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
- 文件数对得上（本项目：`Pose` 3 个 + `DrawMove` / `ReleaseMove` / `HoldMove` 各 20 个）；
- 顺手抽查文件头四个字节（见第七节）。

### 进阶技巧 · 让「移动」按动作阶段接管

**要解决的问题**：一个 submod 里，所有移动事件只能配**同一个**动画文件。只要条件命中，「移动」期间就永远显示同一个姿势——拉弓拉到一半一移动，会**瞬间跳成拉满弓的姿势**，看起来像动作被打断。

**根因**：`IsAttacking` 在整个弓攻击过程（拉弓 → 瞄准 → 放箭）**都为真**。用它当「弓已拉开」的判据，等价于「只要在射箭且移动，就切到保持姿势」。

> ⚠️ **不要用 `IsAttacking` 判断「弓已拉开」**。它只说明「正在攻击」，不区分阶段。要精确到阶段，用 `AttackState`。

**解法**：把同一个动作的不同阶段，拆成多个 submod——它们**共用同一批移动文件名**，但分别放不同阶段的动画、配不同的 `AttackState` 条件，靠 `interruptible` 在阶段推进时自动交接。

| 阶段 | `AttackState` | 接管子模块 | 移动时播放 |
| --- | --- | --- | --- |
| 拉弓中 | `8` = Bow draw | `DrawMove` | 拉弓动画（**继续拉**） |
| 拉满瞄准 | `9` = Bow attached<br>`10` = Bow drawn | `HoldMove` | 拉满姿势（**保持**） |
| 放箭中 | `11` = Bow releasing<br>`12` = Bow released<br>`13` = Bow next attack<br>`14` = Bow follow through | `ReleaseMove` | 放箭动画（**继续放**） |

三条实现要点：

1. **`interruptible: true` 必须开**。阶段推进（8 → 9/10 → 11）时它才会重新求值并切换动画；否则一旦移动，整个过程中会一直停在进入时的那个动画上。
2. **条件尽量互斥，优先级再拉开做兜底**。本项目：`HoldMove` 1750000030 > `ReleaseMove` 1750000020 > `DrawMove` 1750000010。
3. **状态值必须用游戏内实时值核对**。`Shift + O` 选中玩家 → 展开对应条件，那一行会显示**当前值**；对着它确认「拉弓时是几、拉满时是几、放箭时是几」。

> **本项目所用的 8 / 9 / 10 / 11 是怎么定下来的**
>
> - `9`、`10` 由两条独立证据锁定：整合里**全部 9 个**用到 `AttackState` 的专业弓箭 mod（速射弓 `Professional Skill`、`动态闪避射击` 等）都恰好写 `9 OR 10`；且本 mod 上一版用 `9 OR 10` 时，实测在**拉满弓**时确实生效。
> - `8`（前一个）与 `11`（后一个）由 OAR 二进制里枚举名字的**排列顺序**确定：
>   `… Bash, [Unused?], Bow draw, Bow attached, Bow drawn, Bow releasing, Bow released, Bow next attack, Bow follow through, Fire, Firing, Fired`
>   —— 锚定 `Bow attached / Bow drawn = 9 / 10` 后，前后邻居自然确定。

**代价**：拉弓/放箭都是整段全身动画，其间角色仍在移动，所以上半身在拉弓、下半身不动——**会滑行**。这是文件替换层的上限，想两者兼得只能重做动画。

**更省事的替代方案**：如果只是不想「跳到拉满姿势」，可以把 `HoldMove` 收窄成只判 `9/10`，**不做** `DrawMove` / `ReleaseMove`。这样拉弓/放箭途中移动时会**落到下一个同名的提供者**（例如整合里 Gunslicer 的潜行弓移动动画——一套「边走边持弓」的完整动作）。视觉上比滑行自然，代价是它不接续你原来的动作。

### 做完之后要接受的代价

替换动画是「换个文件给游戏播放」，不是「改游戏逻辑」，所以有**物理上限**：

1. **移动会「滑行」**。姿势定格就没有腿部动画，脚必然打滑。想同时保留迈腿，只能重做一套 K 帧动画——这超出文件替换的能力范围。
2. **被替换掉的动画，其内嵌事件一起消失**。原版移动动画里带的 `FootLeft/FootRight` 脚步声事件随替换没了。对潜行通常是好事，但要知道。
3. **会盖掉同文件名的其他 mod**（本项目里盖掉了 Gunslicer 的潜行弓移动动画）。不想盖就删掉对应的子模块文件夹。
4. **运行时不能物理增删动画文件**，改动只在**重启游戏后**生效（运行时只能在编辑器里禁用 submod）。

---

## 六、怎么查「游戏到底请求哪个文件名」

这是改造的**地基**。三条路，从权威到省事：

### 6.1 权威：读 vanilla 行为文件

行为文件是「事件 → 动画路径」映射的唯一定义处。整合里通常有几份副本，任选：

| 文件 | 能查到什么 |
| --- | --- |
| `…\characters\defaultmale.hkx` | **剪辑生成器 + 完整动画路径列表**（最全的“有哪些动画名”） |
| `…\behaviors\0_master.hkx` | 状态机、**行为图变量名**（如 `bBowDrawn`） |
| `…\behaviors\bow_direction_behavior.hkx` | **方向/移动分支**（含潜行分支，能看出「潜行拉弓移动走哪套」） |

**读法**：hkx 是二进制，但这些路径都是明文字符串。用 Python 提 ASCII 串即可：

```python
import re
data = open(path, 'rb').read()
for s in sorted(set(m.group().decode('ascii') for m in re.finditer(rb'[\x20-\x7e]{6,}', data))):
    if 'Animation' in s:
        print(s)
```

> 本机环境注意：没有 `strings` 二进制，用上面的 Python 方案替代。

### 6.2 交叉验证：看专业动画包怎么分包

**比读二进制更直观的一招**：找一个整合里**已知能用**的专业 OAR 动画包，看它的文件夹划分。

本项目就是靠 `Gunslicer OAR Animations Pack` 的 `Bow` / `Bow_Sneak` 两个文件夹，一眼确认了「站姿弓」和「潜行弓」的完整事件集合——包括那 20 个移动/转身文件该放哪、条件该怎么写。**专业包的分包方式 = vanilla 行为结构的镜像**。

### 6.3 省事：直接读 OAR 日志

**跑一次游戏**，然后看日志（路径见第八节）。日志会把**所有被识别为“有人要替换”的原始动画路径**列出来。等于让 OAR 告诉你「哪些文件名是有效的替换目标」。

日志里还会标注该动画是否会被当作 **interruptible**（有替换项时会话外提示），这能直接印证你的 submod 有没有被扫描到。

---

## 七、hkx 文件的版本判定

**这是最容易踩的坑：看标签是判不出 32/64 位的。**

`hkx` 文件头里那个 `hk_2010.2.0-r1` 标签，**Skyrim LE（32 位）和 SE（64 位）共用**。一个 LE 格式的动画丢进 SE，游戏不会报错，只会**加载失败**（角色摆 T-pose 或该动作不播放）。

**唯一可靠的判定方法：与本机已知可用的 SSE 动画做头部逐字节对比。**

```bash
# 待判定的文件
od -A x -t x1z -N 64 "待判定.hkx"
# 参照物：整合里随便一个确定能用的 OAR 动画（比如 Gunslicer 包里的）
od -A x -t x1z -N 64 "已知可用.hkx"
```

本项目实测的**可用 SSE 文件头**（obito 包 与 Gunslicer 包，`od -A x -t x1z -N 64`，两份**完全一致**）：

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

**判定就看 `0x0C` 那个 4 字节**：`08 00 00 00` = 64 位。32 位（LE）文件此处按社区通行说法是 `04 00 00 00`——**但这一条没有在本机实测过**，所以最稳的判定永远是：

> 拿一个**你确定游戏能正常播放**的 SSE 动画当基准，两份文件逐字节比对；一致就能用。

本项目结论：obito 包的 4 个文件头部与整合内已知可用的 SSE 动画**逐字节一致**（`0x0C = 08 00 00 00`），是原生 64 位格式，**不需要任何转换**，可以直接改名使用。

> 若确实遇到 32 位文件，需要先做 LE → SE 的动画转换（社区常用 CATA / hkxcmd 之类的工具）。**这类转换会重写文件，务必先备份，且转换后的文件要在游戏里实测**。

---

## 八、验证与排错

### 8.1 日志位置

```
C:\Users\<用户名>\Documents\My Games\Skyrim Special Edition\SKSE\OpenAnimationReplacer.log
```

（同目录下还有 `OpenAnimationReplacer-DetectionPlugin.log`，是 Detection Plugin 的。）

日志能回答的问题：

| 想看什么 | 怎么找 |
| --- | --- |
| 我的 submod 有没有被扫描到 | 搜**被替换的原动画路径**是否出现在日志里 |
| 有没有动画加载失败 | 搜 `fail` / `invalid` / `could not` |
| DAR 旧 mod 被转成了什么 | 搜 `Legacy` |
| 有哪些动画会被动态替换 | 搜 `interruptible` —— 日志会列出「原始动画 → 会替换」 |

> **建议**：改完一次就**跑一次游戏再看日志**，比反复猜快得多。日志是唯一能区分「配置没加载」和「配置加载了但条件没命中」的手段。

### 8.2 游戏内编辑器（Shift + O）

| 要确认的事 | 怎么看 |
| --- | --- |
| 条件是否命中 | 选中目标后，每条条件旁的**图标**；部分条件会显示**当前检查到的值** |
| 两个 submod 是否打架 | **替换列表**标签页，按优先级排列，看谁胜出 |
| 条件值到底是多少 | 让那一行显示实时值（例如 `AttackState` 拉满弓时应显示 **Bow drawn**）——**这是最好用的自检开关** |
| 配置写错了没 | 编辑器底部的**警告/错误栏** |

**编辑器三模式**（照抄官方，改造时最常用 Author）：

- **Inspect**：只读；
- **Author**：改动**直接写进 `config.json`**（改 mod 本身用这个）；
- **User**：改动写进 `user.json`，**覆盖 `config.json` 除名字/描述外的一切**，可安全删除（给别人做个性化时用这个，别动原文件）。

### 8.3 症状 → 原因 对照表

| 症状 | 优先排查 |
| --- | --- |
| 动画完全没换 | **文件名是不是游戏请求的那个**（第一节铁律 2）；旧 DAR 结构有没有移走；改动后有没有重启游戏 |
| 动画换了，但某个状态掉回原版 | 那个状态请求的是**另一个文件名**（第一节铁律 3）——最常见的就是“移动掉回原版” |
| 不该换的状态也被换了 | **条件太宽**。逐条收紧（本项目就是靠加 `AttackState` 修掉“没拉弦也冻住”） |
| 角色摆 T-pose / 该动作不播放 | hkx 版本/格式不对（第七节）；路径过长（**完整路径 > 260 字符时 OAR 会读不到**，`OAR-教程.md` FAQ 有说明） |
| 有个随机动画在跟我的抢 | 优先级对比，或收窄条件；同优先级会让编辑器报警告 |
| 改了没生效但日志里有 | 条件没命中——用 Shift+O 看每一条的图标和实时值 |

---

## 九、案例复盘：一次「看起来对、实际无效」的改法

**需求**：让一个站姿专用的拉弓动作包**只在潜行时生效**。

**第一版做法**（错的）：给 `_conditions.txt` 加一条 `AND IsSneaking()`。

```
IsActorBase("Skyrim.esm" | 0x00000007) AND IsSneaking()
```

**结果**：条件语法完全正确、文件也确实被 OAR 读取了——**但在潜行状态下毫无效果**。

**原因**：文件名叫 `Bow_IdleDrawn.HKX`。潜行时游戏请求的是 `SneakBow_IdleDrawn.hkx`。**这个文件在潜行状态下根本不会被请求**，条件再精确也没有被求值的机会。

**正确做法**：把文件名改成 `sneakbow_idledrawn.hkx`（内容不变），条件加上 `IsSneaking`。

**这个案例的教训，就是本文第一节的铁律 2**：

> **「换了没效果」先查文件名，再查条件。**

还有一个附带教训：改完这个包之后，用户会立刻发现「**潜行拉弓一移动姿势就变**」——因为移动是 `SneakWalk_*`，又是**另一个文件名**。所以真正的完整方案必然要**同时抢占移动/转身事件**（本项目最终就是这么做才达成的）。

---

## 十、经验清单（照抄即可）

**动手前**

- [ ] 备份原始条件文件与目录结构。
- [ ] 查 hkx 版本（头部与已知可用的 SSE 动画对比）。
- [ ] 查这个文件名在整合里还有哪些提供者（`find -iname`）。
- [ ] 找一个专业 OAR 动画包做参照物，看它怎么分包、怎么配条件。

**改造中**

- [ ] 文件名 = **目标状态下游戏请求的原始文件名**（站姿一套、潜行一套、移动又是一套）。
- [ ] hkx 内容不要改，只改名/挪位置。
- [ ] 条件**由窄到宽**地给：先写“谁 + 什么状态”，再补“手上有什么”“正在做什么”。
- [ ] 需要「实时切换」就开 `interruptible`（= Constant polling）。
- [ ] 旧 DAR 结构**必须移出 `meshes`**，否则新旧两套同时生效。
- [ ] JSON 不要带 BOM；数值包成 `{"value": N}`；`OR` 的子数组键是 `Conditions`。
- [ ] 不确定字段名就去编辑器改一个设置、再 diff `config.json`。

**改造后**

- [ ] 静态校验：JSON 能解析、文件数对、文件头正确。
- [ ] 跑一次游戏，看 OAR 日志有没有把它识别成“有替换项”。
- [ ] 进游戏用 `Shift + O` 看条件图标与实时值，确认每个状态都按预期走。
- [ ] 心里有数地接受代价：**移动会滑行、内嵌事件会丢、会盖掉同名动画**。
- [ ] 不想要了，删掉对应**子模块文件夹**即可（不用整个卸 mod）。

**改别人的 mod 时的礼仪**

- [ ] 保留原作者署名（mod 级 `config.json` 的 `author` 字段）；
- [ ] 不覆盖原始文件，用新目录/新子模块承载你的改动；
- [ ] 改动记进文档，方便回退。

---

## 附录：本次改造的完整配置

**改造前**（DAR 旧格式，4 个站姿弓动画 + 一行条件）：

```
obito定制拉弓动作\
└─ meshes\actors\character\animations\
   └─ DynamicAnimationReplacer\_CustomConditions\1750000000\
      ├─ _conditions.txt      42 B
      ├─ Bow_DrawLight.HKX    61,728 B
      ├─ bow_drawheavy.HKX    61,728 B
      ├─ Bow_IdleDrawn.HKX    28,208 B
      └─ Bow_Release.HKX     104,784 B
```

**改造后**（现目录名：`F:\download\BaiduNetdiskDownload\obito定制拉弓动作-倒立拉弓-潜行版`；MO2 里的同名已安装副本需同步）：

```
obito定制拉弓动作-倒立拉弓-潜行版\
└─ meshes\actors\character\animations\
   └─ OpenAnimationReplacer\ObitoSneakBow\
      ├─ config.json                      ← mod 级
      ├─ Pose\                            ← 子模块 1：潜行拉弓姿势（静止时）
      │  ├─ config.json   priority 1750000000   interruptible: true
      │  ├─ sneakbow_drawlight.hkx  ← Bow_DrawLight.HKX 的内容
      │  ├─ sneakbow_idledrawn.hkx  ← Bow_IdleDrawn.HKX 的内容
      │  └─ sneakbow_release.hkx    ← Bow_Release.HKX 的内容
      ├─ DrawMove\                        ← 子模块 2：移动时继续「拉弓」
      │  ├─ config.json   priority 1750000010   interruptible: true
      │  └─ 20 个移动/转身 hkx（内容全部 = Bow_DrawLight.HKX）
      ├─ ReleaseMove\                     ← 子模块 3：移动时继续「放箭」
      │  ├─ config.json   priority 1750000020   interruptible: true
      │  └─ 20 个移动/转身 hkx（内容全部 = Bow_Release.HKX）
      └─ HoldMove\                        ← 子模块 4：移动时保持「拉满」姿势
         ├─ config.json   priority 1750000030   interruptible: true
         └─ 20 个移动/转身 hkx（内容全部 = Bow_IdleDrawn.HKX）
```

三个移动子模块共用同一批 20 个文件名：

```
SneakWalk_Forward / FrwrdLeft / FrwrdRight / Left / Right /
          Bckward / BckwrdLeft / BckwrdRight            （8 个）
SneakRun_Forward / FrwrdLeft / FrwrdRight / Left / Right /
         Backward / BckwrdLeft / BckwrdRight            （8 个）
Sneak_TurnLeft60 / TurnLeft180 / TurnRight60 / TurnRight180   （4 个）
```

**四个子模块的条件**：

| 子模块 | 条件 |
| --- | --- |
| `Pose` | 玩家 `AND` 潜行 |
| `DrawMove` | 玩家 `AND` 潜行 `AND` (左手弓 `OR` 右手弓) `AND` `AttackState == 8` |
| `ReleaseMove` | 玩家 `AND` 潜行 `AND` (左手弓 `OR` 右手弓) `AND` `AttackState` ∈ {11, 12, 13, 14} |
| `HoldMove` | 玩家 `AND` 潜行 `AND` (左手弓 `OR` 右手弓) `AND` `AttackState` ∈ {9, 10} |

**决策要点回顾**：

- 拆成多个子模块，是因为 **OAR 里一个 submod 内所有动画共享同一套条件**——条件不同就必须拆。`Pose`（静止）与三个移动子模块条件不同；三个移动子模块之间靠 `AttackState` 的阶段互斥。
- 优先级分层（0030 > 0020 > 0010 > 0000）是兜底：条件本就互斥，但万一状态值有重叠，高优先级胜出更符合直觉。
- `bow_drawheavy` 被废弃：vanilla 潜行弓**没有** `SneakBow_DrawHeavy` 这个事件，潜行时重弓也走 `SneakBow_DrawLight`。
- 早先那条 `IsAttacking` 已删除——它是「拉弓拉到一半移动就跳成拉满姿势」的根因（详见第五节的「进阶技巧」）。

---

## 参考

- 本仓库 `OAR-教程.md` —— OAR 官方文档整理（条件全清单、编辑器、变体、预设、函数、Detection Plugin）
- 本仓库 `obito定制拉弓动作-配置解析.md` —— 本次改造的完整记录与证据出处
- OAR 本体源码：<https://github.com/ersh1/OpenAnimationReplacer>
- OAR（Nexus mod 92109）／Detection Plugin（Nexus mod 104806）

> 本文所有结论均在本机实测或对照 vanilla 行为文件核实；不同整合/OAR 版本下条件枚举与行为结构可能略有差异，以游戏内编辑器显示为准。
