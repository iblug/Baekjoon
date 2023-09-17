import sys
input = sys.stdin.readline

y, m, d = map(int, input().split('-'))
n = int(input())
c = 0
for _ in range(n):
    g = list(map(int, input().split('-')))
    if g[0] > y:
        c += 1
    elif g[0] == y and g[1] > m:
        c += 1
    elif g[0] == y and g[1] == m and g[2] >= d:
        c += 1
print(c)