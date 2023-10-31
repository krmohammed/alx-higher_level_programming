#!/usr/bin/python3
"""
This module solves the N queens problem
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""


import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])

        if N < 4:
            print('N must be at least 4')
            sys.exit(1)
    except ValueError:
        print('N must be an integer')
        sys.exit(1)
