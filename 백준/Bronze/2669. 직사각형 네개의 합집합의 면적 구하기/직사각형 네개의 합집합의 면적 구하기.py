g = [[0]*101 for _ in range(101)]

for _ in range(4):
    i, j, k, l = map(int, input().split())
    for x in range(i, k):
        for y in range(j, l):
            g[x][y] = 1
print(sum(map(lambda x: x.count(1), g)))