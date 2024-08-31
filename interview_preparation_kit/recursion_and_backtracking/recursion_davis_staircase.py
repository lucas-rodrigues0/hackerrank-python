#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

dict = {0: 0, 1: 1, 2: 2, 3: 4}
def stepPerms(n):
    if n in dict.keys():
        return dict.get(n)
    result = stepPerms(n-3) + stepPerms(n-2) + stepPerms(n-1)
    dict.update({n: result})
    return dict.get(n)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

    #     fptr.write(str(res) + '\n')

    # fptr.close()
