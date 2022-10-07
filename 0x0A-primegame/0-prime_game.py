#!/usr/bin/python3.7
"""
prime game
"""


def isWinner(x, nums):
    """ checks for winner in a prime game
    """

    def is_prime(n):
        """ Checks if a number is prime
        """
        for i in range(2, int(n ** 0.5) + 1):
            if not n % i:
                return False
        return True

    def add_arr(n, primes):
        """ adds prime to a list
        """
        last_elem = primes[-1]
        if n > last_elem:
            for i in range(last_elem + 1, n + 1):
                if is_prime(i):
                    primes.append(i)
                else:
                    primes.append(0)

    score = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    add_arr(max(nums), primes)

    for round in range(x):
        _sum = sum((i != 0 and i <= nums[round])
                   for i in primes[:nums[round] + 1])
        if (_sum % 2):
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            score[winner] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"

    return None
