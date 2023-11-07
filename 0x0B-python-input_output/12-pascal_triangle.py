#!/usr/bin/python3
"""
provides one function: pascal_triangle()
"""


def pascal_triangle(n):
    """
    computes the pascal's triangle up to n

    Args:
        n: size of triangle

    Returns:
        a list of lists of integers
        representing the Pascal’s triangle of `n
    """
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    triangle = [[1], [1, 1]]
    if n == 2:
        return triangle

    for i in range(n - 2):
        new_row = [1]
        last_row = triangle[-1]
        for j in range(len(last_row)):
            if j == len(last_row) - 1:
                new_row.append(1)
            else:
                sum = last_row[j] + last_row[j + 1]
                new_row.append(sum)
        triangle.append(new_row)

    return triangle
