# Hacker Rank Lists exercice
# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for _ in range(N):
        instruction = input().split()
        command = instruction[0]
        values = list(map(int, instruction[1:]))
        
        if command == 'insert':
            arr.insert(*values)
            
        if command == 'print':
            print(arr)
            
        if command == 'remove':
            arr.remove(*values)
            
        if command == 'append':
            arr.append(*values)
            
        if command == 'sort':
            arr.sort()
            
        if command == 'pop':
            arr.pop()
            
        if command == 'reverse':
            arr.reverse()
