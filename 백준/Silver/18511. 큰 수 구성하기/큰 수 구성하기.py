import sys
input = sys.stdin.readline

from itertools import product

n, m = map(int, input().split())
l = len(str(n))
k = list(input().split())
ans = 0
kk = product(k,repeat=l)
for i in kk:
    num = int(''.join(i))
    if n >= num:
        ans = max(ans, num)
if ans == 0:
    kk = product(k,repeat=l-1)
    for i in kk:
        num = int(''.join(i))
        if n >= num:
            ans = max(ans, num)
print(ans)