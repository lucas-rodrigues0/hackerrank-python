# Hacker Rank Text alignment exercice
# https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true
# Got from https://github.com/nathan-abela/HackerRank-Solutions/blob/master/Python/03%20-%20Strings/07%20-%20Text%20Alignment.py

# Enter your code here. Read input from STDIN. Print output to STDOUT

THICKNESS = int(input()) #This must be an odd number
c = 'H'

# Top Cone
for i in range(THICKNESS):
    print((c*i).rjust(THICKNESS-1)+c+(c*i).ljust(THICKNESS-1))

# Top Pillars
for i in range(THICKNESS+1):
    print((c*THICKNESS).center(THICKNESS*2)+(c*THICKNESS).center(THICKNESS*6))

# Middle Belt
for i in range((THICKNESS+1)//2):
    print((c*THICKNESS*5).center(THICKNESS*6))    

# Bottom Pillars
for i in range(THICKNESS+1):
    print((c*THICKNESS).center(THICKNESS*2)+(c*THICKNESS).center(THICKNESS*6))    

# Bottom Cone
for i in range(THICKNESS):
    print(((c*(THICKNESS-i-1)).rjust(THICKNESS)+c+(c*(THICKNESS-i-1)).ljust(THICKNESS)).rjust(THICKNESS*6))
