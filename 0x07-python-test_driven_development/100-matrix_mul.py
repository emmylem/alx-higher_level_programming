#!/usr/bin/python3
"""Multiply 2 Matrix."""


def matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices."""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if all(type(row) is not list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for x in range(len(m_b[0])):
        row1 = []
        for c in range(len(m_b)):
            row1.append(m_b[c][r])
        inverted_b.append(row1)

    matrix_1 = []
    for row in m_a:
        row1 = []
        for col in inverted_b:
            mul = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            row1.append(mul)
        matrix_1.append(row1)

    return (matrix_1)
