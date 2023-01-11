# https://www.acmicpc.net/problem/1157
# 단어 공부

s = input().upper()
result = {}
for j in s:
    if j not in result.keys():
        result[j] = 0
    result[j] += 1
M = max(result.values())
c = 0
r = ''
for k, v in result.items():
    if M == v:
        c += 1
        r = k
if c > 1:
    print('?')
else:
    print(r)

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