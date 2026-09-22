# 项目长期记忆（skyrim-docs）

## 入口与纪律
- 工作区 = 8 个资料库 + 根 `AGENTS.md`（**agent 入口契约，先读**）。症状类先读
  `01-navigation/troubleshooting-index.md`。**新增库后必跑 `kb.py check`**（漏写 AGENTS.md = 整库对 agent 隐形）。
- 检索走 `scripts/kb.py`：`list → toc → find/grep → show（元数据+大纲）→ read`；
  Python 用 `C:/Users/laptopyu/.workbuddy/binaries/python/versions/3.13.12/python.exe`。
  **禁止读 `index.json`/`index.html`**（内联全库正文，比 `find` 一次大百倍）。
- `aliases` 写"别人会敲的**短查询**"（英文术语/俗称/错拼/上级词），不写整句、不抄 tags。
  `find` 加权：id 100 > 别名精确 60 > tag 40 > 别名模糊 26 > tag 模糊 22 > 标题 20 > 摘要 8。
  查询端**三条归一化**：空格不敏感；**大小写不敏感** → **绝不写 `DynDOLOD`+`dyndolod` 这类变体**
  （find 端冗余，validate 端报 repeated aliases **ERROR**）；中文长串反向包含 → 别名取**更短的核心说法**。
- 交叉引用写 **markdown 相对链接**（同库 `../NN-cat/x.md`，跨库 `../../other-kb/NN-cat/x.md`）。
  **反引号纯文本引用是 `check_links.py` 的盲区** → 报"0 条 / 全部有效"的**空跑假通过**；
  批量修补：技能 `scripts/linkify_refs.py <kb-dir> [--apply]`。
- 条目**必须放带 `NN-` 前缀的分类子目录**（放库根 → `0 entries` 却不报错）；
  `category` 必须与目录名**严格相等**（写短名 = 页面标签变空，不报错）。
- 五件套（build_index/validate_kb/check_index_ui/check_links/fix_links）stock 版在
  `.workbuddy/skills/build-maintainable-kb/scripts/`，各库是副本，**改完必须跑 `sync_scripts.py`**
  （按"含 manifest.json 的一级目录"发现库，不按 `*-kb` 后缀）。技能另有**不同步**工具：
  `linkify_refs.py` / `fix_aliases.py` / `selftest_new_kb.py`。
- 自检：`build_index` → `validate_kb` → `check_index_ui`；动过条目/目录加 `check_links`；
  动过脚本加 `sync_scripts.py --check`。结论必带条目路径，区分 一手源/社区经验/本机实测。

## 环境
- git：`ssh://git@ssh.github.com:443/lambertyu233/skyrim-docs.git`（**必须 443 端口**：本机代理劫持 22，
  报 `Connection closed by 198.18.0.59 port 22`）。文本一律 LF，靠根 `.gitattributes`。
- **活动实例 = `D:\game\JIZIYU J5.0`**（mods 约 1627，OAR v2.3.6）；`E:\game\JIZIYU Y5.0` 是另一实例。
  OAR 日志 `C:\Users\Lambert\Documents\My Games\Skyrim Special Edition\SKSE\OpenAnimationReplacer.log`。
- 工具坑：Bash PATH 被破坏 → 前置 `export PATH="/usr/bin:/bin:/c/Windows/System32:$PATH"`；
  无 `strings`/`grep` 二进制；**`python -c` 不可靠 → 一律写成脚本文件再跑**。

## 动画改造项目（事实全在库中，此处只留指针与项目约定）
- 权威条目（**不要在此重复以下事实**）：`oar-kb/08-practices/animation-key-model.md`（弓箭事件名表、
  `AttackState` 弓枚举、`hk_2010.2.0-r1` **LE/SE 共用**、判"弓已拉开"必须用 `AttackState` 而非
  `IsAttacking`、hkx 权威来源文件）+ `oar-kb/08-practices/authoring-workflow.md`（改造流程）。
