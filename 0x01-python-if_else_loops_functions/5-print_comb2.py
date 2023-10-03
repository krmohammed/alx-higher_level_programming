#!/usr/bin/python3
for c in range(100):
    if c < 10:
        print("{}{}".format(0, c), end=', ')
        continue
    print("{}".format(c), end=', ')
