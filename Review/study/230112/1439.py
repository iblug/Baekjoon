# https://www.acmicpc.net/problem/1439
# 뒤집기

import sys
sys.stdin = open('input.txt', 'r')

data = input()

temp = data[0] # 이전 수를 저장
count = 0
result = 0

# data를 하나씩 탐색
for num in data: 
    if temp != num: # 이전 수와 다르면
        count += 1
        temp = num   

if count % 2 == 0:
    result = count // 2
else:
    result = (count // 2) + 1

print(result)

# result = (count + 1) // 2