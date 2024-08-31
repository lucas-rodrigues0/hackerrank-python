def fibonacci(n):
    ini_val = [0, 1]
    if n in ini_val:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

n = int(input())
print(fibonacci(n))