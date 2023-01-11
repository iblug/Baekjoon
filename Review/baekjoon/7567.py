# https://www.acmicpc.net/problem/7567
# 그릇

d = input()
temp = d[0]
count = 5
for i in d[1:]:
    if temp == i:
        count += 5
        temp = i
    else:
        count += 10
        temp = i
count += 5
print(count)

# 부분을 보지말고 전체를 보자
# 길이로 풀자