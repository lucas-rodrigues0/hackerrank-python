#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    prev_ai = [0 for i in range(len(s1) + 1)]
    for ai in range(len(s1)):
        new_ai = [0]
        for bi in range(len(s2)):
            if s1[ai] == s2[bi]:
                new_ai.append(prev_ai[bi] + 1)
            else:
                new_ai.append(max(new_ai[-1], prev_ai[bi + 1]))
        prev_ai = new_ai
    
    return new_ai[len(s1)]

if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)


