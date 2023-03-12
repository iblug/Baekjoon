import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ds = [input().rstrip() for _ in range(n)]

a = 'ACGT'
r = ''
c = 0
for i in range(m):
    t = [0]*4
    for d in ds:
        t[a.index(d[i])] += 1
    max_ = max(t)
    c += n-max_
    r += a[t.index(max_)]
print(r, c, sep='\n')