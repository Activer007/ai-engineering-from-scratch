#!/usr/bin/env python3
"""Stage-scoped, exact-hash exception for one reviewed symbolic Jacobian table.

The pinned legacy checker remains unmodified and runs in full. This adapter may
remove only its unchanged-prose false positive for the exact frozen table. It
never waives stale source/target/review binding, structure or any other error.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
CORE_SHA = 'd89de5eec36e10edcc391330d973632e3ceedb33fe679de3503dab52a7f6ece8'
SOURCE_COMMIT = '1bafaa88bb4668356791150bec3a6d7df38387eb'
SOURCE_PATH = 'phases/01-math-foundations/04-calculus-for-ml/docs/en.md'
SOURCE_SHA = '0ed4721bd7a01a876bdfd1cafd3a732d645842bf942f708bf32198fd5a8e6794'
BLOCK_ID = '01-04:b0213'
BLOCK_INDEX = 212
BLOCK_SHA = '010551b76c48451f9d45e8cf394192441e2f5f299b1b4a3a6003fa6008e5cc92'
DIAGNOSTIC = '213: unchanged translatable segment needs explicit review'


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def load_core(root):
    p = Path(root) / 'scripts/curated_translation.py'
    if hashlib.sha256(p.read_bytes()).hexdigest() != CORE_SHA:
        raise ValueError('Pinned legacy checker hash changed; adapter invalidated')
    spec = importlib.util.spec_from_file_location('s07_pinned_core', p)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    return core


def reviewed_symbolic_exception(errors, record, review, source, target, core):
    """Filter one diagnostic only after all narrow bindings pass.

    Not a validator by itself: callers must supply the complete core.check_record
    result. Returning residual errors preserves every unrelated failure.
    """
    guards = []
    if DIAGNOSTIC not in errors:
        guards.append('expected symbolic-table diagnostic absent; review required')
    if (record.get('lesson_id') != '01-04' or
            record.get('source_path') != SOURCE_PATH or
            record.get('source_commit') != SOURCE_COMMIT or
            record.get('source_sha256') != SOURCE_SHA or sha(source) != SOURCE_SHA):
        guards.append('symbolic exception source identity mismatch')
    if record.get('status') != 'language-reviewed' or review.get('status') != 'language-reviewed':
        guards.append('symbolic exception requires completed independent language review')
    if (record.get('target_sha256') != sha(target) or
            review.get('reviewed_target_sha256') != sha(target)):
        guards.append('symbolic exception target/review hash mismatch')
    sb, tb = core.blocks(source), core.blocks(target)
    if (len(sb) <= BLOCK_INDEX or len(tb) <= BLOCK_INDEX or
            sha(sb[BLOCK_INDEX]) != BLOCK_SHA or
            sha(tb[BLOCK_INDEX]) != BLOCK_SHA or
            sb[BLOCK_INDEX] != tb[BLOCK_INDEX] or
            core.kind(sb[BLOCK_INDEX]) != 'table'):
        guards.append('symbolic exception exact table mismatch')
    approvals = review.get('unchanged_symbolic_blocks')
    expected = {'segment_id': BLOCK_ID, 'source_sha256': BLOCK_SHA,
                'target_sha256': BLOCK_SHA, 'independent_review_passed': True,
                'classification': 'pure-mathematical-symbol-table'}
    if (not isinstance(approvals, list) or len(approvals) != 1 or
            not isinstance(approvals[0], dict) or
            any(approvals[0].get(k) != v for k, v in expected.items()) or
            approvals[0].get('independent_review_passed') is not True or
            not isinstance(approvals[0].get('reason'), str) or
            not approvals[0]['reason'].strip()):
        guards.append('symbolic exception explicit approval missing or mismatched')
    if guards:
        return list(errors) + guards
    # Do not absorb additional copies: one approved diagnostic, exactly once.
    filtered = list(errors)
    filtered.remove(DIAGNOSTIC)
    return filtered


def check(root=ROOT):
    root = Path(root)
    core = load_core(root)
    d = root / 'i18n/zh/.curated/lessons/01-04'
    record = json.loads((d / 'translation.json').read_text())
    review = json.loads((d / 'review.json').read_text())
    errors = core.check_record(record, root)
    source = (root / SOURCE_PATH).read_text()
    # Use a fixed target, never an unchecked authoring-record path.
    target = (root / ('i18n/zh/' + SOURCE_PATH.replace('/en.md', '/zh.md'))).read_text()
    return errors, reviewed_symbolic_exception(errors, record, review, source, target, core), record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output-dir', type=Path, help='Optional reviewed replay outside checkout')
    args = parser.parse_args()
    legacy, result, record = check(args.root)
    if not result and args.output_dir is not None:
        out = args.output_dir.resolve()
        if out == args.root.resolve() or args.root.resolve() in out.parents:
            raise ValueError('Replay must be outside checkout')
        destination = out / ('i18n/zh/' + SOURCE_PATH.replace('/en.md', '/zh.md'))
        if out not in destination.resolve().parents:
            raise ValueError('Replay path escapes output directory')
        # Assemble the same in-memory record already checked, not a second read.
        content = ''.join(segment['target'] for segment in record['segments'])
        if sha(content) != record['target_sha256']:
            raise ValueError('Validated replay content hash mismatch')
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            if destination.read_bytes() != content.encode('utf-8'):
                raise ValueError('Refuse overwriting a different replay file')
        else:
            destination.write_bytes(content.encode('utf-8'))
    print(json.dumps({'lesson_id': '01-04', 'legacy_errors': legacy,
                      'reviewed_exception': BLOCK_ID if DIAGNOSTIC in legacy and not result else None,
                      'result': 'PASS_WITH_REVIEWED_SYMBOLIC_BLOCK' if not result else 'FAIL',
                      'remaining_errors': result}, ensure_ascii=False, indent=2))
    return 1 if result else 0


if __name__ == '__main__':
    raise SystemExit(main())
