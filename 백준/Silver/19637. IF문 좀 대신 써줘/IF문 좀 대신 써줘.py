import sys
input = sys.stdin.readline

def bs(lo, hi):
    if lo+1 >= hi:
        return t[hi]
    mid = lo+hi >> 1
    if r[mid] < c:
        return bs(mid,hi)
    else:
        return bs(lo,mid)

n, m = map(int, input().split())

r = []
t = []
for _ in range(n):
    a, b = input().split()
    t.append(a)
    r.append(int(b))

for _ in range(m):
    c = int(input())
    print(bs(-1,n))