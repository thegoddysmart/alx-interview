#!/usr/bin/python3
"""
    Determines the fewest number of coins needed to meet
    a given amount total.

    Args:
        coins (list): A list of the values of the coins
        in your possession.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet
        the total.
            Returns -1 if the total cannot be met with
            the given coins.
    """


def makeChange(coins, total):
    """Classic Bottom-Up dynamic programming"""
    temp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp_value += total // coin
            total = total % coin

    return temp_value if total == 0 else -1


# Example usage
if __name__ == '__main__':

    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
