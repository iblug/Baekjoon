import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,t):
    global cnt
    cnt += 1
    v[x] = True
    d[x] = cnt*t
    for c in graph[x]:
        if not v[c]:
            v[c] = True
            dfs(c, t+1)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
v = [False] * (n+1)
d = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for e in graph:
    e.sort(reverse=True)

cnt = 0
dfs(r, 0)
print(sum(d))