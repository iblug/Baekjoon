import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x):
    global cnt
    visited[x] = True
    result[x] = cnt
    cnt += 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 1
result = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for j in graph:
    j.sort()

dfs(r)
print(*result[1:], sep='\n')