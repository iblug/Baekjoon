n = int(input())
data = input()

graph = [['#']*101 for _ in range(101)]
# 남 서 북 동(우회전)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x=50
y=50
graph[x][y] = '.'
index = 0
mx = my = x
nx = ny = y
for i in data:
    if i == 'F':
        x += dx[index]
        y += dy[index]
        mx = max(mx, x)
        my = max(my, y)
        nx = min(nx, x)
        ny = min(ny, y)

        graph[x][y] = '.'
    elif i == 'R':
        index = (index+1)%4
    elif i == 'L':
        index = (index-1)%4
for x1 in range(nx, mx + 1):
    for y1 in range(ny, my + 1):
        print(graph[x1][y1],end='')
    print()