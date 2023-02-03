#!/usr/bin/python3
"""Multiplies 2 matrices."""


import NumPy as np


def lazy_matrix_mul(m_a, m_b):
    """A  function that multiplies 2 matrices
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
