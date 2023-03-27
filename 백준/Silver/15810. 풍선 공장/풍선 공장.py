def check(mid):
    c = 0
    for i in a:
        c += mid//i
    return c >= m

def f(start, end):
    if start + 1 >= end:
        return end
    mid = start + end >> 1
    if check(mid):
        return f(start, mid)
    else:
        return f(mid, end)

n, m = map(int, input().split())
a = list(map(int, input().split()))

print(f(0, max(a)*m))