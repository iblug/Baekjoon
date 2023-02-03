import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    q = deque([x])
    cnt = 0
    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = True
            cnt += 1
            d[now-1] = cnt
            for i in graph[now]:
                q.append(i)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
d = [0] * (n)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
graph = [sorted(i) for i in graph]
bfs(r)
print(*d,sep='\n')