#!/usr/bin/python3
"""
This module solves the N queens problem
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""


import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]
if not isinstance(int(N), int):
    print('N must be a number')
    sys.exit(1)

if int(N) < 4:
    print('N must be at least 4')
    sys.exit(1)
