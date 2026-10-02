#!/usr/bin/env python3
"""S19 fail-closed tests. All review approvals here are synthetic test fixtures."""
import contextlib
import builtins
import copy
import hashlib
import io
import json
import os
import subprocess
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import check_stage as s


class RepairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core = s.load_core(s.ROOT)
        cls.source_text = (s.ROOT / s.SOURCE_PATH).read_text()
        cls.target_text = (s.ROOT / s.TARGET_PATH).read_text()
        cls.base_record = json.loads((s.ROOT / s.RECORD_DIR / 'translation.json').read_text())

    def setUp(self):
        self.source, self.target = self.source_text, self.target_text
        self.record = copy.deepcopy(self.base_record)
        self.record['status'] = 'language-reviewed'
        keys = ('lesson_id', 'source_path', 'source_commit', 'source_blob', 'source_sha256',
                'target_path', 'glossary_version', 'glossary_sha256', 'status')
        self.review = {key: self.record[key] for key in keys}
        self.review['reviewed_target_sha256'] = s.TARGET_SHA
        self.review[s.APPROVAL_FIELD] = [{**s.expected_approval(),
            'reason': 'SYNTHETIC TEST FIXTURE ONLY: exact two-row GFM escape.'}]

    def run_filter(self, errors=None):
        return s.reviewed_table_exception([s.DIAGNOSTIC] if errors is None else errors,
            self.record, self.review, self.source, self.target, self.core)

    def assert_rejected(self):
        self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_exact_approved_repair(self):
        self.assertEqual(self.run_filter(), [])
        self.assertEqual(self.core.validate(self.source, self.target), [s.DIAGNOSTIC])

    def test_inverse_restores_exact_draft_and_core_pass(self):
        original = s.reverse_exact_repair(self.source, self.target, self.core)
        self.assertEqual(s.sha(original), s.ORIGINAL_TARGET_SHA)
        self.assertEqual(len(self.target) - len(original), 8)
        self.assertEqual(self.core.validate(self.source, original), [])

    def test_every_other_core_error_preserved(self):
        errors = [s.DIAGNOSTIC, 'TARGET_CHANGED: concurrent edit; refuse overwrite',
                  'Source blob mismatch', '245: numbers moved across a block or changed']
        self.assertEqual(self.run_filter(errors), errors[1:])

    def test_diagnostic_removed_only_once(self):
        self.assertEqual(self.run_filter([s.DIAGNOSTIC] * 2), [s.DIAGNOSTIC])

    def test_missing_diagnostic_fails_closed(self):
        self.assertTrue(self.run_filter([]))

    def test_near_match_diagnostic_not_removed(self):
        self.assertIn('table_columns mismatch ', self.run_filter(['table_columns mismatch ']))

    def test_old_author_draft_is_not_accepted(self):
        self.target = s.reverse_exact_repair(self.source, self.target, self.core)
        self.record['target_sha256'] = s.sha(self.target)
        self.review['reviewed_target_sha256'] = s.sha(self.target)
        self.assertTrue(self.run_filter(self.core.validate(self.source, self.target)))

    def test_partial_repair_rejected(self):
        self.target = self.target.replace(s.ESCAPED_NORM, s.ORIGINAL_NORM, 1)
        self.assert_rejected()

    def test_extra_escape_rejected(self):
        self.target = self.target.replace('kappa =', r'\kappa =', 1)
        self.assert_rejected()

    def test_changed_formula_and_rebound_hashes_rejected(self):
        self.target = self.target.replace('m > n', 'm < n', 1)
        self.record['target_sha256'] = s.sha(self.target)
        self.review['reviewed_target_sha256'] = s.sha(self.target)
        self.assert_rejected()

    def test_missing_block_rejected(self):
        self.target = self.target.removesuffix(self.core.blocks(self.target)[-1])
        self.assert_rejected()

    def test_changed_source_rejected(self):
        self.source += '\n'
        self.assert_rejected()

    def test_record_and_review_identities_are_pinned(self):
        for obj in (self.record, self.review):
            for key in ('lesson_id', 'source_path', 'target_path', 'source_commit', 'source_sha256'):
                with self.subTest(key=key):
                    old = obj[key]; obj[key] = 'wrong'
                    self.assert_rejected(); obj[key] = old

    def test_source_target_path_traversal_rejected(self):
        self.record['target_path'] = '../outside.md'
        self.assert_rejected()

    def test_status_must_be_reviewed_in_both_records(self):
        for obj in (self.record, self.review):
            for status in ('draft', 'tech-reviewed', None):
                with self.subTest(status=status):
                    obj['status'] = status; self.assert_rejected()
            obj['status'] = 'language-reviewed'

    def test_target_and_review_hashes_are_pinned(self):
        self.record['target_sha256'] = '0' * 64; self.assert_rejected()
        self.record['target_sha256'] = s.TARGET_SHA
        self.review['reviewed_target_sha256'] = '0' * 64; self.assert_rejected()

    def test_missing_approval_rejected(self):
        del self.review[s.APPROVAL_FIELD]; self.assert_rejected()

    def test_duplicate_approval_rejected(self):
        self.review[s.APPROVAL_FIELD] *= 2; self.assert_rejected()

    def test_all_approval_bindings_checked(self):
        approval = self.review[s.APPROVAL_FIELD][0]
        for key in s.expected_approval():
            with self.subTest(key=key):
                old = approval[key]; approval[key] = 'wrong'
                self.assert_rejected(); approval[key] = old

    def test_non_boolean_approval_rejected(self):
        for value in (1, 'true', False, None):
            self.review[s.APPROVAL_FIELD][0]['independent_review_passed'] = value
            self.assert_rejected()

    def test_row_indices_require_exact_integer_list(self):
        for value in ([8.0, 9.0], [8, 9.0], (8, 9), [True, 9], [8], [8, 9, 10]):
            with self.subTest(value=value):
                self.review[s.APPROVAL_FIELD][0]['row_indices_zero_based'] = value
                self.assert_rejected()

    def test_reason_required(self):
        for reason in ('', ' ', None, 7):
            self.review[s.APPROVAL_FIELD][0]['reason'] = reason
            self.assert_rejected()

    def test_unexpected_approval_field_rejected(self):
        self.review[s.APPROVAL_FIELD][0]['allow_other_tables'] = True
        self.assert_rejected()

    def test_per_block_target_hash_checked(self):
        self.record['segments'][5]['target_sha256'] = '0' * 64
        self.assert_rejected()

    def test_per_block_id_checked(self):
        self.record['segments'][3]['segment_id'] = '01-17:b0999'
        self.assert_rejected()

    def test_recorded_target_changed_rejected(self):
        self.record['segments'][2]['target'] += '\n'
        self.assert_rejected()

    def test_table_source_hash_checked(self):
        self.record['segments'][s.BLOCK_INDEX]['source_sha256'] = '0' * 64
        self.assert_rejected()

    def test_english_fallback_rejected(self):
        self.target = self.source
        errors = self.core.validate(self.source, self.target)
        result = self.run_filter(errors)
        self.assertIn('No Chinese prose; English fallback rejected', result)

    def test_changed_pinned_core_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / 'scripts/curated_translation.py'; p.parent.mkdir()
            p.write_text('# changed core\n')
            with self.assertRaisesRegex(ValueError, 'core hash changed'):
                s.load_core(temp)

    def make_checkout(self, root):
        paths = [s.SOURCE_PATH, s.TARGET_PATH, 'scripts/curated_translation.py',
                 'i18n/zh/.curated/TERMINOLOGY.md', self.record['additional_glossary_path']]
        for path in paths:
            p = root / path; p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes((s.ROOT / path).read_bytes())
        # Reuse read-only Git object access, never copy old translations or caches.
        git_dir = subprocess.check_output(
            ['git', '-C', str(s.ROOT), 'rev-parse', '--absolute-git-dir'], text=True).strip()
        (root / '.git').write_text('gitdir: ' + git_dir + '\n')
        d = root / s.RECORD_DIR; d.mkdir(parents=True)
        (d / 'translation.json').write_text(json.dumps(self.record, ensure_ascii=False))
        (d / 'review.json').write_text(json.dumps(self.review, ensure_ascii=False))

    def test_verified_core_bytes_executed_despite_later_path_change(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); p = root / 'scripts/curated_translation.py'
            p.parent.mkdir(); verified = (s.ROOT / 'scripts/curated_translation.py').read_bytes()
            p.write_bytes(verified)
            calls = []
            def swap_before_compile(content, filename, mode):
                self.assertEqual(content, verified)
                self.assertEqual(hashlib.sha256(content).hexdigest(), s.CORE_SHA)
                p.write_text('raise AssertionError("UNVERIFIED CORE EXECUTED")\n')
                calls.append(True)
                return builtins.compile(content, filename, mode)
            with mock.patch.object(s, 'compile', side_effect=swap_before_compile, create=True):
                core = s.load_core(root)
            self.assertEqual(calls, [True])
            self.assertTrue(callable(core.check_record))
            self.assertIn('UNVERIFIED', p.read_text())

    def test_input_symlinks_rejected_before_external_bytes_or_core_check(self):
        input_paths = [s.SOURCE_PATH, s.TARGET_PATH, s.RECORD_DIR + '/translation.json',
                       s.RECORD_DIR + '/review.json', 'i18n/zh/.curated/TERMINOLOGY.md',
                       self.record['additional_glossary_path']]
        for relative in input_paths:
            with self.subTest(path=relative), tempfile.TemporaryDirectory() as temp:
                root = Path(temp) / 'repo'; root.mkdir(); self.make_checkout(root)
                path = root / relative
                external = Path(temp) / 'external'; external.write_bytes(path.read_bytes())
                path.unlink(); path.symlink_to(external)
                opened_external = []
                real_fdopen = os.fdopen
                def guarded_fdopen(fd, *args, **kwargs):
                    if os.readlink('/proc/self/fd/' + str(fd)) == str(external):
                        opened_external.append(True)
                    return real_fdopen(fd, *args, **kwargs)
                with mock.patch.object(s, 'load_core', return_value=self.core), \
                     mock.patch.object(self.core, 'check_record', wraps=self.core.check_record) as core_check, \
                     mock.patch.object(s.os, 'fdopen', side_effect=guarded_fdopen):
                    with self.assertRaises(OSError):
                        s.check(root)
                    core_check.assert_not_called()
                self.assertEqual(opened_external, [])

    def test_core_input_symlink_rejected_without_read(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'repo'; p = root / 'scripts/curated_translation.py'
            p.parent.mkdir(parents=True)
            external = Path(temp) / 'external.py'
            external.write_bytes((s.ROOT / 'scripts/curated_translation.py').read_bytes())
            p.symlink_to(external)
            with mock.patch.object(s.os, 'fdopen', side_effect=AssertionError('unexpected read')):
                with self.assertRaises(OSError):
                    s.load_core(root)

    def test_input_directory_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'repo'; root.mkdir(); self.make_checkout(root)
            directory = root / s.TARGET_PATH
            directory.unlink(); directory.parent.rmdir()
            external = Path(temp) / 'external'; external.mkdir()
            (external / 'zh.md').write_text(self.target)
            directory.parent.symlink_to(external, target_is_directory=True)
            with self.assertRaises(OSError):
                s.check(root)

    def test_record_selected_asset_symlink_preflighted(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'repo'; root.mkdir(); self.make_checkout(root)
            external = Path(temp) / 'external'; external.write_text('must not read')
            (root / 'asset.svg').symlink_to(external)
            path = root / s.RECORD_DIR / 'translation.json'
            record = json.loads(path.read_text())
            record['assets'] = [{'source_path': 'asset.svg', 'target_path': 'asset.svg'}]
            path.write_text(json.dumps(record))
            with mock.patch.object(s, 'load_core', return_value=self.core), \
                 mock.patch.object(self.core, 'check_record', wraps=self.core.check_record) as core_check:
                with self.assertRaises(OSError):
                    s.check(root)
                core_check.assert_not_called()

    def test_nonregular_input_rejected_without_fifo_read(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); os.mkfifo(root / 'input')
            with self.assertRaisesRegex(ValueError, 'not a regular file'):
                s._read_input(root, 'input')

    def test_full_core_check_and_review_binding(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); self.make_checkout(root)
            legacy, remaining, _ = s.check(root)
            self.assertEqual(legacy, [s.DIAGNOSTIC]); self.assertEqual(remaining, [])
            p = root / s.RECORD_DIR / 'review.json'
            review = json.loads(p.read_text()); review['source_blob'] = '0' * 40
            p.write_text(json.dumps(review))
            legacy, remaining, _ = s.check(root)
            self.assertIn('Review binding mismatch: source_blob', legacy)
            self.assertIn('Review binding mismatch: source_blob', remaining)

    def test_full_core_error_not_filtered(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); self.make_checkout(root)
            p = root / s.RECORD_DIR / 'translation.json'
            record = json.loads(p.read_text()); record['glossary_sha256'] = '0' * 64
            p.write_text(json.dumps(record))
            legacy, remaining, _ = s.check(root)
            self.assertIn('Glossary changed; review invalidated', legacy)
            self.assertIn('Glossary changed; review invalidated', remaining)

    def test_real_draft_without_review_cannot_replay(self):
        self.record['status'] = 'draft'
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'repo'; root.mkdir(); self.make_checkout(root)
            (root / s.RECORD_DIR / 'review.json').unlink()
            output = Path(temp) / 'out'
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(s.main(['--root', str(root), '--output-dir', str(output)]), 1)
            self.assertFalse(output.exists())

    def test_successful_cli_replay_uses_checked_in_memory_record(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'repo'; root.mkdir(); self.make_checkout(root)
            output = Path(temp) / 'out'
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(s.main(['--root', str(root), '--output-dir', str(output)]), 0)
            self.assertEqual((output / s.TARGET_PATH).read_bytes(), self.target.encode())

    def test_replay_roundtrip_and_identical_existing_content(self):
        with tempfile.TemporaryDirectory() as temp:
            a = s._replay_checked_record(self.record, Path(temp) / 'a', s.ROOT)
            b = s._replay_checked_record(self.record, Path(temp) / 'b', s.ROOT)
            s._replay_checked_record(self.record, Path(temp) / 'a', s.ROOT)
            self.assertEqual(a.read_bytes(), b.read_bytes())
            self.assertEqual(hashlib.sha256(a.read_bytes()).hexdigest(), s.TARGET_SHA)

    def test_replay_different_content_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / s.TARGET_PATH; path.parent.mkdir(parents=True)
            path.write_text('keep this')
            with self.assertRaisesRegex(ValueError, 'different replay file'):
                s._replay_checked_record(self.record, temp, s.ROOT)
            self.assertEqual(path.read_text(), 'keep this')

    def test_replay_rejects_checkout_and_descendant(self):
        for path in (s.ROOT, s.ROOT / 'new-output'):
            with self.assertRaisesRegex(ValueError, 'outside checkout'):
                s._replay_checked_record(self.record, path, s.ROOT)

    def test_replay_rejects_path_traversal(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, 'traversal'):
                s._replay_checked_record(self.record, Path(temp) / 'x/../y', s.ROOT)

    def test_replay_rejects_output_root_symlink(self):
        with tempfile.TemporaryDirectory() as temp:
            real = Path(temp) / 'real'; real.mkdir()
            link = Path(temp) / 'link'; link.symlink_to(real, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, 'symlink'):
                s._replay_checked_record(self.record, link, s.ROOT)
            self.assertEqual(list(real.iterdir()), [])

    def test_replay_rejects_nested_directory_symlink(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / 'out'; out.mkdir()
            real = Path(temp) / 'real'; real.mkdir()
            (out / 'i18n').symlink_to(real, target_is_directory=True)
            with self.assertRaises(OSError):
                s._replay_checked_record(self.record, out, s.ROOT)
            self.assertEqual(list(real.iterdir()), [])

    def test_replay_rejects_file_symlink(self):
        with tempfile.TemporaryDirectory() as temp:
            real = Path(temp) / 'real'; real.write_text('preserve')
            out = Path(temp) / 'out'; dest = out / s.TARGET_PATH
            dest.parent.mkdir(parents=True); dest.symlink_to(real)
            with self.assertRaises(OSError):
                s._replay_checked_record(self.record, out, s.ROOT)
            self.assertEqual(real.read_text(), 'preserve')

    def test_replay_rejects_nonregular_file(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp) / s.TARGET_PATH; dest.parent.mkdir(parents=True)
            os.mkfifo(dest)
            with self.assertRaisesRegex(ValueError, 'not a regular file'):
                s._replay_checked_record(self.record, temp, s.ROOT)

    def test_replay_changed_in_memory_record_rejected(self):
        self.record['segments'][0]['target'] += 'changed'
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, 'content hash mismatch'):
                s._replay_checked_record(self.record, temp, s.ROOT)
            self.assertFalse((Path(temp) / s.TARGET_PATH).exists())

    def test_replay_record_status_or_path_rejected(self):
        for key, value in [('status', 'draft'), ('target_path', '../escape')]:
            old = self.record[key]; self.record[key] = value
            with tempfile.TemporaryDirectory() as temp:
                with self.assertRaisesRegex(ValueError, 'record binding mismatch'):
                    s._replay_checked_record(self.record, temp, s.ROOT)
            self.record[key] = old

    def test_concurrent_creator_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / 'out'
            real_open = os.open
            created = []
            def competing_open(path, flags, *args, **kwargs):
                if flags & os.O_EXCL and not created:
                    fd = real_open(path, flags, *args, **kwargs)
                    os.write(fd, b'concurrent content'); os.close(fd); created.append(True)
                return real_open(path, flags, *args, **kwargs)
            with mock.patch.object(s.os, 'open', side_effect=competing_open):
                with self.assertRaisesRegex(ValueError, 'different replay file'):
                    s._replay_checked_record(self.record, output, s.ROOT)
            self.assertEqual((output / s.TARGET_PATH).read_bytes(), b'concurrent content')


if __name__ == '__main__':
    unittest.main()
