#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(0)
    else:
        infin_add = 0
        for i, j in enumerate(sys.argv):
            if i == 0:
                continue
            infin_add += int(j)
        print(infin_add)
