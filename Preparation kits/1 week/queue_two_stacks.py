# Hacker Rank Queue using two stacks exercice
# https://www.hackerrank.com/challenges/one-week-preparation-kit-queue-using-two-stacks/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

q = []

for _ in range(int(input())):
    cmd = list(input().split())
    
    if cmd[0] == '1':
        q.append(cmd[1])
    if cmd[0] == '2':
        q.pop(0)
    if cmd[0] == '3':
        print(q[0])
