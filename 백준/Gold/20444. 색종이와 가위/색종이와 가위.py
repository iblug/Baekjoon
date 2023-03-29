def f(start, end):
    if start > end:
        return 'NO'
    mid = start + end >> 1
    if (mid+1)*(n-mid+1) < k:
        return f(mid+1, end)
    elif (mid+1)*(n-mid+1) > k:
        return f(start, mid-1)
    else:
        return 'YES'

n, k = map(int, input().split())

print(f(0, n//2+1))