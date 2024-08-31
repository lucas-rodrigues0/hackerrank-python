#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    prefix_sum = 0
    max_modulo_sum = 0
    prefix_sums = []

    for num in a:
        # Update the prefix sum modulo m
        prefix_sum = (prefix_sum + num) % m

        # Update max_modulo_sum with the current prefix_sum
        max_modulo_sum = max(max_modulo_sum, prefix_sum)

        # Binary search to find the smallest prefix sum greater than the current prefix_sum
        lo, hi = 0, len(prefix_sums)
        while lo < hi:
            mid = (lo + hi) // 2
            if prefix_sums[mid] > prefix_sum:
                hi = mid
            else:
                lo = mid + 1

        if lo < len(prefix_sums):
            # There exists a prefix sum greater than the current one
            max_modulo_sum = max(max_modulo_sum, prefix_sum - prefix_sums[lo] + m)

        # Insert the current prefix_sum into the sorted list
        prefix_sums.insert(lo, prefix_sum)

    return max_modulo_sum

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

