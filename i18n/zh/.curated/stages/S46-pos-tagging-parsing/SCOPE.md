# S46 范围：05/07 词性标注与句法分析

固定源为本 fork 的 1bafaa88bb4668356791150bec3a6d7df38387eb，课程 phases/05-nlp-foundations-to-advanced/07-pos-tagging-parsing，英文 SHA-256 为 05fb67fdbec5afafc9e35f4d96de29663c1a37022ad70bbe3f97e804366c8a6e，共 254 行。本文从固定英文逐段独立新译，没有读取旧中文、旧 PR 或缓存。

先修为 05/01 文本处理和 02/14 朴素 Bayes，均由协调者确认在本批开始前已验收；作者完整读取两课固定英文，并完整读取本课 HMM、Viterbi 和句法标注上下文。51 项控制与词表通过本地字节、固定 Git 对象和 manifest SHA 三方核验。DEPENDENCIES.json 的 SHA-256 为 8a65fdf399fd2734bcf95145a8a02a92a8161cfe3a308792b69f38b54b489abc。

本阶段作者写入仅包含中文正文、05-07 的 draft translation.json、本 SCOPE 和术语增量。独立审员与协调者分别持有审核和终验权限；不改公共控制、索引、英文、源码、远端、Actions、部署或合并状态。

正文共 103 块，52 个非空块，其中 42 个可译块及 10 个保护围栏。保留 14 个标题、1 张三列表格、3 个练习、4 条参考、2 个 figure 标识和全部公式、代码、路径、数值。没有相对 SVG 引用，不复制未引用的 assets/pos-parse.svg。

作者完成全文英中技术对照，再另遍通读完整中文。完整预读 109 行 stdlib canonical main.py 后运行全部 3 个演示；另行执行两段安全 Python 正文定义与 16 项有限核验。没有运行 spaCy/模型、NLTK/Brown 数据下载、Stanza、trankit、外部 API 或产物提示词，也不以 toy 运行声称复现 Brown 准确率。

源文关于词形还原必需 POS、语法分析等同 token 分类、标注体系、EOS 收尾、人工一致率上限、算法家族与性能等疑点独立记入作者报告，不在译文中暗改。原控制 strict、33 回归、两个新目录逐字节重放、三项仓库审计与原站 parser 离线结果分别记录；离线 parser 不代表 GitHub GFM 或真实网站验收。最终发布验收由协调者另行处理。
