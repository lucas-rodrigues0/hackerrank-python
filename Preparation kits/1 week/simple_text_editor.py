# Hacker Rank Simple text editor exercice
# https://www.hackerrank.com/challenges/one-week-preparation-kit-simple-text-editor/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
s= ''
prev_s = []

for _ in range(int(input())):
    cmd = input().split()
    
    if cmd[0] == '1':
        prev_s.append(s)
        s += cmd[1]
        
    if cmd[0] == '2':
        prev_s.append(s)
        idx = -abs(int(cmd[1]))
        s = s[:idx]
        
    if cmd[0] == '3':
        print(s[int(cmd[1]) - 1])
        
    if cmd[0] == '4':
        s = prev_s[-1]
        prev_s.pop()
