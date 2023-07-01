import sys
sys.setrecursionlimit(10**6)

def f(a, b):
    if a == 0:
        return b
    return f(b%a, a)

a, b = map(int, input().split())

print(a*b//f(a, b))