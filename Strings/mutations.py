# Hacker Rank Mutations exercice
# https://www.hackerrank.com/challenges/python-mutations/problem

# Alternative solution: return string[:position] + character + string[position + 1:]

def mutate_string(string, position, character):
    aux_list = list(string)
    aux_list[position] = character
    return ''.join(aux_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
