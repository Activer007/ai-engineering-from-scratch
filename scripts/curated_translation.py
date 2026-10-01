#!/usr/bin/env python3
"""Offline, English-first authoring and verification for the curated zh pilot.

No network, provider API, legacy cache, fallback translation, or publication.
Authoring records are reviewed inputs; zh.md is reproducibly assembled from them.
"""
from __future__ import annotations
import argparse
import collections
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CONTROL = Path('i18n/zh/.curated')
SOURCE_COMMIT = '1bafaa88bb4668356791150bec3a6d7df38387eb'
FENCE = re.compile(r'^\s*(`{3,}|~{3,})([^\n]*)$')
INLINE = re.compile(r'(?<!`)(`+)(.+?)\1(?!`)')


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()


def blocks(text):
    """Lossless block scanner. Fences and display math are single protected nodes."""
    result, current, fence, math = [], [], None, False
    def flush():
        if current:
            result.append(''.join(current)); current.clear()
    for line in text.splitlines(keepends=True):
        token = FENCE.match(line.rstrip('\n'))
        if fence:
            current.append(line)
            if token and token[1][0] == fence[0] and len(token[1]) >= len(fence) and not token[2].strip():
                fence = None; flush()
            continue
        if math:
            current.append(line)
            if line.strip() == '$$': math = False; flush()
            continue
        if token:
            flush(); fence = token[1]; current.append(line); continue
        if line.strip() == '$$':
            flush(); math = True; current.append(line); continue
        if not line.strip():
            flush(); result.append(line)
        else:
            current.append(line)
    if fence or math:
        raise ValueError('Truncated fence or display math; candidate rejected')
    flush()
    return result


def kind(text):
    s = text.lstrip()
    if not s.strip(): return 'separator'
    if FENCE.match(s.splitlines()[0]): return 'fence'
    if s.startswith('$$'): return 'display_math'
    if s.startswith('#'): return 'heading'
    if s.startswith('|'): return 'table'
    if re.match(r'(?:[-*+] |\d+[.)] )',s): return 'list'
    if s.startswith('>'): return 'blockquote'
    return 'paragraph'


def fence_parts(text):
    lines=text.splitlines()
    return FENCE.match(lines[0])[2].strip(), '\n'.join(lines[1:-1])


def without_protected(text):
    result=[]
    for b in blocks(text):
        if kind(b) not in ('fence','display_math'):
            result.append(INLINE.sub('', b))
    return ''.join(result)


def numeric_tokens(prose):
    values=[]
    for m in re.finditer(r'[-−+]?\d+(?:[.,]\d+)*(?:%)?',prose):
        value=m[0]
        # Hyphens in lexical compounds (factor-of-10, mid-2026) are not minus signs.
        if value.startswith('-') and re.search(r'[A-Za-z]{2,}$',prose[:m.start()]):value=value[1:]
        values.append(value)
    return values


def signature(text):
    bs=blocks(text)
    prose=without_protected(text)
    return {
        'kinds':[kind(b) for b in bs],
        'headings':[len(m[1]) for m in re.finditer(r'^(#{1,6}) ',prose,re.M)],
        'inline_code':[m[2] for b in bs if kind(b) not in ('fence','display_math') for m in INLINE.finditer(b)],
        'math':re.findall(r'(?<!\\)\$[^$\n]+?(?<!\\)\$(?!\d)',prose),
        'latex_math':re.findall(r'\\\([^\n]+?\\\)|\\\[[\s\S]+?\\\]',prose),
        'links':re.findall(r'\]\(([^)]+)\)',prose),
        'urls':re.findall(r'https?://[^\s<>)\]，。；：、]+',prose),
        'numbers':numeric_tokens(prose),
        'symbolic_units':re.findall(r'(?<![A-Za-z])(?:ns|μs|ms|Hz|kHz|MHz|GHz|KiB|MiB|GiB|KB|MB|GB|TB|FLOPs|TFLOPS)(?![A-Za-z])',prose),
        'metadata':re.findall(r'^\*\*(Type|Languages|Language|Prerequisites|Time):\*\*',prose,re.M),
        'immutable_metadata':re.findall(r'^\*\*(Type|Languages|Language):\*\*(.*)$',prose,re.M),
        'table_columns':[len(re.split(r'(?<!\\)\|', INLINE.sub('',line)))-2 for line in prose.splitlines() if line.startswith('|')],
    }


