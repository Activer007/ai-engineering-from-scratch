# S49 范围：从零实现 Word2Vec

2026-10-02。排他作者范围仅 `05/03`，前置 `05/02` 与 `03/03` 已审。本轮沿用 68 课验收后的固定支持组合，不领取其他课程。

- 固定英文：`phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec/docs/en.md`
- 英文 commit：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 英文 SHA-256：`566500e6c43ebc3624a117e76843be1100be7951ac7780c37f15241299846b27`
- 中文：`i18n/zh/phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec/docs/zh.md`
- 作者记录：`i18n/zh/.curated/lessons/05-03/translation.json`，保持 draft，独立审校与最终验收由协调者绑定
- 支持依赖：`DEPENDENCIES.json` 的 56 项逐本地字节、固定 Git 对象及 SHA-256 核对一致；manifest SHA-256 `2203c6d084751deb9a644d1e74c3ba7d5531108ad9c600db94d24da3b93cb498`

从固定英文独立新译，不读取旧中文课文、缓存或历史翻译 PR。完整覆盖 267 行、113 块、46 个可译块、16 个标题、11 个围栏、1 张术语表、3 道练习与 3 项参考。代码、公式、行内标识、数值、图形、路径、URL 与元数据键保持；一个裸围栏仅补 `text`。源 Unicode 图与 `figure` 标识均保留载荷，不重画。

作者完成全文英中技术对照和另遍纯中文通读；独立审员另做全文双审，不读作者自查结论、不跨改正文。原 strict、33 项控制回归、两个全新目录重放与三项仓库审计分别记证据。只有完整预读的本课安全 NumPy/标准库代码可在外部 timeout 下离线执行，canonical 原示例规模不改。跳过 gensim、外部向量/数据、网络、安装、模型调用及输出提示词执行。

源中的训练规模与历史、默认架构、负采样分布/筛除数量、重复索引梯度、类比与去偏强断言、练习与输入边界只单列。站点 parser、GitHub GFM、完整网站、移动/交互与 CI 分开判定；作者范围不提前宣称终验通过。
