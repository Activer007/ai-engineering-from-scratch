#!/usr/bin/env python3
"""Fail-closed tests for S07's exact symbolic-table exception."""
import copy
import tempfile
import unittest
from pathlib import Path
import check_stage as s


class SymbolicExceptionTests(unittest.TestCase):
    def setUp(self):
        self.core = s.load_core(s.ROOT)
        self.source = (s.ROOT / s.SOURCE_PATH).read_text()
        self.target = self.source
        self.record = {'lesson_id': '01-04', 'source_path': s.SOURCE_PATH,
                       'source_commit': s.SOURCE_COMMIT, 'source_sha256': s.SOURCE_SHA,
                       'target_sha256': s.sha(self.target), 'status': 'language-reviewed'}
        self.review = {'status': 'language-reviewed', 'reviewed_target_sha256': s.sha(self.target),
                       'unchanged_symbolic_blocks': [{'segment_id': s.BLOCK_ID,
                       'source_sha256': s.BLOCK_SHA, 'target_sha256': s.BLOCK_SHA,
                       'independent_review_passed': True,
                       'classification': 'pure-mathematical-symbol-table',
                       'reason': 'Only symbolic Jacobian entries; independently checked unchanged.'}]}

    def run_filter(self, errors=None):
        return s.reviewed_symbolic_exception([s.DIAGNOSTIC] if errors is None else errors,
                                            self.record, self.review, self.source, self.target, self.core)

    def test_exact_approved_table(self):
        self.assertEqual(self.run_filter(), [])

    def test_other_errors_preserved(self):
        self.assertEqual(self.run_filter([s.DIAGNOSTIC, 'TARGET_CHANGED', 'fenced payload changed']),
                         ['TARGET_CHANGED', 'fenced payload changed'])

    def test_duplicate_diagnostic_not_fully_removed(self):
        self.assertEqual(self.run_filter([s.DIAGNOSTIC, s.DIAGNOSTIC]), [s.DIAGNOSTIC])

    def test_unrelated_unchanged_prose(self):
        self.assertIn('17: unchanged translatable segment needs explicit review',
                      self.run_filter(['17: unchanged translatable segment needs explicit review']))

    def test_missing_approval(self):
        del self.review['unchanged_symbolic_blocks']; self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_non_boolean_approval(self):
        self.review['unchanged_symbolic_blocks'][0]['independent_review_passed'] = 'true'
        self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_wrong_block_hash(self):
        self.review['unchanged_symbolic_blocks'][0]['target_sha256'] = '0' * 64
        self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_wrong_block_id(self):
        self.review['unchanged_symbolic_blocks'][0]['segment_id'] = '01-04:b0214'
        self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_wrong_lesson(self):
        self.record['lesson_id'] = '01-05'; self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_wrong_source_path(self):
        self.record['source_path'] = 'other'; self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_stale_source(self):
        self.source += '\n'; self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_modified_table(self):
        self.target = self.target.replace('df1/dx1', 'df1/dx2')
        self.record['target_sha256'] = s.sha(self.target)
        self.review['reviewed_target_sha256'] = s.sha(self.target)
        self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_added_prose_in_table(self):
        self.target = self.target.replace('| | x1', '| untranslated | x1')
        self.record['target_sha256'] = s.sha(self.target)
        self.review['reviewed_target_sha256'] = s.sha(self.target)
        self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_stale_review(self):
        self.review['reviewed_target_sha256'] = '0' * 64
        self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_multiple_approvals(self):
        self.review['unchanged_symbolic_blocks'].append(copy.deepcopy(self.review['unchanged_symbolic_blocks'][0]))
        self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_self_review_not_accepted(self):
        self.record['status'] = 'draft'; self.assertIn(s.DIAGNOSTIC, self.run_filter())

    def test_legacy_hash_change_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / 'scripts/curated_translation.py'; p.parent.mkdir()
            p.write_text('# changed checker\n')
            with self.assertRaisesRegex(ValueError, 'hash changed'):
                s.load_core(temp)

    def test_silent_math_mutation_cannot_evade_exception(self):
        self.target = self.target.replace('df1/dx1', 'df1/dy1')
        self.record['target_sha256'] = s.sha(self.target)
        self.review['reviewed_target_sha256'] = s.sha(self.target)
        self.assertTrue(self.run_filter([]))

    def test_missing_expected_diagnostic_fails_closed(self):
        self.assertTrue(self.run_filter([]))

    def test_no_diagnostic_wrong_lesson(self):
        self.record['lesson_id'] = '01-05'
        self.assertIn('symbolic exception source identity mismatch', self.run_filter([]))

    def test_no_diagnostic_missing_approval(self):
        del self.review['unchanged_symbolic_blocks']
        self.assertIn('symbolic exception explicit approval missing or mismatched', self.run_filter([]))

    def test_no_diagnostic_stale_review(self):
        self.review['reviewed_target_sha256'] = '0' * 64
        self.assertIn('symbolic exception target/review hash mismatch', self.run_filter([]))

    def test_no_diagnostic_changed_source(self):
        self.source += '\n'
        self.assertIn('symbolic exception source identity mismatch', self.run_filter([]))

    def test_english_fallback_still_fails(self):
        errors = self.core.validate(self.source, self.target)
        result = self.run_filter(errors)
        self.assertIn('No Chinese prose; English fallback rejected', result)
        self.assertTrue(any('unchanged translatable' in e for e in result))


if __name__ == '__main__':
    unittest.main()
