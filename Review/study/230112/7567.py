# https://www.acmicpc.net/problem/7567
# 그릇

import sys
sys.stdin = open('input.txt', 'r')

data = input()

temp = data[0]
count = 10

for dish in data[1:]:
    if temp == dish:
        count += 5
    else:
        count += 10
    temp = dish

print(count)









# 부분을 보지말고 전체를 보자
# 길이로 풀자