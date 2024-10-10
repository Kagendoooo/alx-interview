#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Args:
        boxes ([int]): list of lists of integers.

    Returns: True if unlocked otherwise False
    """

    n = len(boxes)
    unlocked = set([0])
    keys = boxes[0]

    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == n
