# S19：仅两行 GFM 范数竖线的失效封闭适配

本扩展只处理 01/17 `Linear Systems` 的关键术语表两行，不修改核心控制或 S07 的适用范围，不改变任何数学含义。源表的未转义范数竖线被 GitHub GFM 当作额外列分隔符，导致后半内容丢失。协调者已明确批准在中文表这两行的八个竖线前各插入一个反斜杠。独立审校未完成时，实际作者记录仍为 `draft`，本适配必须拒绝通过或重放。

## 固定绑定

- 课号：`01-17`
- 英文基线：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 英文路径：`phases/01-math-foundations/17-linear-systems/docs/en.md`
- 中文路径：`i18n/zh/phases/01-math-foundations/17-linear-systems/docs/zh.md`
- 核心检查器 SHA256：`d89de5eec36e10edcc391330d973632e3ceedb33fe679de3503dab52a7f6ece8`
- 英文全文 SHA256：`de9a2c0f1e09351e6061834a651110bdab18ae3df534315ea2a62a33a156af49`
- 原作者稿 SHA256：`bc3f3ad518bb5df4d47d6edc1533608dc1f8f4ff8a36ef059b9c893c0a6d3c4d`
- 修后中文 SHA256：`f6528cdd6f2c1bf70d86828e7c9b02e9308311c142e05dc0df1b007bb3c33305`
- 唯一表块：`01-17:b0245`，完整 249 块中的零基索引 244
- 英文表 SHA256：`68ad5dd85bd0e7abbd8c9261ad7a68a71c213d664d6ad8a297f41bd630d1be45`
- 原中文表 SHA256：`c5adc6b46c0e132478c6195e5968cf01a6a45cc151ba6024643091c259355953`
- 修后中文表 SHA256：`a33b6d0aea9afd64cb45f699831103665043186feaff2ce4c0d369c22d790ba5`

表内零基行索引 8 和 9（含表头、分隔行计数）各有一个 `||Ax - b||`，且仅它们改为 `\|\|Ax - b\|\|`。正文其他范数、代码、公式、图载荷全部保持原样。

## 校验顺序与失败语义

1. 所有适配器输入通过目录文件描述符逐组件 `O_NOFOLLOW` 打开，最终文件还须为普通文件；不沿输入 symlink 读取外部目标。核心文件只读取一次，先对这份字节做 SHA256 校验，再直接 `compile/exec` 同一份字节；不二次导入文件路径，也不使用 pyc。原 core 调用前还会对其记录指定的源/目标、核心和附加词表、assets 输入做无跟随预检；原 core 保持不变并继续执行它自身的路径保护。
2. 对实际记录完整执行原 `core.check_record(record, root)`。任何来源 Git、source blob、全文 hash、术语、review、结构、代码、数值或其他错误都保留。原 strict 不放宽，正确修后稿在原 strict 下仍应只得到 `table_columns mismatch`。
3. 绑定课号、固定源/目标路径、英文提交、全文源 hash、修后目标 hash、完整 249 块的 ID/目标文本/逐块目标 hash，以及对应表的源 hash。
4. `translation.json` 与独立 `review.json` 的状态均须为 `language-reviewed`。review 的身份字段及 `reviewed_target_sha256` 必须绑定修后字节；原 core 继续核查它的 source blob、术语等绑定。
5. review 中必须只有一个符合下面协议的 `gfm_table_repairs` 条目。布尔值必须是真正的 `true`；行号必须是仅含两个精确整数的列表 `[8, 9]`，不能用浮点数或布尔值替代；反斜杠数量必须是精确整数八；理由须为非空字符串。字段缺失、多出、重复或 hash/行号不符都拒绝。
6. 只逆转该表的两处指定范数中的八个反斜杠。必须同时还原原中文表 hash 与完整原稿 hash，字符差严格为八，反斜杠差也严格为八。以还原后的稿件执行原 `core.validate(source, normalized_target)`，必须返回空错误列表。
7. 所有窄范围绑定成立后，才从完整原错误列表中删除一次、且仅一次确切字符串 `table_columns mismatch`。其他错误原样留下；重复诊断仍留一个，因此仍失败。缺失该诊断也失败封闭。只有完整原错误列表恰为这一个诊断时才能得到成功。

