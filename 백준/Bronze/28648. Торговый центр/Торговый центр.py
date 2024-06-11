import sys
input = sys.stdin.readline

n = int(input())
r = 1e9
for _ in range(n):
    t, l = map(int, input().split())
    r = min(r, t+l)
print(r)