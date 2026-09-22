# 项目长期记忆（skyrim-docs）

## 【入口】知识库怎么被 agent 使用
- 本工作区 = **7 个资料库** + 根目录 `AGENTS.md`（**agent 入口契约，先读它**）。
  `01-navigation` 是**跨库排错索引**：手里是"症状"时先读 `01-navigation/troubleshooting-index.md`。
- 检索一律走 **`scripts/kb.py`**，不要"通读"：
  `list` → `toc <kb>` → `find <kw>` / `grep` → `show <id>`（元数据+大纲）→ `read <id>`。
  调用：`C:/Users/laptopyu/.workbuddy/binaries/python/versions/3.13.12/python.exe scripts/kb.py …`。
- **禁止读 `index.json` / `index.html`**：内联每条正文渲染 HTML（oar-kb 单库 296KB），
  `find` 一次只回 ~1.7KB，差 174 倍。
- **`aliases`**（全部条目已补齐）：`tags` 说"属于什么主题"，`aliases` 说"别人会用什么词来找"。
  `find` 加权：id 100 > 别名精确 60 > tag 40 > 别名模糊 26 > tag 模糊 22 > 标题 20 > 摘要 8。
  写**短查询**、别写整句、别抄 tags。搜索端两条归一化：① 空格不敏感（不必写两遍）；
  ② 中文长串反向包含 → 别名要写**更短的核心说法**。
- **新增库后必须跑 `kb.py check`**（会报出 `AGENTS.md` 漏写的库 = 整个库对 agent 隐形）。
- 结论必须带条目路径引用，并区分一手源 / 社区经验 / 本机实测。

## 资料库的目录与脚本纪律（血泪）
- **条目必须放在带 `NN-` 前缀的分类子目录**。`build_index.py` 跳过**库根层**，
  条目写在库根 → 输出 `0 entries` **却不报错**。库根只放 manifest/index/README/AGENTS.md。
- `category` 必须与目录名**严格相等**；写成短名只表现为"页面标签变空"，不报错。
- 五件套（build_index / validate_kb / check_index_ui / check_links / fix_links）在技能与**各库**
  共 N 份副本，**必须指纹为 1**。规范版在
  `D:\game\上古卷轴5\.workbuddy\skills\build-maintainable-kb\scripts\`（项目级）。
  **改完脚本必须跑 `scripts/sync_scripts.py`**，否则产生隐性分叉。
  sync 按"含 manifest.json 的一级目录"发现库，**不按 `*-kb` 后缀**（否则 `01-navigation` 会漏）。
- **构建器与校验器的收集规则必须逐条对齐**（曾出现"构建收 1 条、校验数 0 条"的假报错）。
- **自检三连**：`build_index` → `validate_kb` → `check_index_ui`；动过条目/目录再加 `check_links`；
  动了脚本再加 `sync_scripts.py --check`。

## 环境
- **git 远程**：`ssh://git@ssh.github.com:443/lambertyu233/skyrim-docs.git`
  （**必须 443 端口**：本机 `HTTP(S)_PROXY=127.0.0.1:7897` 劫持 22 端口，
  表现为 `Connection closed by 198.18.0.59 port 22`；`ssh -p 443 -T git@ssh.github.com` 可验证）。
- **本仓库文本一律 LF**，靠根 `.gitattributes`（`* text=auto eol=lf`）强制。新克隆先确认它在。
- **活动实例 = `D:\game\JIZIYU J5.0`**（mods 约 1627）；`E:\game\JIZIYU Y5.0` 是另一实例（约 1297）。
  查整合/装 mod 一律以 **D 盘**为准。已装 OAR **v2.3.6**。
- OAR 日志：`C:\Users\Lambert\Documents\My Games\Skyrim Special Edition\SKSE\OpenAnimationReplacer.log`。
- 工具坑：Bash 的 PATH 被破坏 → 命令前 `export PATH="/usr/bin:/bin:/c/Windows/System32:$PATH"`；
  **没有 `strings`/`grep` 二进制**，提二进制字符串用托管 Python + `re.finditer(rb"[\x20-\x7e]{6,}", data)`。
  **`python -c` 不可靠**（转义+嵌套引号被静默吞掉）→ 一律把脚本**写成文件**再执行。

