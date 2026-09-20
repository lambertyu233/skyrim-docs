# 项目长期记忆（skyrim-docs）

## 环境
- **活动实例 = `D:\game\JIZIYU J5.0`**（mods 约 1627，obito 拉弓动作已装于此）；`E:\game\JIZIYU Y5.0` 是另一个实例（mods 约 1297）。查整合/装 mod 一律以 **D 盘**为准，判据是 OAR 日志里的游戏路径。
- 已装 `OAR动作框架-Open Animation Replacer`（**v2.3.6**，条件名单与版本新增信息全文写在它的 `meta.ini` 里）。
- OAR 日志：`C:\Users\Lambert\Documents\My Games\Skyrim Special Edition\SKSE\OpenAnimationReplacer.log`（同目录另有 `-DetectionPlugin.log`）。排错必看：搜被替换的原动画路径判断 submod 是否被扫描到。
- 工具坑：本机 Bash 的 PATH 被破坏，命令前须 `export PATH="/usr/bin:/bin:$PATH"`；且**没有 `strings`/`grep` 二进制** → 提二进制字符串用托管 Python：
  `C:\Users\Lambert\.workbuddy\binaries\python\versions\3.13.12\python.exe` + `re.finditer(rb"[\x20-\x7e]{6,}", data)`。

## Skyrim 动画事件地图（可复用的硬事实）
- 站姿弓：`Bow_DrawLight` / `Bow_DrawHeavy` / `Bow_IdleDrawn` / `Bow_Release`；站姿拉弓中移动 = `BowDrawn_Walk*` + `BowDrawn_Turn60/180`。
- 潜行弓：`SneakBow_DrawLight` / `SneakBow_IdleDrawn` / `SneakBow_Release`（无 SneakBow_DrawHeavy）；潜行（含拉弓）移动 = 通用 `SneakWalk_*` / `SneakRun_*` / `Sneak_Turn*` / `SneakMTIdle`。
- 挖事件名的权威来源（vanilla，整合内有副本）：
  - `mods\FNIS SE 7.6 XXL\Meshes\actors\character\characters\defaultmale.hkx`（剪辑生成器 + 动画路径列表）
  - `mods\Nemesis Engine 数据\meshes\actors\character\behaviors\bow_direction_behavior.hkx`（方向/移动行为，含潜行分支）
  - `mods\FNIS SE 7.6 XXL\Meshes\actors\character\behaviors\0_master.hkx`（行为图变量名，如 `bBowDrawn`）
- hkx 格式：标签 `hk_2010.2.0-r1` **LE/SE 共用**，判版本要和整合内已知可用的 SSE 动画做头部逐字节对比。
- OAR 条件要点：`AttackState` 弓专用枚举 **8=Bow draw / 9=Bow attached / 10=Bow drawn / 11=Bow releasing / 12~14=released/next attack/follow through**；**判「弓已拉开」必须用 `AttackState`，绝不能用 `IsAttacking`**（它在整段弓攻击过程都为真，会导致「拉弓一半移动就跳成拉满姿势」）；`HasGraphVariable` 只能判变量是否存在，不能读值；`IsEquippedType` 的 `Type` 值 7=Bow，左右手用 `"Left hand": true/false`；submod 开 `interruptible: true` 即启用 Constant polling（条件变化立刻换动画，**多 submod 按阶段交接时必须开**）。
- 权威 JSON 写法样例：`mods\女性动作补充包Gunslicer OAR Animations Pack\...\Bow_Sneak\config.json`（mod 级 + 子模块级两层 config.json）、`mods\动态闪避射击 Dynamic Dodge Shot\...\Sneak Bow Dodge Right\config.json`（AttackState 用法）。
- obito 拉弓动作 mod 的位置：源 `F:\download\BaiduNetdiskDownload\obito定制拉弓动作-倒立拉弓-潜行版`，MO2 已安装副本 `D:\game\JIZIYU J5.0\mods\` 同名。**改动画要同时改这两份**。

## 本项目产物
- `OAR\OAR-教程.md`：OAR 通用教程（官方文档整理）。
- `OAR\OAR-补充文档.md`：**改造实战补充**——替换的心智模型（键=路径+文件名，一个事件=一个文件）、DAR/OAR 目录对照、优先级三来源、条件文本/JSON 双语法、六步改造法、**进阶技巧：用 AttackState 按动作阶段拆分移动接管**、行为文件查事件名、hkx 版本判定、排错对照表、经验清单。

## 改造别人的动画包（可复用方法论）
1. 文件名 = **目标状态下游戏请求的原始文件名**（站姿/潜行/移动是三套事件名）；「换了没效果」先查文件名，再查条件。
2. hkx 内容不改，只改名 + 挪位置；旧 DAR 目录必须移出 `meshes\`（否则与 OAR 原生结构双份生效）。
3. 一个 submod 内所有动画共享同一套条件 ⇒ 条件不同就拆成多个子模块；需要实时切换就开 `interruptible: true`。
4. **想让「移动不打断一次性动作」**：按 `AttackState` 阶段拆成多个 submod，共用同一批移动事件名、各放不同阶段动画，靠 `interruptible` 自动交接。
5. 学 `config.json` 字段名最快的办法：Shift+O 作者模式改一个设置 → diff 文件找新增字段。
6. 专业 OAR 动画包（如 Gunslicer 的 `Bow` / `Bow_Sneak`）的分包方式 = vanilla 行为结构的镜像，是最好的参照物。
