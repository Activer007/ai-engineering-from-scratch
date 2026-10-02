# S06 矩阵变换术语增量 v1.0

2026-10-02。联用核心、试点及S05术语；本课由二维几何进入实/复特征值，必须按语境区分，不覆盖既有词义。API、路径、数字、单位、公式和18个围栏载荷保持原样。

| EN | 推荐呈现 | 语境 / 保护规则 |
|---|---|---|
| transformation / composition | 变换 / 复合 | A后B对应B @ A，不能随中文语序倒置乘法 |
| basis vector | 基向量 | 矩阵列给出标准基向量的像；不是行 |
| rotation / scaling | 旋转 / 缩放 | 角度单位、正负号、顺/逆时针与轴保持 |
| shear / shearing | 剪切（shear）/ 剪切变换 | 不强译成切割；源双参数实现的面积条件单列 |
| reflection | 反射（reflection） | 明确关于哪条轴，不能改成沿轴方向的反射 |
| eigenvalue / eigenvector | 特征值 / 特征向量 | 保留首现英文；不同于奇异值/奇异向量 |
| eigendecomposition | 特征分解（eigendecomposition） | 源可对角化条件完整保留；通常换基不一定纯旋转，源问题单列 |
| characteristic equation | 特征方程（characteristic equation） | 行列式等于零的方程，不改公式 |
| diagonal matrix | 对角矩阵 | Λ、对角元与V、V⁻¹对象原样 |
| determinant | 行列式（determinant） | 数值符号与绝对值严格区分；源绝对值错误忠实保留并单列 |
| trace | 迹（trace） | 矩阵对角元之和；不是调试跟踪 |
| orientation | 取向（orientation） | 行列式负号改变取向；不是单个向量指向 |
| magnitude | 绝对值 / 模 | 实特征值取绝对值，复特征值取模；向量语境仍为模长，勿统一成维数 |
| stretches / flips / collapses | 拉伸 / 翻转 / 压缩（坍缩） | 跟随源具体维度对象；不用术语选择偷偷修正源结论 |
| change of basis | 换基 | 源文写rotation时译旋转，另记技术缺陷，不静默重写 |
| principal component / PCA | 主成分 / 主成分分析（PCA） | 固定数学语境；缩写保留 |
| recurrent neural network / RNN | 循环神经网络（RNN） | 不将特征值大小的教学概括强化成完整梯度判据 |

Matplotlib、NumPy、Python、Julia、ReLU、API与类名保留。裸数学/说明围栏可仅加text标签，载荷不变；若确有GFM乘号转义需要，只做最小可逆修复并记来源/目标hash。技术修正不属于本翻译阶段。
