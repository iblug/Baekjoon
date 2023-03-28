m, n = map(int, input().split())
l = list(map(int, input().split()))

def check(mid):
    c = 0
    for i in l:
        c += i//mid
    return c >= m

def bs(lo, hi):
    if lo + 1 >= hi:
        return lo
    mid = lo + hi >> 1
    if check(mid):
        return bs(mid, hi)
    else:
        return bs(lo, mid)

print(bs(0, int(1e9)))