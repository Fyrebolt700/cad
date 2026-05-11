"""
analyze_cycles.py

Analyzes actuator validation cycle data and generates:
- summary_report.md
- position_error_plot.png

Run:
python analyze_cycles.py --input cycle_log.csv
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="cycle_log.csv")
    parser.add_argument("--error-limit", type=float, default=3.0)
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"File not found: {input_path}")

    df = pd.read_csv(input_path)
    df["abs_error_deg"] = df["position_error_deg"].abs()

    total_cycles = len(df)
    pass_count = int((df["abs_error_deg"] <= args.error_limit).sum())
    fail_count = total_cycles - pass_count
    max_error = df["abs_error_deg"].max()
    mean_error = df["abs_error_deg"].mean()

    report = f"""# Actuator Validation Summary

## Test Results

- Total cycles: {total_cycles}
- Pass count: {pass_count}
- Fail count: {fail_count}
- Error limit: ±{args.error_limit:.1f} degrees
- Mean absolute position error: {mean_error:.2f} degrees
- Max absolute position error: {max_error:.2f} degrees

## Pass Criteria

A cycle passes if the measured actuator position is within the selected position error limit.

## Notes

This script supports both simulated data and serial data from a future microcontroller or DAQ setup.
"""

    Path("summary_report.md").write_text(report)

    plt.figure()
    plt.plot(df["cycle"], df["position_error_deg"], marker="o")
    plt.axhline(args.error_limit, linestyle="--")
    plt.axhline(-args.error_limit, linestyle="--")
    plt.xlabel("Cycle")
    plt.ylabel("Position Error (deg)")
    plt.title("Actuator Position Error Over Cycles")
    plt.tight_layout()
    plt.savefig("position_error_plot.png", dpi=200)

    print(report)
    print("Saved summary_report.md and position_error_plot.png")


if __name__ == "__main__":
    main()
