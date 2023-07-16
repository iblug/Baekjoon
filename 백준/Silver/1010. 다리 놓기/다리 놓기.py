import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    r = 1
    for i in range(m-n+1, m+1):
        r *= i
    for j in range(1, n+1):
        r //= j
    print(r)