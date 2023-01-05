n, m = map(int, input().split())
data = list(map(int, input().split()))

graph = [0] * (m +1)
result = 0

for i in data:
    graph[i] += 1

for i in range(1, m + 1):
    b = sum(graph[i + 1:])
    result += graph[i] * b


print(result)
