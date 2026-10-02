# S36 交付报告：朴素 Bayes

2026-10-02。作者检查和独立全文双审已完成，协调者已实际验证固定内容的 GitHub GFM。聚合验证已完成。快照 **58/523 已审课程草稿、2课进行中、463课未开始**；README另计，发布/合并0，实时总数由PR7单一索引维护。用户发布验收仍未过，最终证据提交后的远端字节/CI查询记录在PR说明和单一索引。网站完整页面、移动布局、交互图、CI 与发布均未标记通过，不把“尚未验证”写成已发生 CI 失败。

## 范围与固定字节

- 唯一课程：`02/14 Naive Bayes`；源 `phases/02-ml-fundamentals/14-naive-bayes/docs/en.md`；目标 `i18n/zh/phases/02-ml-fundamentals/14-naive-bayes/docs/zh.md`
- English commit：`1bafaa88bb4668356791150bec3a6d7df38387eb`；源 blob：`1a77bfdf32803abf06123925554d824f8955e512`
- 源 SHA256：`cda8fef9420715c6fd52a94ea81e2d3a93ae60d32e08a4170ddf8e56696b5a63`
- 最终中文 SHA256：`a2efd527f172dc69a3332ca1e7788604d0eae1d348b2d2311c88d65835e1eb87`
- 源和译文均为 461 行、279 块；120 个候选块中 118 块自然语言新译，MultinomialNB 与 GaussianNB 两个 API 标题原样保留；33 标题、20 围栏、4 表、9 个关键术语、5 练习、4 参考。20 围栏中有 7 Python、1 Mermaid、1 figure、11 个原裸围栏；裸围栏仅加 text，所有载荷不变。
- 43 项依赖的本地文件、固定 Git 对象和 SHA256 已由作者与独立审员核对。只使用固定英文新译；不使用旧中文、缓存或历史翻译 PR。
- 协调者提供的远端上下文：PR #42，support `fbfa810a57d3db1cde65914ca8139dc267a86507`，content `9dc6b438555ff3271db955260ad8a957d8ae1800`。这些信息不代替最终远端字节和 CI 读回。

## 审校与精确差量

作者完整英中技术对照之后，另做一次纯中文全文通读。独立审员未读作者自审，完成全部 120 候选的英中对照、20 围栏保护及最终中文全文通读，最终结论为 PASS_TRANSLATION_WITH_SOURCE_ISSUES，无剩余翻译必改。所有 279 块均绑定源和最终目标 hash。

- 初次冻结 `e059846fc92d96fec1eb6c56bce3d75aeea291268acb7a0b0a412013f2b17381`。中间稿 `f0479d790e34ba9e225553bdbc6d77dbdd00dbbbe66e0f2cefb67abe1602020d` 曾为两处数量加英文并补 TF-IDF 首释，随后按协调结论恢复自然中文数量。
- 恢复过程中一份未绑定暂态 `b63ed9da1bfc3831794735e5e7a0f50dd975f13cc3723e80b3f68a66e0b77b53` 被逆验证发现残留空格，随后定向修正；不是验收稿。完整差量链保存在作者记录中。
- 最终相对初稿仅 b0079：`TF-IDF 值` → `TF-IDF（词频-逆文档频率，Term Frequency - Inverse Document Frequency）值`。精确逆替换恢复初稿全文件 hash；其他 278 块和全部 20 围栏相同。未重新 capture。
- b0017 的 millions of features → 数百万个特征，b0055 的 a million documents → 一百万篇文档，均保留自然中文。逐项等值量级映射已获协调者认可并写入 translation 记录，独立审员已核对。
- 实际 GFM 未要求任何格式修复；最终正文继续冻结。

## 离线控制与实际 GFM

作者与独立审员分别通过原 strict、33 项原控制回归，以及各自两次 Markdown 重放。最终两份重放均与 a2efd527… 逐字节一致。核心 render 只重放 Markdown，不能证明站点布局或交互。

本仓库离线 parser 在最终稿上输出 38,919 字节 HTML、4 表、18 个普通代码块、1 figure 和 1 Mermaid；发现 20 个空标题 ID 与重复 bayes ID，结果为 BLOCKED_SOURCE_RENDERER。该结果保留为源站点解析器局限，不能被 GitHub GFM 通过替代。

协调者使用 dot 云 Chrome 在 immutable content `9dc6b438555ff3271db955260ad8a957d8ae1800` 的实际观察如下；本草案整理者未独立浏览：

- 33 个标题，其中 2 个 API 原名标题；4 个表格含表头分别为 4×4、5×3、8×3、10×3
- 25 个 strong、0 个 em、0 处未解析粗体标记
- 1 幅分类流水线 Mermaid 的全部节点已实际读取并截图；不把该截图算作网站内 figure 交互验证

