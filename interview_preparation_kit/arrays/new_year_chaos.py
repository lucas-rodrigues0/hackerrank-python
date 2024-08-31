#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes = 0
    p1 = 1
    p2 = 2
    p3 = 3
    
    for i in range(len(q)):
        if q[i] == p1:
            p1 = p2
            p2 = p3
            p3 += 1
        elif q[i] == p2:
            bribes += 1
            p2 = p3
            p3 += 1
        elif q[i] == p3:
            bribes += 2
            p3 += 1
        else:
            print('Too chaotic')
            return
    
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
