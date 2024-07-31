import sys
input = sys.stdin.readline

n = int(input())
p = [0] + [int(input()) for _ in range(n)]
m = int(input())
r = 0
for _ in range(m):
    r += p[int(input())]
print(r)