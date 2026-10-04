# S112-video-understanding 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：Video Understanding — Temporal Modeling。

本地check-only own3候选，未安装、未发布，不计课程完成。复用107 TERM上下文校准和已有独立技术/中文审校；不重扫全部历史词表。common115=107 TERM+8 controls，own3另计，未来总118。原提案表格数据行逐字保留。

| English | 本课译法 | 语境及来源 |
|---|---|---|
| Video Understanding — Temporal Modeling | 视频理解：时序建模 | 固定英文 H1，不添加副标题 |
| temporal modeling / temporal structure | 时序建模 / 时序结构 | 沿时间维度建模，不是静态图像结构 |
| temporal pooling | 时序池化 | 沿时间汇聚；pooling 沿 S83/S85/S86 |
| frame / clip / video | 帧 / 片段 / 视频 | 单张图像 / 采样子序列 / 整段视频；不用梯度裁剪的 clip 译法 |
| frame sampling / frame sampler | 帧采样 / 帧采样器 | 选择时间索引，不自动包含视频解码 |
| uniform / dense / multi-clip sampling | 均匀采样 / 密集采样 / 多片段采样 | 均匀分布 / 连续窗口 / 多窗口测试平均 |
| spatio-temporal / space-time patch | 时空 / 时空块 | 视频的时间与空间维度；patch 不是软件补丁 |
| joint / divided / factorised attention | 联合式 / 分离式 / 分解式注意力 | 联合全时空 / 块内时间与空间 / 跨块交替；原文区别保留 |
| inflation / inflated convolution | 膨胀 / 膨胀卷积 | 沿时间复制二维权重，不等于空洞卷积；首次说明 inflation |
| factorised convolution | 分解式卷积 | 空间卷积后接时间卷积，中间非线性不遗漏 |
| appearance / motion / action recognition | 外观 / 运动 / 动作识别 | 静态外观信号、时间变化、任务类型分开 |
| clip-level / video-level accuracy | 片段级 / 视频级准确率 | 单个片段与多个片段平均预测分开；不把原文“更高”当保证 |
| order-invariant | 具有顺序不变性 | 时序池化不区分帧排列；不等同所有视频模型无视顺序 |
| convolutional neural network / CNN | 卷积神经网络 / CNN | 沿 S83/S85；原文 CNN 列表含 ViT 的问题另列 |
| embedding / token | 嵌入（embedding）/ token（词元，此处对应时空块） | 沿核心，视觉 token 不强称自然语言单词 |
| backbone / transfer learning | 主干网络（backbone）/ 迁移学习（transfer learning） | 沿 ADDENDUM/S85/S91，不用骨干网络 |
| average pooling / max-pool | 平均池化 / 最大池化 | 沿 S85/S86，不套 S44 文本上下文的均值汇聚 |
| batch norm / BN | 批量归一化（BN） | 沿 S85/S88/S91，统计量不等于权重 |
| receptive field | 感受野（receptive field） | 沿 S83/S85；源等价性断言不扩展为证明 |
| API / prompt / pipeline | API（应用程序编程接口）/ 提示词（prompt）/ 管线（pipeline） | 沿核心及 S88；保留标识符/路径/英文图载荷 |
| model zoo / video captioning / video QA | 模型库 / 视频描述生成 / 视频问答 | 模型名和 API 保留原样 |

## 沿用和消歧

时序/时空、帧/片段/视频分别对应维度与粒度；inflation为沿时间复制权重，不与空洞卷积混同；联合式、分离式、分解式注意力保留原模式区别。Eleven million等值为一千一百万；5-10 points在准确率语境为5-10个百分点；T/8、3-5x、形状、代码、模型及图载荷保持。

## 保护规则

核心及补充表优先。首次出现按本课语境说明，专名、API、模型ID、标识符、路径、URL、公式、数值及代码/图载荷保持；英文没有的章节不补造。源内矛盾、宽泛或版本性断言另列SCOPE，不静默改写技术含义，不把翻译PASS当作运行或安全验证。

只依赖固定英文和术语起草；先修中文正式验收不是门禁。既有政策内质量示例曾附带出现，已披露且未复用；未使用旧中文课程正文、segments或作者记录。语言审校、真实GFM、运行和批次分别记录。
