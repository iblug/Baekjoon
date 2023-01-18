# https://www.acmicpc.net/problem/2581
# 소수

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
M = int(input())

graph = [0] * (M+1)
graph[1] = 1
for i in range(2, M+1):
    for j in range(i, M+1, i):
        if j == i:
            continue
        else:
            graph[j] = 1

result = [x for x in range(N, M+1) if graph[x] == 0]
# result = []
# for x in range(M-N+1):
#     if graph[x+N] == 0:
#         result.append(x+N)

if result:
    print(sum(result), result[0], sep='\n')
else:
    print(-1)
