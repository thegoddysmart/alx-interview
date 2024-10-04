#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix by 90 degrees clockwise in place.

    Args:
        matrix (list of list): The n x n matrix to rotate.
    """
    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
