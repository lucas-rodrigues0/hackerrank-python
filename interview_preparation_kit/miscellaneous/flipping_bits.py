#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def convert_bit(b):
    inverted = ""
    for i in b:
        if i == '1':
            inverted += '0'
        else:
            inverted += '1'
    return inverted

def flippingBits(n):
    bit32 = "{:032b}".format(n)
    inv_bit32 = convert_bit(bit32)
    return int(inv_bit32, 2)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
