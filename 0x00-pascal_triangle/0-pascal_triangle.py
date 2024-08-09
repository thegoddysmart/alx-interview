#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(num_rows):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """

    if num_rows <= 0:
        return []
    triangle = [[] for _ in range(num_rows)]
    for row_index in range(num_rows):
        for col in range(row_index+1):
            if col < row_index:
                if col == 0:
                    triangle[row_index].append(1)
                else:
                    triangle[row_index].append(
                        triangle[row_index-1][col] + triangle[row_index-1][col-1])
            elif col == row_index:
                triangle[row_index].append(1)

    return triangle
