#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys
import signal

# Initialize global variables
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


# Set up signal handler for KeyboardInterrupt (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Split the line into components
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])    # File size is the last element
        except (ValueError, IndexError):
            continue  # Skip lines that don't match the expected format

        # Update total file size
        total_size += file_size

        # Update status code count if the status code is valid
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats when CTRL+C is pressed
    print_stats()
    sys.exit(0)
