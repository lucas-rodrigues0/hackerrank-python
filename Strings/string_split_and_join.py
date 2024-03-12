# Hacker Rank String split and join exercice
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
    string_list = line.split(' ')
    return "-".join(string_list)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
