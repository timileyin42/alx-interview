#!/usr/bin/python3
"""
Determines the fewest num of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Calculates the minimum num of coins needed to make change for a given total
    Returns:
    The minimum num of coins needed to make change, or -1 if it is not possible
    """
    if total <= 0:
        return 0

    remaining = total
    coins_count = 0
    coin_num = 0
    sorted_coins = sorted(coins, reverse=True)
    u = len(coins)

    while remaining > 0:
        if coin_num >= u:
            return -1
        if remaining - sorted_coins[coin_num] >= 0:
            remaining -= sorted_coins[coin_num]
            coins_count += 1
        else:
            coin_num += 1
    return coins_count
