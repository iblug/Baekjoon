import sys
sys.stdin = open('input.txt', 'r')
from collections import deque



# import sys
# input = sys.stdin.readline

# def BFS(i):
#     q.append(i)
#     # print(i)
#     print(q)
#     # for v in i:

#     pass

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = [-1] * (n + 1)
result[x] = 0

q = deque([x])
# q.append([x])
while q:
    v = q.popleft()
    # print(v)
    for i in graph[v]:
        # print(i)
        if result[i] == -1:
            result[i] = result[v] + 1
        q.append(i)
        # result[i] = min(result[i], result[i] + 1)
        # print(q)

# print(q, graph, result)


# for i in graph:

for j in range(1, n+1):
    if k not in result:
        print(-1)
        break
    if result[j] == k:
        print(j)

# print(j for j in range(n+1) if result[j] == k)

