"""
serial_logger.py

Logs actuator validation cycle data from a serial device.

Expected serial line format from a microcontroller:
cycle,target_angle,measured_angle,status

Example:
1,90,89.4,PASS

If no serial port is available, run with --simulate to generate sample data:
python serial_logger.py --simulate --cycles 50
"""

import argparse
import csv
import random
import time
from datetime import datetime
from pathlib import Path


def write_header_if_needed(csv_path: Path) -> None:
    if not csv_path.exists():
        with csv_path.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "cycle",
                "target_angle_deg",
                "measured_angle_deg",
                "position_error_deg",
                "status",
            ])


def log_row(csv_path: Path, cycle: int, target: float, measured: float, status: str) -> None:
    error = measured - target
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            cycle,
            f"{target:.2f}",
            f"{measured:.2f}",
            f"{error:.2f}",
            status,
        ])


def simulate(csv_path: Path, cycles: int) -> None:
    write_header_if_needed(csv_path)

    target_angles = [0, 45, 90, 135, 180, 135, 90, 45]
    for cycle in range(1, cycles + 1):
        target = target_angles[(cycle - 1) % len(target_angles)]
        drift = 0.015 * cycle
        noise = random.uniform(-1.2, 1.2)
        measured = target + drift + noise
        error = abs(measured - target)
        status = "PASS" if error <= 3.0 else "FAIL"

        log_row(csv_path, cycle, target, measured, status)
        print(f"cycle={cycle}, target={target:.1f}, measured={measured:.1f}, status={status}")
        time.sleep(0.03)


def log_from_serial(csv_path: Path, port: str, baud: int) -> None:
    try:
        import serial
    except ImportError as exc:
        raise SystemExit("Install pyserial first: pip install pyserial") from exc

    write_header_if_needed(csv_path)

    with serial.Serial(port, baud, timeout=1) as ser:
        print(f"Logging from {port} at {baud} baud. Press Ctrl+C to stop.")
        while True:
            line = ser.readline().decode(errors="ignore").strip()
            if not line:
                continue

            try:
                cycle_s, target_s, measured_s, status = line.split(",")
                cycle = int(cycle_s)
                target = float(target_s)
                measured = float(measured_s)
                log_row(csv_path, cycle, target, measured, status)
                print(line)
            except ValueError:
                print(f"Skipped malformed line: {line}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="cycle_log.csv", help="Output CSV file")
    parser.add_argument("--port", default=None, help="Serial port, ex: COM3 or /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=9600)
    parser.add_argument("--simulate", action="store_true")
    parser.add_argument("--cycles", type=int, default=50)
    args = parser.parse_args()

    csv_path = Path(args.output)

    if args.simulate:
        simulate(csv_path, args.cycles)
    elif args.port:
        log_from_serial(csv_path, args.port, args.baud)
    else:
        raise SystemExit("Use --simulate or provide --port.")


if __name__ == "__main__":
    main()
