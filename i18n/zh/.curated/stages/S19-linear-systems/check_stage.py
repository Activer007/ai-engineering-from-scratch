#!/usr/bin/env python3
"""Fail-closed S19 adapter for two reviewed GFM norm-pipe escapes only.

Run the pinned core check in full. Remove one exact table-columns diagnostic
only for the frozen final lesson and explicit independent review. This does
not authorize any mathematical correction or any other lesson's exception.
"""
import argparse
import hashlib
import types
import json
import os
from pathlib import Path
import stat

ROOT = Path(__file__).resolve().parents[5]
CORE_SHA = 'd89de5eec36e10edcc391330d973632e3ceedb33fe679de3503dab52a7f6ece8'
SOURCE_COMMIT = '1bafaa88bb4668356791150bec3a6d7df38387eb'
LESSON_ID = '01-17'
SOURCE_PATH = 'phases/01-math-foundations/17-linear-systems/docs/en.md'
TARGET_PATH = 'i18n/zh/phases/01-math-foundations/17-linear-systems/docs/zh.md'
RECORD_DIR = 'i18n/zh/.curated/lessons/01-17'
SOURCE_SHA = 'de9a2c0f1e09351e6061834a651110bdab18ae3df534315ea2a62a33a156af49'
ORIGINAL_TARGET_SHA = 'bc3f3ad518bb5df4d47d6edc1533608dc1f8f4ff8a36ef059b9c893c0a6d3c4d'
TARGET_SHA = 'f6528cdd6f2c1bf70d86828e7c9b02e9308311c142e05dc0df1b007bb3c33305'
BLOCK_ID = '01-17:b0245'
BLOCK_INDEX = 244
BLOCK_COUNT = 249
SOURCE_TABLE_SHA = '68ad5dd85bd0e7abbd8c9261ad7a68a71c213d664d6ad8a297f41bd630d1be45'
ORIGINAL_TABLE_SHA = 'c5adc6b46c0e132478c6195e5968cf01a6a45cc151ba6024643091c259355953'
TARGET_TABLE_SHA = 'a33b6d0aea9afd64cb45f699831103665043186feaff2ce4c0d369c22d790ba5'
ROW_INDICES = [8, 9]
ORIGINAL_NORM = '||Ax - b||'
ESCAPED_NORM = r'\|\|Ax - b\|\|'
DIAGNOSTIC = 'table_columns mismatch'
APPROVAL_FIELD = 'gfm_table_repairs'


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def _read_input(root, relative):
    """Read one contained regular file, never following any symlink component."""
    if (not isinstance(relative, str) or not relative or '\\' in relative or
            Path(relative).is_absolute() or '..' in Path(relative).parts):
        raise ValueError('Unsafe S19 input path')
    root = Path(root)
    if '..' in root.parts:
        raise ValueError('Unsafe S19 input root traversal')
    path = root.absolute() / relative
    parent_fd = _open_directory_chain(path.parent, create=False)
    try:
        fd = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent_fd)
        with os.fdopen(fd, 'rb') as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise ValueError('S19 input is not a regular file')
            return stream.read()
    finally:
        os.close(parent_fd)


def load_core(root):
    path = Path(root).absolute() / 'scripts/curated_translation.py'
    content = _read_input(root, 'scripts/curated_translation.py')
    if hashlib.sha256(content).hexdigest() != CORE_SHA:
        raise ValueError('Pinned core hash changed; S19 adapter invalidated')
    # Execute these exact verified bytes; no second path read, loader or pyc.
    core = types.ModuleType('s19_pinned_core')
    core.__file__ = str(path)
    exec(compile(content, str(path), 'exec'), core.__dict__)
    return core


def expected_approval():
    """Protocol fields only; the reviewer must independently supply approval."""
    return {
        'segment_id': BLOCK_ID,
        'source_table_sha256': SOURCE_TABLE_SHA,
        'original_target_table_sha256': ORIGINAL_TABLE_SHA,
        'repaired_target_table_sha256': TARGET_TABLE_SHA,
        'row_indices_zero_based': ROW_INDICES[:],
        'inserted_backslashes': 8,
        'classification': 'gfm-table-norm-pipe-escape',
        'independent_review_passed': True,
    }