def validate(source,target):
    sb,tb=blocks(source),blocks(target)
    errors=[]
    if len(sb)!=len(tb): return [f'Block count differs: {len(sb)} != {len(tb)}']
    for i,(a,b) in enumerate(zip(sb,tb),1):
        if kind(a) in ('fence','display_math'):
            if kind(a)=='display_math':
                if a!=b:errors.append(f'{i}: display math changed')
            else:
                al,ac=fence_parts(a);bl,bc=fence_parts(b)
                if ac!=bc:errors.append(f'{i}: fenced payload changed')
                if al!=bl and not (not al and bl=='text'):errors.append(f'{i}: fence language changed')
                if not bl:errors.append(f'{i}: unlabelled fence')
        if kind(a)=='separator' and a!=b: errors.append(f'{i}: separator changed')
    sa,ta=signature(source),signature(target)
    for key in sa:
        if key in ('numbers','inline_code','symbolic_units'):
            if collections.Counter(sa[key])!=collections.Counter(ta[key]):errors.append(f'{key} mismatch')
        elif sa[key]!=ta[key]:errors.append(f'{key} mismatch')
    for i,(a,b) in enumerate(zip(sb,tb),1):
        if kind(a) in ('separator','fence','display_math'):continue
        aa,bb=signature(a),signature(b)
        for key in ('numbers','inline_code','symbolic_units'):
            if collections.Counter(aa[key])!=collections.Counter(bb[key]):errors.append(f'{i}: {key} moved across a block or changed')
    for i,(a,b) in enumerate(zip(sb,tb),1):
        if kind(a) not in ('separator','fence','display_math') and a==b:
            words=re.sub(r'^\*\*(?:Type|Languages|Language):\*\*.*$', '', a, flags=re.M)
            words=INLINE.sub('',words)
            if len(re.findall(r'[A-Za-z]{2,}',words))>=4:errors.append(f'{i}: unchanged translatable segment needs explicit review')
    if re.search(r'PROTECT\d|TODO_TRANSLATE|\[TRANSLATE\]',target):errors.append('Unresolved translation placeholder')
    if not re.search('[\u4e00-\u9fff]',target):errors.append('No Chinese prose; English fallback rejected')
    return errors


def record_path(lesson_id):
    if not re.fullmatch(r'\d{2}-\d{2}', lesson_id):
        raise ValueError('Expected lesson ID NN-MM')
    return ROOT/CONTROL/'lessons'/lesson_id/'translation.json'


def capture(lesson):
    lp=Path(lesson)
    if len(lp.parts)!=3 or lp.parts[0]!='phases' or '..' in lp.parts:raise ValueError('Expected phases/<phase>/<lesson>')
    lesson_id=lp.parts[1][:2]+'-'+lp.parts[2][:2]
    sp=lp/'docs/en.md';tp=Path('i18n/zh')/lp/'docs/zh.md'
    s=(ROOT/sp).read_text();t=(ROOT/tp).read_text()
    pinned=subprocess.check_output(['git','-C',str(ROOT),'show',f'{SOURCE_COMMIT}:{sp}']).decode()
    if s!=pinned:raise ValueError('Working English differs from pinned source')
    errors=validate(s,t)
    if errors:raise ValueError('; '.join(errors))
    rp=record_path(lesson_id)
    if rp.exists():raise ValueError('Authoring record already exists; edit it deliberately, never recapture reviewed content')
    segments=[];heading=[];ordinal=0
    for i,(a,b) in enumerate(zip(blocks(s),blocks(t)),1):
        k=kind(a)
        if k=='heading':
            level=len(re.match(r'#+',a)[0]);heading=heading[:level-1]+[a.strip()]
        if k!='separator':ordinal+=1
        segments.append({'segment_id':f'{lesson_id}:b{i:04d}', 'kind':k,'heading_path':heading[:], 'ordinal':ordinal,'source_sha256':sha(a),'target':b})
    rec={'schema_version':1,'lesson_id':lesson_id,'source_path':str(sp),'source_commit':SOURCE_COMMIT,'source_blob':git('rev-parse',f'{SOURCE_COMMIT}:{sp}'),'source_sha256':sha(s),'target_path':str(tp),'target_sha256':sha(t),'glossary_version':'1.0','glossary_sha256':sha((ROOT/CONTROL/'TERMINOLOGY.md').read_text()),'status':'draft','provenance':{'method':'English-first assistant authored; deterministic offline assembly','provider':'OpenAI assistant runtime','model':'not exposed by runtime','sampling_parameters':'not exposed by runtime','api_calls':0,'external_api_cost':0,'token_usage':'not exposed; no estimate invented','run_date':'2026-10-01'},'segments':segments}
    rp.parent.mkdir(parents=True,exist_ok=True);rp.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
    return rp


