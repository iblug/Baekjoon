# https://www.acmicpc.net/problem/2979
# 트럭 주차

import sys
sys.stdin = open('input.txt', 'r')

a, b, c = map(int, input().split())
data = [0] * 101
for _ in range(3):
    i, o = map(int, input().split())
    for n in range(i, o):
        data[n] += 1
result = 0
result += data.count(1) * a
result += data.count(2) * b * 2
result += data.count(3) * c * 3
print(result)

# 처음엔 i, o 따로 리스트 만들었다가 하다보니 깨달음

