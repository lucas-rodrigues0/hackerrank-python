#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    plants = p
    days = 0
    stack = []

    for plant in plants:
        days_to_die = 1
        
        # Check if the current plant has more pesticide than the plant on its left
        while stack and plant <= stack[-1][0]:
            _, prev_days_to_die = stack.pop()
            days_to_die = max(days_to_die, prev_days_to_die + 1)

        # If the stack is not empty, it means the current plant dies at some point
        if stack:
            days = max(days, days_to_die)
        else:
            days_to_die = 0

        stack.append((plant, days_to_die))

    return days

if __name__ == '__main__':

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

