#!/usr/bin/python3

import sys


def print_statistics(file_size, status_codes):
    """Prints statistics"""
    print(f"File size: {file_size}")
    for code in sorted(status_codes):
        if status_codes[code] != 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line, file_size, status_codes):
    """Parses each line and updates statistics"""
    return file_size, status_codes


def main():
    count = 0
    file_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            file_size, status_codes = parse_line(line, file_size, status_codes)
            count += 1

            if count % 10 == 0:
                print_statistics(file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)
        raise

if __name__ == '__main__':
    main()
