N = int(input())

graph = [0] * (N+1)
for i in range(2, N+1):
    if graph[i] == 0:
        while True:
            if N % i == 0:
                print(i)
                for j in range(i, N+1, i):
                    graph[j] = 1
                N //= i
            else:
                break