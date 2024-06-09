import sys
input = sys.stdin.readline

n = int(input())
m = 0
for _ in range(n):
    a, b = map(int, input().split())
    if m < a*b:
        m = a*b
print(m)