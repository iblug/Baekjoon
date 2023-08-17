n = ' '+input()
m = ' '+input()
d = [[0 for _ in n] for _ in m]
for y in range(1, len(m)):
    for x in range(1, len(n)):
        d[y][x] = max(d[y-1][x], d[y][x-1], d[y-1][x-1]+(n[x] == m[y]))
print(d[-1][-1])