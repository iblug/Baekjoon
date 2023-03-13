import sys
input = sys.stdin.readline

n, c, w = map(int, input().split())
t = {}
for _ in range(n):
    a = int(input())
    t[a] = t.get(a, 0) + 1
max_ = max(t.keys())

r = 0
for i in range(1, max_+1):
    co = 0
    for tt in t:
        if tt%i == 0:
            p = (tt//i-1)*c
        else:
            p = (tt//i)*c
        if (tt//i)*i*w < p:
            continue
        co += ((tt//i)*i*w-p)*t[tt]
    if r <= co:
        r = co

print(r)