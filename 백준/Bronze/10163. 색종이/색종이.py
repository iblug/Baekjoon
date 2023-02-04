import sys
input = sys.stdin.readline

d = [[0]*1001 for _ in range(1001)]

n = int(input())

for c in range(1, n+1):
    x, y, a, b = map(int, input().split())
    for i in range(x, x+a):
        for j in range(y, y+b):
            d[i][j] = c
for m in range(n):
    sum_ = 0
    for i in d:
        sum_ += i.count(m+1)
    print(sum_)