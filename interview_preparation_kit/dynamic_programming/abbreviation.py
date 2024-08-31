#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    n = len(a)
    m = len(b)
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]:
                if j < m and a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = True
                if a[i].islower():
                    dp[i + 1][j] = True
                    
    return 'YES' if dp[n][m] else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
