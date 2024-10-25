import sys
input = sys.stdin.readline

n = int(input())
a = [input().rstrip() for _ in range(n)]
b = [input().rstrip() for _ in range(n)]
r = 0
for i in range(n):
    if a[i] == b[i]:
        r += 1
print(r)