# S55 命名实体识别：单课独立重译范围

2026-10-02。仅处理 05/06 Named Entity Recognition；开始于 73/523 课已审草稿之后。

- 固定源提交：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 英文：`phases/05-nlp-foundations-to-advanced/06-named-entity-recognition/docs/en.md`，321 行，SHA256 `1234e5808229ac25f3c65b1fe1baab736e525591c4cf847cc28690af25d46e71`
- 中文：`i18n/zh/phases/05-nlp-foundations-to-advanced/06-named-entity-recognition/docs/zh.md`
- 明确先修：05/02（S44 词袋与 TF-IDF）、05/03（S49 Word2Vec），均已审。语序与序列标注术语参照固定 S46 增量。
- `DEPENDENCIES.json` 绑定 61 份固定控制/术语；逐份核对本地字节、固定 Git blob 与 SHA256。该清单 SHA256 为 `76d8f679c62315b286cf662157d9eaa3d71f23f8dd09aa9b6ed0bcc00b6205fe`。
- 从固定英文独立逐块新译，不读取历史中文、缓存或旧上游 PR。代码、figure、产物提示词、标签、接口、路径、链接、公式、数值与单位保留；裸围栏只补 `text`。固定九种通用章节名，有则统一，没有则不增造。
- 源目录有 `assets/ner.svg`，但固定英文没有引用它；本课不新增图引用或图副本。
- 作者完整英中技术自查后另遍完整中文通读；独立审员另做同等双审。源技术问题单列，不由译文暗修。记录保持 draft，逐块绑定 source/target hash，并记录自然中文数量等值映射。
- 完整预读 106 行 canonical 后，可在外置 timeout 下运行原默认规则/BIO 小型演示及明确标注的有限离线夹具。不得把此结果称为 HMM、CRF、BiLSTM、Transformer 或 LLM 训练验证。
- 不安装库、不下载模型/语料、不执行生产模型调用或交付提示词。文档 `sklearn-crfsuite`、`torchcrf`、spaCy、Transformers 等示例只静态核读；缺失资源和未执行部分明确记录。
- 使用未修改的原 capture/check/render、33 项回归、两个全新仓库外目录字节重放及三项仓库审计。实际 GitHub GFM、聚合、远端与 CI 状态另验；本阶段不声称完整网站、移动端、交互、用户批准或发布通过。

作者仅写本课正文、作者 draft 记录和本阶段支持文件；公共 review、索引、远端、PR 和最终门禁由协调者管理。
