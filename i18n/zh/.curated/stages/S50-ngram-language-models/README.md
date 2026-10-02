# S50：N-gram 语言模型

2026-10-02 协调终验补记：累计 71 课联合严格检查及两次字节重放通过（69课原strict，既有S07/S19精确适配各1；无新增例外），原33回归和24/50适配防护及仓库数量审计通过。联合验收快照 71/523、2课仍进行中、450课未开始，实际完成总数以PR #7单一索引的最终读回为准。下文作者交接时的聚合pending已由本补记关闭。最终证据提交后远端全文件与CI查询在PR说明/单一索引独立读回记录；final_acceptance=false指完整网站和用户发布验收，不是省略翻译审核。未合并、未发布。

05/16 已完成英文独立新译、作者两遍自查、另一位审员的全文技术对照与独立中文通读，并通过实际 GitHub GFM 检查。当前为 fork draft PR #56 的阶段证据草案；聚合验证、最终远端全文件字节核对与精确最终提交的 CI 查询待协调者回填，`final_acceptance=false`。

固定英文提交为 `1bafaa88bb4668356791150bec3a6d7df38387eb`，英文 SHA-256 为 `92d3b5e90a0730efd6819090e514a562e02185a3a1b65f78b60331692adbb9ee`，中文 SHA-256 为 `65df45c729d3417c64bc4bc546bf2a712c62ba98e3c0870da7c9fc4dd0a41fd4`。正文共 256 行、105 块、43 个可译块、15 个标题、10 个围栏、1 张表、3 个练习和 5 条参考，逐块绑定源文与译文 hash。原代码、公式、数值、链接与图载荷保持不变。56 项固定控制及词表依赖已逐项核对 Git 对象与本地 hash，见 [DEPENDENCIES.json](DEPENDENCIES.json)、[SCOPE.md](SCOPE.md) 和 [TERMINOLOGY.md](TERMINOLOGY.md)。

作者和独立审员均完整预读并分别运行原 118 行 stdlib main，保留原默认规模：10 个训练句、2 个测试句、28 个词表项，种子 1、7、42。原输出为 Laplace 困惑度 10.29、Kneser-Ney 困惑度 4.42。作者另执行全部 5 个文档 Python 代码块和 25 项有限检查；独立审员另执行同样 5 个块和 14 项有限检查。各自使用外置超时和独立夹具，没有改动原 main 的执行规模。这只是本地小语料二元演示；Brown、Shakespeare、Birkbeck、KenLM 和 Transformer 性能实验均未运行，交付提示词未执行。

作者与独立审员分别通过原完整 `check`、33 项原回归，以及各自两份全新仓库外目录的 Markdown 字节重放。作者三项仓库审计通过：523 个课程无问题；认证审计为 67 课、12 份测评、505 道测评题无问题；README 计数和书籍卷表一致。有限夹具的中途错误预期已修正并保留记录，不将其误称为源程序缺陷。

相对资源 `../assets/ngram.svg` 从固定源精确复制，source/Git/target 三方 SHA-256 均为 `06a8718f1b24c551a6b62b85200c33c7ba193a94c8e6e63c5b1b224a666d5c07`。资源单独列入作者 manifest；原 `render` 只重放 Markdown，不会自动复制或打包 SVG。

作者本人在 dot 云 Chrome 的独立标签检查了[实际固定提交页面](https://github.com/Activer007/ai-engineering-from-scratch/blob/5b237395a1edd480cb809388edff03b13dc49780/i18n/zh/phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer/docs/zh.md)：57 个正文 DOM 文本单元、15 个标题及非空唯一锚点、19 个行内代码、10 个围栏载荷全部匹配。表格完整为 8 行 × 3 列（含表头）；24 处粗体、1 处斜体正确，残留 `**` 为零。相对 SVG 的四个阶段、三条箭头、39 个文字标签和底部两行说明均已实际目视核读。全部代码保存了截图，长提示词经横向滚动核到最后的 `<UNK>` 句。两处 `figure` 仅显示代码占位，不代表网站交互通过。

独立审员单列 15 组源问题，详见 [VALIDATION.json](VALIDATION.json)。重点包括 bits/nats 与字符/token 分母不能混换，KN/OOV 的归一化边界，原 main 与文档的 OOV 行为差异，Laplace 的 BOS/EOS 支持集，非法折扣、零质量采样、随机种子可能同输出，以及困惑度裁剪和性能比较条件。译文忠实保留源文，没有暗修这些问题。自然数量和时间单位逐块记录等值映射；`100K`、原公式和数值不变。

独立审员执行的原站离线解析仍产生 9 个空标题锚点；这与 GitHub 的实际正常锚点是两条不同验证结果。完整网站、移动端、交互图、托管 CI 和发布验收均未通过；当前 GFM 通过不能代替这些门禁。
