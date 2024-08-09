#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers 
    representing the Pascal’s triangle of n:
    """

    if n <= 0:
        return []

    
    """Let's initialize an empty resulting array """
    triangle = [[] for idx in range(n)]

    for li in range(n):
        for col in range(li+1):
            if(col < li):
                if(col == 0):
                    """ the first column is always set to 1 """
                    triangle[li].append(1)
                else:
                    triangle[li].append(triangle[li-1][col] + triangle[li-1][col-1])
            elif(col == li):
                """ the diagonal is always set to 1 """
                triangle[li].append(1)

    return triangle
