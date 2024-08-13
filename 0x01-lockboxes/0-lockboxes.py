#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked starting from box 0.
    :param boxes: List of lists where each sublist contains keys to other boxes
    :return: Treu if all boxes can be opened, otherwise False
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0]

    while keys:
        key = keys.pop()
        if key < n and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])

    return all(opened)
