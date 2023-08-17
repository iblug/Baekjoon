import sys
input = sys.stdin.readline

n = ' '+input().rstrip()
m = ' '+input().rstrip()
d = [[0 for _ in n] for _ in m]
for y in range(1, len(m)):
    for x in range(1, len(n)):
        if n[x] == m[y]:
            d[y][x] = d[y-1][x-1]+1
        else:
            d[y][x] = max(d[y-1][x], d[y][x-1])
print(d[-1][-1])
