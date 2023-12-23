import sys, math
input = sys.stdin.readline

k = int(input())
for i in range(1, k + 1):
    print(f'Data Set {i}:')
    r = 0
    n, s, d = map(int, input().split())
    for j in range(n):
        dd, v = map(int, input().split())
        if math.ceil(dd/s) <= d:
            r += v
    print(r)
    print()
