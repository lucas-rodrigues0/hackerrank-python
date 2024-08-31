#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    order_prices = sorted(prices)
    num_toys = 0
    money = k
    for toy in order_prices:
        if toy < money:
            money -= toy
            num_toys += 1
        else:
            break
    return num_toys

if __name__ == '__main__':


    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)


