# Hacker Rank Designer door mat exercice
# https://www.hackerrank.com/challenges/designer-door-mat/problem
# Got from https://github.com/nathan-abela/HackerRank-Solutions/blob/master/Python/03%20-%20Strings/09%20-%20Designer%20Door%20Mat.py

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())

for i in range(int(N/2)):
    string = ".|." * (2 * i + 1)
    x = string.center(M, '-')
    print(x)

print("WELCOME".center(M, '-'))

for i in reversed(range(int(N/2))):
    string = ".|." * (2 * i + 1)
    x = string.center(M, '-')
    print(x)