def reverse_exact_repair(source, target, core):
    """Reverse exactly eight characters, never normalize any other markup."""
    source_blocks, target_blocks = core.blocks(source), core.blocks(target)
    if len(source_blocks) != BLOCK_COUNT or len(target_blocks) != BLOCK_COUNT:
        raise ValueError('S19 complete block count mismatch')
    source_table, table = source_blocks[BLOCK_INDEX], target_blocks[BLOCK_INDEX]
    if (core.kind(source_table) != 'table' or core.kind(table) != 'table' or
            sha(source_table) != SOURCE_TABLE_SHA or sha(table) != TARGET_TABLE_SHA):
        raise ValueError('S19 exact source/repaired table hash mismatch')
    rows = table.splitlines(keepends=True)
    for index in ROW_INDICES:
        if index >= len(rows) or rows[index].count(ESCAPED_NORM) != 1:
            raise ValueError('S19 exact norm escape absent from approved row')
        rows[index] = rows[index].replace(ESCAPED_NORM, ORIGINAL_NORM, 1)
    original_table = ''.join(rows)
    if (sha(original_table) != ORIGINAL_TABLE_SHA or
            len(table) - len(original_table) != 8 or
            table.count('\\') - original_table.count('\\') != 8):
        raise ValueError('S19 inverse repair is not the exact eight backslashes')
    target_blocks[BLOCK_INDEX] = original_table
    original_target = ''.join(target_blocks)
    if sha(original_target) != ORIGINAL_TARGET_SHA:
        raise ValueError('S19 inverse repair does not restore frozen author draft')
    if core.validate(source, original_target) != []:
        raise ValueError('S19 normalized core validation is not clean')
    return original_target


def reviewed_table_exception(errors, record, review, source, target, core):
    """Accept only one pinned repair; preserve all other full-core errors.

    This helper does not replace core.check_record. check() always runs that
    complete check first. Success requires its sole error to be DIAGNOSTIC.
    """
    guards = []
    if DIAGNOSTIC not in errors:
        guards.append('S19 expected table-columns diagnostic absent')
    if not isinstance(record, dict) or not isinstance(review, dict):
        return list(errors) + guards + ['S19 record/review must be objects']
    identity = {'lesson_id': LESSON_ID, 'source_path': SOURCE_PATH,
                'target_path': TARGET_PATH, 'source_commit': SOURCE_COMMIT,
                'source_sha256': SOURCE_SHA}
    if (any(record.get(k) != v for k, v in identity.items()) or
            any(review.get(k) != v for k, v in identity.items()) or
            sha(source) != SOURCE_SHA):
        guards.append('S19 pinned source/lesson/path identity mismatch')
    if record.get('status') != 'language-reviewed' or review.get('status') != 'language-reviewed':
        guards.append('S19 requires completed independent language review')
    if (sha(target) != TARGET_SHA or record.get('target_sha256') != TARGET_SHA or
            review.get('reviewed_target_sha256') != TARGET_SHA):
        guards.append('S19 final target/review hash mismatch')
    approval = review.get(APPROVAL_FIELD)
    expected = expected_approval()
    if (not isinstance(approval, list) or len(approval) != 1 or
            not isinstance(approval[0], dict) or
            set(approval[0]) != set(expected) | {'reason'} or
            any(approval[0].get(k) != v for k, v in expected.items()) or
            approval[0].get('independent_review_passed') is not True or
            not isinstance(approval[0].get('row_indices_zero_based'), list) or
            len(approval[0]['row_indices_zero_based']) != 2 or
            any(type(index) is not int for index in approval[0]['row_indices_zero_based']) or
            type(approval[0].get('inserted_backslashes')) is not int or
            not isinstance(approval[0].get('reason'), str) or
            not approval[0]['reason'].strip()):
        guards.append('S19 unique explicit repair approval missing or mismatched')
    try:
        target_blocks = core.blocks(target)
        segments = record.get('segments')
        if (not isinstance(segments, list) or len(segments) != BLOCK_COUNT or
                len(target_blocks) != BLOCK_COUNT or
                any(not isinstance(segment, dict) or
                    segment.get('segment_id') != f'{LESSON_ID}:b{i:04d}' or
                    segment.get('target') != block or
                    segment.get('target_sha256') != sha(block)
                    for i, (segment, block) in enumerate(zip(segments, target_blocks), 1)) or
                segments[BLOCK_INDEX].get('source_sha256') != SOURCE_TABLE_SHA):
            guards.append('S19 complete recorded target-block binding mismatch')
        reverse_exact_repair(source, target, core)
    except (ValueError, TypeError, IndexError) as error:
        guards.append(str(error))
    if guards:
        return list(errors) + guards
    filtered = list(errors)
    filtered.remove(DIAGNOSTIC)  # Deliberately remove only one exact occurrence.
    return filtered


def _preflight_core_inputs(root, record, already_read):
    """Reject symlinks in every record-selected input before the legacy call."""
    paths = ['i18n/zh/.curated/TERMINOLOGY.md']
    if isinstance(record, dict):
        paths += [record.get('source_path'), record.get('target_path')]
        if 'additional_glossary_path' in record:
            paths.append(record['additional_glossary_path'])
        assets = record.get('assets', [])
        if isinstance(assets, list):
            for asset in assets:
                if isinstance(asset, dict):
                    paths += [asset.get('source_path'), asset.get('target_path')]
    for path in paths:
        if path is None or path in already_read:
            continue
        try:
            _read_input(root, path)
        except FileNotFoundError:
            pass  # The original checker must retain its missing-file error.


