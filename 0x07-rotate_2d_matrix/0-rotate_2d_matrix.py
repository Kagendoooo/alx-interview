#!/usr/bin/python3
"""
Rotate a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the 2D matrix 90 degrees clockwise
    Matrix must be edited in place
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the rotation
    for i in range(n):
        matrix[i].reverse()
