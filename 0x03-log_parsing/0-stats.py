#!/usr/bin/python3
"""
Log parsing script that reads from stdin and computes metrics
"""

import sys
import signal
import re

# Initialize metrics
total_file_size = 0
status_code_counts = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
line_count = 0

# Regex pattern to validate and extract data from log lines
log_pattern = re.compile(
    r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_metrics():
    """Prints the accumulated metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interrupt signal to print metrics."""
    print_metrics()
    raise KeyboardInterrupt


# Set up signal handler for keyboard interrupt (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    # Reading from stdin
    for line in sys.stdin:
        line_count += 1

        # Match the line with the log pattern
        match = log_pattern.match(line.strip())
        if match:
            ip, date, status_code, file_size = match.groups()
            total_file_size += int(file_size)

            # Count status codes if they are in the predefined set
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

    # After processing all lines, print the final metrics
    print_metrics()

except KeyboardInterrupt:
    sys.exit(0)
