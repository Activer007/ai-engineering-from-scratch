# S73 神经网络调试：范围与验收

- 唯一正文源：固定提交 `1bafaa88bb4668356791150bec3a6d7df38387eb` 的 `phases/03-deep-learning-core/13-debugging-neural-networks/docs/en.md`，711 行；完整阅读403行 `code/debug_neural_nets.py` 后静态审查。
- 唯一中文目标：`i18n/zh/phases/03-deep-learning-core/13-debugging-neural-networks/docs/zh.md`。从英文独立新译，不使用旧中文、缓存或其他翻译PR。
- 激活由协调者在实际 index90 精确双读回后明确授权；03-01至03-10均在已验收90集合内。S61/S66/S69仍pending，不作为已验收支持。
- DEPENDENCIES.json的78项路径/commit/SHA256须逐项匹配本地及固定Git字节；原33测试所需00-04三文件仅作测试夹具，不作翻译记忆或发布。
- 保留代码、注释、API、Mermaid、figure、数学含义、数值、单位、路径和URL。原无语言围栏只补text。普通正文星号显示问题先报协调者；不改保护载荷或增加validator例外。
- 作者全文技术对照与单独中文通读逐块双哈希记录；源问题独立分列。独立审校者另做全文双读，协调者才可规范化review。
- 已检查当前环境torch不可用，因此跳过torch导入、训练、hook和gradcheck运行；不安装，不跑默认训练、不用GPU、不下载数据、不运行wandb/TensorBoard或遥测。可做明确标为静态/标准库逻辑的有界检查。
- 原strict、原33控制、78固定pin、两套全新原CLI重放须通过。网站锚点、手机、figure交互、实际GitHubGFM、hostedCI、bookPDF及用户发布为不同门禁；本地通过不冒充实际渲染或发布。
- 源gradient_check强制训练模式与dtype、类别标签.double()、状态恢复不足、hook生命周期、LR范围与启发式诊断风险分别记录，不暗修正文。
- 作者不写review.json、commit、远端、PR或总索引；协调者为唯一发布者。
