# Hacker Rank String validators exercice
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
  
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))
