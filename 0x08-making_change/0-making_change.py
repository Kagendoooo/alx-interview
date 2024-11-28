#!/usr/bin/python3
"""
Make change from coins
"""


def makeChange(coins, total):
    """Fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    dloop = [float('inf')] * (total + 1)
    dloop[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dloop[i] = min(dloop[i], dloop[i - coin] + 1)
    return dloop[total] if dloop[total] != float('inf') else -1
