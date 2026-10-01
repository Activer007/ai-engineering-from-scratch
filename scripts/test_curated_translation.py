#!/usr/bin/env python3
import json
from pathlib import Path
import tempfile
import unittest
from curated_translation import blocks,sha,validate,classify_drift,safe_write,check_record,assemble

EN='# Title\n\nA `key` has 64 values and $5 credit.\n\n```python\nx = 1\n```\n'
ZH='# 标题\n\n一个 `key` 有 64 个值和 $5 额度。\n\n```python\nx = 1\n```\n'

def record(source=EN,target=ZH):
 return {'source_path':'en.md','target_path':'zh.md','source_sha256':sha(source),'target_sha256':sha(target),'segments':[{'segment_id':f'00-04:b{i}','source_sha256':sha(a),'target':b} for i,(a,b) in enumerate(zip(blocks(source),blocks(target)))]}

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
