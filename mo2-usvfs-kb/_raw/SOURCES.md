# 来源存档（_raw，索引构建会忽略）

本目录用于保存上游原文 / 抓取摘要，便于后续同步。索引脚本不扫描本目录。

## 已参考的来源与关键事实

### 1. USVFS GitHub README — https://github.com/ModOrganizer2/usvfs
- 官方定义：让 Windows 程序创建只对选定进程可见的文件/目录链接；靠 API hooking 骗过文件访问函数，打开"其实在别处"的文件。
- 当前 alpha，核心组件 of MO2，GPLv3。
- 对比 NTFS 符号链接：进程可见(否→仅选定进程)、会话结束消失、不需目标写权限、不需管理员、跨文件系统(FAT32/只读/网络)、多目录 overlay、虚拟 unlink(隐藏/替换)。
- 代价：CPU/内存开销、仅初始化阶段激活(依赖 DLL 可能错过)、新 bug 源、杀软误报。

### 2. MO2 Wiki - Debugging usvfs — https://github.com/ModOrganizer2/modorganizer/wiki/Debugging-usvfs
- 日志格式：timestamp <pid:tid> [L] message [param]...
- 所有 hook 以 `hook_` 开头并含原函数名（如 hook_GetFileAttributesW）。
- 字段：lpFileName=原始路径；reroute.fileName()=重定向后真实路径；res / originalError / fixedError。
- DeleteFile() 未重定向时不打日志。
- spawn_delay 设置（INI [Settings] spawn_delay=X 秒）；Process Monitor；Visual Studio attach + Child Process Debugging Power Tool。

### 3. STEP Mod Organizer 指南 — https://stepmodifications.org/wiki/Guide:Mod_Organizer
- 完整 wikitext 已抓取存档：`_raw/Guide_Mod_Organizer.wiki.txt`（约 156 KB，经 `scripts/fetch_mediawiki.py --api https://stepmodifications.org/wiki/api.php "Guide:Mod_Organizer"`）。
- VFS 在运行时部署 mod，保持游戏真实文件系统完整。
- 特性：多游戏、mod 隔离、profile、加载顺序、冲突解决、BSA 解包、Nexus 集成、BAIN/FOMOD、存档查看器、归档失效、分类。
- 第 14 章 Priorities / 14.1 Conflict Resolution（含 BSA Priorities）；第 16 章 Overwrite（What is / How files end up / Maintaining a Clean Overwrite）。
- 使用与运维章节要点（1.1.0 据此新增 21 条 05-usage 条目）：安装与首次启动（先跑一次游戏/portable vs instanced）、工具栏与左右窗格（Flags 图例）、安装四途径与 Mod Exists（Merge/Replace/Rename/Keep Backup）、Simple/BAIN/FOMOD/手动安装、更新与卸载、启用与插件激活（备份/恢复、Lock load order、Sort=LOOT）、下载与 meta/Query Info/nxmhandler、Modify Executables 字段与自动识别清单、工具配方（LOOT/xEdit/Wrye Bash/FNIS/SkyProc/SKSE/CK/BodySlide/SBW/FCXE）、快捷方式与 profile 专属快捷方式、分类（categories.dat）、筛选与分组、Filetree 与 `.mohidden`、BSA 管理与 Unmanaged/Back-date BSAs、Saves 与 Fix Mods、备份恢复、警告与潜在 mod 顺序、INI 与 ini tweaks、Settings 四页、Load Mechanism 与 Steam AppID、插件三类与黑名单、FAQ。
- 关键数值（勿凭记忆改写）：Steam AppID —— Skyrim 72850 / FONV 22380 / FO3 22300（GOTY 22370）/ Oblivion 22330 / Skyrim CK 202480；实例数据目录 `%LocalAppData%/ModOrganizer`；分类文件 `categories.dat`。

### 4. DeepWiki - ModOrganizer2/modorganizer — https://deepwiki.com/ModOrganizer2/modorganizer
- VFS 节点类：DirectoryEntry(src/shared/directoryentry.h)、FileEntry(src/shared/fileentry.h)、FilesOrigin(src/shared/filesorigin.h)、FileRegister(src/shared/fileregister.h)、VirtualFileTree(src/core/virtualfiletree.h)。
- DirectoryRefresher：mod 变动时后台多线程重建虚拟文件树（src/CMakeLists.txt:296）。
- ModInfo 层次：ModInfoRegular / ModInfoForeign / ModInfoOverwrite / ModInfoSeparator / ModInfoBackup。

### 5. MO2 Wiki - Troubleshooting — https://github.com/ModOrganizer2/modorganizer/wiki/Troubleshooting
- USVFS hook 被杀软误判；需把整个 MO2 目录加排除（Acronis/Avast/Bitdefender/Malwarebytes/VIPRE/Windows Defender）。
- Windows Event Log 服务异常会妨碍 hook LOOT/Wrye Bash/xEdit；清空系统日志后须真正重启。

### 6. MO2 Wiki - HVCI/USVFS — https://github.com/ModOrganizer2/modorganizer/wiki/Disabling-Hardware-enforced-Stack-Protection-to-run-protected-executables-through-USVFS
- Hardware-enforced Stack Protection (Intel CET / AMD Shadow Stack) 可阻止受保护 exe 经 usvfs 运行。
- 用户侧：Windows 安全中心 → 漏洞利用保护 → 程序设置 → 关闭该 exe 的硬件强制栈保护。
- 开发者侧：/CETCOMPAT:NO 或 .NET <CETCompat>false</CETCompat>。