## 作者运行范围

作者全文预读 344 行 `code/naive_bayes.py` 后，以外部 30 秒 timeout 原样运行，使用已安装、allowlist 内的 NumPy 2.3.5，exit 0。五个原演示分别为 Multinomial 文本、Gaussian 连续特征、两变体比较、训练集大小、混淆矩阵。原样本数、随机种子、alpha 与循环次数未变。

- Multinomial 原测试准确率 1.0000；Gaussian 原测试准确率 0.9823
- 原五个 alpha 取值、七个训练集规模的文本准确率均为 1.0000；这不能证明随规模提高或找到平滑最优点
- 文本混淆矩阵为 [[83,0],[0,77]]。canonical 不包含 sklearn 导入或 sklearn 对照，尽管正文声称有该比较
- 作者另在外置 np 上下文运行两个原正文 fit 类（b0169、b0177），并与 canonical 做 10 组有限核验。缺 np 的 NameError 是独立审员首先复现，不能算作作者做过

作者 10 组有限核验：

1. doc and canonical multinomial fit：{"classes": ["not-spam", "spam"], "feature_probabilities": [[0.05084745762711865, 0.09322033898305086, 0.8559322033898306], [0.5294117647058824, 0.39869281045751637, 0.0718954248366013]]}
2. source example scores versus normalized posterior：{"scores": [-3.1078323225332722, -8.841465285908503], "posterior": [0.9967751313013796, 0.0032248686986203093], "rounded_source_score_second": -8.838, "rounded_source_intermediate_sum": -8.838000000000001}
3. predict_log_proba returns unnormalized scores：{"raw_exp_sum": 0.05599268477275386, "normalized": [[0.002152226014515728, 0.9978477739854842]]}
4. finite large-count normalization：{"probability": [[0.0, 1.0]]}
5. negative input doc/canonical guard difference：{"canonical": "ValueError", "document": "accepts then creates nonfinite log probabilities"}
6. Gaussian doc/canonical fit and zero variance：{"vars": [[1e-09, 1e-09], [1e-09, 1e-09]], "correct": true}
7. Gaussian log-density and posterior normalization：{"manual_scores": [-999999981.8077583, -6499999981.807757]}
8. balanced XOR marginal blind spot：{"multinomial_accuracy": 0.5, "gaussian_accuracy": 0.5}
9. synthetic generator parameter boundaries：{"n_features_201": "ValueError from hardcoded 120 tail", "n_samples_301_actual": 300}
10. alpha-zero absent-word arithmetic boundary：{"alpha1_empty_doc": [0.5, 0.5], "alpha0_empty_doc": "NaN"}

## 独立运行范围

独立审员只运行已完整阅读的两个原正文 fit 类，未读或运行 canonical。先在缺失 np 的原上下文复现 NameError，再明确在外置命名空间提供已安装 NumPy 和合成数组。未给类添加预测方法；额外分数公式是外部核验，不冒充执行正文不存在的方法。

独立审员 9 组有限核验：

1. Shown fit depends on undeclared np：{"exception": "NameError", "message": "name 'np' is not defined"}
2. Multinomial smoothed counts and priors：{"probabilities": [[0.6666666666666666, 0.3333333333333333], [0.25, 0.75]], "prior": [0.5, 0.5]}
3. Source mail log expressions are scores before normalizing：{"normalized_posterior": [0.9967751313013796, 0.003224868698620312], "raw_exp_sum": 0.04484235138331929, "exact_smoothed_log_scores_before_normalization": [-3.1078323225332727, -8.841465285908503]}
4. alpha0 allows infinities and zero-times-logzero NaN：{"feature_log_probs": [["0", "-inf"], ["-inf", "0"]], "sample_log_scores": ["NaN", "-inf"]}
5. Gaussian population moments plus fixed variance floor：{"means": [[1.0, 2.0], [5.0, 6.0]], "variances": [[1e-09, 1e-09], [1e-09, 1e-09]], "priors": [0.5, 0.5]}
6. Gaussian output is density and can exceed1：{"density_at_mean": 12615.6626101008}
7. Duplicated correlated evidence can change class ordering：{"true_joint_odds_duplicate_is_same_event": 0.75, "naive_product_odds": 2.25}
8. Strong99percent prior need not overwhelm evidence：{"prior_odds": 0.010101010101010102, "likelihood_ratio": 1000, "posterior_odds": 10.101010101010102}
9. Smoothing probabilities sum to1：{"spam": 1.0, "not_spam": 1.0}

