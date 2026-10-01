#!/usr/bin/env python3
import copy
from contextlib import contextmanager
import hashlib
import json
import subprocess
import shutil
import sys
from pathlib import Path
import tempfile
import unittest
from curated_translation import blocks,sha,validate,classify_drift,safe_write,check_record,check_assets,assemble,ROOT,CONTROL,record_path,SOURCE_COMMIT

EN='# Title\n\nA `key` has 64 values and $5 credit.\n\n```python\nx = 1\n```\n'
ZH='# 标题\n\n一个 `key` 有 64 个值和 $5 额度。\n\n```python\nx = 1\n```\n'

def record(source=EN,target=ZH):
 return {'lesson_id':'00-04','status':'draft','schema_version':1,'source_path':'en.md','target_path':'zh.md','source_sha256':sha(source),'target_sha256':sha(target),'segments':[{'segment_id':f'00-04:b{i}','source_sha256':sha(a),'target':b} for i,(a,b) in enumerate(zip(blocks(source),blocks(target)))]}


@contextmanager
def production_fixture():
 """Copy only a new pilot lesson into /tmp; read pinned Git objects without mutation."""
 with tempfile.TemporaryDirectory() as d:
  root=Path(d)
  lesson_id='00-04'
  rp=CONTROL/'lessons'/lesson_id/'translation.json'
  review_path=rp.with_name('review.json')
  r=json.loads((ROOT/rp).read_text())
  required=[rp,r['source_path'],r['target_path'],CONTROL/'TERMINOLOGY.md']
  for path in required:
   target=root/path;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/path,target)
  git_dir=subprocess.check_output(['git','-C',str(ROOT),'rev-parse','--absolute-git-dir'],text=True).strip()
  (root/'.git').write_text('gitdir: '+git_dir+'\n')
  # The P1 PR need not contain later-batch records or the eventual addendum.
  # Exercise the optional extension with explicit temporary fixture content.
  r['additional_glossary_path']=str(CONTROL/'TERMINOLOGY-ADDENDUM.md')
  addendum=root/r['additional_glossary_path'];addendum.write_text('# 测试术语补充表\n',encoding='utf-8')
  r['additional_glossary_sha256']=hashlib.sha256(addendum.read_bytes()).hexdigest()
  (root/rp).write_text(json.dumps(r,ensure_ascii=False),encoding='utf-8')
  keys=('lesson_id','source_path','source_commit','source_blob','source_sha256','target_path','glossary_version','glossary_sha256','status')
  review={key:r[key] for key in keys};review['reviewed_target_sha256']=r['target_sha256']
  (root/review_path).write_text(json.dumps(review))
  yield root,r,root/review_path


