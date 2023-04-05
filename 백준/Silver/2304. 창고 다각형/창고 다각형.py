import sys
input = sys.stdin.readline

n = int(input())
g = [0]*1001
max_ = 0
b = []
for _ in range(n):
    l, h = map(int, input().split())
    if h > max_:
        max_ = h
        a = []
    if h == max_:
        a.append(l)
    g[l] = h
    b.append(l)

a_ma = max(a)
a_mi = min(a)
b_ma = max(b)
b_mi = min(b)

c = 0
d = 0
for i in range(b_mi, a_mi):
    if g[i] > d:
        d = g[i]
    c += d
d = 0
for i in range(b_ma, a_ma, -1):
    if g[i] > d:
        d = g[i]
    c += d
c += (a_ma - a_mi + 1)*max_

print(c)