本扩展不是普遍的 Markdown 规范化器。新增修复、别的课文、表格改写或源更新都不能复用这里的批准；应重新决定范围并完成新审校。

## 独立 reviewer 的协议示例

以下仅为协议示例，不是实际独立审批准，不能由作者据此声称审校完成。独立 reviewer 在全文英文技术对照和另次中文通读完成后，才能将对应批准写入真实的 `review.json`。真实 review 仍须包含原 core 要求的所有身份/术语/状态字段以及修后 `reviewed_target_sha256`。

```json
{
  "status": "language-reviewed",
  "reviewed_target_sha256": "f6528cdd6f2c1bf70d86828e7c9b02e9308311c142e05dc0df1b007bb3c33305",
  "gfm_table_repairs": [
    {
      "segment_id": "01-17:b0245",
      "source_table_sha256": "68ad5dd85bd0e7abbd8c9261ad7a68a71c213d664d6ad8a297f41bd630d1be45",
      "original_target_table_sha256": "c5adc6b46c0e132478c6195e5968cf01a6a45cc151ba6024643091c259355953",
      "repaired_target_table_sha256": "a33b6d0aea9afd64cb45f699831103665043186feaff2ce4c0d369c22d790ba5",
      "row_indices_zero_based": [8, 9],
      "inserted_backslashes": 8,
      "classification": "gfm-table-norm-pipe-escape",
      "independent_review_passed": true,
      "reason": "示例占位：独立 reviewer 应写入自己实际完成检查后的理由。"
    }
  ]
}
```

`expected_approval()` 只是程序内的协议常量，既不读取也不生成真实批准。测试中的 review 都是明确标记的临时合成夹具，测试通过不意味着真实独立审校已完成。作者自查仍绑定原稿 hash，不能自动继承为修后独立审校。

## 安全重放

通过上述全部校验后，可以把同一份已校验的内存记录重放到 checkout 外。不会第二次读取可能被并发修改的作者记录。

- 输出目录不得含 `..`，不得在 checkout 内，不接受任何已有路径组件为 symlink
- 目标路径固定为本课中文路径，不从记录接受任意输出路径
- 逐级目录创建/打开使用目录文件描述符和 `O_NOFOLLOW`，拒绝中间目录或最终文件 symlink
- 组装字节再次绑定修后全文 hash
- 新目标使用 `O_CREAT | O_EXCL | O_NOFOLLOW`，不覆盖并发创建的文件
- 已有目标只允许普通文件且字节完全相同；不同内容、FIFO 等非普通文件拒绝，原内容不变
- 即使并发创建碰撞，检查失败也不会通过覆盖来恢复

这是离线作者记录重放，不是课程程序执行、GitHub 发布、网站渲染或最终网页验收。

```bash
python3 scripts/curated_translation.py check --id 01-17
# 对正确修后稿预期仍 FAIL，且只有 table_columns mismatch
python3 i18n/zh/.curated/stages/S19-linear-systems/test_stage.py
python3 i18n/zh/.curated/stages/S19-linear-systems/check_stage.py
python3 i18n/zh/.curated/stages/S19-linear-systems/check_stage.py --output-dir /tmp/s19-reviewed-replay-a
python3 i18n/zh/.curated/stages/S19-linear-systems/check_stage.py --output-dir /tmp/s19-reviewed-replay-b
```

真实 review 尚未就绪时后面三条必须 FAIL，不能为了运行重放填造批准。通过全部绑定后，适配成功标签为 `PASS_WITH_REVIEWED_GFM_REPAIR`。原站中文空锚点/重复锚点、实际 GitHub GFM 验证、有限课程运行与源技术错误继续分开记录，适配不能豁免这些门槛。

## 独立控制审后的补强

输入 symlink 外读、核心 hash 到执行的二次路径读取、浮点行号与整数行号相等，这三项由独立控制审指出并加入回归。当前测试为 50 项：包括固定输入/记录选定 asset 的外链被拒绝且外部文件未打开读取、目录 symlink、非普通文件，以及 hash 后替换核心路径仍只执行先前已验证的字节。所有批准仍为测试临时夹具，不写真实 review。
