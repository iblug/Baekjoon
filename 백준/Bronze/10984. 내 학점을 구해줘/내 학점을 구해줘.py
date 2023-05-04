import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    h, p = 0, 0
    n = int(input())
    for j in range(n):
        a, b = map(float, input().split())
        h += a
        p += b*a
    print(int(h), round(p/h, 1))