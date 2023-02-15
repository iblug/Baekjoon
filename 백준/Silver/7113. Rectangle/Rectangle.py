import sys
sys.setrecursionlimit(10**6)

def cut(n, m, c):
    if n < m:
        return cut(n, m-n, c+1)
    elif n > m:
        return cut(n-m, m, c+1)
    else:
        return c+1

n, m = map(int, input().split())
print(cut(n, m, 0))