#!/bin/python3

import math
import os
import random
import re
import sys

class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
            self.size[i] = 1
            return i
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unionBySize(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return
        isize = self.size[irep]
        jsize = self.size[jrep]

        if isize < jsize:
            self.parent[irep] = jrep
            self.size[jrep] += self.size[irep]
        else:
            self.parent[jrep] = irep
            self.size[irep] += self.size[jrep]


def maxCircle(queries):
    dset = DisjointSet()
    maxlen = 0
    maxlens = []
    for query in queries:
        f1, f2 = query
        dset.unionBySize(f1, f2)
        maxlen = max(maxlen, dset.size[dset.find(f1)])
        maxlens.append(maxlen)
    return maxlens

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
