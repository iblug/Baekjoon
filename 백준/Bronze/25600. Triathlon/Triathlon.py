import sys
input = sys.stdin.readline

n = int(input())
r = 0
for _ in range(n):
    a, d, g = map(int, input().split())
    if a == d+g:
        r = max(r, a**2*2)
    else:
        r = max(r, a*(d+g))
print(r)