# Hacker Rank Balanced brackets exercice
# https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    char_list = []
    res_match = {'{':'}','(':')','[':']'}
    for i in range(len(s)):
        if s[i] in ['(','{','[']:
            char_list.append(s[i])
        else:
            if len(char_list) == 0:
                return 'NO'
            if res_match.get(char_list.pop()) != s[i]:
                return 'NO'

    if len(char_list)>0:
        return 'NO'

    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
