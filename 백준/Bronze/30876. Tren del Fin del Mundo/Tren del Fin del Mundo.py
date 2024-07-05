import sys
input = sys.stdin.readline

t = int(input())
y1 = 1001
for _ in range(t):
    x, y = map(int, input().split())
    if y1 > y:
        y1 = y
        x1 = x
print(x1, y1)