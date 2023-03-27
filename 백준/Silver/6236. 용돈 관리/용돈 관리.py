import sys
input = sys.stdin.readline

def Check(mid):
    r = mid
    c = 1
    for i in d:
        if r < i:
            r = mid - i
            c += 1
        else:
            r -= i
    return c <= m

def f(s, e):
    if s + 1 >= e:
        return e
    mid = s + e >> 1
    if Check(mid):
        return(f(s, mid))
    else:
        return(f(mid, e))

n, m = map(int, input().split())
d = [int(input()) for _ in range(n)]

print(f(max(d)-1, int(1e9)))