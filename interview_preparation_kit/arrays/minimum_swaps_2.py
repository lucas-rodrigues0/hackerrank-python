#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    visited = [False]*len(arr)
    for i in range(len(arr)):
        if not visited[i]:
            a = i
            b = arr[i] - 1
            l = 1
            visited[i] = True
            while b != i:
                visited[b] = True
                a = b
                b = arr[b] - 1
                l += 1
            swaps += l - 1
    return swaps

if __name__ == '__main__':


    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)


