# Hacker Rank Time conversion exercice
# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period = s[-2:]
    time_arr = s[:-2].split(':')
    result = ""
    if period == 'PM' and time_arr[0] == '12':
        result = ":".join(time_arr)
    if period == 'AM' and time_arr[0] == '12':
        time_arr[0] = '00'
        result = ":".join(time_arr)
    if period == 'PM' and time_arr[0] != '12':
        hour = int(time_arr[0])
        time_arr[0] = str(hour + 12).zfill(2)
        result = ":".join(time_arr)
    if period == 'AM' and time_arr[0] != '12':
        result = ":".join(time_arr)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
