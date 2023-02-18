import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    o = 0
    s = 0
    q = deque([x])
    dep[x] = 0
    while q:
        x = q.popleft()
        if v[x]:
            continue
        o += 1
        s += o*dep[x]
        v[x] = True
        for c in graph[x]:
            if not v[c]:
                dep[c] = min(dep[c], dep[x] + 1)
                q.append(c)
    return s

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
v = [False] * (n+1)
dep = [1e9]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for e in graph:
    e.sort()

print(bfs(r))