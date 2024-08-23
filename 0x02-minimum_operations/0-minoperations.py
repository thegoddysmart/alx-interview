#!/usr/bin/python3

""" Minimum Operations Module """


def minOperations(n):
    """
    Calculate the minimum number of operations needed to get exactly `n`
    characters in a text file starting from a single character using
    only "Copy All" and "Paste" operations.

    Args:
        n (int): The number of characters to achieve.

    Returns:
        int: The minimum number of operations required to reach `n` characters.
             Returns 0 if `n` is less than or equal to 1 as no operations are needed.
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2

    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1

    return operations