# Hacker Rank Check strict superset exercice
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

set_a = set(map(int, input().split()))

result = True

for _ in range(int(input())):
    set_b = set(map(int, input().split()))
    if not set_a.issuperset(set_b):
        result = False
        
print(result)
