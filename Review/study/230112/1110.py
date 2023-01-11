# https://www.acmicpc.net/problem/1110
# 더하기 사이클

import sys
sys.stdin = open('input.txt', 'r')

data = int(input())
count = 0
new = -1 # 새로운 수

x = data // 10 # 10의 자리
y = data % 10 # 1의 자리

while new != data:
    new = 10*y + (x + y)%10
    x = new // 10
    y = new % 10
    count += 1
print(count)