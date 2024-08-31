#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    total = 0
    # List of flower cost in desc order
    c = sorted(c, reverse=True)

    for i in range(len(c)):
        purchase = i//k
        flower_cost = c[i]
        cost = (purchase + 1) * flower_cost
        total += cost

    return total

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

