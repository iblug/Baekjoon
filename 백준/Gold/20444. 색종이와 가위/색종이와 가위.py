def check(mid):
    return (mid+1)*(n-mid+1) <= k

def f(start, end):
    if start+1 >= end:
        return start
    mid = start + end >> 1
    if check(mid):
        return f(mid, end)
    else:
        return f(start, mid)

n, k = map(int, input().split())

a = f(0, n//2+1)
if (a+1)*(n-a+1) == k:
    print('YES')
else:
    print('NO')