import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    r = 0
    for i in range(n):
        if a[i] != b[i]:
            r += 1
    print(r)