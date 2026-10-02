# S47 集成方法审校交付报告

2026-10-02 协调终验补记：累计 69 课联合严格检查及两次字节重放通过（67课原strict，既有S07/S19精确适配各1；无新增例外），原33回归和24/50适配防护及仓库数量审计通过。联合验收快照 69/523、4课仍进行中、450课未开始，实际完成总数以PR #7单一索引的最终读回为准。下文作者交接时的聚合pending已由本补记关闭。最终证据提交后远端全文件与CI查询在PR说明/单一索引独立读回记录；final_acceptance=false指完整网站和用户发布验收，不是省略翻译审核。未合并、未发布。

仅从固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb` 新译 02/11；来源 SHA256 `64b7a605139b29e5400bd8d0d44a77a977dd4787e3140133d9f4c05f162e2532`，最终正文 `450b636656f9fc103940bb432af55af1894cc2fafd6af626f0687d8d37859cdf`。PR #53 为 fork 内草稿。先修 02/10 已审，56项术语/控制依赖固定。

## 全文审校与保护

355行、155块、68候选块均完成作者英中对照及另次中文通读；非作者独立再做完整技术对照与中文通读并逐块绑定，无未解决翻译必改项。10围栏保护，代码/公式/API/路径不改。原strict、33回归、作者和审员各自双目录重放通过。

## 有限运行边界

作者完整预读502行canonical，仅以非main模块调用6个原NumPy/标准库演示，默认轮次不改，另16项有限核验；第7个sklearn演示与main未运行。原正文缺np先复现，再用外部明确NumPy上下文；缺少SimpleRegressionTree仅在有限外置夹具提供源代码原实现。审员只检查文档，10项有限核验、原50轮AdaBoost；未提供SimpleRegressionTree、未跑完整GBM/canonical/sklearn。不存在完整所有代码验收的声明。

## 实际 GitHub 渲染

协调者在自己的dot云Chrome亲自检查固定内容commit `91d0df40804c9cb0cd997a8cf2c7902382770550`：24标题、7×4和10×3完整表、15strong、0em、无残留粗体。全文及10围栏载荷可读；三幅Mermaid实际iframe的11/9/9节点全部读取并视觉核对。Bagging与Stacking用顶部/底部缩放视图覆盖，Boosting用展开对话框完整显示。figure仅显示保护代码占位，不代表原站交互通过。没有新格式修改。

## 英文源问题（保留原意，未暗修）

- {"id": "S47-peer-source-01", "category": "weak_to_strong_theorem", "blocks": ["b0003", "b0009"], "finding": "弱学习到强学习的定理需要相应学习问题、分布及弱优势条件；任意弱模型组合不保证提高。源学习目标忽略条件。", "source_changed": false}
- {"id": "S47-peer-source-02", "category": "majority_vote_arithmetic", "blocks": ["b0021", "b0023", "b0025"], "finding": "按源独立同准确率二项式公式，21个p=.6模型多数正确概率为0.8256221336382272，101个为0.9791033089952995，与源74%/84%不符；译文保持源数字。偶数票数还需平局规则。", "source_changed": false}
- {"id": "S47-peer-source-03", "category": "diversity_vs_independence", "blocks": ["b0027", "b0039", "b0151"], "finding": "错误必须不相关是过强必要条件；相关系数0.9的10个等方差模型均值方差仍可为0.91<1。独立、不相关与多样性不等价，有限公式不证明任何数据上的准确率保证。", "source_changed": false}
- {"id": "S47-peer-source-04", "category": "bootstrap_and_bagging", "blocks": ["b0037", "b0039"], "finding": "63.2%/36.8%为大样本近似；有限n袋外概率(1-1/n)^n，n2为.25。袋外评估仍需防调参选择偏差；Bagging降方差和不增偏差并非无条件。", "source_changed": false}
- {"id": "S47-peer-source-05", "category": "algorithm_performance_claims", "blocks": ["b0013", "b0015", "b0049", "b0071", "b0123"], "finding": "单树必过拟合、Bagging仅降方差/Boosting仅降偏差、低学习率必泛化更好、Kaggle/生产占比均是简化或经验断言，没有统一保证。", "source_changed": false}
- {"id": "S47-peer-source-06", "category": "random_forest_and_xgboost_options", "blocks": ["b0041", "b0077"], "finding": "候选特征sqrt或三分之一、每层/每树/每节点列子采样、加权分位草图等依算法模式与库版本；本任务未运行外部库验证当前默认。", "source_changed": false}
- {"id": "S47-peer-source-07", "category": "adaboost_assumptions", "blocks": ["b0055", "b0059", "b0109"], "finding": "指数更新假定y及预测为-1/+1，任意基学习器须支持样本权重和弱优势；代码未拒绝0/1标签，未处理err>=.5/完美分类提前结束。", "source_changed": false}
- {"id": "S47-peer-source-08", "category": "stump_threshold_boundary", "blocks": ["b0105"], "finding": "只枚举观测阈值且用严格小于，恒定特征不能产生全负预测：有限夹具返回全正加权错.8，但全负可达.2，源实现存在边界限制。", "source_changed": false}
- {"id": "S47-peer-source-09", "category": "adaboost_state_and_ties", "blocks": ["b0109"], "finding": "fit不清空stumps/alphas，原50轮重复fit累积100树；err=.5时alpha0、预测sign0为0，超出已述二值标签；未fit也返回标量0，空训练除零。", "source_changed": false}
- {"id": "S47-peer-source-10", "category": "document_execution_context", "blocks": ["b0105", "b0109", "b0113"], "finding": "正文三类均无np导入，实际先复现NameError后外置绑定NumPy；SimpleRegressionTree没有正文定义，本审不补替代实现，原100树梯度提升首次迭代就NameError。", "source_changed": false}
- {"id": "S47-peer-source-11", "category": "gradient_boosting_loss_scope", "blocks": ["b0065", "b0067", "b0069", "b0113"], "finding": "任意损失需可求相应负梯度/次梯度；平方损失负梯度等于残差需要1/2系数约定。正文实现仅平方误差回归返回连续值，非通用分类梯度提升。", "source_changed": false}
- {"id": "S47-peer-source-12", "category": "tabular_dominance_and_successor", "blocks": ["b0079", "b0127", "b0131"], "finding": "XGBoost始终优于神经网络、LightGBM为其后继者、未来不改变等源陈述过于绝对，依数据/预算/版本；不把固定课文视作最新推荐。", "source_changed": false}
- {"id": "S47-peer-source-13", "category": "stacking_routing_and_leakage", "blocks": ["b0087", "b0089"], "finding": "元学习器未必学到显式区域路由；需折外或独立留出预测，源must交叉验证的说法排除了有效留出方案。全训练集范围与每折排除样本的语义应区别。", "source_changed": false}
- {"id": "S47-peer-source-14", "category": "soft_voting_calibration", "blocks": ["b0095"], "finding": "概率均值更好依赖校准/质量/多样性，不以较高自信保证正确；源通常限定已保留。", "source_changed": false}
- {"id": "S47-peer-source-15", "category": "unexecuted_library_comparison", "blocks": ["b0117", "b0139", "b0141", "b0143", "b0145", "b0147"], "finding": "与sklearn相近准确率、100树随机森林、早停、堆叠、XGBoost速度等实验未由本审执行；canonical含外部sklearn路径而未读取或运行整个文件。", "source_changed": false}
- {"id": "S47-peer-source-16", "category": "diagrams_and_outputs", "blocks": ["b0035", "b0047", "b0085", "b0097", "b0135"], "finding": "三个Mermaid与figure注册标识逐字保护，未实际浏览其渲染；两输出提示词/技能仅路径与说明被审，不执行其指令。", "source_changed": false}

## 剩余门槛

聚合重放、最终远端全文件字节及精确head CI查询由协调终验回填。Actions未启用；空CI结果不是通过。完整课程网站、移动/交互与用户发布验收未通过，final_acceptance=false。未合并、未发布。