## Skyrim 动画事件地图（可复用硬事实）
- 站姿弓：`Bow_DrawLight/Heavy` / `Bow_IdleDrawn` / `Bow_Release`；拉弓中移动 = `BowDrawn_Walk*` + `BowDrawn_Turn60/180`。
- 潜行弓：`SneakBow_DrawLight` / `SneakBow_IdleDrawn` / `SneakBow_Release`（无 `_DrawHeavy`）；
  潜行（含拉弓）移动 = 通用 `SneakWalk_*` / `SneakRun_*` / `Sneak_Turn*` / `SneakMTIdle`。
- 事件名权威来源（vanilla 副本）：`mods\FNIS SE 7.6 XXL\Meshes\actors\character\characters\defaultmale.hkx`、
  `mods\Nemesis Engine 数据\...\behaviors\bow_direction_behavior.hkx`、`...\behaviors\0_master.hkx`。
- hkx 标签 `hk_2010.2.0-r1` **LE/SE 共用**，判版本要与已知可用的 SSE 动画逐字节对比。
- OAR 条件要点：`AttackState` 弓枚举 **8=draw / 9=attached / 10=drawn / 11=releasing / 12~14=released…**；
  **判「弓已拉开」必须用 `AttackState`，绝不能用 `IsAttacking`**（整段弓攻击都为真）；
  `HasGraphVariable` 只能判存在、不能读值；`IsEquippedType` 的 `Type` 7=Bow；
  submod 开 `interruptible: true` = Constant polling（多 submod 按阶段交接时必须开）。
