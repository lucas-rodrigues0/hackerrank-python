# Hacker Rank sWAP cASE exercice
# https://www.hackerrank.com/challenges/swap-case/problem

#Alternative solution: return s.swapcase()

def swap_case(s):
    """Swaps characters upper/lower cases"""
    swaped_string = ''
    for char in s:
        if char.isupper():
            swaped_string += char.lower()
        elif char.islower():
            swaped_string += char.upper()
        else:
            swaped_string += char
    return swaped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
