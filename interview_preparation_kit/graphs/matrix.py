#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY roads
#  2. INTEGER_ARRAY machines
#
class Item(object):
    def __init__(self, value, has_machine=False):
        self.value = value
        self.parent = self
        self.has_machine = has_machine
        self.rank = 0

class DisjointSets(object):
    def __init__(self):
        self.items_by_value = {}
    
    def new_set(self, x, has_machine=False):
        x_item = Item(x, has_machine)
        self.items_by_value[x] = x_item
        return x_item
    
    def union(self, x_item, y_item):
        x_root = self.find(x_item)
        y_root = self.find(y_item)
        has_machine = x_root.has_machine or y_root.has_machine
        if x_root.rank == y_root.rank:
            rank = x_root.rank + 1
            x_root.parent = y_root
            y_root.rank = rank
            y_root.has_machine = has_machine
        elif x_root.rank > y_root.rank:
            y_root.parent = x_root
            x_root.has_machine = has_machine
        else:
            x_root.parent = y_root
            y_root.has_machine = has_machine

    def find(self, x_item):
        if x_item.parent == x_item:
            return x_item
        else:
            # Path compression
            x_item.parent = self.find(x_item.parent)
            return x_item.parent

    def find_by_value(self, x):
        x_item = self.items_by_value.get(x)
        if x_item:
            return self.find(x_item)
        return None
        
    
# Complete the minTime function below.
def minTime(roads, machines):
    sorted_roads = sorted(roads, key=lambda x: x[2], reverse=True)
    machines_set = set(machines)
    cost = 0
    dsets = DisjointSets()
    for city_a, city_b, road_cost in sorted_roads:
        # print("Looking at %s and %s (cost: %s)" % (city_a, city_b, road_cost))
        a_has_machine = city_a in machines_set
        b_has_machine = city_b in machines_set
        a_root = dsets.find_by_value(city_a)
        b_root = dsets.find_by_value(city_b)
        
        if a_root is None:
            # print("  Adding %s to the sets" % city_a)
            a_root = dsets.new_set(city_a, a_has_machine)
        if b_root is None:
            # print("  Adding %s to the sets" % city_b)
            b_root = dsets.new_set(city_b, b_has_machine)
        
        if a_root.value == b_root.value:
            # already joined
            # print("  cities already joined")
            continue
        if a_root.has_machine and b_root.has_machine:
            # print("  cannot join the cities")
            # cannot join
            cost += road_cost
        else:
            dsets.union(a_root, b_root)
       
    return cost


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input().strip())
        machines.append(machines_item)

    result = minTime(roads, machines)


