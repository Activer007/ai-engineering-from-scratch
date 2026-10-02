# S30 交付报告：音频基础

本阶段仅包含 06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform。正文与全部 89 块已完成作者自查、独立技术审和独立中文通读；没有必须修改的翻译问题。协调者已完成指定内容 commit 的实际 GitHub GFM 与相对 SVG 显示检查。聚合验证已完成。本阶段快照 **52/523 已审课程草稿、0课收尾中、471课未开始**；README另计，发布/合并0，实时总数由PR7单一索引维护。用户发布验收仍未通过。

## 固定来源与正文

- 仓库：Activer007/ai-engineering-from-scratch；PR #36。
- English commit：`1bafaa88bb4668356791150bec3a6d7df38387eb`。
- English：`phases/06-speech-and-audio/01-audio-fundamentals/docs/en.md`。
- English SHA256：`9ef0e33271e866ee2ec72280d40ffed14a488cce7941780b2495ccbadf77f7ee`。
- 中文：`i18n/zh/phases/06-speech-and-audio/01-audio-fundamentals/docs/zh.md`。
- 中文 SHA256：`d7cdba790e8aeb29e04eb23ec7ccdb30e5c5da45bf719b6b68c71b17a8287cee`。
- 实际 GFM 内容 commit：`acbd00fbe2872bed4d2c93aab67936140d6279aa`；支持 commit：`d93ef97cc8a55ab6dede5fd661b4233c74c86015`。最终证据提交后的全部远端字节结果另记于PR完成说明和总索引。
- 37 项依赖逐文件绑定固定支持 commit 与 SHA256。全部 English-first 新译；未读取旧中文、缓存或旧 PR 作草稿。
- 142 行、89 块、41 可译块、14 标题、3 表、4 围栏（3 Python、1 figure）、1 相对 SVG、3 练习、5 参考。

源的先修元数据把 01/06 标作 Vectors & Matrices、01/14 标作 Probability Distributions，与固定目录的 01/06 概率分布、01/14 范数距离错位。元数据按源保留；协调者已确认按编号或名称理解所需的数学课均已审。

## 审校与控制

作者先完成全文英中技术对照，再单独通读全文中文。独立审员未读取作者自审结论、未跨改正文，另行完整核对 89 块、41 译块、3 表、3 练习、5 参考与全部 4 个受保护围栏，并完成另一次纯中文通读。独立结论为 `PASS_TRANSLATION_WITH_SOURCE_ISSUES`，无必改项。

作者与独立审员分别通过原 strict 检查、原 33 项控制回归及两次独立输出目录重放。协调者随后将公共记录的全部 89 块绑定到同一正文 hash。各层证据不互相冒充：作者运行不是独立运行，离线解析不是浏览器验收，GitHub GFM 显示通过也不等于课程站点完整验收。

核心 `render` 命令只重放 Markdown。四份作者/独立 Markdown 重放文件均与冻结正文逐字一致；不能把这项结果称为已重放 SVG。SVG 由作者按源复制、独立审员核对清单/路径/XML与固定 Git 字节，协调者再单独复制并核验哈希。

## 作者有限代码验证

作者完整预读 `code/main.py` 的 128 行后，以外部 30 秒 timeout 原样运行，退出码 0。程序仅使用 math、os、struct、tempfile、wave；输入是合成信号，临时 WAV 是程序生成的数据，没有录制或读取用户音频。代码及原示例规模未改。

canonical 演示产生 512 个采样值，440 Hz 峰落在 437.5 Hz，混合信号峰约为 218.8、437.5、875.0 Hz；7 kHz/10 kHz 示例的栅格峰约为 3007.8 Hz，朴素抽取示例峰为 1000 Hz。这些有限结果不代表正文中的理想频点均精确可达。

作者另行完整预读并按源顺序执行正文 b0049/b0055 的 sine 与 DFT 定义，进行 8 组有限核验：

1. 采样数与幅度界限：256 点、最大幅度 0.5。
2. 正文与 canonical DFT 一致，最大分量误差约 `3.55e-15`；64 点幅度 0.5 的整数频点正弦得到未经归一化的模 16。
3. 440 Hz 非整数频点：512 点、8 kHz 时实际峰为索引 28，即 437.5 Hz。
4. 7 kHz 在 10 kHz 采样下等于负相位的 3 kHz 正弦，最大差约 `3.23e-14`，峰为 3000 Hz。
5. 24 kHz 的 7 kHz 信号每三个点取一个后，峰折叠到 1000 Hz。
6. 单声道 int16 WAV 写入/读回：5 点、16 kHz，最大误差 `3.0517578125e-05`。
7. 立体声临时 fixture 暴露 `read_wav` 的单声道假设，触发 `struct.error`；未修源实现。
8. Nyquist 零相位正弦采样近零；偶数 1024 点的含 DC/Nyquist 双端点非负频点数为 513。

