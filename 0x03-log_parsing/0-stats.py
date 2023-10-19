#!/usr/bin/python3
import sys


def print_stats(total_size, status_counts):
    """
    Print the statistics: total file size and number of lines by status code.
    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_counts.keys())
    for code in sorted_status_codes:
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 7:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                if status_code in status_counts:
                    status_counts[status_code] += 1
                total_size += file_size
                line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        pass  # Handle Ctrl+C gracefully

    print_stats(total_size, status_counts)
