import sys
input = sys.stdin.readline

def bi_l(v:list, t:int) -> int:
    s = -1
    e = len(v)
    while (s+1 < e):
        mid = (s+e)//2
        if v[mid] >= t:
            e = mid
        else:
            s = mid
    return e

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
a = sorted(data)
dp_a = [a[0][1]]
for i in range(1, n):
    if dp_a[-1] < a[i][1]:
        dp_a.append(a[i][1])
    else:
        dp_a[bi_l(dp_a, a[i][1])] = a[i][1]
print(n-len(dp_a))
