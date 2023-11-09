#!/usr/bin/python3
"""
log parsing
"""
import sys


status_code = {
        200: 0, 301: 0,
        400: 0, 401: 0,
        403: 0, 404: 0,
        405: 0, 500: 0
    }
line_num = 0
file_size_t = 0

try:
    for line in sys.stdin:
        parsed = line.strip().split()
        if len(parsed) > 2:
            stat_code = int(parsed[-2])
            file_size = int(parsed[-1])

            file_size_t += file_size
            if stat_code in status_code:
                status_code[stat_code] += 1

            line_num += 1

            if line_num % 10 == 0:
                print("File size: {}".format(file_size_t))
                for code, count in sorted(status_code.items()):
                    if count > 0:
                        print("{}: {}".format(code, count))
except KeyboardInterrupt:
    print("Total file size: {}".format(file_size_t))
    for code, count in sorted(status_code.items()):
        if count > 0:
            print("{}: {}".format(code, count))
