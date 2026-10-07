"""Run with: python3 -m unittest discover -s tests -v"""

import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("tracker", Path(__file__).resolve().parents[1] / "tools" / "tracker.py")
tracker = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = tracker
spec.loader.exec_module(tracker)


class TrackerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "data").mkdir()
        self.catalog = [
            {"id": "nc-001", "title": "Contains Duplicate"},
            {"id": "nc-002", "title": "Valid Anagram"},
        ]
        self.write_json("neetcode150.json", self.catalog)
        self.write_json("topics.json", [{"id": "systems.ownership", "title": "Worker ownership", "domain": "systems"}])
        self.write_json("reviews.json", [])
        self.today = date(2026, 10, 7)

    def write_json(self, filename, value):
        (self.root / "data" / filename).write_text(json.dumps(value), encoding="utf-8")

    def events(self):
        return json.loads((self.root / "data" / "reviews.json").read_text())

    def record(self, outcome, on=None, item_id="nc-001", evidence="Explained and tested the result."):
        on = on or self.today
        return tracker.record_attempt(self.root, item_id, outcome, on, evidence, today=max(self.today, on))

    def test_intervals_advance_from_actual_review_date_and_cap(self):
        on = self.today
        state = self.record("independent", on)
        self.assertEqual(state.due, on + timedelta(days=1))
        for interval in (3, 7, 14, 30, 30):
            on = state.due + timedelta(days=2)  # Late reviews are anchored to the actual attempt.
            state = self.record("independent", on)
            self.assertEqual(state.due, on + timedelta(days=interval))
        self.assertEqual(len(self.events()), 6)

    def test_assisted_and_unsuccessful_outcomes_reset(self):
        for outcome in ("learned", "hinted", "needs_review"):
            with self.subTest(outcome=outcome):
                self.write_json("reviews.json", [])
                self.record("independent")
                self.record("independent", self.today + timedelta(days=1))
                state = self.record(outcome, self.today + timedelta(days=4))
                self.assertEqual(state.stage, 0)
                self.assertEqual(state.due, self.today + timedelta(days=5))

    def test_same_day_retry_does_not_advance_interval(self):
        self.record("learned")
        self.record("independent")
        state = self.record("independent")
        self.assertEqual(state.stage, 0)
        self.assertEqual(state.due, self.today + timedelta(days=1))
        self.assertEqual(len(self.events()), 3)

    def test_early_independent_attempts_preserve_due_date_and_stage(self):
        self.record("learned", date(2026, 10, 7))
        state = self.record("independent", date(2026, 10, 8))
        self.assertEqual(state.due, date(2026, 10, 11))
        self.assertEqual(state.stage, 1)
        for day in (9, 10):
            state = self.record("independent", date(2026, 10, day), evidence="Extra early practice.")
            self.assertEqual(state.due, date(2026, 10, 11))
            self.assertEqual(state.stage, 1)
            self.assertEqual(state.last_date, date(2026, 10, day))
            self.assertEqual(state.evidence, "Extra early practice.")
        state = self.record("independent", date(2026, 10, 11))
        self.assertEqual(state.stage, 2)
        self.assertEqual(state.due, date(2026, 10, 18))
        self.assertEqual(len(self.events()), 5)

    def test_daily_attempts_cannot_skip_the_longer_review_gaps(self):
        for day in range(7, 18):
            state = self.record("independent", date(2026, 10, day))
        # Due reviews occurred on Oct 8 and Oct 11. Daily practice after that
        # neither earns the 14/30-day stages nor moves the Oct 18 review.
        self.assertEqual(state.stage, 2)
        self.assertEqual(state.due, date(2026, 10, 18))
        self.assertEqual(len(self.events()), 11)

    def test_overdue_reviews_persist_and_display_is_capped(self):
        for item_id in ("nc-001", "nc-002", "systems.ownership"):
            self.record("learned", item_id=item_id)
        before = (self.root / "data" / "reviews.json").read_bytes()
        text = tracker.status_text(self.root, self.today + timedelta(days=5), limit=1)
        self.assertIn("3 overdue", text)
        self.assertIn("Backlog beyond this 1-item display: 2", text)
        self.assertEqual(before, (self.root / "data" / "reviews.json").read_bytes())
        text = tracker.status_text(self.root, self.today + timedelta(days=1))
        self.assertIn("0 overdue, 3 today", text)

    def test_invalid_dates_and_future_record_do_not_write(self):
        for bad_date in ("2026-2-01", "2026-02-30", "20261007", "not-a-date", None):
            with self.subTest(value=bad_date), self.assertRaises(tracker.TrackerError):
                tracker.parse_date(bad_date)
        with self.assertRaises(tracker.TrackerError):
            tracker.record_attempt(self.root, "nc-001", "independent", self.today + timedelta(days=1), "Tested.", today=self.today)
        self.assertEqual(self.events(), [])

    def test_chronology_is_per_item_and_rejects_backdated_append(self):
        self.record("learned")
        self.record("hinted", self.today - timedelta(days=2), item_id="nc-002")
        before = (self.root / "data" / "reviews.json").read_bytes()
        with self.assertRaises(tracker.TrackerError):
            self.record("independent", self.today - timedelta(days=1))
        self.assertEqual(before, (self.root / "data" / "reviews.json").read_bytes())
        self.assertFalse((self.root / "data" / ".reviews.lock").exists())

    def test_membership_outcome_and_evidence_validation(self):
        for item_id, outcome, evidence in (("", "learned", "test"), ("missing", "learned", "test"), ("nc-001", "mastered", "test"), ("nc-001", "learned", "  ")):
            with self.subTest(item_id=item_id, outcome=outcome, evidence=evidence), self.assertRaises(tracker.TrackerError):
                self.record(outcome, item_id=item_id, evidence=evidence)
        self.assertEqual(self.events(), [])
        state = self.record("learned", item_id="systems.ownership")
        self.assertEqual(state.stage, 0)

    def test_corrupt_json_or_invalid_events_are_never_overwritten(self):
        review_path = self.root / "data" / "reviews.json"
        for contents in ("{broken", "{}", '[{"item_id":"missing"}]'):
            with self.subTest(contents=contents):
                review_path.write_text(contents)
                with self.assertRaises(tracker.TrackerError):
                    self.record("learned")
                self.assertEqual(review_path.read_text(), contents)
                self.assertFalse((self.root / "data" / ".reviews.lock").exists())

    def test_failed_atomic_replacement_preserves_previous_file(self):
        self.record("learned")
        before = (self.root / "data" / "reviews.json").read_bytes()
        with patch.object(tracker.os, "replace", side_effect=OSError("simulated filesystem failure")):
            with self.assertRaises(OSError):
                self.record("independent", self.today + timedelta(days=1))
        self.assertEqual(before, (self.root / "data" / "reviews.json").read_bytes())
        self.assertEqual(list((self.root / "data").glob(".*.tmp")), [])
        self.assertFalse((self.root / "data" / ".reviews.lock").exists())

    def test_existing_lock_blocks_append_and_is_not_removed(self):
        lock = self.root / "data" / ".reviews.lock"
        lock.write_text("another writer")
        with self.assertRaises(tracker.TrackerError):
            self.record("learned")
        self.assertEqual(self.events(), [])
        self.assertTrue(lock.exists())

    def test_dashboard_separates_help_and_independent_and_lists_every_item(self):
        self.record("learned", evidence="Needed a frequency-map explanation.")
        self.record("independent", self.today + timedelta(days=1), evidence="Solved without hints; checked duplicates.")
        self.record("hinted", item_id="nc-002", evidence="Used hint | then checked\nexamples.")
        text = tracker.dashboard_text(self.root, self.today + timedelta(days=1))
        self.assertIn("**2** problems studied with explanations or hints", text)
        self.assertIn("**1** problems demonstrated independently", text)
        self.assertIn("Independent on latest attempt | 1", text)
        self.assertIn("| **Catalog total** | **2** |", text)
        self.assertIn("systems.ownership", text)
        self.assertIn("hint \\| then checked examples", text)

    def test_as_of_view_excludes_later_attempts_but_future_view_is_allowed(self):
        self.record("learned")
        self.record("independent", self.today + timedelta(days=3))
        historical = tracker.dashboard_text(self.root, self.today)
        self.assertIn("**0** problems demonstrated independently", historical)
        future = tracker.status_text(self.root, self.today + timedelta(days=50))
        self.assertIn("1 overdue", future)


if __name__ == "__main__":
    unittest.main()
