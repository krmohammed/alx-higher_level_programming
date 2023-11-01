#!/usr/bin/python3
"""
provides one function, matrix_mul()
"""


def matrix_mul(m_a, m_b):
    """
    multiplies two matrices

    Args:
        m_a (list): first matrix
        m_b (list): second matrix

    Returns:
        product of the two matrices
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if not all(len(j) > 0 for j in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if not all(len(j) > 0 for j in m_b):
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if not all(type(j) in [int, float] for j in i):
            raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        if not all(type(j) in [int, float] for j in i):
            raise TypeError("m_b should contain only integers or floats")
    if not all(len(m_a[0]) == len(i) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(i) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    product = []
    for j in range(len(m_a)):
        row_p = []
        for k in range(len(m_b[0])):
            sum = 0
            for i in range(len(m_a[0])):
                sum += m_a[j][i] * m_b[i][k]
            row_p.append(sum)
        product.append(row_p)
    return product
