import sys
input = sys.stdin.readline

m = int(input())
k = 1
for _ in range(m):
    a, b = map(int, input().split())
    if a == k:
        k = b
    elif b == k:
        k = a
print(k)