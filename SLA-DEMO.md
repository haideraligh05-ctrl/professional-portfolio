# Complaint SLA demo

Run with Python 3.10 or later from the repository root.

```bash
python3 sla.py complaints.csv --as-of 2026-01-03T12:00:00Z
```

The CSV contains synthetic records and deadlines measured in elapsed hours. Open records become overdue after their deadline. Resolved records are compared against their actual resolution time. The output is a CSV suitable for importing into Excel.
