#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):

    num_pairs = 0
    odd_socks = []
    print(n)
    print(ar)
    for sock in ar:
        print(num_pairs)
        print(odd_socks)
        if sock not in odd_socks:
            print('add sock')
            odd_socks.append(sock)
        
        if sock in odd_socks:
            print('remove sock')
            odd_socks.remove(sock)
            num_pairs += 1
            
    return num_pairs
    

if __name__ == '__main__':


    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

