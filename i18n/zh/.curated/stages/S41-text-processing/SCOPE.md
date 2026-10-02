# S41 文本处理：作者范围

2026-10-02。唯一作者课程 05/01 Text Processing — Tokenization, Stemming, Lemmatization。固定 English commit `1bafaa88bb4668356791150bec3a6d7df38387eb`，源 SHA256 `d7070af33a9656a02ce6dcf42966d6c8c401035df0f8fa244ec37c12ca4d210b`。

- 源 `phases/05-nlp-foundations-to-advanced/01-text-processing/docs/en.md`；目标 `i18n/zh/phases/05-nlp-foundations-to-advanced/01-text-processing/docs/zh.md`
- 46 项支持/词表依赖均已按 DEPENDENCIES.json 与本地字节、固定 Git 对象和 SHA256 核验；AGENTS/control 脚本保持固定版本
- English-first 全新翻译，完整正文、两表、三个练习与三项参考。固定英文无 Learning Objectives 段，不擅自添加；代码、REPL 输出、figure、markdown 提示词围栏全部保护
- 作者全文英中技术对照及另次纯中文全文通读后冻结。第四线 translate_pretraining_data 独立审本课；本作者独立审协调者的 S39，未收到 S39 冻结稿前不读取作者草稿
- 原 strict、33 回归及两个新目录重放；完整预读后只运行 stdlib 原例和有限核验。NLTK、spaCy、tokenizers、transformers 不运行或安装，不下载语料/模型，不调用网络/API
- 源 Porter 规则、Unicode/词性回退、库性能与版本示例等问题单列，不暗修源。实际 GitHub GFM、公共 review、总索引和远端由协调者负责
- 只写本课、S41 增量和自己的 QA，不新领课、不改共享固定词表、不写远端
