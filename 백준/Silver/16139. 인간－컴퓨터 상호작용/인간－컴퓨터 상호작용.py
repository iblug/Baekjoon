import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())

d = {}

for i, e in enumerate(s):
    if e not in d:
        d[e] = [0]*len(s)
    d[e][i] = 1

for v in d.values():
    for i in range(1, len(v)):
        v[i] += v[i-1]

for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    
    if a not in d:
        print(0)
        continue
        
    if l > 0:
        print(d[a][r] - d[a][l-1])
    else:
        print(d[a][r])