@contextmanager
def asset_fixture():
 """Exercise the asset gate from frozen English files already present in main."""
 with production_fixture() as (root,_,__):
  lesson=Path('phases/06-speech-and-audio/02-spectrograms-mel-features')
  source_path=str(lesson/'docs/en.md');asset_path=str(lesson/'assets/mel-features.svg')
  target_asset='i18n/zh/'+asset_path
  for src,dest in ((source_path,source_path),(asset_path,asset_path),(asset_path,target_asset)):
   p=root/dest;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/src,p)
  manifest={'source_path':source_path,'target_path':'i18n/zh/'+str(lesson/'docs/zh.md'),
            'assets':[{'source_path':asset_path,'target_path':target_asset,'source_commit':SOURCE_COMMIT,
                       'sha256':hashlib.sha256((root/asset_path).read_bytes()).hexdigest()}]}
  yield root,manifest,(root/source_path).read_text()


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
  with production_fixture() as (root,r,_):
   for segment in r['segments']:segment['segment_id']='same'
   self.assertIn('Duplicate stable segment IDs',check_record(r,root))
 def test_unknown_and_reviewed_statuses_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'zh.md';p.write_text(ZH)
   for status in ('unknown','language-reviewed','tech-reviewed','approved'):
    with self.assertRaises(ValueError):safe_write(p,ZH,sha(ZH),status)
 def test_real_cli_render_refuses_clobber_and_replays(self):
  with production_fixture() as (root,r,_), tempfile.TemporaryDirectory() as output:
   (root/'scripts').mkdir();shutil.copyfile(Path(__file__).with_name('curated_translation.py'),root/'scripts/curated_translation.py')
   command=[sys.executable,str(root/'scripts/curated_translation.py'),'render','--output-dir',output]
   first=subprocess.run(command,capture_output=True,text=True);self.assertEqual(first.returncode,0,first.stderr)
   rendered=Path(output)/r['target_path'];self.assertEqual(rendered.read_bytes(),(root/r['target_path']).read_bytes())
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
  with production_fixture() as (root,r,_):
   self.assertEqual(check_record(r,root),[])
   source=root/r['source_path'];source.write_text(source.read_text()+'Changed source.\n')
   self.assertTrue(any('SOURCE_STALE' in e for e in check_record(r,root)))
  with production_fixture() as (root,r,_):
   target=root/r['target_path'];target.write_text(target.read_text()+'人工修改。\n')
   self.assertTrue(any('TARGET_CHANGED' in e for e in check_record(r,root)))

 def test_required_production_bindings_cannot_be_omitted(self):
  with production_fixture() as (root,r,_):
   for key in ('schema_version','source_commit','source_blob','glossary_version','glossary_sha256','status','lesson_id'):
    changed=copy.deepcopy(r);del changed[key]
    with self.subTest(key=key):self.assertTrue(check_record(changed,root))

 def test_source_and_glossary_bindings_reject_changes(self):
  with production_fixture() as (root,r,_):
   for key,value in [('source_commit','0'*40),('source_blob','0'*40),('glossary_sha256','0'*64),('glossary_version','2.0')]:
    changed=copy.deepcopy(r);changed[key]=value
    with self.subTest(key=key):self.assertTrue(check_record(changed,root))
   glossary=root/CONTROL/'TERMINOLOGY.md';glossary.write_text('Changed glossary')
   self.assertTrue(any('Glossary changed' in e for e in check_record(r,root)))
   glossary.unlink();self.assertIn('Core glossary unavailable',check_record(r,root))

 def test_reviewed_records_require_complete_matching_review(self):
  with production_fixture() as (root,r,p):
   original=json.loads(p.read_text())
   for key in original:
    for action in ('remove','change'):
     review=copy.deepcopy(original)
     if action=='remove':review.pop(key)
     else:review[key]='wrong'
     p.write_text(json.dumps(review))
     with self.subTest(key=key,action=action):self.assertTrue(check_record(r,root))
   for bad in ('{bad json','[]'):
    p.write_text(bad);self.assertTrue(check_record(r,root))
   p.unlink();self.assertTrue(check_record(r,root))
   r['status']='draft';self.assertEqual(check_record(r,root),[])

 def test_current_target_and_record_do_not_refresh_old_review(self):
  with production_fixture() as (root,r,_):
   r['segments'][0]['target']=r['segments'][0]['target'].replace('# ','# 新版',1)
   changed=assemble(r);r['target_sha256']=sha(changed);(root/r['target_path']).write_text(changed)
   self.assertIn('REVIEW_STALE: reviewed target hash differs',check_record(r,root))

 def test_unknown_approved_and_mismatched_review_statuses_rejected(self):
  with production_fixture() as (root,r,p):
   original=json.loads(p.read_text())
   for status in ('unknown','approved','',None):
    changed=copy.deepcopy(r);changed['status']=status
    review=copy.deepcopy(original);review['status']=status;p.write_text(json.dumps(review))
    with self.subTest(status=status):self.assertIn('Unsupported record status',check_record(changed,root))
   p.write_text(json.dumps(original));r['status']='tech-reviewed'
   self.assertIn('Review binding mismatch: status',check_record(r,root))

 def test_additional_glossary_requires_pair_and_current_bytes(self):
  with production_fixture() as (root,r,_):
   for key in ('additional_glossary_path','additional_glossary_sha256'):
    changed=copy.deepcopy(r);changed.pop(key);self.assertIn('Additional glossary path/hash must be paired',check_record(changed,root))
   p=root/r['additional_glossary_path'];p.write_text('Changed additive terms')
   self.assertIn('Additional glossary changed; review invalidated',check_record(r,root))
   p.unlink();self.assertIn('Missing or unsafe additional glossary',check_record(r,root))

 def test_record_and_additional_glossary_paths_are_contained(self):
  with production_fixture() as (root,r,_), tempfile.TemporaryDirectory() as outside:
   external=Path(outside)/'outside.txt';external.write_text('External')
   (root/'escape').symlink_to(Path(outside),target_is_directory=True)
   for key in ('source_path','target_path','additional_glossary_path'):
    for path in (str(external),'../outside.txt','escape/outside.txt',''):
     changed=copy.deepcopy(r);changed[key]=path
     with self.subTest(key=key,path=path):self.assertTrue(check_record(changed,root))

 def test_review_symlink_cannot_escape_root(self):
  with production_fixture() as (root,r,p), tempfile.TemporaryDirectory() as outside:
   external=Path(outside)/'review.json';external.write_bytes(p.read_bytes());p.unlink();p.symlink_to(external)
   self.assertIn('Missing, unsafe or invalid review.json for reviewed record',check_record(r,root))

 def test_assets_require_manifest_and_pinned_source_and_target(self):
  with asset_fixture() as (root,r,source):
   self.assertEqual(check_assets(r,source,root),[])
   for assets in (None,[],[r['assets'][0],r['assets'][0]]):
    changed=copy.deepcopy(r)
    if assets is None:changed.pop('assets')
    else:changed['assets']=assets
    with self.subTest(assets=assets):self.assertTrue(check_assets(changed,source,root))
   for key,value in (('sha256','0'*64),('source_commit','0'*40),('target_path',r['target_path'])):
    changed=copy.deepcopy(r);changed['assets'][0][key]=value;self.assertTrue(check_assets(changed,source,root))
   asset=r['assets'][0];sp=root/asset['source_path'];tp=root/asset['target_path'];original=sp.read_bytes()
   tp.write_bytes(b'Changed SVG');self.assertTrue(check_assets(r,source,root));tp.unlink();self.assertTrue(check_assets(r,source,root))
   tp.write_bytes(original);sp.write_bytes(b'Changed source SVG');self.assertTrue(check_assets(r,source,root))
   tp.write_bytes(sp.read_bytes());changed=copy.deepcopy(r);changed['assets'][0]['sha256']=hashlib.sha256(sp.read_bytes()).hexdigest()
   self.assertIn('Asset source differs from pinned Git commit',check_assets(changed,source,root))
   sp.unlink();self.assertTrue(check_assets(r,source,root))

 def test_asset_paths_are_contained(self):
  with asset_fixture() as (root,r,source), tempfile.TemporaryDirectory() as outside:
   external=Path(outside)/'outside.svg';external.write_text('<svg/>')
   (root/'escape').symlink_to(Path(outside),target_is_directory=True)
   for key in ('source_path','target_path'):
    for path in (str(external),'../outside.svg','escape/outside.svg'):
     changed=copy.deepcopy(r);changed['assets'][0][key]=path
     with self.subTest(key=key,path=path):self.assertIn('Unsafe asset path',check_assets(changed,source,root))

 def test_lesson_identity_and_metadata_are_required(self):
  with production_fixture() as (root,r,_):
   changed=copy.deepcopy(r);changed['lesson_id']='99-99';self.assertTrue(check_record(changed,root))
   for key in ('kind','heading_path','ordinal'):
    changed=copy.deepcopy(r);changed['segments'][0].pop(key);self.assertIn('Missing or invalid authoring segments',check_record(changed,root))
  for lesson_id in ('../00-04','/tmp/00-04','00-04/extra',''):
   with self.assertRaises(ValueError):record_path(lesson_id)

 def test_cli_check_is_read_only_and_render_blocks_stale_review(self):
  with production_fixture() as (root,r,p), tempfile.TemporaryDirectory() as output:
   (root/'scripts').mkdir();shutil.copyfile(Path(__file__).with_name('curated_translation.py'),root/'scripts/curated_translation.py')
   script=str(root/'scripts/curated_translation.py')
   paths=[p for p in root.rglob('*') if p.is_file()]
   before={p:p.read_bytes() for p in paths}
   passed=subprocess.run([sys.executable,script,'check'],capture_output=True,text=True)
   self.assertEqual(passed.returncode,0,passed.stderr);self.assertEqual(before,{p:p.read_bytes() for p in paths})
   review=json.loads(p.read_text());review['reviewed_target_sha256']='0'*64;p.write_text(json.dumps(review))
   refused=subprocess.run([sys.executable,script,'render','--output-dir',output],capture_output=True,text=True)
   self.assertNotEqual(refused.returncode,0);self.assertIn('REVIEW_STALE',refused.stdout)
   self.assertFalse(any(Path(output).rglob('*')))

if __name__=='__main__':unittest.main()
