#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primality' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def primality(n):
    if n == 1:
        return 'Not prime'

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return 'Not prime'
    return 'Prime'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        result = primality(n)

    #     fptr.write(result + '\n')

    # fptr.close()
