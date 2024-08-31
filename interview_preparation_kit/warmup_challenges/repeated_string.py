#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    total_full_str = n // len(s)
    reminder = n % len(s)
    count = 0

    for i in range(len(s)):
        if s[i] == 'a':
            count += 1

    count *= total_full_str
    
    for i in range(reminder):
        if s[i] == 'a':
            count += 1
            
    return count

if __name__ == '__main__':

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