- obito 拉弓 mod：源 `F:\download\BaiduNetdiskDownload\obito定制拉弓动作-倒立拉弓-潜行版`，
  MO2 副本 `D:\game\JIZIYU J5.0\mods\` 同名。**改动画要同时改这两份。**

## 改造别人的动画包（可复用方法论）
1. 文件名 = **目标状态下游戏请求的原始文件名**；「换了没效果」先查文件名，再查条件。
2. hkx 内容不改，只改名 + 挪位置；旧 DAR 目录必须移出 `meshes\`（否则双份生效）。
3. 一个 submod 内所有动画共享同一套条件 ⇒ 条件不同就拆子模块；要实时切换就开 `interruptible`。
4. **让「移动不打断一次性动作」**：按 `AttackState` 阶段拆多个 submod，共用同一批移动事件名、
   各放不同阶段动画，靠 `interruptible` 自动交接。
5. 学 `config.json` 字段最快的办法：Shift+O 作者模式改一个设置 → diff 文件找新增字段。
6. 专业 OAR 包（如 Gunslicer 的 `Bow` / `Bow_Sneak`）= vanilla 行为结构的镜像，是最好的参照物。

## 工具使用教训（跨项目通用）
- **同一文件不要在同一条消息里并行发多个 Edit**：会互相覆盖，只有最后一次落盘，
  但每个都返回 success（静默丢写入）。同文件改多处要串行或改用 Python 脚本替换。
- **站内相对链接的 `../` 层数由目录深度决定**，手写极易错；`validate_kb.py` **完全不查正文链接**
  → 坏链能长期潜伏。改目录结构或批量写条目后**务必跑 `check_links.py`**。
- **无 git 时怎么复盘历史改动**：`index.json` 内联了每条渲染 HTML，若其 mtime 早于某次 md 修改，
  它就是"修改前快照"；按 `_file` 求 `href` 与 `](...)` 差集即可还原那次改动动了哪些链接。
- **生成器脚本写文件必须 `newline="\n"`**：默认文本模式在 Windows 上会把 `\n` **静默**转成 `\r\n`。
  **只归一化产物而不修生成器，下次重跑又会被写回去。**
- **用正则改 frontmatter 不要对 group 偏移做切片**：`m.start()` 指向 `---` 起点（含分隔符），
  而 `m.group(1)` **不含**分隔符 —— 写成
  `text[:m.start()] + new_raw + text[m.start()+len(raw):]` 会**丢掉开头的 `---\n`**，
  同时把原 `raw` 的末 4 字符挤到 `summary` 行末尾。2026-09-22 这样**静默破坏了 33 个条目**，
  构建从 43 条跌到 10 条。**正确写法是拼回完整块**：`"---\n" + new_raw + "\n---\n" + text[m.end():]`。
- **校验不能只查"关键字段是否存在"**：垃圾被追加到**同一行末尾**时，行首/字段存在性检查
  全都抓不到（当时误判成"已是干净的"）。要断言**每个非空行都是合法的 `key: value`**，
  或直接用 `build_index` 的条目数做端到端校验。这也说明技能里那条
  「先逐文件断言锚点恰好命中 1 次、**再逐行比对证明只有目标行变化、字节增量等于替换差值**」
  的纪律，光守住前半句不够。
- **PowerShell 的 `Add-Type` 被本机安全策略禁止**（"compiles and loads .NET code at runtime"）
  → 要调 Win32 API 就改用**托管 Python + ctypes**（如 `shell32.SHFileOperationW` 做回收站删除）。
  ⚠️ 且沙箱下 SHFileOperation 可能返回非 0、`C:\$Recycle.Bin` 里也查不到条目 ——
  **动用户目录的文件，备份必须自己做，别把回收站当保险。**

## 已有的库（现状）
- `01-navigation`：跨库排错索引（症状 → 条目路径 + 最易误判的分叉点）。
- `oar-kb`（33 条 / 10 类）：OAR 官方口径来自 Nexus 描述 + **源码** + 作者 Patreon。
  三条核实结论：① OAR **确实没有 wiki**；② 从 `src/Conditions.h` 抽 `GetName()` 得 **125 个条件名**，
  与官方清单逐条比对无遗漏；③ **`IsPlayer` 条件不存在**（Detection 页面示例是文档笔误）。
  `09-sources/unreliable-sources.md` 逐条取证 CSDN 的 **12 处编造**。
- `behaviour-engine-kb`（28 条 / 8 类）：Havok Behavior = 非确定性有限状态机；序列化进 hkx 包；
  **Patcher（FNIS/Nemesis/Pandora，新增动画）vs Replacer（OAR/DAR，替换已有）是两类**；
  FNIS 7.6 闭源停更、Nemesis 中级以上无公开文档、Pandora v4.4.0-beta 支持全生物；
  **Pandora 不是 Nemesis 的 fork**（社区常错）。
- `community-shaders-kb`（2.1.0，7 类，64 条）：稳定 **1.8.x**、开发 1.9.0；**Nexus 是唯一受支持渠道**；
  支持 1.6.1170 / 1.6.1179 / 1.5.97，**1.6.640 / 1.7.99 / 1.7.104 不支持**；GPU 口径 **Vulkan 1.4+**；
  **VR 停止支持**；Upscaling 不支持 XeSS；帧生成仅 ≥120Hz。**进阶资料在 GitHub Developer Wiki**。
  已精修 15 个功能条目，其余 32 个仍是摘要级。
- `creation-kit-kb`、`mo2-usvfs-kb`：均已换成 stock 脚本与 stock manifest，
  私有功能（`CATS`、status 徽章、状态过滤等）已移除；`kind`/`status` 仍作数据保留。
- `character-appearance-kb`（2026-09-22 新建，v1.1.0）：**捏脸与身形资料库**（**44 条 / 9 类**：
  总览 / 前置 / 脸 / 身形 / 骨骼物理 / NPC 分配 / 排错 / 安装实务 / 来源）。
  来源为 Nexus 发布页描述正文、GitHub 官方仓库、UESP 与 Creation Kit wiki（API 抓取）。
  **问"身型原理 / 为什么拖滑块衣服跟着变 / 为什么换预设就穿模"只读一条**：
  `03-body/morph-runtime-vs-bake.md` —— 它给出**运行时 morph（不改文件、只影响玩家）
  vs 离线烘焙（写进 .nif 顶点、影响所有 NPC）**这条主线，以及
  `Zeroed Sliders + Build Morphs + Batch Build` 的正解工作流。
  **最重要的产出是 `08-sources/unreliable-and-unconfirmed.md`**：逐条列出 **13 条已知错误知识**
  （RaceMenu 不需要 PapyrusUtil、BodySlide 无 `-o`/`-m`、HPH 作者是 KouLeifoh 不是 Kalilies、
  `modding.wiki` 不托管 STEP、HDT-SMP 仓库名是 `hdt-skyrimse-mods`、
  Skyrim Outfit System 不是身形分配工具、SPID 分的是服装、Eyes of Beauty SE 版本是 1.2、
  CBPC 管不了头发衣服、九大猫/醉梦/陶德查无实据、
  RaceMenu 滑块不是 -1~+1、BodySlide 预设不能当 RaceMenu 预设用、拖滑块改不了 NPC 身材）
  与 **17 项未确认事项**。
- 各库（现 7 个）的 stock 脚本行为要点：页头标题/副标题**从 manifest 注入**（`kb.description` 里别再重复写
  `source_name` 那句）；正文开头的 `# H1` 会被 `_strip_leading_h1()` 剥掉。
