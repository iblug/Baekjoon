import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(x):
    global cnt
    cnt += 1
    result[x] = cnt
    for i in graph[x]:
        if not result[i]:
            dfs(i)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for d in graph:
    d.sort(reverse=True)
cnt = 0
result = [0]*(n+1)
dfs(r)
print(*result[1:], sep='\n')