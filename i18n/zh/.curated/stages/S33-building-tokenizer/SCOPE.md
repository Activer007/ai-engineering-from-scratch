# S33 从零构建分词器：作者范围

- 唯一排他课程 10/02；English-first 新译，不读取旧中文、缓存或历史 PR。
- 源 `phases/10-llms-from-scratch/02-building-a-tokenizer/docs/en.md`，固定 commit `1bafaa88bb4668356791150bec3a6d7df38387eb`，SHA256 `3e2af805d324028b1c673be3bebad6f17dc74ca2ffa0f1f050aa2d5d56d61da1`。
- 目标 `i18n/zh/phases/10-llms-from-scratch/02-building-a-tokenizer/docs/zh.md`，逐块记录 `i18n/zh/.curated/lessons/10-02/translation.json`。
- 447 行、175 块、73 可译块、15 围栏（10 Python、1 Mermaid、1 figure、3 裸围栏补 text）、3 表、3 练习、5 参考。
- 40 项支持/术语文件 hash 与固定 Git commit 逐字节校验。唯一显式前置 10/01 已审，只读词表不复用旧中文课文。
- 作者全文英中技术对照与另次纯中文通读；作者记录保持 draft，不冒充独立审。S32 作者负责本课独立审；本作者审 S32。
- 代码、模型/库/API、Unicode 例子、数值、公式、路径、链接、图载荷完整保护。源生产级/无损/压缩率等强断言只单列，未暗修。
- 全文读取运行源码后，只有标准库受限路径可运行。Python -I -S 隔离第三方包和环境路径，让源码原有 regex/tiktoken ImportError 分支生效；不会加载第三方代码，不安装、不下载语料或模型、不联网。
- 无公共 review、索引、远端修改。实际 GitHub GFM/图与联合终验由协调者负责。
