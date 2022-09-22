#!/usr/bin/python3
"""
Change comes from within
"""

"""from typing import List"""


def makeChange(coins, total):
    """ determines the fewest amont of coins needed
    """
    if total < 1:
        return 0
    """ sort coins from greatest to least """
    coins.sort(reverse=True)
    count = 0
    for key in range(len(coins)):
        number = total // coins[key]
        count += number
        total -= number * coins[key]
    if total is 0:
        return count
    else:
        return -1       
