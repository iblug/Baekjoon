import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(float, input().split())
    print(round(abs(a-b), 1))