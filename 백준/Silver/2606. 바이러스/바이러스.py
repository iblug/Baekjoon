import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(sum(visited)-1)