## 独立有限代码验证

独立审员只运行其完整预读的正文 b0049/b0055，不读取或运行 canonical 程序，也不进行音频文件操作。其 8 组核验独立于作者：

1. 1 秒、16 kHz 正弦得到 16000 点，最大绝对幅度 0.5。
2. N=8 单位幅度正弦的共轭峰与缩放：正频原始模为 4。
3. 有限 Parseval 归一化：时域能量 4，频域能量除 N 约为 4。
4. 7 kHz/10 kHz 与负 3 kHz 正弦的最大差约 `3.23e-14`。
5. N=100 的正频混叠峰为索引 30，即 3000 Hz。
6. N=256、16 kHz 的 440 Hz 理想索引 7.04，实际峰为索引 7，即 437.5 Hz。
7. 1024 点含 DC/Nyquist 的非负频点数为 513，间距为 15.625 Hz。
8. int16 范围为 -32768 到 32767，共 65536 个量化级。

独立 DFT 的最大 N 为 256。两方都跳过 b0045 的 soundfile 外部文件示例；未安装或运行 soundfile、torchaudio、librosa、matplotlib 等非 allowlist 库，没有网络/API/模型调用、音频下载或用户录音。未执行整秒 16 kHz 的二次复杂度 DFT、录音降采样练习或完整 STFT 绘图练习。

## SVG 与渲染证据

相对资产：`i18n/zh/phases/06-speech-and-audio/01-audio-fundamentals/assets/audio-fundamentals.svg`，SHA256 `056bbdb5cd8ac4971ea7170a3a9bc8ad7ce6e76089f6bf854802ffd9d2157c85`。源、中文副本及固定 Git 字节一致，载荷未翻译或重画。

协调者在 dot 云浏览器检查 immutable content commit `acbd00fbe2872bed4d2c93aab67936140d6279aa`，报告实际 GitHub GFM：14 标题；3 表的含表头尺寸分别为 7×2、6×3、9×3；15 个 strong；3 个意图内 em（Nyquist 频率、混叠、帧）；0 意外 em、0 残留 `**`、0 Mermaid。相对 SVG 的加载状态为 complete，实际截图中完整可见波形、采样、DFT、混叠及采样率面板。此项来源为协调者浏览器观察，本草案作者未声称亲自进行该浏览。

离线课程站点 parser 生成 12830 字节 HTML、3 表、3 普通代码块、1 figure、0 Mermaid，无重复 heading ID，但 8 个中文标题生成空 ID，结果为 `BLOCKED_SOURCE_RENDERER`。这不是实际站点、移动端或交互测试通过证据。GitHub GFM 中保留的 `figure` 围栏不代表课程站点的 mel-scale 交互已经验收。

## 保留的源风险

作者报告分为 12 组，独立报告分为 10 组；分组不同，不将其相加成独立缺陷总数。共同主题包括先修编号错位、模型/年份/流程强断言、单声道归一化波形假设、Nyquist 边界与理想滤波器、int16 范围与 float32 精度、DFT 模与信号幅度/负频约定、FFT 长度与频点端点计数、加窗效果与短时表示、库默认 dtype/功能时效、练习计算量及引用/图示边界。

作者另外运行并记录 canonical 与正文规模/标题不一致、mono-only WAV reader、读写缩放差、朴素抽取与未实现的 proper 对照等边界；独立审员未运行 canonical，因此不能借其报告声称独立复现这些项目。所有源文字和保护载荷均按源保留，没有暗修技术事实。

## 验收边界

聚合重放已完成，最终证据提交后的远端字节与CI状态查询记录在PR完成说明和单一索引。完整实际站点/移动端/交互验收、托管CI及用户发布验收均未通过。Actions未启用，空状态不是CI成功；无merge、部署或上游写入。

## 协调者联合验收

组合 **50课原strict + S07精确符号表例外 + S19精确两行竖线适配**，共52课两次输出逐字节一致。原33、S07的24、S19的50控制及523课/67认证课/12评测/505题审计、README计数通过，英文/源码/通用控制未改。core只重放Markdown；每份清单绑定的SVG另经hash验证后复制到两个输出，参与整体字节比较。远端最后提交字节和元数据在提交后独立核实并写入PR与总索引，不把托管CI、应用网站或发布验收写成通过。
