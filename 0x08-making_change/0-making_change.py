#!/usr/bin/python3
"""
Make change from coins
"""


def makeChange(coins, total):
    """Fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count += total // coin
            total %= coin
    return count if total == 0 else -1