两个角色均未加载 sklearn，5 个 sklearn 正文段均未运行，未安装库、下载外部数据或模型、调用网络/模型 API。有限示例通过不等于教材所有强断言、概率校准、库兼容性或生产性能通过。

## 源问题与验证边界

作者归纳 14 组、独立审员归纳 15 组，分组重叠，不能相加算作 29 个不同问题。以下保留独立审的 15 组定位摘要，正文与公式均未暗修：

1. **条件独立并非数学上必错、排序也非保证**（02-14:b0003, 02-14:b0009, 02-14:b0017, 02-14:b0019, 02-14:b0037, 02-14:b0043, 02-14:b0049, 02-14:b0051, 02-14:b0053, 02-14:b0251, 02-14:b0259）：条件独立是模型假设，某些数据生成过程可成立，不是数学上固有错误。违背假设会改变概率与类别排序，冗余重复计数不保证抵消。有限先验odds=.25、重复证据LR=3示例，真实同事件odds=.75而朴素重复乘积=2.25，类别判断翻转。P=.7意味着多数类而非每个样本标签保证。
2. **模型比较与高维几何强断言**（02-14:b0015, 02-14:b0017, 02-14:b0019, 02-14:b0051, 02-14:b0055, 02-14:b0141, 02-14:b0143, 02-14:b0197, 02-14:b0257, 02-14:b0269）：高维距离集中不等于所有点距离严格相等，KNN是否有用依数据内在结构。正则化等影响LR/树表现；NB小样本必优、大样本LR必学真边界、单遍几秒百万文档、快几个数量级均依实现与数据。未运行性能基准或研究当前库速度。
3. **联合分布与计数模型的范围**（02-14:b0035, 02-14:b0039, 02-14:b0041, 02-14:b0075, 02-14:b0079, 02-14:b0081）：2^10000对应二元出现向量，词计数的组合空间不同。Multinomial计数在固定总数下并非独立计数变量；教材常以条件独立词项事件得到计数加权对数分数。并非每种NB每特征仅需一个计数，Gaussian需矩统计量。
4. **邮件例子和对数后验缺归一化**（02-14:b0061, 02-14:b0065, 02-14:b0067, 02-14:b0069, 02-14:b0071, 02-14:b0129, 02-14:b0151, 02-14:b0165, 02-14:b0167）：邮件示例的对数值为未归一化分数，非完整log posterior；多项式系数和证据项在分类比较可消去。predict_log_proba段也应区分得分与归一化API语义，并显式词次数权重。精确平滑比率得到分数约[-3.107832,-8.841465]，归一化概率约[.996775,.003225]；源小数按舍入保留。
5. **变体分布和缺席证据**（02-14:b0087, 02-14:b0089, 02-14:b0091, 02-14:b0095, 02-14:b0097, 02-14:b0099, 02-14:b0103, 02-14:b0179, 02-14:b0221）：Gaussian式是密度而非点概率，密度可大于1；连续特征不保证类内独立正态。Bernoulli缺席对类别比较的证据取决于两类缺席概率，不是任何缺席都惩罚所有类别。短文本哪个模型最佳依数据，不由长度单独决定。有限方差1e-9在均值密度约12615.66。
6. **平滑的词表、先验和超参数条件**（02-14:b0107, 02-14:b0109, 02-14:b0111, 02-14:b0113, 02-14:b0115, 02-14:b0117, 02-14:b0121, 02-14:b0263）：平滑保护已建词表内某类未出现的特征，不自动处理整个训练词表之外的字符串。alpha=1的均匀Dirichlet解释对应后验均值等具体估计方式；一般alpha是对称先验而非所有alpha都均匀。表内推荐并非最佳alpha保证，验证集选择与数据规模有关。
7. **对数计算和零值输入边界**（02-14:b0125, 02-14:b0127, 02-14:b0129, 02-14:b0133, 02-14:b0151, 02-14:b0169）：多个小概率相乘可能下溢但不是所有数百概率必然下溢。log不能消除真正零概率或非法输入；alpha=0时出现-inf，0计数乘-inf会成NaN。原类不校验alpha、负计数、空训练集、shape等，有限alpha0夹具复现NaN。
8. **正文fit缺少外部np上下文**（02-14:b0157, 02-14:b0163, 02-14:b0165, 02-14:b0167, 02-14:b0169, 02-14:b0173, 02-14:b0177, 02-14:b0209）：两个展示类只含fit且引用未导入np，不能独立拼接后视为完整预测实现。独立审先复现NameError，再在外部明确提供已安装allowlist NumPy与合成数组，仅运行原fit。未添加预测方法；外部公式核验不冒称执行了正文不存在的方法。canonical及其sklearn对照未由本独立审读取或运行。
9. **固定方差项与特征缩放**（02-14:b0177, 02-14:b0239, 02-14:b0243）：代码用总体方差ddof0再固定加1e-9，与按数据尺度的库实现不能无条件等同。Gaussian在理想模型下对可逆特征线性缩放的分类具有特定不变性，但固定加性方差项与浮点精度会改变结果；Multinomial改变计数尺度会改变似然/先验的相对作用。
10. **TF-IDF、负值与特征平移建议**（02-14:b0079, 02-14:b0213, 02-14:b0215, 02-14:b0217, 02-14:b0237）：常见词并非必定无类别信息，稀有词也未必有区分力。非负TF-IDF作为MultinomialNB权重是常用应用，不是严格整数多项式计数模型。源同时说TF-IDF非负与某些设置可负，需明确具体变换；把负值平移为正不保证保留原模型意义或Gaussian假设。
11. **库API及校准说明的验证范围**（02-14:b0201, 02-14:b0203, 02-14:b0207, 02-14:b0215, 02-14:b0223, 02-14:b0225, 02-14:b0229, 02-14:b0231, 02-14:b0233, 02-14:b0241）：BernoulliNB默认二值化行为、class_prior与各变体参数名、CalibratedClassifierCV的分数接口/折内拟合依库实现与版本；本审未导入sklearn，故不为源精确API断言背书。校准需足量且代表性的留出数据，不能保证概率总更接近真实频率。外部示例还依赖X/train_texts/Pipeline等共享上下文。
12. **类别不平衡与后验**（02-14:b0241）：99%先验不一定压过任意似然。有限演算(.01/.99)*1000约10.101，少数类足够强的似然证据仍可胜出；手改先验改变目标分布，不能当作普遍校准方法。
13. **失效模式的范围与反例描述**（02-14:b0253, 02-14:b0255, 02-14:b0257, 02-14:b0259）：均衡XOR原特征单独无信息是特定结构，但不能从中推导所有NB均无非线性边界，Gaussian类方差不同可产生二次边界。源所谓完全相关但提供相反证据的例子未给联合分布，解释不充分。LR也不是任意真实边界的万能估计，足量数据不能消除模型误设。
14. **合成演示、练习与参考范围**（02-14:b0183, 02-14:b0185, 02-14:b0189, 02-14:b0191, 02-14:b0247, 02-14:b0263, 02-14:b0265, 02-14:b0267, 02-14:b0269, 02-14:b0271, 02-14:b0279）：合成分布是构造条件，非现实性能证明；本审不运行外部数据、sklearn比较或绘图练习，不将教材的训练集规模/收益陈述作为实测。4参考原题/作者/年/URL保持，Ng/Jordan结果的假设及外部材料未扩展研究。
15. **保护载荷与实际GFM边界**（02-14:b0027, 02-14:b0039, 02-14:b0065, 02-14:b0069, 02-14:b0081, 02-14:b0089, 02-14:b0097, 02-14:b0113, 02-14:b0129, 02-14:b0133, 02-14:b0147, 02-14:b0151, 02-14:b0153, 02-14:b0195, 02-14:b0275）：20围栏逐字保护，11个原裸围栏只加text；表中转义条件竖线、公式和API大小写原样。运行时密度/对数风险不改变原公式。中文粗体标签后空格已观察源码，裸乘号是否意外强调仍待协调者真实GitHub GFM，离线parser不等于实际站点验收。

独立风险第 15 组中“实际 GFM 待查”的历史状态已由上文协调者浏览器观察更新；站点 parser、完整网站、移动与交互边界仍然有效。作者另确认 canonical 无 sklearn 比较、200 维文本生成器的硬编码边界、301 请求样本实际生成 300、零 alpha/缺席词可产生 NaN；这些事实不触发翻译中的源修正。

## 交付边界

仅本fork draft，无merge/部署/上游写入/Actions启用。新增两条作者线10/03和12/04已按用户扩容要求实际开始，未计入已审课程。CI查询空数组不是成功；实际站点与用户发布验收保持未过。

## 协调者联合验证

组合 **56课原strict + S07精确符号表例外 + S19精确两行竖线适配**，58课两次输出逐字节一致。原33/S07的24/S19的50控制及523课/67认证课/12评测/505题审计、README/book计数通过，英文/源码/通用控制未改。核心只重放Markdown，全部清单SVG单独核hash复制到两个输出并参与整体比较。最终提交后的远端全文件字节、PR元数据和CI查询另记于PR完成说明/单一索引，不冒称发布或CI通过。
