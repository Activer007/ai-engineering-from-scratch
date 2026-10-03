# S70 RAG 分块策略术语增量 v1.0

2026-10-03；固定英文 05-23；联用核心、增补及 74 项固定支持依赖，承接 S59 信息检索和 S64 嵌入模型。只读取术语，不复用旧中文课文。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| chunk / chunking | 文本块 / 分块（chunking） | 文档切分单位，不等同 token |
| RAG / embedding / reranking | 检索增强生成（RAG）/ 嵌入（embedding）/ 重排序 | 首现解释；向量表示与候选重排有别 |
| token / character | token（词元）/ 字符 | 模型处理单位与 Python 字符串长度有别；tokens 源形保留 |
| fixed / recursive / semantic / sentence chunking | 固定长度 / 递归 / 语义 / 句子分块 | 名称不保证代码实现满足所有约束 |
| overlap / context cliff | 重叠 / 上下文悬崖 | 相邻块共享内容；质量骤降的源表述，不是本轮实测 |
| parent-document / child / parent | 父文档 / 子块 / 父块 | 小块检索、大块返回，保留父块去重含义 |
| late chunking / contextual retrieval | 后期分块 / 上下文检索 | 前者全文 token 嵌入后池化，后者添加生成的上下文前缀 |
| factoid / multi-hop / stratified eval | 事实型 / 多跳 / 分层评测 | 多跳指跨线索推理，按查询类型分层 |
| recall@5 / MRR / cosine similarity | recall@5（召回率）/ MRR（平均倒数排名）/ 余弦相似度 | 指标原名保留；any-gold-hit 与标准召回率的差异单列问题 |
| LLM / pooling / ablation | 大语言模型（LLM）/ 池化 / 消融实验 | 保留模型、类、函数、参数和代码字符串 |

通用标题沿用增补；Pitfalls→常见陷阱。品牌、论文标题、代码/figure/SVG、链接、路径、N、top-K、日期数字、69% → 54%、35-50%、5k/2.5k、token(s) 保留；k 首次说明为千。元数据 ~60 minutes→~60 分钟。英文数量词按义等值：six→六，one→一个，two→两个，zero→零，first→首先/第一次；不将百分比擅改为百分点。Feb/Jan→二月/一月。保留强调边界空格，避免中文标点吞掉 GFM 粗体。源六种策略却列七种等问题另行记录，不静默纠正。
