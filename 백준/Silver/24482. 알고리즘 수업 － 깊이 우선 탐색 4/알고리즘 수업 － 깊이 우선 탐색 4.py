import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,t):
    visited[x] = True
    d[x] = t
    for now in graph[x]:
        if not visited[now]:
            dfs(now,t+1)
    pass

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
d = [-1]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for ele in graph:
    ele.sort(reverse=True)

dfs(r,0)
print(*d[1:], sep='\n')