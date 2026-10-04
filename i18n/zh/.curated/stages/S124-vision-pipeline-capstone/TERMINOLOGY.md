# S124-vision-pipeline-capstone 术语约定

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；本地 own3 支持候选，未安装、未发布。以下完整保留作者术语提案的本课用法及保护边界，提案证据 SHA256 `0db185250b7bb6a86e81853acccf7e15a2f37acaf903f6d0e4b2a31514fc0021`。原作者 common127 已包含 S117 修订 TERM；本轮只追加 S121–S123 已独核固定 TERM 作为参考，当前 common130，不替换旧作者历史。

| English | 本课用法 | 语境与依据 |
|---|---|---|
| vision pipeline / pipeline | 视觉管线 / 管线（pipeline） | 沿 S57/S77/S88/S112；串联预处理、模型和结构化输出，不是流水线并行 |
| capstone | 综合项目 | 核心词表 |
| data contract | 数据契约（data contract） | 模型边界的数据字段、类型和约束；不隐含当前示例能验证坐标语义 |
| detector / classifier | 检测器（detector）/ 分类器（classifier） | 检测器定位目标，分类器接收裁剪图像；与检测头、分类头区别 |
| bounding box / box | 边界框 / 框 | 沿 S94/S100；坐标顺序、像素单位及实际代码保持 |
| preprocessing / postprocessing | 预处理 / 后处理 | 沿 S77/S82；解码及输入变换，与 NMS、掩码处理区别 |
| normalization | 归一化 | 本课泛指数值范围处理，代码除以255；mean/std 变换在先修中为标准化，不混同 |
| mask / crop / resize | 掩码 / 裁剪区域、裁剪 / 尺寸调整 | 沿 S97/S100；crop 名词和动词按语境使用 |
| NMS | 非极大值抑制 NMS | 沿 S94/S100；首现解释，不修改图或代码 |
| RLE | 游程编码 RLE | 掩码编码；保留编码与解码两方向，不背书源 mask 类型或大小保证 |
| latency / throughput | 延迟 / 吞吐量 | 核心词表；等待窗口增加延迟与批量前向提升吞吐量分别表述 |
| batching / micro-batcher | 批处理 / 微批处理器（micro-batcher） | 按固定窗口汇集跨请求工作；不暗示本例已实现 |
| typed object / typed interface | 带类型定义的对象 / 带类型定义的接口 | 与语义有效性验证分开；源普适承诺另列风险 |
| schema | schema（结构定义） | 沿核心与 S110；正文术语表首现说明 |
| trace ID | 追踪 ID（trace ID） | 串联同一请求各阶段日志；source per-request 语义完整 |
| failure code | 错误码 | 同失败模式段用词；每类失败对应具体代码，不是泛化为HTTP状态码 |
| fallback path | 回退路径 | 分类器超时仍返回检测结果的替代路径 |
| health check / readiness probe | 健康检查 / 就绪探针 | 服务能否响应的低开销端点；不是医学检查 |
| prompt / skill / endpoint | 提示词（prompt）/ 技能 / 端点（endpoint） | 核心；输出路径和服务标识符不译 |
| NSFW / PII | NSFW（不宜在工作场所展示的内容）/ PII（个人身份信息） | 保留缩写，PII 沿补充词表 |
| verification gate | 验证关卡 | 本课正文没有该词；如后续说明引用工程检查，沿已修正 S117 与 S111/S120，不另造译法 |

通用九项章节沿冻结补充表；源未有的章节不增加。模型、产品、API、代码、数学、数值、链接、路径、Mermaid 与 figure 载荷保留。自然语言 Seven/two/five、Three、Five seconds/an hour 分别等值译为七/两个/五个、三、五秒/一小时，不添加数字字面量。
