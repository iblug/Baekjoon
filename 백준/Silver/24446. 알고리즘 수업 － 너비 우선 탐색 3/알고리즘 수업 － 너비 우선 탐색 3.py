import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([x])
    visited[x] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[now]+1

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [-1] *(n+1)
bfs(r)
print(*visited[1:], sep='\n')