- 索引页侧栏交互（2026-09-22 改造）：**两个把手共用同一个 `.navfab` 外形**（26×58 右半圆
  `border-radius:0 30px 30px 0`、白底蓝字、hover 实心蓝、`position:fixed;top:50%` 垂直居中）：
  展开态 `#navtoggle`（‹）贴**侧栏右缘** `left:230px`；收起态 `#navfab`（›）贴**视口左缘** `left:0`，
  只有 `.navfab.show` 才 `display:flex`。**收起 = 整条消失**（`aside.collapsed{display:none}`，
  旧的「收窄到 78px 窄条」已废弃），配 `aside.collapsed + main{padding-left:44px}` 给正文让位。
  ⚠️ `#navtoggle` **必须留在 `<aside>` 的 DOM 子树内**（只用 `fixed` 把位置挪到侧栏右缘）：
  ① 收起时它随 `aside{display:none}` **自动隐藏**，不需要额外 JS；
  ② `check_index_ui.py` 只**静态解析 `<aside>` 内的 button**，把它移到 `</aside>` 之外就取不到元素 → 断言会假失败。
  `check_index_ui.py` 覆盖 `.collapsed` / `.show` / 两个把手同 class / localStorage；
  `validate_kb.py` 的 `REQUIRED_PAGE_IDS` 已含 `navfab`（缺它 = 模板回退到旧版）。
  ⚠️ 该脚本把页面 `<script>` 与断言段**拼成同一个文件**执行，顶层变量重名会直接 `SyntaxError`
  → 页面里绑定 `#navfab` 用 IIFE 包住局部变量。
- `category` 必须与所在目录名严格相等 —— 宽容校验比没有校验更危险（曾放过 47 个 `category: features`）。
- 改资料库页面一律改 `scripts\build_index.py` 的模板再重建，**不要手改 `index.html`**。
- **技能是项目级**（`D:\game\上古卷轴5\.workbuddy\skills\build-maintainable-kb\`；用户 2026-09-22
  明确选择**不**复制到用户级，避免两份 stock 副本互相分叉）。技能 `scripts/` 就是 stock 源：
  **新建库时从那里复制五件套**（索引页模板即 `build_index.py` 的 `HTML_TEMPLATE`），新库自动继承当前 UI。
- **技能的 `scripts/selftest_new_kb.py`**：在系统 temp 里从零造一个最小库并断言它继承了当前索引页 UI
  （两个半圆把手、旧样式零残留、全 LF），**跑完即删、不碰真实库** —— 新建库后、或改过索引页模板后跑一次；
  给索引页加新特性时顺手在里面补一条断言（这是"新库会不会继承"的唯一自动化保障）。
- 已删除的 `~/.workbuddy/skills/_t_kb/`（旧的试渲染测试库，含一份过期的 `build_index.py`，易被误抄）；
  备份仍在 `%TEMP%\_t_kb-backup-20260922-112233\`。
