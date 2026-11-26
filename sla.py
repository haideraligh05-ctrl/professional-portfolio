import argparse
import csv
import sys
from datetime import datetime, timedelta


def parse_timestamp(value):
    timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if timestamp.utcoffset() is None:
        raise ValueError(f"Timestamp requires a UTC offset: {value}")
    return timestamp


def evaluate(record, as_of):
    opened = parse_timestamp(record["opened_at"])
    hours = int(record["sla_hours"])
    if hours <= 0 or opened > as_of:
        raise ValueError("SLA hours must be positive and opening must be on or before the report time")

    deadline = opened + timedelta(hours=hours)
    resolved = record["resolved_at"]
    if resolved:
        closed = parse_timestamp(resolved)
        if not opened <= closed <= as_of:
            raise ValueError("Resolution must fall between opening and the report time")
        status = "Resolved within SLA" if closed <= deadline else "Resolved late"
    else:
        status = "Overdue" if as_of > deadline else "Open within SLA"
    return record["id"], deadline.isoformat(), status


def main():
    parser = argparse.ArgumentParser(description="Report SLA status for complaint records.")
    parser.add_argument("input_csv")
    parser.add_argument("--as-of", required=True, type=parse_timestamp)
    args = parser.parse_args()

    results = []
    with open(args.input_csv, newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        for record in reader:
            try:
                results.append(evaluate(record, args.as_of))
            except (KeyError, TypeError, ValueError, OverflowError) as error:
                parser.error(f"CSV line {reader.line_num}: {error}")

    writer = csv.writer(sys.stdout)
    writer.writerow(("id", "deadline", "status"))
    writer.writerows(results)


if __name__ == "__main__":
    main()
