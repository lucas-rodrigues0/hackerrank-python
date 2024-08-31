#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m, w, p, n):
    if n <= p: return math.ceil(n / (m * w))

    curr = candy = 0
    ans = float('inf')

    while candy < n:
        if candy < p:
            i = math.ceil((p - candy) / (m * w))
            curr += i
            candy += m * w * i
            continue

        buy,candy = divmod(candy , p)
        total = m + w + buy
        half = total // 2

        if m > w :
            m = max(m, half)
            w = total - m
        else:
            w = max(w, half)
            m = total - w

        curr += 1
        candy += m * w
        ans = min(ans, curr + math.ceil((n - candy) / (m * w)))

    return min(ans, curr)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

