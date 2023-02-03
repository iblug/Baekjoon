from collections import deque
deep = 100001

def bfs(x):
    q=deque()
    q.append(x)
    distance[x] = 0
    while q:
        now = q.popleft()
        if now == k:
            break
        visited[now] = True
        for i in graph[now]:
            if not visited[i]:
                distance[i] = min(distance[i],distance[now]+1)
                q.append(i)
    return distance[now]

n, k = map(int, input().split())

graph = [[] for _ in range(deep)]
visited = [False] * deep
distance = [1e9] * deep
for i in range(0, deep):
    if -1 < i-1:
        graph[i].append(i-1)
    if i+1 < deep:
        graph[i].append(i+1)
    if i*2 < deep:
        graph[i].append(i*2)
print(bfs(n))