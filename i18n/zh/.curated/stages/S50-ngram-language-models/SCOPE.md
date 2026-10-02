# S50 范围：N-gram 语言模型

2026-10-02。仅翻译 05/16 Text Generation Before Transformers — N-gram Language Models。前置 05/01 与 02/14 已完成审校；不以旧中文、旧翻译缓存或历史上游 PR 作翻译记忆。

- 固定源提交：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 英文：`phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer/docs/en.md`，256 行，SHA-256 `92d3b5e90a0730efd6819090e514a562e02185a3a1b65f78b60331692adbb9ee`
- 中文：`i18n/zh/phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer/docs/zh.md`
- SVG：固定源 `phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer/assets/ngram.svg` 精确复制到对应中文 `assets/ngram.svg`，SHA-256 `06a8718f1b24c551a6b62b85200c33c7ba193a94c8e6e63c5b1b224a666d5c07`；原相对链接不变，作者记录绑定资源清单
- 支持：`DEPENDENCIES.json` 的 56 项固定控制与术语，逐项核对本地、Git 固定对象和 SHA-256；本阶段词表仅为独立增量

从英文逐段独立新译，完整英中技术自查后另次通读中文。源公式、数值、代码、标识符、链接、图载荷、交付提示词保持；源技术问题单列，不暗修正文。自然语言数量与时间单位逐块记录等值映射，不放宽控制。

检查使用原 `curated_translation.py` 的首次 capture、完整 check、两份全新仓库外目录 render，另运行原 33 项回归和三项仓库审计。正文和 SVG 的字节核验分别记录；render 本身不复制 SVG。完整预读后，以外置 timeout 运行原 118 行 stdlib 演示及有界夹具。重点核对 bits/nats、字符与 token 的量纲、Kneser-Ney 归一化与 OOV、困惑度比较条件。外部语料、模型、安装、API、交付提示词和大规模实验不作为执行门槛。

作者仅写本课中文、对应 SVG、draft 作者记录及本阶段文件；独立审员另作全文技术审和中文通读。公共审核状态、实际 GitHub GFM、最终远端字节、聚合检查、CI 查询和索引由协调流程分别验收。翻译审校不代表完整网站、移动端、交互功能、托管 CI 或发布验收。
