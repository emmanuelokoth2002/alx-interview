#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys


file_size = 0
stat = {
    '200': 0, '301': 0, '400': 0,
    '401': 0, '403': 0, '404': 0,
    '405': 0, '500': 0
}


def disp_stat():
    """
    prints the matrics
    """
    print('File size: {}'.format(file_size))
    for a, b in sorted(stat.items()):
        if b > 0:
            print('{}: {}'.format(a, b))


if __name__ == '__main__':
    lineNum = 0
    try:
        for line in sys.stdin:
            line = line.split()
            lineNum += 1
            try:
                file_size += int(line[-1])
                if line[-2] in stat.keys():
                    stat[line[-2]] += 1
            except (IndexError, ValueError):
                pass
            if lineNum % 10 == 0:
                disp_stat()
    except KeyboardInterrupt:
        disp_stat()
        raise
    else:
        disp_stat()
