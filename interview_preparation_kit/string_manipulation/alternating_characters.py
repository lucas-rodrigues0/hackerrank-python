#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    curr_char = ''
    deletion = 0
    for c in s:
        if curr_char and curr_char == c:
            deletion += 1
        curr_char = c

    return deletion

if __name__ == '__main__':


    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

