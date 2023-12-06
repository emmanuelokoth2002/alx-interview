#!/usr/bin/python3

def is_prime(n):
    """
    This function checks for prime numbers.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_winner(x, nums):
    """
    it then determines the winner of the game.
    """
    maria_wins = 0
    ben_wins = 0
    for _ in range(x):
        n = nums.pop()
        while n > 1:
            for num in nums:
                if is_prime(num) and n % num == 0:
                    n //= num
                    break
            else:
                break
        if n == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
