import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())

for _ in range(n):
    u = int(input())
    if u < 1000:
        print(u, u * a)
    else:
        print(u, 1000*a + (u-1000) * b)