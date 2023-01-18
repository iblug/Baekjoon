# https://www.acmicpc.net/problem/11653
# 소인수분해

import sys
sys.stdin = open('input.txt', 'r')

# import time
# start = time.time()
# N = int(1e7-4)

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

# end = time.time()
# print(end - start)

# 백준 처리중 7분 걸림

## 큰수부터 **0.5 처리하기?
## 답 다시 보기