- 项目约定：obito 拉弓 mod 有**两份**——源
  `F:\download\BaiduNetdiskDownload\obito定制拉弓动作-倒立拉弓-潜行版` 与 MO2 副本
  `D:\game\JIZIYU J5.0\mods\` 同名，**改动画必须同时改这两份**。

## 工具教训（跨项目通用）
> **详细条目已归到技能里**：`.workbuddy/skills/build-maintainable-kb/SKILL.md` 的
> 「环境坑（实战踩过）」与「注意事项」两节 —— 改 frontmatter 的切片陷阱、并行 Edit 互相覆盖、
> 「等长占位」必失效、校验不能只查字段存在性、生成器必须 `newline=""`、坏链不会报错等。
> **要补/查这些教训就去技能里改，不要在这里重复。**
- 本机特有：**PowerShell `Add-Type` 被安全策略禁止** → 调 Win32 API 用托管 Python + ctypes；
  沙箱下回收站不可靠，**动用户目录的文件备份必须自己做**。

## 已有库（8 库 / 309 条）
- `01-navigation`（1）：跨库排错索引（症状 → 条目路径 + 最易误判的分叉点）。
- `skyrim-tools-kb`（67 / 13 类，2026-09-22 新建）：模改**工具链**。硬事实：SKSE64 与本体
  **精确版本对应**（1.5.97→2.0.20 / 1.6.640→2.2.3 / 1.6.1170→2.2.6）、Address Library
  **SE/AE 二选一**装错静默失效、**LOOT 只管插件顺序不管资源覆盖**、**ESL 有记录数容量前提**。
  最重要产出 `12-sources/common-misconceptions.md`（**18 条错误认知**）与
  `12-sources/unreliable-sources.md`。来源纪律：只用官方 wiki / 官方仓库 / Nexus 发布页 /
  一手文档，**排除 CSDN、toolify 等内容农场与聚合站**。
- `oar-kb`（33 / 10）：**OAR 没有 wiki**；从 `src/Conditions.h` 抽 `GetName()` 得 **125 个条件名**；
  **`IsPlayer` 条件不存在**。`09-sources/unreliable-sources.md` 取证 CSDN **12 处编造**。
- `behaviour-engine-kb`（28 / 8）：Havok Behavior = 非确定性 FSM，序列化进 hkx；
  **Patcher（FNIS/Nemesis/Pandora，新增）vs Replacer（OAR/DAR，替换）**；FNIS 7.6 闭源停更；
  **Pandora 不是 Nemesis 的 fork**（社区常错）。
- `community-shaders-kb`（64 / 7）：稳定 1.8.x；**Nexus 是唯一受支持渠道**；
  1.6.1170 / 1.6.1179 / 1.5.97 支持；GPU 口径 **Vulkan 1.4+**；VR 停止支持；进阶看 GitHub Developer Wiki。
- `character-appearance-kb`（44 / 9）：核心 `03-body/morph-runtime-vs-bake.md`（**运行时 morph 只影响玩家
  vs 离线烘焙写进 .nif 影响所有 NPC**；正解 `Zeroed Sliders + Build Morphs + Batch Build`）；
  产出 `08-sources/unreliable-and-unconfirmed.md`（**13 条错误知识 + 17 项未确认**）。
- `creation-kit-kb`（29）、`mo2-usvfs-kb`（43）：已统一到 stock 脚本与 stock manifest。

## 索引页 UI（细节以 `build_index.py` 模板 + `check_index_ui.py` 断言为准）
- **改页面一律改 `build_index.py` 模板再重建，别手改 `index.html`**；标题/副标题从 `manifest.kb` 注入，
  正文开头 `# H1` 会被剥掉。收起态是**整条消失**（`aside.collapsed{display:none}`），不是窄条。
- ⚠️ `#navtoggle` **必须留在 `<aside>` DOM 子树内**（`check_index_ui.py` 只静态解析 `<aside>` 内 button，
  移出去会**假失败**）。⚠️ 该脚本把页面 `<script>` 与断言段拼成同一文件执行 → 顶层变量重名 `SyntaxError`。
- 技能是**项目级**（2026-09-22 用户明确不复制到用户级，避免两份 stock 分叉）。
