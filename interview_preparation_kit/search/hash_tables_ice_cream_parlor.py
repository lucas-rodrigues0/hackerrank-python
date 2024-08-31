#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    result = []
    checked = {}
    
    for i in range(len(cost)):
        y = money - cost[i]
        if y not in checked:
            checked[cost[i]] = i
        else:
            result = [checked[y] + 1, i + 1]

    print(f"{min(result)} {max(result)}")
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
