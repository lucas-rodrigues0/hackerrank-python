# Hacker Rank Diagonal difference exercice
# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    right_d = []
    left_d = []
    reverse_arr = arr[::-1]
    for i in range(n):
        right_d.append(arr[i][i])
        left_d.append(reverse_arr[i][i])
    
    right_sum = sum(right_d)
    left_sum = sum(left_d)
    
    return abs(right_sum - left_sum)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
