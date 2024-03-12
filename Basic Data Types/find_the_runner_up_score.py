# Hacker Rank Find the Runner-up score exercice
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score_list = list(arr)
    
    score_list.sort()
    
    max_score = max(score_list)
    result = 0
    
    for index in range(len(score_list)-1,-1,-1):        
        if score_list[index] < max_score:
            result = score_list[index]
            break
            
    print(result)