def assemble(record): return ''.join(s['target'] for s in record['segments'])


def contained_path(root, value):
    """Validate every record-controlled path before reading it, including symlinks."""
    if not isinstance(value, str) or not value or '\\' in value:
        raise ValueError('Unsafe record path')
    p=Path(value)
    if p.is_absolute() or '..' in p.parts or not (root/p).resolve().is_relative_to(root.resolve()):
        raise ValueError('Unsafe record path')
    return root/p


def check_review(record, root):
    """Reviewed status is meaningful only when a separate review binds these bytes."""
    if record['status']=='draft': return []
    try:
        path=contained_path(root,str(CONTROL/'lessons'/record['lesson_id']/'review.json'))
        review=json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return ['Missing, unsafe or invalid review.json for reviewed record']
    if not isinstance(review,dict):return ['Invalid review.json object']
    errors=[]
    for key in ('lesson_id','source_path','source_commit','source_blob','source_sha256','target_path',
                'glossary_version','glossary_sha256','status'):
        if review.get(key)!=record[key]:errors.append('Review binding mismatch: '+key)
    if review.get('reviewed_target_sha256')!=record['target_sha256']:
        errors.append('REVIEW_STALE: reviewed target hash differs')
    return errors


def check_assets(record, source, root):
    """Require manifests for relative SVGs and compare source, frozen Git and copy."""
    errors=[]
    assets=record.get('assets',[])
    if not isinstance(assets,list):return ['Invalid assets manifest']
    source_base=Path(record['source_path']).parent
    target_base=Path(record['target_path']).parent
    expected={}
    for link in re.findall(r'\]\(([^)]+)\)',source):
        clean=link.split('#',1)[0].split('?',1)[0]
        if not clean.endswith('.svg') or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:|/',clean):continue
        sp=os.path.normpath(source_base/clean);tp=os.path.normpath(target_base/clean)
        expected[sp]=tp
    seen=set()
    for asset in assets:
        if not isinstance(asset,dict):errors.append('Invalid asset entry');continue
        try:
            sp=contained_path(root,asset.get('source_path'))
            tp=contained_path(root,asset.get('target_path'))
        except ValueError:
            errors.append('Unsafe asset path');continue
        source_path=asset['source_path']
        if source_path in seen:errors.append('Duplicate asset entry')
        seen.add(source_path)
        if expected.get(source_path)!=asset['target_path']:errors.append('Asset is not a matching relative SVG destination')
        if asset.get('source_commit')!=SOURCE_COMMIT:errors.append('Unapproved asset source commit')
        digest=asset.get('sha256')
        if not isinstance(digest,str) or not re.fullmatch(r'[0-9a-f]{64}',digest):
            errors.append('Missing or invalid asset hash');continue
        try:
            original=sp.read_bytes();translated=tp.read_bytes()
            pinned=subprocess.check_output(['git','-C',str(root),'show',f'{SOURCE_COMMIT}:{source_path}'],stderr=subprocess.DEVNULL)
        except (OSError,subprocess.CalledProcessError):
            errors.append('Missing or unavailable asset source/target');continue
        if original!=pinned:errors.append('Asset source differs from pinned Git commit')
        if original!=translated:errors.append('Asset target differs from source')
        if any(hashlib.sha256(data).hexdigest()!=digest for data in (original,translated,pinned)):
            errors.append('Asset hash mismatch')
    if seen!=set(expected):errors.append('Relative SVG assets missing from manifest or unexpected assets present')
    return errors


