#!/usr/bin/python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    ben_wins = 0
    maria_wins = 0

    for n in nums:
        prime_numbers = [i for i in range(2, n + 1) if is_prime(i)]
        prime_set = set(prime_numbers)
        
        moves = 0
        while prime_set:
            if moves % 2 == 0:
                selected = max(prime_set)
                prime_set -= set(range(selected, n + 1, selected))
                maria_wins += 1
            else:
                selected = max(prime_set)
                prime_set -= set(range(selected, n + 1, selected))
                ben_wins += 1
            moves += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
