#!/usr/bin/env python3
import json
import subprocess
import shutil
import sys
from pathlib import Path
import tempfile
import unittest
from curated_translation import blocks,sha,validate,classify_drift,safe_write,check_record,assemble

EN='# Title\n\nA `key` has 64 values and $5 credit.\n\n```python\nx = 1\n```\n'
ZH='# 标题\n\n一个 `key` 有 64 个值和 $5 额度。\n\n```python\nx = 1\n```\n'

def record(source=EN,target=ZH):
 return {'lesson_id':'00-04','status':'draft','schema_version':1,'source_path':'en.md','target_path':'zh.md','source_sha256':sha(source),'target_sha256':sha(target),'segments':[{'segment_id':f'00-04:b{i}','source_sha256':sha(a),'target':b} for i,(a,b) in enumerate(zip(blocks(source),blocks(target)))]}

class CuratedTest(unittest.TestCase):
 def test_lossless_blocks(self):self.assertEqual(''.join(blocks(EN)),EN)
 def test_full_translation(self):self.assertEqual(validate(EN,ZH),[])
 def test_metadata_code_numbers_preserved(self):
  for wrong in [ZH.replace('`key`','`键`'),ZH.replace('64','32'),ZH.replace('x = 1','x = 2')]:self.assertTrue(validate(EN,wrong))
 def test_multibacktick_keyboard(self):self.assertEqual(validate('# X\n\nUse ``Ctrl+` ``.\n','# 标题\n\n使用 ``Ctrl+` ``。\n'),[])
 def test_unlabelled_fence_only_annotation(self):self.assertEqual(validate('# X\n\n```\nx\n```\n','# 标题\n\n```text\nx\n```\n'),[])
 def test_truncated_generation_rejected(self):
  with self.assertRaises(ValueError):blocks('```python\nx')
 def test_no_english_fallback(self):self.assertIn('No Chinese prose; English fallback rejected',validate(EN,EN))
 def test_source_single_paragraph_change(self):
  r=record();changes=classify_drift(r['segments'],EN.replace('64','32'))
  self.assertTrue(any(x['state']=='changed_or_added' for x in changes));self.assertTrue(any(x['state']=='deleted_or_changed' for x in changes))
 def test_move_preserves_segment_identity(self):
  r=record();new=''.join(reversed(blocks(EN)));changes=classify_drift(r['segments'],new)
  self.assertTrue(any(x['state']=='moved' for x in changes));self.assertEqual({x['segment_id'] for x in changes},{x['segment_id'] for x in r['segments']})
 def test_file_rename_preserves_identity(self):self.assertTrue(all(x['state']=='renamed' for x in classify_drift(record()['segments'],EN,renamed=True)))
 def test_concurrent_edit_is_preserved(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'zh.md';p.write_text(ZH+'人工修订\n')
   with self.assertRaises(ValueError):safe_write(p,ZH,sha(ZH))
   self.assertIn('人工修订',p.read_text())
 def test_approved_target_cannot_be_overwritten(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'zh.md';p.write_text(ZH)
   with self.assertRaises(ValueError):safe_write(p,ZH,sha(ZH),status='approved')
 def test_failed_generation_retains_previous_candidate(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'zh.md';p.write_text(ZH)
   for bad in ('','```python\nx'):
    with self.assertRaises(ValueError):safe_write(p,bad,sha(ZH))
    self.assertEqual(p.read_text(),ZH)
 def test_review_counterexamples(self):
  examples=[
   ('# X\n\nTime: -2 ms.\n','# 标题\n\n耗时：2 s。\n'),
   ('# X\n\n$x + 2$ is a value.\n','# 标题\n\n$x + 3$ 是一个值。\n'),
   ('# X\n\n$2 + x$ is a value.\n','# 标题\n\n$2 + y$ 是一个值。\n'),
   ('# X\n\n**Type:** Build\n**Languages:** Python\n','# 标题\n\n**Type:** Learn\n**Languages:** Rust\n'),
   (EN,EN.replace('# Title','# 标题')),
  ]
  for en,zh in examples:self.assertTrue(validate(en,zh),(en,zh))
 def test_duplicate_identity_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/'en.md').write_text(EN);(root/'zh.md').write_text(ZH);r=record()
   for segment in r['segments']:segment['segment_id']='same'
   self.assertIn('Duplicate stable segment IDs',check_record(r,root))
 def test_unknown_and_reviewed_statuses_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'zh.md';p.write_text(ZH)
   for status in ('unknown','language-reviewed','tech-reviewed','approved'):
    with self.assertRaises(ValueError):safe_write(p,ZH,sha(ZH),status)
 def test_real_cli_render_refuses_clobber_and_replays(self):
  with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as output:
   root=Path(d);(root/'scripts').mkdir();shutil.copyfile(Path(__file__).with_name('curated_translation.py'),root/'scripts/curated_translation.py')
   control=root/'i18n/zh/.curated/lessons/00-04';control.mkdir(parents=True)
   (root/'en.md').write_text(EN);(root/'zh.md').write_text(ZH);(control/'translation.json').write_text(json.dumps(record()))
   command=[sys.executable,str(root/'scripts/curated_translation.py'),'render','--output-dir',output]
   first=subprocess.run(command,capture_output=True,text=True);self.assertEqual(first.returncode,0,first.stderr)
   rendered=Path(output)/'zh.md';self.assertEqual(rendered.read_text(),ZH)
   again=subprocess.run(command,capture_output=True,text=True);self.assertEqual(again.returncode,0,again.stderr)
   rendered.write_text('人工改稿')
   refused=subprocess.run(command,capture_output=True,text=True);self.assertNotEqual(refused.returncode,0);self.assertEqual(rendered.read_text(),'人工改稿')
 def test_signed_arithmetic_and_lexical_hyphens(self):
  self.assertTrue(validate('# X\n\nUse -2 ms.\n','# 标题\n\n使用 2 ms。\n'))
  self.assertEqual(validate('# X\n\nA factor-of-10 in mid-2026.\n','# 标题\n\n2026 年中为 10 倍。\n'),[])
 def test_numeric_reordering_requires_same_block_multiset(self):
  self.assertEqual(validate('# X\n\nSubtract 5 from 3.\n','# 标题\n\n从 3 中减去 5。\n'),[])
  self.assertTrue(validate('# X\n\nThe first is 3.\n\nThe second is 5.\n','# 标题\n\n第一个是 5。\n\n第二个是 3。\n'))
 def test_replay_and_rollback(self):
  r=record();self.assertEqual(assemble(r),assemble(json.loads(json.dumps(r))));self.assertEqual(assemble(r),ZH)
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'zh.md';p.write_text(ZH);changed=ZH+'\n'
   safe_write(p,changed,sha(ZH));safe_write(p,assemble(r),sha(changed));self.assertEqual(p.read_text(),ZH)
 def test_hashes_gate_source_and_target(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/'en.md').write_text(EN);(root/'zh.md').write_text(ZH);r=record();self.assertEqual(check_record(r,root),[])
   (root/'en.md').write_text(EN.replace('64','32'));self.assertTrue(any('SOURCE_STALE' in e for e in check_record(r,root)))

if __name__=='__main__':unittest.main()
