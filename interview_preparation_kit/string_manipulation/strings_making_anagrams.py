#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    
    total_deletion = (counter_a - counter_b) + (counter_b - counter_a)
    return total_deletion.total()
    
    
    
if __name__ == '__main__':


    a = input()

    b = input()

    res = makeAnagram(a, b)

