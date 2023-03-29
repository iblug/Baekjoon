def bs(lo, hi, target, arr):
    if lo+1 >= hi:
        if abs(arr[lo]-target) < abs(arr[hi]-target):
            return lo
        else:
            return hi
    mid = lo + hi >> 1
    if arr[mid] > target:
        return bs(lo, mid, target, arr)
    elif arr[mid] < target:
        return bs(mid, hi, target, arr)
    else:
        return mid

n = int(input())
a = sorted(map(int, input().split()))

aa, bb = a[0], a[1]
for i in range(n-1):
    ii = -a[i]
    t = bs(i+1,n-1, ii, a)
    if abs(aa+bb) > abs(a[i]+a[t]):
        aa = a[i]
        bb = a[t]

print(aa, bb)
