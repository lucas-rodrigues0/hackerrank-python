#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valleys = 0
    prev_level = 0
    curr_level = 0
    
    for idx in range(steps):
        prev_level = curr_level
        if path[idx] == 'U':
            curr_level += 1
        else:
            curr_level -= 1
        
        if curr_level == 0 and prev_level == -1:
            valleys += 1
    
    return valleys

if __name__ == '__main__':


    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)


