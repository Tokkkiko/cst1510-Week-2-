
"""
RECORD CHECK - IT
=================

Name  :
Lane  : IT
Date  :

Run it: python template.py
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Calculate the difference, percentage and status of a record."""
    difference = value - limit
    percent = (value / limit) * 100

    if value <= limit:
        status = "OK"
    else:
        status = "OVER LIMIT"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one IT system record."""
    print(f"Label:      {label}")
    print(f"Value:      {value:.2f}")
    print(f"Limit:      {limit:.2f}")
    print(f"Difference: {difference:+.2f}")
    print(f"Percent:    {percent:.2f}%")
    print(f"Status:     {status}")
    print("-" * 30)


# ====================================================================== STORE

def load_records(path):
    """Load IT monitoring records from a file."""
    records = []

    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                label, value, limit = line.split(",")

                record = {
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                }

                records.append(record)

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []

    return records


# =============================================================== PROCESS + OUTPUT

if __name__ == "__main__":
    records = load_records("records_sample.txt")
    over_limit_count = 0

    with open("results.txt", "w") as w:
        for record in records:
            difference, percent, status = check_record(
                record["value"], record["limit"]
            )

            print_report(
                record["label"],
                record["value"],
                record["limit"],
                difference,
                percent,
                status
            )

            if status == "OVER LIMIT":
                over_limit_count += 1

            w.write(f"{record['label']},{status}\n")

    print(f"Total IT records over limit: {over_limit_count}")

    with open("results.txt", "r") as f:
        for line in f:
            print(line.strip())
