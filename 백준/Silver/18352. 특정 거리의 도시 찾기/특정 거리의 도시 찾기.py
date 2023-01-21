import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [1e9] * (N+1)
visited = [False] * (N+1)
distance[X] = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

q = deque([X])
while q:
    now = q.popleft()
    if visited[now] == False:
        visited[now] = True
        for i in graph[now]:
            q.append(i)
            distance[i] = min(distance[now]+1, distance[i])
result = [j for j in range(N+1) if distance[j] == K]
if result:
    print(*result,sep='\n')
else:
    print(-1)