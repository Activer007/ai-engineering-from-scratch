# S59 信息检索与搜索：范围

2026-10-03。仅新译 05-14，英文固定提交 1bafaa88bb4668356791150bec3a6d7df38387eb，源 phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/docs/en.md，目标 i18n/zh/phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/docs/zh.md。逐块完整翻译，保持代码、figure、数学、数值、模型 ID、URL 及强调边界。复制相对 assets/retrieval.svg 固定 Git 字节并记录 manifest。无其他课文改动、旧译读取、远端、PR 或总索引操作。

协调者已读回 78 课闭环，05-02 与 05-04 两项显式先修均就绪；参考 S44/S54 术语、核心及增补词表，DEPENDENCIES.json 66 项固定 SHA256 与 Git 字节逐项核查。真实编码器、交叉编码器、SPLADE/ColBERT 为介绍与扩展，不虚报其先修完成或运行效果。

已完整预读英文 234 行和 code/main.py 116 行。仅运行有限离线 stdlib canonical main.py 及数学边界夹具，外部 timeout；fake_dense_rank 为词项集合重叠教学演示，不能当作真实稠密检索。禁止 sentence_transformers、模型下载、网络、生产向量库、外部语料和训练。保留原文潜在问题并单列问题账本。

作者技术对读与中文通读覆盖全部最终块并绑定 SHA256。原版 strict、33 controls、两个新目录重建对字节；不修改验证器或引入适配。GitHub GFM 实际页面、课程网站/移动端/交互及 hosted CI 是独立未通过门禁，不能用离线解析替代。PDF 已知缺 xelatex.fmt，不安装系统依赖。
