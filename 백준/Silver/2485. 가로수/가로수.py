import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def gcd(x, y):
    if x == 0:
        return y
    return gcd(y%x, x)

t =  int(input())
d = [int(input()) for _ in range(t)]
d.sort()
r = []
for i in range(t-1):
    a = d[i+1] - d[i]
    r.append(a)
b = r[0]
for i in range(len(r)):
    c = gcd(b, r[i])
    if c < b:
        b = c
cnt = 0
for i in r:
    cnt += i//b-1

print(cnt)