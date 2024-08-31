#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def maxRegion(grid):
    def connected(matrix, i, j):
        if not (0 <= i < len(matrix)) or not (0 <= j < len(matrix[0])):
            return 0  # 1
    
        if matrix[i][j] != 1:
            return 0  # 2
    
        result = 1  # 3
        matrix[i][j] = 0  # 4
    
        for ii in range(i-1, i+2):
            for jj in range(j-1, j+2):
                if i != ii or j != jj:
                    result += connected(matrix, ii, jj)  # 5
    
        return result
    
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            result = max(result, connected(grid, i, j))  # 1
    return result

if __name__ == '__main__':

    n = 5

    m = 5

    grid = [
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0],
    ]

    # for _ in range(n):
    #     grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)
    print(res)


