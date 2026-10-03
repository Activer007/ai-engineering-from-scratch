# S58 学习率调度术语增量 v1.0

2026-10-03。继承核心/补充及 66 项依赖，尤其 S43 优化器与 S53 权重初始化；唯一课文来源是固定英文 03-09。不借术语修正源事实。

| EN | 推荐呈现 | 语境与保护边界 |
|---|---|---|
| learning rate / schedule | 学习率（learning rate）/ 学习率调度（schedule） | LR 缩写保留；步到学习率的函数，不是训练作业排程 |
| step decay / cosine annealing | 阶梯衰减（step decay）/ 余弦退火（cosine annealing） | 阶梯间隔由实现 step 决定，不与正文 epoch 混为一谈 |
| warmup / linear warmup | 预热（warmup）/ 线性预热 | 学习率从低值上升，与缓存预热无关 |
| cosine decay / warm restart | 余弦衰减 / 热重启（warm restart） | 重设学习率，不是重置全部模型权重 |
| 1cycle policy | 1cycle 策略 | 单周期先升后降；不把简化实现说成完整生产算法 |
| convergence / divergence / oscillation | 收敛 / 发散 / 振荡 | 区分损失降低、稳定和泛化质量 |
| LR range test | 学习率范围测试（LR range test） | 短训练逐步增加学习率，非独立模型评估 |
| peak learning rate / eta min | 峰值学习率 / Eta min（学习率下限） | lr_max、lr_min、eta_min 等标识符原样 |
| loss landscape / basin / sharp minimum | 损失曲面 / 吸引域 / 尖锐极小值 | 继承 S43；不把尖锐极小值推荐暗改成平坦 |
| optimizer statistics / moment | 优化器统计量 / 矩 | 源 Adam 方差/偏差校正解释的局限单列，不静默补正 |
| epoch / step / token | 轮（epoch）/ 步 / token（词元） | 整轮、参数更新步和文本单位不可互换 |

品牌、人物、模型、API/代码/公式原样。million（百万）、trillion（万亿）保留源量词和数值并解释；时间元数据 minutes 译分钟，正文所有数值不换算。通用九个章节沿补充表。源比例、历史模型配置、效果断言忠实翻译，另列未核实/内部矛盾。
