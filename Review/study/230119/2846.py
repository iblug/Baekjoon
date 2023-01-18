# https://www.acmicpc.net/problem/2846
# 오르막길

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
p = list(map(int, input().split()))
# print(p)
step = 0
result = 0
for i in range(N-1):
    print(p[i+1]-p[i])
    if (p[i]<p[i+1]):
        step += p[i+1]-p[i]
    # print(i)
    else:
        step = 0
    result = max(result, step)
    print('step : ',step)
print(result)
"""

N = int(input())
p = list(map(int, input().split()))
result = 0
low = high = p[0]
for now in p:
    if now <= high:
        low = now
        high = now
    else:
        high = now
    result = max(result, high - low)
print(result)

""" 

# 줄이기 가능
# low, high를 하나로
# step, result를 하나로
