import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    global cnt
    q = deque([x])
    visited[x] = cnt
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                cnt += 1
                visited[i] = cnt

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort(reverse=True)

bfs(r)
print(*visited[1:], sep='\n')