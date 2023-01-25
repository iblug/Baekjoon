n = int(input())
graph=[1] * n

a = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            graph[i] += 1

print(*graph)