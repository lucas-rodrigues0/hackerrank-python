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
from collections import deque

def isBalanced(s):
    dq = deque([])
    brackets = {'}': '{', ']': '[', ')': '('}

    for char in s:
        if char in brackets.values():
            dq.append(char)
        elif dq and char in brackets.keys():
            prev_char = dq.pop()
            if prev_char != brackets[char]:
                return 'NO'
        elif not dq and char in brackets.keys():
            return 'NO'

            
    return 'YES' if not dq else 'NO'
    

if __name__ == '__main__':

    # t = int(input().strip())

    # for t_itr in range(t):
    s = "([[]{}]"

    result = isBalanced(s)

    print(result)


# }][}}(}][))] NO

# [](){()} YES

# () YES

# ({}([][]))[]() YES

# {)[](}]}]}))}(())( NO

# ([[) NO

    

    

    

    

    

    