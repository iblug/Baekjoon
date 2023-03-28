def bs(lo, hi):
    if lo > hi:
        return False
    mid = lo + hi >> 1

    if B[mid] < i:
        return bs(mid+1, hi)
    elif B[mid] > i:
        return bs(lo, mid-1)
    else:
        return True

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))
result = []

for i in A:
    if not bs(0, b-1):
        result.append(i)
print(len(result), ' '.join(map(str, sorted(result))), sep='\n')