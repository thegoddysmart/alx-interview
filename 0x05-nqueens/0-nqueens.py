#!/usr/bin/python3
"""
N QUEENS ALGORITHM WITH BACKTRACKING
"""
import sys


class NQueen:
    """
    This class solves N Queen Problem
    """

    def __init__(self, n):
        """
        Initialize global variables
        """
        self.n = n
        self.x = [0 for i in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """
        Check if k-th Queen can be placed in the i-th column.

        Args:
            k: The row of the queen to place.
            i: The column of the queen.

        Returns:
            bool: True if the queen can be placed, otherwise False.
        """

        for j in range(1, k):
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def nQueen(self, k):
        """ Try to place queens on the board recursively.

        Args:
            k: The current queen to place (should start from 1).
        """
        for i in range(1, self.n + 1):
            if self.place(k, i):
                # Place the queen
                self.x[k] = i
                if k == self.n:
                    # Placed all 4 Queens, store the solution
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.res.append(solution)
                else:
                    # Place the next queen
                    self.nQueen(k + 1)
        return self.res


# Main execution

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
res = queen.nQueen(1)

for i in res:
    print(i)