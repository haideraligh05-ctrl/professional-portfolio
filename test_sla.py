import unittest

from sla import evaluate, parse_timestamp


class ComplaintSLATest(unittest.TestCase):
    def setUp(self):
        self.record = {
            "id": "C001",
            "opened_at": "2026-01-02T12:00:00Z",
            "sla_hours": "24",
            "resolved_at": "",
        }

    def test_status_at_deadline_boundaries(self):
        cases = (
            ("2026-01-03T12:00:00Z", "", "Open within SLA"),
            ("2026-01-03T12:00:01Z", "", "Overdue"),
            ("2026-01-03T12:00:00Z", "2026-01-03T17:00:00+05:00", "Resolved within SLA"),
            ("2026-01-03T12:00:01Z", "2026-01-03T12:00:01Z", "Resolved late"),
        )
        for report_time, resolved_at, expected in cases:
            with self.subTest(report_time=report_time, resolved_at=resolved_at):
                record = {**self.record, "resolved_at": resolved_at}
                self.assertEqual(
                    evaluate(record, parse_timestamp(report_time)),
                    ("C001", "2026-01-03T12:00:00+00:00", expected),
                )

    def test_timestamp_requires_timezone(self):
        with self.assertRaisesRegex(ValueError, "UTC offset"):
            parse_timestamp("2026-01-03T12:00:00")

    def test_rejects_invalid_records(self):
        report_time = parse_timestamp("2026-01-03T12:00:00Z")
        invalid_fields = (
            {"sla_hours": "0"},
            {"opened_at": "2026-01-04T12:00:00Z"},
            {"resolved_at": "2026-01-02T11:59:59Z"},
            {"resolved_at": "2026-01-03T12:00:01Z"},
        )
        for changes in invalid_fields:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                evaluate({**self.record, **changes}, report_time)


if __name__ == "__main__":
    unittest.main()
