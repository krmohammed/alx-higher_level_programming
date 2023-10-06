#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = 'argument' if len(sys.argv) == 2 else 'arguments'
    if len(sys.argv) > 1:
        print('{:d} {}:'.format(len(sys.argv) - 1, arg))
        for i, j in enumerate(sys.argv):
            if i == 0:
                continue
            print('{:d}: {}'.format(i, j))
    else:
        print('{:d} {}.'.format(len(sys.argv) - 1, arg))
