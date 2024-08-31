#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    i = 0
    jumps = 0
    
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
            jumps += 1
        elif  i + 1 < len(c) and c[i + 1] == 0:
            i += 1
            jumps += 1

            
    return jumps


if __name__ == '__main__':

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)


