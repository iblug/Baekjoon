import sys
input = sys.stdin.readline

n = int(input())
r = 1e9
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b and b < r:
        r = b
if r == 1e9:
    print(-1)
else:
    print(r)