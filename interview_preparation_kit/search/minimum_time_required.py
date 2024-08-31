#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    # make a modest guess of what the days may be, and use it as a starting point
    efficiency = [1.0/x for x in machines]
    lower_bound = int(goal / sum(efficiency)) - 1
    upper_bound = lower_bound + max(machines) + 1
    
    while lower_bound < upper_bound -1:
        days = (lower_bound + upper_bound)//2
        produce = sum([days//x for x in machines])
        if produce >= goal:
            upper_bound = days
        elif produce < goal:
            lower_bound = days
        
    return upper_bound

if __name__ == '__main__':

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

