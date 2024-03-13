# Hacker Rank Set mutation exercice
# https://www.hackerrank.com/challenges/py-set-mutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

len_A = int(input())
set_A = set(map(int, input().split()))

for _ in range(int(input())):
    op = input().split()
    set_B = set(map(int, input().split()))
    
    if op[0] == 'update':
        set_A.update(set_B)
    if op[0] == 'intersection_update':
        set_A.intersection_update(set_B)
    if op[0] == 'difference_update':
        set_A.difference_update(set_B)
    if op[0] == 'symmetric_difference_update':
        set_A.symmetric_difference_update(set_B)
        
print(sum(set_A))
