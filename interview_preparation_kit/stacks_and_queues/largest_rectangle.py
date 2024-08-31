#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    stack_idx = []
    max_area = 0
    idx = 0

    while idx < len(h):
        if not stack_idx or h[idx] >= h[stack_idx[-1]]:
            stack_idx.append(idx)
            idx += 1
        else:
            top = stack_idx.pop()
            width = idx if not stack_idx else idx - stack_idx[-1] - 1
            max_area = max(max_area, h[top] * width)

    while stack_idx:
        top = stack_idx.pop()
        width = idx if not stack_idx else len(h) - stack_idx[-1] - 1
        max_area = max(max_area, h[top] * width)
    
    return max_area

if __name__ == '__main__':

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

