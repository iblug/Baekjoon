import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    k = int(input())
    d[k] = d.get(k, 0) + 1
r = sorted(d.items(), key=lambda x: x[1])
print(r[-1][1])