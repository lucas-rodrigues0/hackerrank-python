# Hacker Rank Nested lists exercice
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    std_list = []
    scores = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        std_list.append((name, score))
        scores.add(score)
    
    second_min_score = sorted(scores)[1]
    sorted_students = sorted(std_list)
    
    for std, sco in sorted_students:
        if sco == second_min_score:
            print(std)
