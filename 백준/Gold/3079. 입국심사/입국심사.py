import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline

def check(mid):
    c = 0
    for i in t:
        c += mid//i
    return c >= m

def f(s, e):
    if s+1 >= e:
        return e
    mid = s+e >> 1
    if check(mid):
        return f(s, mid)
    else:
        return f(mid, e)

n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]
print(f(0, max(t)*m))