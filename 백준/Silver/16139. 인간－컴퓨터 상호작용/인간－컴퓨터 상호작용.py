import sys
input = sys.stdin.readline

from collections import defaultdict

s = input().rstrip()
q = int(input())

d = defaultdict(lambda: [0]*len(s))

for i, e in enumerate(s):
    for j in range(i, len(s)):
        d[e][j] += 1
for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    if l > 0:
        print(d[a][r] - d[a][l-1])
    else:
        print(d[a][r])