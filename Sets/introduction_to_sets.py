# Hacker Rank Introduction to sets exercice
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # your code goes here
    distinct_heights = set(array)
    total_heights = len(distinct_heights)
    
    return round((sum(distinct_heights) / total_heights), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
