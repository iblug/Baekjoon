import sys
input = sys.stdin.readline

m, h = map(int, input().split())
n = int(input())
r = 0
for _ in range(n):
    c, b = map(int, input().split())
    r += max(c*m, b*h)
print(r)