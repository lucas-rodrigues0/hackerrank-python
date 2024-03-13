# Hacker Rank Symmetric difference exercice
# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

# Alternative solution: 
# Difference in each sets
# c = a.difference(b)
# d = b.difference(a)

# Union of difference
# e = c.union(d)

# Converting set to a list
# RESULT = list(e)

# Sorting
# RESULT.sort()

# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
M_SET = set(map(int, input().split()))
N = int(input())
N_SET = set(map(int, input().split()))

intersection = M_SET.intersection(N_SET)
union_set = M_SET.union(N_SET)
symmetric_diff = [i for i in union_set if i not in intersection]

symmetric_diff.sort()

for val in symmetric_diff:
    print(val)
