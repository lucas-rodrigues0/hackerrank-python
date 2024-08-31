#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    arr.sort()

    min_dif = abs(arr[0] - arr[1])

    for i in range(len(arr)-1):
        dif = abs(arr[i] - arr[i+1])
        if dif < min_dif:
            min_dif = dif
    return min_dif
        

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

