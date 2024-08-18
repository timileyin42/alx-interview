#!/usr/bin/python3
"""Function to rotate a 2D matrix 90 degrees clockwise in place"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.
    Args:
        matrix (list of list of int): The n x n 2D matrix to rotate.
    Do not return anything. The matrix is modified in place.
    """
    n = len(matrix)

    for u in range(n):
        for v in range(u, n):
            matrix[u][v], matrix[v][u] = matrix[v][u], matrix[u][v]

    for u in range(n):
        matrix[u].reverse()
