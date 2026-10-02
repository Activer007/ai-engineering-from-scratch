# S39 模型评估：审校交付报告

2026-10-02 统一终验补记：本课及累计 59 课联合严格检查、两次逐字节重放通过（原 strict 57 课，既有 S07/S19 各一精确适配；没有新增例外）。原回归 33、两适配防护 24/50、仓库数量审计全部通过。快照 59/523 已审草稿、4 课进行中、460 课未开始。下文作者交接时的聚合 pending 已由本补记关闭；最终证据提交后的远端全字节及 CI 查询在 PR 说明与 PR #7 单一索引读回记录，避免自引用提交。final_acceptance=false 专指用户发布/完整网站验收，未合并或发布。

2026-10-02。本课 02/09 从固定英文独立新译。作者技术自查和另遍中文通读、独立全文双审均完成，133 块及最终中文 hash 全部绑定，无剩余翻译必改。

## 固定范围

- 英文 commit：`1bafaa88bb4668356791150bec3a6d7df38387eb`；SHA256：`4c0ac1f4722a3525dd3dbc7290238a75ac414b195c7715129db05ec36a99619e`
- 中文 SHA256：`4291afe5638cfc450bb5d0571182c7f4dca47e097a4b8f1c7397f33c61fab7fc`
- 679 行、133 块、57 可译块、23 标题、10 围栏、2 表、3 练习、3 参考，46 项固定依赖已核验
- [PR #44](https://github.com/Activer007/ai-engineering-from-scratch/pull/44)；[实际 GFM 固定正文](https://github.com/Activer007/ai-engineering-from-scratch/blob/6b3bfeb371bde823dc92aba390d427e1222653c8/i18n/zh/phases/02-ml-fundamentals/09-model-evaluation/docs/zh.md)

## 技术与中文审校

作者完整读取英文，逐块新译并完成独立于对照的中文通读。另一作者不读作者 QA，完成全部英中技术对照及另遍 679 行中文通读；源技术缺陷单列，未暗修英文、代码、公式或技术结论。术语、API、数字、路径和保护载荷均保留，未引入新控制例外。

## 有限运行边界

作者完整预读 461 行 Python canonical 后原样运行 8 个演示，另外执行 6 个标准库正文块。原 100/200/500 轮、300/200 样本、种子不改；canonical 与正文演示 stdout 一致。21 项有限行为检查及 1 项固定 Git 字节核验通过。

独立审员仅完整预读并执行 6 个原标准库正文块及 10 组有限检查，未读或运行 canonical。Julia 380 行仅清点，未完整读取或运行；Julia 不可用。sklearn 例未执行，没有安装、下载或模型调用。有限检查包括复现源错误，不代表全部示例正确或生产可用。

## 实际 GitHub GFM

协调者亲自在 dot 云 Chrome 检查固定正文：23 标题，两表含表头 3×3、10×3，25 strong、0 em、0 未解析粗体。两幅 Mermaid 的全部 iframe 标签已读取并截图；五折图很宽，默认缩放较小，节点及均值路径完整，无载荷更改。另看回归公式和完整术语表截图。figure 只显示代码标识，不代表站点交互通过。本课无 GFM 格式修复。

## 独立审校列出的 13 组源风险

1. Generalization and blanket claims：Train score alone is not unseen-data evaluation but does not prove memorization. Holdout estimates depend on representative sampling and distribution; neither holdout nor sound evaluation guarantees arbitrary production performance.
2. Splits and CV assumptions：Coherent ratios, finite rounding, time/group separation and dependence matter. Label stratification alone is insufficient for temporal or grouped observations. CV is not always more stable than every holdout. Source single-use test principle preserved.
3. Fold remainder and validation errors：kfold(12,5) gives validation sizes[2,2,2,2,4]. Stratified8majority/2minority,k5 gives sizes[1,1,1,1,6] and minority[0,0,0,0,2], contrary to approximate class-ratio aim. k>n/zero k/ratios/shapes not validated; random.seed mutates global state.
4. Confusion metrics scope：Single fixed confusion matrix does not yield every ROC or regression metric. Metric choice depends on costs/prevalence, not clinical/fraud labels alone. Functions assume0/1; zip silently truncates unequal inputs. accuracy([2,2],[2,0])=0 and accuracy([0,1],[0])=1 reproduced. Empty denominator0 is a convention.
5. ROC/AUC missing origin and range：roc_curve omits threshold above maximum and initial(0,0). Labels[0,1],scores[.5,.5] give only(1,1) and AUC0 instead of tied ranking0.5. Perfect ranking1 and reverse ranking0 demonstrated; source0.5–1 term-table range wrong. One-class ROC and AUC0.5 interpretation require conditions.
6. Regression metric boundaries：R2 variance-explained interpretation has conditions. Zero baseline refers to evaluation-set mean; demo uses training mean and obtains negative baseline. Constant perfect target returns0. Empty MSE raisesZeroDivisionError and unequal lengths can return misleading0. Normal MSE/MAE/R2 fixture checked.
7. Learning and validation curve heuristics：High score reasoning assumes higher-is-better; bias/variance diagnosis and adding data are not guarantees. n5 default subset rounds to0 then raisesIndexError. Requested size50 on8-item pool reports50 but actually trains8. Same fixed validation used repeatedly.
8. Demo scaling leakage：Original regression demo standardizes full X_reg columns before split, contradicting split-first guidance. Finite fixture full mean33.6667 versus train-only.5; no source repair. Executed unchanged demo output is not a clean leakage-free evaluation claim.
9. Paired t statistic：Code divides variance byK rather thanK-1, inflating nonzero statistic bysqrt(K/(K-1)); fixture ratio1.11803398875 forK5. Overlapping CV training folds violate ordinary independent paired-sample assumptions without further treatment. Fixed df4 threshold requires assumptions; zero std forces t0 even if mean nonzero.
10. Toy estimators and demonstrations：Clipped sigmoid, online updates, no convergence/input/shape checks. Linear regression divides each online update byn and omits factor2 relative to full squared loss; learning-rate meaning differs from batch MSE. Original seeds/data sizes/100,200,500 epochs unchanged; synthetic single runs are not general benchmarks.
11. External library excluded：sklearn example not run or installed; source library parity/current defaults unverified. No network, external datasets/models or outputs skill execution. Reviewer did not read or run canonical; only fully read original document blocks used.
12. Exercise definitions：Average precision is not automatically trapezoidal PR AUC. Nested CV must include inner-fold preprocessing/tuning. Label permutation assesses association under exchangeability; model-comparison difference statistic and finite Monte Carlo p-value convention unstated.100 repeats yield coarse resolution. Exercises not implemented.
13. Protected visuals and references：2 Mermaid/1 figure payload unchanged. Raw multiplication symbols kept for actual GFM.3 references retained, not opened. Offline parser15 empty IDs; not live website/mobile/interaction acceptance.

这些问题保留忠实译文并列入结构化证据。原站 parser 的 15 个中文空锚点仍未解决；完整网站、移动端、交互图、托管 CI 和用户发布验收未通过。
