# Hacker Rank Intersection operation exercice
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
en_newspaper = input().split()
b = int(input())
fr_newspaper = input().split()

print(len(set(en_newspaper) & set(fr_newspaper)))
