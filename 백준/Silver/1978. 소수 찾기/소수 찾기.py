import sys

N = int(input())
data = list(map(int, input().split()))

max_ = max(data)

graph = [True] * (max_+1)
graph[0] = False
graph[1] = False

for i in range(2, max_+1):
    if graph[i]:
        for j in range(2*i, max_+1, i):
            graph[j] = False
result = [i for i in data if graph[i]]
print(len(result))