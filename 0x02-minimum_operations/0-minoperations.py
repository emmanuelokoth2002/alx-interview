#!/usr/bin/python3
"""
Calculate the minimum number of operations to obtain n 'H' characters
in a file.
"""


def minOperations(n):
    """
    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required.

    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
