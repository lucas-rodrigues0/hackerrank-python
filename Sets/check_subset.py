# Hacker Rank Check subset exercice
# https://www.hackerrank.com/challenges/py-check-subset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    len_set_a = int(input())
    set_a = set(map(int, input().split()))
    len_set_b = int(input())
    set_b = set(map(int, input().split()))
    
    print(set_a.issubset(set_b))
