n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())

for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    if c == 'D':
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        time += 1

        nx = x + dx[direction]
        ny = y + dy[direction]

        #
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        #
        else:
            # time += 1
            break
        x, y = nx, ny  #
        # time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulate())

'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''
'''
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
'''
'''
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''
