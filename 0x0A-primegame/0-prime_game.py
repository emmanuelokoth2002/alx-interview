#!/usr/bin/python3.4.3
"""
0-prime_game.py file
"""


def is_prime(n):
    """Check if a number is prime."""
    primes = []
    filtered = [True] * (x + 1)
    for p in range(2, x+1):
        if (filtered[p]):
            primes.append(p)
            for i in range(p, x+1, p):
                filtered[i] = False
    return primes


def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primes = primeNo(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
