# S45 范围

2026-10-02。仅从固定英文独立新译 10/04 Pre-Training a Mini GPT (124M Parameters)。前置 10/01–03 已由协调者验收；不复用历史中文、缓存或旧上游 PR。

- 固定英文提交：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 源文件：`phases/10-llms-from-scratch/04-pre-training-mini-gpt/docs/en.md`
- 源 SHA256：`5c3f2214d795c44638f037e6b2493e3190516a5bf89202060467298dc2f39dbb`
- 中文文件：`i18n/zh/phases/10-llms-from-scratch/04-pre-training-mini-gpt/docs/zh.md`
- 支持依赖：`DEPENDENCIES.json` 中 51 项，均验证本地字节、固定 Git 对象及清单 hash 一致；清单 SHA256 为 `f2ee0315957d81b0af2ab64ef17da1c253396eedc899c57ac8d884bd9b057db7`
- 作者记录保持 draft；全文技术自查和另遍中文通读后交另一作者独立双审
- 代码、图、公式、路径、API、标识符、数值及符号单位不变；仅一个裸围栏补 `text`
- 原英文技术缺陷单列，不在译文中暗修。canonical Python、正文示例、外部有限夹具的运行结果分别记录，不将小模型演示称为完整 GPT-2 预训练
- 不安装依赖，不下载数据或模型，不调用外部模型 API，不执行交付提示词，不运行 124M 训练；执行前完整预读，外置超时限制
- 作者只写本课中文、作者记录和阶段范围/术语；协调者负责公共审核记录、远端、GFM、索引与终验
- 完整网站、移动端、交互图、托管 CI 和发布验收不由本阶段作者自证
