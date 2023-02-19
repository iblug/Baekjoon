import sys
input = sys.stdin.readline

def dfs(x, y):
    s = [(x, y)]
    while s:
        x, y = s.pop()
        j = graph[x][y]
        if j == -1:
            return True
        visited[x][y] = True
        if j == 0:
            continue
        if x+j < n and not visited[x+j][y]:
            s.append((x+j, y))
        if y+j < n and not visited[x][y+j]:
            s.append((x, y+j))
    return False

n = int(input())

graph= [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

if dfs(0, 0):
    print('HaruHaru')
else:
    print('Hing')