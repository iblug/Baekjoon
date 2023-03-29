def bs(lo, hi):
    if lo+1 >= hi:
        if abs(a[lo]+a[i]) <= abs(a[hi]+a[i]):
            return lo
        else:
            return hi
    mid = lo + hi >> 1
    if a[mid] > -a[i]:
        return bs(lo, mid)
    elif a[mid] < -a[i]:
        return bs(mid, hi)
    else:
        return mid

n = int(input())
a = sorted(map(int, input().split()))
r = []
for i in range(n-1):
    t = bs(i+1,n-1)
    r.append((a[i], a[t], abs(a[i]+a[t])))

result = min(r, key=lambda x:x[2])
print(result[0], result[1])