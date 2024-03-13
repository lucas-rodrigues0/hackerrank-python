# Hacker Rank No idea exercice
# https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

def happiness_count(arr, like, dislike):
    happiness = 0
    
    for i in arr:
        if i in like:
            happiness += 1
        if i in dislike:
            happiness -= 1
    
    return happiness
    
len_arr, len_sets = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
like = set(map(int, input().split()))
dislike = set(map(int, input().split()))

result = happiness_count(arr, like, dislike)
print(result)
