# Hacker Rank Grid challenge exercice
# https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    sorted_grid = []
    rows = len(grid)
    cols = len(grid[0])
    
    for s in grid:
        sorted_grid.append(sorted(s))
    
    def check_sorted(s: list):
        aux_s = s[:]
        s.sort()
        return s == aux_s

    result = 'YES'
    for row in range(cols):
        c = []
        for col in range(rows):
            c.append(sorted_grid[col][row])
        if not check_sorted(c):
            result = 'NO'

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
