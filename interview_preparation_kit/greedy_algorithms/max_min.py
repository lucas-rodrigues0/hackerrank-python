#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr = sorted(arr)
    result = arr[k-1] - arr[0]
    for i in range(len(arr)-k+1):
        if arr[i+k-1] - arr[i] < result:
            result = arr[i+k-1] - arr[i]
    return result
    
if __name__ == '__main__':

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