def check_record(record, root=ROOT):
    errors=[]
    if not isinstance(record,dict):return ['Invalid authoring record object']
    required=('schema_version','lesson_id','source_path','source_commit','source_blob','source_sha256',
              'target_path','target_sha256','glossary_version','glossary_sha256','status','segments')
    missing=[key for key in required if key not in record]
    if missing:return ['Missing required record fields: '+', '.join(missing)]
    if record['schema_version']!=1:errors.append('Unsupported schema version')
    if record['status'] not in ('draft','tech-reviewed','language-reviewed'):errors.append('Unsupported record status')
    if not isinstance(record['lesson_id'],str) or not re.fullmatch(r'\d{2}-\d{2}',record['lesson_id']):
        errors.append('Invalid lesson ID')
    for key,length in (('source_blob',40),('source_sha256',64),('target_sha256',64),('glossary_sha256',64)):
        if not isinstance(record[key],str) or not re.fullmatch('[0-9a-f]{'+str(length)+'}',record[key]):
            errors.append('Missing or invalid '+key)
    if errors:return errors
    try:
        sp=contained_path(root,record['source_path']);tp=contained_path(root,record['target_path'])
        glossary=contained_path(root,str(CONTROL/'TERMINOLOGY.md'))
    except ValueError:return ['Unsafe record path']
    match=re.fullmatch(r'phases/(\d{2}-[^/]+)/(\d{2}-[^/]+)/docs/en\.md',record['source_path'])
    if not match or record['lesson_id']!=match[1][:2]+'-'+match[2][:2]:
        errors.append('Source path does not match lesson ID')
    if record['target_path']!='i18n/zh/'+str(Path(record['source_path']).with_name('zh.md')):
        errors.append('Target path does not match source lesson')
    try:
        source_bytes=sp.read_bytes();target_bytes=tp.read_bytes()
        source=source_bytes.decode('utf-8');target=target_bytes.decode('utf-8')
    except (OSError,UnicodeError):return errors+['Missing or invalid UTF-8 source/target file']
    if record['source_commit']!=SOURCE_COMMIT:errors.append('Unapproved source commit')
    try:
        pinned=subprocess.check_output(['git','-C',str(root),'show',f"{SOURCE_COMMIT}:{record['source_path']}"],stderr=subprocess.DEVNULL)
        if source_bytes!=pinned:errors.append('Source differs from pinned Git commit')
    except (OSError,subprocess.CalledProcessError):errors.append('Pinned Git source unavailable')
    blob=hashlib.sha1(b'blob '+str(len(source_bytes)).encode()+b'\0'+source_bytes).hexdigest()
    if blob!=record['source_blob']:errors.append('Source blob mismatch')
    if record['glossary_version']!='1.0':errors.append('Unsupported core glossary version')
    try:
        if hashlib.sha256(glossary.read_bytes()).hexdigest()!=record['glossary_sha256']:
            errors.append('Glossary changed; review invalidated')
    except OSError:errors.append('Core glossary unavailable')
    has_addendum=[key in record for key in ('additional_glossary_path','additional_glossary_sha256')]
    if any(has_addendum):
        if not all(has_addendum):errors.append('Additional glossary path/hash must be paired')
        else:
            try:
                addendum=contained_path(root,record['additional_glossary_path'])
                if hashlib.sha256(addendum.read_bytes()).hexdigest()!=record['additional_glossary_sha256']:
                    errors.append('Additional glossary changed; review invalidated')
            except (OSError,ValueError):errors.append('Missing or unsafe additional glossary')
    errors.extend(check_review(record,root))
    errors.extend(check_assets(record,source,root))
    segments=record['segments']
    required_segment=('segment_id','kind','heading_path','ordinal','source_sha256','target')
    if not isinstance(segments,list) or any(not isinstance(s,dict) or any(k not in s for k in required_segment) for s in segments):
        return errors+['Missing or invalid authoring segments']
    if any(not isinstance(s['target'],str) or not isinstance(s['segment_id'],str) for s in segments):
        return errors+['Invalid segment target or identity']
    generated=assemble(record)
    ids=[s['segment_id'] for s in record['segments']]
    if len(ids)!=len(set(ids)): errors.append('Duplicate stable segment IDs')
    if sha(source)!=record['source_sha256']:errors.append('SOURCE_STALE: approval invalidated')
    if sha(target)!=record['target_sha256']:errors.append('TARGET_CHANGED: concurrent edit; refuse overwrite')
    if generated!=target:errors.append('Target does not match reviewed authoring segments')
    if sha(generated)!=record['target_sha256']:errors.append('Authoring output hash mismatch')
    sb=blocks(source)
    heading=[];ordinal=0
    if len(sb)==len(record['segments']):
        for i,(b,segment) in enumerate(zip(sb,record['segments'])):
            k=kind(b)
            if k=='heading':
                level=len(re.match(r'#+',b)[0]);heading=heading[:level-1]+[b.strip()]
            if k!='separator':ordinal+=1
            if segment['kind']!=k:errors.append('Invalid segment kind')
            if segment['heading_path']!=heading:errors.append('Invalid source heading context')
            if segment['ordinal']!=ordinal:errors.append('Invalid segment ordinal')
    if len(sb)!=len(record['segments']):errors.append('Source segment count changed')
    elif any(sha(b)!=s['source_sha256'] for b,s in zip(sb,record['segments'])):errors.append('Source segment identity/content changed')
    errors.extend(validate(source,target))
    return errors


