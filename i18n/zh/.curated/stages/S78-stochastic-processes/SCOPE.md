# S78 随机过程：范围与门禁

- 启动日期：2026-10-03（UTC）；作者仅在独立 worktree 本地写作。
- 唯一英文源 commit：`1bafaa88bb4668356791150bec3a6d7df38387eb`。
- 源路径：`phases/01-math-foundations/22-stochastic-processes/docs/en.md`（461 行）；SHA256 `c0c39f418206fc6ff14a9755bd9663147c3ab4b2f35beb03edd909c746ee3fc8`。
- 目标路径：`i18n/zh/phases/01-math-foundations/22-stochastic-processes/docs/zh.md`。
- 已完整阅读代码：`phases/01-math-foundations/22-stochastic-processes/code/stochastic.py`（278 行）；SHA256 `55423be8d4f037f431c00bc5dba886703794d30bb728f3dd93f0e40a497efc9e`。仅导入 NumPy，没有本地导入。
- 先修条件：源要求 Phase 1 Lessons 06–07；对应已接受 S09 概率与 S10 Bayes，术语锁定记录分别在 DEPENDENCIES.json 中固定至 `c50b75b631ed51798040328ea9cfbcaa1d9f3fbf` 与 `c40a71e39637472f687acd8a317b6305767b6fb6`。不借用同波未接受课；正式95索引由协调者双读并授权本次启动。
- 本 stage 的 `DEPENDENCIES.json` 恰为83个不可变 path/commit/SHA256 pin，包含 S69 与最终 S72/S74/S75/S76，排除待审 S61/S66/S73。启动时逐一核对工作 bytes 和 Git bytes；最终再核。
- 新译仅来自固定英文全文；不读取旧中文、缓存、上游452/457或其他作者稿；既有中文仅用已接受术语。三件00-04样例仅供原33控制测试，不用于翻译。
- 代码、注释、公式、路径、数字、Mermaid/figure 载荷完整保留；原无标签围栏仅补 `text`。本源无相对 SVG，不增加资产。`figure` 保留不等于交互机制已验证。
- 运行范围：仅离线 NumPy/stdlib，固定种子、CPU、单线程和外部30秒 timeout。随机游走至多32条×256步；2–4态链至多1000步；1–2维 Langevin/MH 至多1000步或样本；扩散至多16点×32步。
- 不运行原默认主程序、10000×1000游走、长天气链、50000步 Langevin、100000样本 MH 或提议参数扫描。小夹具不等于默认运行或收敛证明；不训练、不下载、不联网、不使用 GPU、分布式、真实后验或输出提示词。
- 作者执行原 strict、原33控制、两份全新目录精确重放；每块技术英中对照和独立中文通读分别绑定最终 hash；源问题单列，不暗改算法或断言。记录保持 draft，不自写独审。
- 发布、support commit、PR、索引及计数仅由协调者操作；作者不 commit/fetch/远端写入。独立全文审校、真实不可变 GitHub GFM（含两图完整标签）、站点锚点/移动布局/figure、hosted CI、整书构建及用户发布许可均为独立门禁，尚未通过。
