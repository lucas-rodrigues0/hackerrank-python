# Hacker Rank Plus minus exercice
# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positives = 0
    negatives = 0
    zeros = 0
    len_arr = len(arr)
    
    for i in arr:
        if i > 0:
            positives += 1
        if i < 0:
            negatives += 1
        if i == 0:
            zeros += 1
    
    r_positives = positives/len_arr
    r_negatives = negatives/len_arr
    r_zeros = zeros/len_arr
    
    print(round(r_positives, 6))
    print(round(r_negatives, 6))
    print(round(r_zeros, 6))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
