"""Generate a small synthetic CSV for development use only.

Writes data/synthetic.csv at the repo root (the data/ folder is gitignored)
with 100 rows and columns id (int), timestamp (ISO-8601), value (float).
Uses a fixed seed and only the Python standard library. Prints aggregates
only, never raw rows.

Usage:
    python ml/make_synthetic.py
"""

import csv
import random
import statistics
from datetime import datetime, timedelta, timezone
from pathlib import Path

SEED = 42
ROW_COUNT = 100
START = datetime(2026, 1, 1, tzinfo=timezone.utc)
STEP = timedelta(hours=1)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "data" / "synthetic.csv"


def make_rows(rng: random.Random, count: int) -> list[dict]:
    return [
        {
            "id": i,
            "timestamp": (START + i * STEP).isoformat(),
            "value": round(rng.uniform(0.0, 10.0), 3),
        }
        for i in range(1, count + 1)
    ]


def main() -> None:
    rng = random.Random(SEED)
    rows = make_rows(rng, ROW_COUNT)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "timestamp", "value"])
        writer.writeheader()
        writer.writerows(rows)

    mean_value = statistics.fmean(row["value"] for row in rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT_PATH.relative_to(REPO_ROOT).as_posix()}")
    print(f"Mean value: {mean_value:.3f}")


if __name__ == "__main__":
    main()
