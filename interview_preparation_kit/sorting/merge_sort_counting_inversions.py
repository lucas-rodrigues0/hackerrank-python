#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    n = len(arr)
    if n == 1:
        return 0
        
    n1 = n // 2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    ans = countInversions(arr1) + countInversions(arr2)
    
    i1, i2 = 0, 0
    for i in range(n):
        if i1 < n1 and (i2 >= n2 or arr1[i1] <= arr2[i2]):
            arr[i] = arr1[i1]
            ans += i2
            i1 += 1
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    return ans

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

