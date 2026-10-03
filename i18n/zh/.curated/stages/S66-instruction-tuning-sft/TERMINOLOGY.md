# S66 指令微调术语增量 v1.0

2026-10-03；联用核心术语、补充表及固定 70 项支持。来源仅为固定英文 10-06，前置术语使用已接受 S45/10-04，不采用 S61/10-05。

| EN | 推荐呈现 | 语境与边界 |
|---|---|---|
| instruction tuning / SFT | 指令微调 / 监督微调（SFT） | 从指令—响应样本学习行为；保留源概括，不把噪声更新称为已验证训练 |
| base model | 基座模型 | 相对于指令微调模型；随机初始化演示不等于预训练检查点 |
| token / tokenizer | token（词元）/ 分词器（tokenizer） | 保留 token；字节 ID 与自然语言单词不等同 |
| loss masking / loss mask | 损失掩码处理 / 损失掩码 | 在目标 token 对齐的位置屏蔽损失；不是注意力掩码 |
| masked cross-entropy | 带掩码的交叉熵 | 以有效响应 token 数归一化；零响应特例单列 |
| chat template / role marker | 聊天模板 / 角色标记 | system、user、assistant 为角色标识；代码原样 |
| instruction-response pair | 指令—响应对 | response 统一为响应，不混淆网络返回值 |
| catastrophic forgetting | 灾难性遗忘（catastrophic forgetting） | 原有能力受损；阈值是源启发式，非通用保证 |
| weight tying | 权重绑定（weight tying） | 同一嵌入矩阵用于输入与输出；沿 S45，与补充表权重共享同义 |
| held-out instruction set | 留出的指令集 | 用于评估，不暗示源演示已严格分离训练数据 |
| epoch / warmup / weight decay | 训练轮次 / 预热 / 权重衰减 | 与步骤、样本数区分 |
| logits / gradient | logits（未经归一化的分数）/ 梯度 | 源 dlogits 未接入参数更新，不据此声称反向传播成立 |

数量保留源形：1 million（百万）、billions（数十亿量级）；7B、52K、4M、2T 等不改数字。minutes → 分钟；hour → 小时；tokens/second → tokens/second（每秒 token 数）；15x → 15x（15 倍）不可另加新数字，正文采用“15x”。论文标题、品牌、模型名、URL、代码标识符原样。
