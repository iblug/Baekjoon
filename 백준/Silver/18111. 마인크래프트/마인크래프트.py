import sys
from collections import Counter
input = sys.stdin.readline

n, m, b = map(int, input().split())
data = []
for _ in range(n):
    data.extend(list(map(int,input().split())))
data = Counter(data)
h = 0
t = 0

ans_t = 1e9
ans_h = 0
while h <= 256:
    c1 = c2 = 0
    for k, v in data.items():
        if k < h:
            c1 += (h-k) * v
        elif k > h:
            c2 += (k-h) * v
    if (b - c1 + c2) < 0:
        break
    t = c1 + 2*c2
    if t <= ans_t:
        ans_t = t
        ans_h = h
        h += 1
    else:
        break
print(ans_t, ans_h)
