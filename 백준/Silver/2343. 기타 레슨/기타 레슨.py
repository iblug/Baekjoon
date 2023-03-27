def check(mid):
    cnt = 1
    t = 0
    for i in c:
        if t + i > mid:
            cnt += 1
            t = 0
        if i > mid:
            return False
        t += i
    return cnt <= m

def f(s, e):
    if s+1 >= e:
        return e
    mid = s+e >> 1
    if check(mid):
        return f(s, mid)
    else:
        return f(mid, e)

n, m = map(int, input().split())
c = list(map(int, input().split()))

print(f(0, max(c)*n))