from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(start:tuple, end:str, maps:list, r:int, c:int):
    visited = [[False]*c for _ in range(r)]
    q = deque([start])

    while q:
        x, y, cost = q.popleft()

        if maps[x][y] == end:
            return cost

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0<= nx <r and 0<= ny <c and maps[nx][ny] != 'X':
                if not visited[nx][ny]:
                    q.append((nx, ny, cost+1))
                    visited[nx][ny] = True

    return -1

def solution(maps):
    r = len(maps)
    c = len(maps[0])

    f = 0
    for i in range(r):
        for j in range(c):
            if maps[i][j] == 'S':
                s = (i, j, 0)
                f += 1
            if maps[i][j] == 'L':
                l = (i, j, 0)
                f += 1
            if f == 2:
                break
        if f == 2:
            break

    s_l = bfs(s, 'L', maps, r, c)
    l_e = bfs(l, 'E', maps, r, c)

    if s_l != -1 and l_e != -1:
        return s_l + l_e

    return -1