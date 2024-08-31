#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    q = itertools.chain.from_iterable([(a, k), (b, -k)] for a, b, k in queries)
    return max(itertools.accumulate(c for _, c in sorted(q, key=lambda x: (x[0], -x[1]))))


if __name__ == '__main__':


    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)


