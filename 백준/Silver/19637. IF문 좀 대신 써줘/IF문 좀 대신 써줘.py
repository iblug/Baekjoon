import sys
input = sys.stdin.readline

def bc(s,e):
    if s > e:
        return t[s]
    mid = (s+e)//2
    if c > r[mid]:
        return bc(mid+1,e)
    else:
        return bc(s,mid-1)

n, m = map(int, input().split())

r = []
t = []

for _ in range(n):
    a, b = input().split()
    t.append(a)
    r.append(int(b))
for _ in range(m):
    c = int(input())
    print(bc(0,n-1))