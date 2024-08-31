#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    imp_contests = []
    unimp_contests = []
    for contest in contests:
        value = contest[0]
        importance = contest[1]
        if importance:
            imp_contests.append(value)
        else:
            unimp_contests.append(value)
    sort_imp_contests = sorted(imp_contests, reverse=True)
    for idx in range(len(sort_imp_contests)):
        if idx >= k:
            sort_imp_contests[idx] = -abs(sort_imp_contests[idx])
    
    return sum(sort_imp_contests + unimp_contests)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)


