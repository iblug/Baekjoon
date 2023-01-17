graph = [[0] * 15 for _ in range(15)]
for i in range(15):
    graph[0][i] = i
    graph[0][0] = 0

for x in range(1, 15):
    for y in range(1, 15):
        for y1 in range(1, y+1):
            graph[x][y] += graph[x-1][y1]

T = int(input())

for _ in range(T):
    xx = int(input())
    yy = int(input())
    print(graph[xx][yy])