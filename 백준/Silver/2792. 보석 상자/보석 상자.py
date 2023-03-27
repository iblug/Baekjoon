import sys
input = sys.stdin.readline

def Check(mid):
    r = 0
    for i in d:
        if i % mid:
            r += i // mid + 1
        else:
            r += i // mid
    return r <= n

def f(s, e):
    mid = s + e >> 1
    if s+1 >= e:
        return e
    if Check(mid):
        return f(s, mid)
    else:
        return f(mid, e)

n, m = map(int, input().split())
d = [int(input()) for _ in range(m)]

print(f(0, max(d)))