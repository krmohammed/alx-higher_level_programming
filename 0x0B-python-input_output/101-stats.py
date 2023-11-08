#!/usr/bin/python3
"""
log parsing
"""
import sys


status_code = {'200': , '301': , '400': , '401': , '403': , '404': , '405': , '500': }
line_num = 0
file_size_t = 0

try:
    for line in sys.stdin:
        parsed = line.split()
        if len(parsed) >= 7:
            stat_code = int(parts[-2])
            file_size = int(parts[-1])

            file_size_t += file_size
            if code in status_code:
                status_code[code] += 1

            line_num += 1

            if line_num % 10 == 0:
                print("Total file size: {}".format(file_size_t))
                for code, count in sorted(status_code.items()):
                    if count > 0:
                        print("{}: {}".format(code, count))

except KeyboardInterrupt:
    print("Total file size: {}".format(file_size_t))
    for code, count in sorted(status_code.items()):
        if count > 0:
            print("{}: {}".format(code, count))
