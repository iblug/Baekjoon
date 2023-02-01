import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
def bfs(graph, v, visited):
    q = deque([v])
    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = True
            print(now,end=' ')
            for i in graph[now]:
                q.append(i)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i] = sorted(graph[i])

dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph, v, visited)