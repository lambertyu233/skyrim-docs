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
- `behaviour-engine-kb\`：**FNIS / Nemesis / Pandora 动作引擎资料库**（28 条目 / 8 分类，见 `index.html` 离线浏览器）。要点：Havok Behavior = 非确定性有限状态机中间件、序列化进 hkx 包；**Patcher（引擎，新增动画命令）vs Replacer（OAR/DAR，按条件替换已有动画）是两类**；FNIS 7.6 闭源停更、Nemesis 中级以上无公开文档、Pandora v4.4.0-beta 全生物支持且兼容两者补丁格式；**Pandora 不是 Nemesis 的 fork**（社区常错）。源存档在 `_raw\`，含 fore 2012 一手帖（hkx 只是包格式，连骨骼也压里面）与 scorrp10 的动画数据库解释。维护：`scripts\build_index.py` + `scripts\validate_kb.py`。
  - `index.html` 已升到 1.0.2：修掉「分类过滤选不了全部」（`全部` 按钮漏绑 onclick 的老 bug）、加了分类过滤收起/展开（localStorage 记忆）、去掉详情页冗余 tip；1.0.2 把脚本对齐到技能 stock 版。
- **四个资料库（behaviour-engine-kb / community-shaders-kb / creation-kit-kb / mo2-usvfs-kb）的 `build_index.py` + `validate_kb.py` + `check_index_ui.py` 三件套，已全部与技能 stock 版逐字节相同**（规范版在 `~/.workbuddy/skills/build-maintainable-kb/scripts/`）。**2026-09-21 完成全库对齐，不再有任何分叉。**
  - `community-shaders-kb` 与 `creation-kit-kb` 都按维护者要求**整体换成 stock 脚本**，各自私有功能（`CATS` 数组、`category_label`/`path` 字段、status 徽章与 `.b-*` 样式、侧栏「状态过滤」、硬编码页头标题）已全部移除；两者的 `manifest.json` 也转成 stock 形状（`kb.{name,description,locale}` + `schema` + `categories[].dir/title/desc` + `version/generated_at/sources/tooling`）。**条目正文与 frontmatter 一字未改**，旧脚本与旧 manifest 备份在各自 `_raw/legacy-*-2026-09-21/`。
  - frontmatter 的 `kind`/`status` 仍作为**数据保留**（照常写进 `index.json`），只是页面不再呈现徽章；`gen_features.py`（生成器）与 `fetch_*.py`（上游抓取）作为遗留工具保留。
  - stock 脚本两个行为要点：页头标题/副标题**从 manifest 注入**（`kb.description` 里别再重复写 `source_name` 那句，否则副标题重复）；正文开头的 `# H1` 会被 `_strip_leading_h1()` 剥掉（详情面板已单独显示标题）。
- 四库都有完整**五件套**：`build_index.py` + `validate_kb.py`（结构+索引+模板校验）+ `check_index_ui.py`（索引页交互回归，Node + DOM 桩、不需要浏览器）+ `check_links.py`（站内相对链接 lint，附带换行提示）+ `fix_links.py`（修链）。**这 5 个脚本在技能与四库中共 20 份副本、每个脚本指纹数均为 1（逐字节同源）**。改完模板必须重建并跑 validate + check_ui；**动过条目或目录后必须加跑 check_links**。
- **`category` 必须与所在目录名严格相等**（如 `02-features`）。`build_index.py` 是拿 frontmatter 的 `category` 去 `CAT_LABELS` 查中文标签的，写成 `features` 这类短名会**静默**变成空标签。2026-09-21 发现 community-shaders-kb 的 47 个功能条目真的写错了，已修正；同时把 `validate_kb.py` 里「允许省略 `NN-` 前缀」的宽容校验改成严格相等，并新增「每个有条目的目录必须在 `manifest.categories[].dir` 里声明过」的交叉校验。**宽容校验比没有校验更危险。**
- 改资料库页面一律改 `scripts\build_index.py` 的模板再重建，**不要手改 `index.html`**。

