from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    visted = [False] * (n+1)
    q = deque([x])
    visted[x] = True
    cnt = 1
    while q:
        now = q.popleft()
        for v in graph[now]:
            if not visted[v]: 
                q.append(v)
                visted[v] = True
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

result = []

max = 0
result = []
for i in range(1, n+1):
    cnt = bfs(i)
    if max < cnt:
        max = cnt
        result = [i]
    elif max == cnt:
        result.append(i)

print(*result)