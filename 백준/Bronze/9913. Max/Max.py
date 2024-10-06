import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    k = int(input())
    d[k] = d.get(k, 0) + 1

print(max(d.values()))