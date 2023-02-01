import sys
input = sys.stdin.readline

def dfs(graph, x, visited):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            dfs(graph, i, visited)                

e = int(input())
v = int(input())
graph = [[] for _ in range(e+1)]
visited = [False]*(e+1)
for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)
print(visited.count(True)-1)