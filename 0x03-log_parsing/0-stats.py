#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""
import sys
import signal

total_size = 0
status_codes_count = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handle the signal for CTRL+C (KeyboardInterrupt)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        print(f"Processing line: {line.strip()}")

        parts = line.split()
        if len(parts) < 7:
            print(f"Skipped line (not enough parts): {line.strip()}")
            continue

        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            print(f"Status code: {status_code}, File size: {file_size}")
        except (ValueError, IndexError):
            print(f"Skipped line (parsing error): {line.strip()}")
            continue

        total_size += file_size
        print(f"Total file size updated to: {total_size}")

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
            print(f"Status code {status_code} count updated to: "
                  f"{status_codes_count[status_code]}")

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
