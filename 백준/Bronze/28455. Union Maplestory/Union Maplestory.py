import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
r = sorted(L, reverse=True)[:42]

c = 0
for e in r:
    if e >= 250:
        c += 5
    elif e >= 200:
        c += 4
    elif e >= 140:
        c += 3
    elif e >= 100:
        c += 2
    elif e >= 60:
        c += 1
print(sum(r), c)
