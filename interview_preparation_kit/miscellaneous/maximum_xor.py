#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.
def maxXor(arr, queries):
    trie = dict()
    cur = trie
    #build a trie of numbers' bits prefixes
    for a in arr:
        for bit in map(int, bin(a)[2:].zfill(30)):
            if bit not in cur:
                cur[bit] = {}
            cur = cur[bit]
        cur = trie
    
    rez = []
    #given a trie of bits prefixes and a query, do a greedy search on it
    for q in queries:
        sub_rez = ''
        for bit in map(int, bin(q)[2:].zfill(30)):
            if 1 - bit in cur:
                sub_rez += '1'
                cur = cur[1 - bit]
            else:
                sub_rez += '0'
                cur = cur[bit]
        rez.append(int(sub_rez, 2))
        cur = trie
    return rez

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
