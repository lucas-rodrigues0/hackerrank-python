# Hacker Rank Set.add() exercice
# https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

distinct_countries = set()

for _ in range(int(input())):
    country = input()
    distinct_countries.add(country)
    
print(len(distinct_countries))
