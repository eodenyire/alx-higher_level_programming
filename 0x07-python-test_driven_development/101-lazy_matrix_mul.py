#!/usr/bin/python3.5
"""

Module containing a function to perform lazy matrix multiplication using NumPy.

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Perform matrix multiplication using NumPy.

    Args:
        m_a: First matrix
        m_b: Second matrix

    Returns:
        Result of the multiplication

    Raises:
        TypeError: If m_a or m_b is not a valid matrix

    """

    return (np.matmul(m_a, m_b))

