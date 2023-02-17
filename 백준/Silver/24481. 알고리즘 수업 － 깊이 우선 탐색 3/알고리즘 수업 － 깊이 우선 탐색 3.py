import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,t):
    d[x] = t
    for now in graph[x]:
        if d[now] == -1:
            dfs(now, t+1)
    return

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
d = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

dfs(r,0)
print(*d[1:], sep='\n')