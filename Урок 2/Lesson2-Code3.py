import sys

sys.setrecursionlimit(3000)

def akk(m, n):
    if m == n:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))

print(akk(3, 4))