# S54 范围：GloVe、FastText 与子词嵌入

2026-10-02。仅独立新译 05/04；显式先修 05/03 Word2Vec 已验收。固定英文提交 `1bafaa88bb4668356791150bec3a6d7df38387eb`，路径 `phases/05-nlp-foundations-to-advanced/04-glove-fasttext-subword/docs/en.md`，SHA256 `b92cf9d14b8729b4a378b0b4f468f4d957f6600c15d876b091d8dec54d8d3e47`，261 行。目标为 `i18n/zh/` 下对应目录的 `docs/zh.md`。

61 项固定控制及术语依赖见 DEPENDENCIES.json，均按 Git 提交和 SHA256 逐字核验。正文独立从英文新译，不使用历史中文或缓存。9 个通用章节名沿增补表；英文不存在的章节不补造。全部代码、公式、figure 标识符、API、数值、URL、路径保持源载荷；唯一未标语言的围栏加 text。源中未引用 assets/embeddings.svg，故本课不新增资产引用或副本。

作者完整技术对照后另遍全文中文通读，保留 draft 和逐块来源/数量等值映射；再由独立审员双审。原 strict、33 回归、两个全新目录字节重放和仓库审计分别记录。原 88 行 canonical 仅演示字符片段和六词、10 次 BPE 合并，不等同训练 GloVe 或 FastText。代码完整预读后只有限执行已装 NumPy/标准库，外置 timeout；不安装、下载词向量/语料或调用模型，不执行交付提示词。源事实/实现边界单列，译文不暗修。

实际 GitHub GFM、网站、CI 和远端最终验收分开记录；作者无远端、公共 review 或总索引写入职责。本阶段不授权新课程。
