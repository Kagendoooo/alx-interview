#!/usr/bin/python3
"""
Function returns list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Returns list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        List[List[int]]: Pascal's triangle.
    """
    if n <= 0:
        return []
    tri = []
    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = tri[i - 1][j - 1] + tri[i - 1][j]

        tri.append(row)
    return tri
