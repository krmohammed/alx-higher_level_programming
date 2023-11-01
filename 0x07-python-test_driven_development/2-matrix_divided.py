#!/usr/bin/python3
"""
provides one function, matrix_divide()
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix by div

    Args:
        matrix (list): matrix
        div (int/float): divisor

    Returns: new matrix
    """
    if type(matrix) is not list or not all(type(i) is list for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if not all(len(matrix[0]) == len(j) for j in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        if not all(type(j) in [int, float] for j in i):
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for i in matrix:
        new_matrix.append([round(j / div, 2) for j in i])
    return new_matrix
