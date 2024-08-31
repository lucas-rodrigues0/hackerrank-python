#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    maxes = [0] * len(arr)

    maxes[0] = max(arr[0], 0)
    maxes[1] = max(arr[0], arr[1], 0)
    
    for i in range(2, len(arr)):
        maxes[i] = max(arr[i], maxes[i - 1], maxes[i - 2] + arr[i], 0)

    return maxes[-1]
    
    

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)


