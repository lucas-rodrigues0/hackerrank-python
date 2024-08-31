#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    a = Counter(s1)
    b = Counter(s2)
    if a - b == a:
        return 'NO'
    return 'YES'

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)