def check(root=ROOT):
    root = Path(root)
    core = load_core(root)
    record_path = RECORD_DIR + '/translation.json'
    review_path = RECORD_DIR + '/review.json'
    record = json.loads(_read_input(root, record_path))
    source = _read_input(root, SOURCE_PATH).decode('utf-8')
    target = _read_input(root, TARGET_PATH).decode('utf-8')
    try:
        review_bytes = _read_input(root, review_path)
    except FileNotFoundError:
        review = {}
    else:
        try:
            review = json.loads(review_bytes)
        except (UnicodeError, ValueError):
            review = {}
    _preflight_core_inputs(root, record, {record_path, review_path, SOURCE_PATH, TARGET_PATH})
    # Run all core checks, including its own review and source Git bindings.
    # Adapter-owned reads above are no-follow; the pinned core remains unchanged.
    legacy_errors = core.check_record(record, root)
    remaining = reviewed_table_exception(legacy_errors, record, review, source, target, core)
    return legacy_errors, remaining, record


def _output_path(output_dir, root):
    output_dir = Path(output_dir)
    if '..' in output_dir.parts:
        raise ValueError('Replay path traversal rejected')
    absolute = output_dir.absolute()
    # Reject symlinks even if they resolve to an otherwise acceptable location.
    for item in (absolute, *absolute.parents):
        if item.is_symlink():
            raise ValueError('Replay symlink path rejected')
    resolved = absolute.resolve()
    if resolved == Path(root).resolve() or Path(root).resolve() in resolved.parents:
        raise ValueError('Replay must be outside checkout')
    return absolute


def _open_directory_chain(path, create=False):
    """Open/create directories without following symlinks, using dirfd scope."""
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.parts[1:]:
            try:
                child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            except FileNotFoundError:
                if not create:
                    raise
                try:
                    os.mkdir(part, mode=0o755, dir_fd=fd)
                except FileExistsError:
                    pass  # A concurrent creator must still pass NOFOLLOW below.
                child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        return fd
    except BaseException:
        os.close(fd)
        raise


def _replay_checked_record(record, output_dir, root):
    """Private write step; caller must pass the same record returned by check()."""
    if (record.get('status') != 'language-reviewed' or record.get('lesson_id') != LESSON_ID or
            record.get('target_path') != TARGET_PATH or record.get('target_sha256') != TARGET_SHA):
        raise ValueError('Replay record binding mismatch')
    content = ''.join(segment['target'] for segment in record['segments'])
    if sha(content) != TARGET_SHA:
        raise ValueError('Validated replay content hash mismatch')
    out = _output_path(output_dir, root)
    destination = out / TARGET_PATH
    parent_fd = _open_directory_chain(destination.parent, create=True)
    try:
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW
        try:
            fd = os.open(destination.name, flags, 0o644, dir_fd=parent_fd)
        except FileExistsError:
            fd = os.open(destination.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                         dir_fd=parent_fd)
            with os.fdopen(fd, 'rb') as existing:
                if not stat.S_ISREG(os.fstat(existing.fileno()).st_mode):
                    raise ValueError('Replay destination is not a regular file')
                if existing.read() != content.encode('utf-8'):
                    raise ValueError('Refuse overwriting a different replay file')
        else:
            with os.fdopen(fd, 'wb') as stream:
                stream.write(content.encode('utf-8'))
                stream.flush()
                os.fsync(stream.fileno())
    finally:
        os.close(parent_fd)
    return destination


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output-dir', type=Path, help='Optional reviewed replay outside checkout')
    args = parser.parse_args(argv)
    try:
        legacy, remaining, record = check(args.root)
        replay = None
        if not remaining and args.output_dir is not None:
            replay = str(_replay_checked_record(record, args.output_dir, args.root))
        result = {'lesson_id': LESSON_ID, 'legacy_errors': legacy,
                  'reviewed_repair': BLOCK_ID if not remaining else None,
                  'result': 'PASS_WITH_REVIEWED_GFM_REPAIR' if not remaining else 'FAIL',
                  'remaining_errors': remaining, 'replay_path': replay}
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as error:
        result = {'lesson_id': LESSON_ID, 'result': 'FAIL', 'remaining_errors': [str(error)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['result'] == 'PASS_WITH_REVIEWED_GFM_REPAIR' else 1


if __name__ == '__main__':
    raise SystemExit(main())