## 改造别人的动画包（可复用方法论）
1. 文件名 = **目标状态下游戏请求的原始文件名**（站姿/潜行/移动是三套事件名）；「换了没效果」先查文件名，再查条件。
2. hkx 内容不改，只改名 + 挪位置；旧 DAR 目录必须移出 `meshes\`（否则与 OAR 原生结构双份生效）。
3. 一个 submod 内所有动画共享同一套条件 ⇒ 条件不同就拆成多个子模块；需要实时切换就开 `interruptible: true`。
4. **想让「移动不打断一次性动作」**：按 `AttackState` 阶段拆成多个 submod，共用同一批移动事件名、各放不同阶段动画，靠 `interruptible` 自动交接。
5. 学 `config.json` 字段名最快的办法：Shift+O 作者模式改一个设置 → diff 文件找新增字段。
6. 专业 OAR 动画包（如 Gunslicer 的 `Bow` / `Bow_Sneak`）的分包方式 = vanilla 行为结构的镜像，是最好的参照物。


## 工具使用教训（跨项目通用，务必遵守）
- **同一文件不要在同一条消息里并行发多个 Edit**：会互相覆盖，只有最后一次落盘，但每个都返回 success（静默丢写入）。改同一文件要**串行**发 Edit；不同文件可以并行。改完用 grep 抽查关键标记。
- **站内相对链接的 `../` 层数由目录深度决定**，手写极易错（`02-features/core/x.md` 引根目录要 `../../`）。`validate_kb.py` 只查 frontmatter 与索引，**完全不查正文链接** → 坏链能长期潜伏。**改目录结构或批量写条目后务必跑 `check_links.py`。**
- 本机 Bash 的 PATH 被破坏，命令前须 `export PATH="/usr/bin:/bin:$PATH"`。托管 Python：`C:/Users/laptopyu/.workbuddy/binaries/python/versions/3.13.12/python.exe`。
- **无 git 的库怎么复盘历史改动**：`index.json` **内联了每条渲染后的 HTML 正文**；若它的 mtime 早于某次 md 修改，它就是天然的「修改前快照」。做法：按 `_file` 把快照里的 `href="..."` 与当前 md 的 `](...)` 求差集，即可还原那次改动动了哪些链接。本次据此算出三库共修 **61 处**坏链（先前口头报的 31/31 是错的）。**mtime 也能佐证**：三库 15:38 被改动的 md 文件数（1/15/19）与差集算出的文件数完全吻合。
- **生成器脚本写文件必须 `newline="\n"`**：默认文本模式在 Windows 上会把 `\n` **静默**转成 `\r\n`。creation-kit 的 `gen_features.py` 就这样产出了 4 个 CRLF 条目。**只归一化产物而不修生成器，下次重跑又会被写回去。**

## community-shaders-kb 现状（2.1.0，2026-09-21）
- 分类 7 个：`00-overview` / `01-installation` / `02-features` / `03-reference` / `04-development` / `05-tools` / **`06-community`（本版新增）**。共 64 条目。
- 已精修 **15 个**功能条目（含工作原理/参数/需求/兼容/贡献者）：cloud-shadows、dynamic-cubemaps、extended-materials、extended-translucency、grass-collision、grass-lighting、inverse-square-lighting、light-limit-fix、screen-space-shadows、sky-sync、subsurface-scattering、terrain-shadows、water-effects、skylighting、upscaling。**其余 32 个仍是摘要级**（官方只给一句话，下轮应从 Nexus 各附加 MOD 页取材）。
- **脚本五件套**：`build_index.py` / `validate_kb.py` / `check_index_ui.py` / `check_links.py` / `fix_links.py` —— 已于 2026-09-21 **全部进技能 stock 版并推广到四库**（此前的「待办」已完成，无残留分叉）。
- `gen_features.py` 已降级为脚手架：**默认跳过已存在文件**，需 `--force` 才重写；**不要误跑**，否则 15 个精修条目会退回模板。它仍用文本模式 `open(path,"w",encoding="utf-8")` 写文件（Windows 上会产出 CRLF），且仍写 `category: features`（2.0.0 修掉的老坑）——**下次动它要一并修**。
- 全部 md 换行已统一为 **LF**（2.1.0 归一 35 个文件）。

## Community Shaders 硬事实（上游口径，2026-09）
- 版本：稳定 **1.8.x**（1.8.4 = 2026-08-26）；开发 **1.9.0**（2026-09-20 PR 构建）。**Nexus 是唯一受支持渠道**。
- 支持游戏版本：**1.6.1170(Steam) / 1.6.1179(GOG) / 1.5.97**；1.6.640、1.7.99、1.7.104 均不支持；除 1.5.97 外无 LTS。GPU 口径 **Vulkan 1.4+**。
- **VR 停止支持** → Open Shaders；**Linux 不官方支持** → Fluorine。
- **Upscaling 不支持 XeSS**；**帧生成仅 ≥120Hz**，需 Windowed/Borderless。
- **进阶资料在 GitHub Developer Wiki**（`community-shaders/skyrim-community-shaders/wiki`）：全功能 CS/ENB/VR 对照矩阵、A/B 测试、`TESTCUBEMAP`/`LLFDEBUG`。用户 wiki 上没有这些。
