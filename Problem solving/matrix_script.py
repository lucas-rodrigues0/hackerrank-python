# Hacker Rank Matrix script exercice
# https://www.hackerrank.com/challenges/matrix-script/problem

#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
msg = ''

for _ in range(n):
    matrix_item = list(input())
    matrix.append(matrix_item)

for col in range(m):
    for row in range(n):
        msg += matrix[row][col]
            
msg = re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', " ", msg)
print(msg)
