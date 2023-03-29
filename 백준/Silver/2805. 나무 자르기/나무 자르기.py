def check(mid):
    c = 0
    for i in d:
        if i > mid:
            c += i-mid
    return c >= m

def bs(lo, hi):
    if lo+1 >= hi:
        return lo
    mid = lo+hi >> 1
    if check(mid):
        return bs(mid, hi)
    else:
        return bs(lo, mid)

n, m = map(int, input().split())
d = list(map(int, input().split()))

print(bs(0, max(d)))