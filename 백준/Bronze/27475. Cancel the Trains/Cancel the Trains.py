import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i, j = 0, 0
    r = 0
    while i < n and j < m:
        if a[i] == b[j]:
            r += 1
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    print(r)