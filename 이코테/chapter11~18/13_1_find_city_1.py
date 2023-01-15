# import sys
# sys.stdin = open('input.txt', 'r')

# from collections import deque

# def BFS(i):
#     q = deque()
#     pass

import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = []
result = [1e9] * (n+1)
result[x] = 0
for _ in range(m):
    graph.append(list(map(int, input().split())))

for i in graph:
    result[i[1]] = min(result[i[1]], result[i[0]] + 1)

for j in range(1, n+1):
    if k not in result:
        print(-1)
        break
    if result[j] == k:
        print(j)

# print(j for j in range(n+1) if result[j] == k)


# print(n, m, k, x, graph, result)