def classify_drift(old_segments,new_source,renamed=False):
    """Conservative read-only incremental plan, preserving IDs for exact moved blocks."""
    by_hash=collections.defaultdict(list)
    for i,s in enumerate(old_segments):by_hash[s['source_sha256']].append((i,s['segment_id']))
    used=set();changes=[]
    for j,b in enumerate(blocks(new_source)):
        matches=[x for x in by_hash[sha(b)] if x[0] not in used]
        if len(matches)>1 and kind(b)!='separator':
            changes.append({'segment_id':None,'state':'ambiguous_duplicate','new_ordinal':j});continue
        if matches:
            i,sid=matches[0];used.add(i)
            changes.append({'segment_id':sid,'state':'moved' if i!=j else ('renamed' if renamed else 'unchanged')})
        else:changes.append({'segment_id':None,'state':'changed_or_added','new_ordinal':j})
    changes.extend({'segment_id':s['segment_id'],'state':'deleted_or_changed'} for i,s in enumerate(old_segments) if i not in used)
    return changes


def safe_write(path,new_text,expected_hash,status='draft'):
    if status not in ('draft',):raise ValueError('Only draft candidates are writable')
    if path.is_symlink():raise ValueError('Refuse symlink target')
    actual=sha(path.read_text()) if path.exists() else None
    if actual!=expected_hash:raise ValueError('Concurrent target modification; refusing overwrite')
    if not new_text.strip():raise ValueError('Empty/truncated candidate rejected')
    blocks(new_text)
    fd,tmp=tempfile.mkstemp(dir=path.parent,prefix='.curated-')
    try:
        with os.fdopen(fd,'w') as f:f.write(new_text)
        if (sha(path.read_text()) if path.exists() else None)!=expected_hash:raise ValueError('Concurrent target modification during preparation')
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('action',choices=['capture','check','render','drift'])
    p.add_argument('--lesson',help='phases/<phase>/<lesson> for initial authoring capture')
    p.add_argument('--id',help='NN-MM; omit to check/render all recorded lessons')
    p.add_argument('--output-dir',type=Path,help='separate assembly destination; never rewrites checked-in zh.md')
    a=p.parse_args()
    if a.action=='capture':
        if not a.lesson:p.error('--lesson required')
        print(capture(a.lesson).relative_to(ROOT));return
    paths=[record_path(a.id)] if a.id else sorted((ROOT/CONTROL/'lessons').glob('*/translation.json'))
    if not paths:p.error('No authoring records selected')
    failed=False
    for rp in paths:
        r=json.loads(rp.read_text());errors=check_record(r)
        if a.action=='drift':
            print(json.dumps({'lesson_id':r['lesson_id'],'changes':classify_drift(r['segments'],(ROOT/r['source_path']).read_text()),'status':'stale' if errors else r['status']},ensure_ascii=False));continue
        if errors:
            print(r['lesson_id']+': FAIL: '+'; '.join(errors));failed=True;continue
        if a.action=='render':
            if not a.output_dir:p.error('--output-dir required')
            target=a.output_dir.resolve()/r['target_path']
            base=a.output_dir.resolve()
            if not target.resolve().is_relative_to(base) or target.is_symlink():raise ValueError('Output escapes destination or is a symlink')
            if target.resolve().is_relative_to(ROOT):raise ValueError('Render only outside the repository')
            target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and sha(target.read_text()) != r['target_sha256']: raise ValueError('Existing render differs; concurrent output preserved')
            safe_write(target,assemble(r),r['target_sha256'] if target.exists() else None)
        print(r['lesson_id']+': PASS')
    if failed:raise SystemExit(1)

if __name__=='__main__':main()
