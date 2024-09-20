import sys
input = sys.stdin.readline

n = int(input())
r = 0
for _ in range(n):
    a, b = map(float, input().split())
    r += a * b
print(f'{r:.3f}')