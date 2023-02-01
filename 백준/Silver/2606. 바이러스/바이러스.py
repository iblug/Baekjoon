import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            dfs(i)                

e = int(input())
v = int(input())
graph = [[] for _ in range(e+1)]
visited = [False]*(e+1)
for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(visited.count(True)-1)