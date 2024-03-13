# Hacker Rank Set discard remove & pop exercice
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Had to reverse the order from insertion on the set so the pop function would get the right values to remove

n = int(input())
l_input = input().split()
s = set()

for i in reversed(l_input):
    s.add(int(i))

for i in range(int(input())):
    s1 = input().split()
    if s1[0] == 'pop':
        s.pop()
    elif s1[0] == 'remove':
        s.discard(int(s1[1]))
    elif s1[0] == 'discard':
        s.discard(int(s1[1]))

print(sum(s))
