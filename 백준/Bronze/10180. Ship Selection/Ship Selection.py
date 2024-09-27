import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r = 0
    n, d = map(int, input().split())
    for _ in range(n):
        v, f, c = map(int, input().split())
        if d <= v*(f/c):
            r += 1
    print(r)