# https://www.acmicpc.net/problem/1157
# 단어 공부

import sys
sys.stdin = open('input.txt', 'r')

data = input().upper() # 대문자로 입력
result = {} # dict 생성
for j in data:
    # if j not in result.keys():
    result[j] = result.get(j, 0) + 1
    # result[j] += 1
M = max(result.values())
count = 0
result = ''
for key, value in result.items():
    if M == value:
        count += 1
        result = key

if count > 1:   # 여러개면
    print('?')
else:
    print(result)
























# 억지로 맞췄다
# 더 쉬운 방법이 없을까
# max의 인덱스
# 인덱스 + 값 = enumerate()
# 처리속도 긺

#######################################################


# A~Z 탐색
# .count() 사용
# max_num > cnt 일때
# max_num == cnt 일때