# https://www.acmicpc.net/problem/1193
# 분수찾기

x = int(input())
i = s = 0
while True:
    i += 1
    s += i
    if x <= s:
        break
if i % 2 == 0:
    print(f'{i-s+x}/{s-x+1}')
else:
    print(f'{s-x+1}/{i-s+x}')

# i 찾기 연습