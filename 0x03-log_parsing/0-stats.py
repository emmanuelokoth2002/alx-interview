#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics."""
import sys

POSSIBLE_STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}
LINES_READ = 0
STATUS_CODES_MAP = {}
TOTAL_FILE_SIZE = 0


def print_stats():
    """Prints out the statistics."""
    print("File size: {}".format(TOTAL_FILE_SIZE))
    for status, count in sorted(STATUS_CODES_MAP.items()):
        print("{}: {}".format(status, count))


try:
    for line in sys.stdin:
        line_tokens = line.split()
        try:
            file_size = int(line_tokens[-1])
            TOTAL_FILE_SIZE += file_size
            status_code = int(line_tokens[-2])
            if status_code in POSSIBLE_STATUS_CODES:
                STATUS_CODES_MAP[status_code] = STATUS_CODES_MAP.get(status_code, 0) + 1
        except ValueError:
            pass
        LINES_READ += 1
        if LINES_READ % 10 == 0:
            print_stats()

    if LINES_READ % 10 != 0:
        print_stats()

except KeyboardInterrupt:
    print_stats()
