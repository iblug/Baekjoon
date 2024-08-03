import sys
input = sys.stdin.readline

n , x = map(int, input().split())
r = 1e9
b = 0

for i in range(n):
    s, t = map(int, input().split())
    if x >= s + t and b < s:
        r = s + t
        b = s
print(-1 if r > x else b)