# Hacker Rank Captains room exercice
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

N = input()
ROOM_LIST = input().split()

counter = dict(Counter(ROOM_LIST))

result = min(zip(counter.values(), counter.keys()))[1]
print(result)
