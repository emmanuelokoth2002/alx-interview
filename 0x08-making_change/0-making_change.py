#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins you have, return -1.
    """
    if total < 1:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
