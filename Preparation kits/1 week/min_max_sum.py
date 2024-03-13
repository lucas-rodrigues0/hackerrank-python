# Hacker Rank Min max sum exercice
# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sorted_array = sorted(arr)
    maximum_sum = sum(sorted_array[1:])
    minimum_sum = sum(sorted_array[:-1])
    print(f"{minimum_sum} {maximum_sum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
