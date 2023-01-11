# https://www.acmicpc.net/problem/10809
# 알파벳 찾기


# 알파벳 소문자로 이루어진 문자열 s 입력받기
s = input() 

# 길이가 26(알파벳 개수)인 리스트를 -1로 초기화
result = [-1 for _ in range(26)] 

# 배열 s의 요소를 탐색
for i in s:
    a_i = ord(i) - ord('a') # result의 index에 각 요소 대입하기 위해 'a'의 유니코드값을 빼줌
    if result[a_i] != -1: 
        continue            # 이미 찾은 알파벳이면 contiue하고 다음 탐색
    result[a_i] = s.index(i)# 처음 찾은 알파벳이면 index를 reault에 할당
print(*result, sep=' ') # 출력 예시대로 출력

# .index()는 찾는 문자가 없는 경우 ValueError에러 발생

#########################################

# find() 활용 # .find()는 리스트, 튜플, 딕셔너리에 사용하면 AttributeError 발생
# 없으면 -1를 리턴 # index를 쓰면 ValueError에러 발생
s = input()
result = [-1 for _ in range(26)] 

for i in s:
    result[ord(i)-ord('a')] = s.find(i)

print(*result, sep=' ')

#########################################

# BEST

s = input()
for i in range(97, 123):    # range(ord('a'), ord('z') + 1)
    print(s.find(chr(i)), end=' ') # 없으면 -1 반환
#

string = input()

for i in range(26) :
    print(string.find(chr(97+i)), end = ' ') # 위와 같음

#########################################

# dict이용?(출력 길이도 길고, key에 한번만 접근하면 되니까 굳이 필요없다)

s = input()
result = {}
for i in range(ord('a'), ord('z') + 1):
    result[chr(i)] = -1
for j in s:
    if result[j] != -1:
        continue
    result[j] = s.find(j)

for k in result.values():
    print(k, end=' ')


############################################

# 숏코딩

print(*map(input().find,map(chr,range(97,123))))
# 알파벳 map형을 리턴받고
# 다시 map으로 input().find를 적용시킨다. map형으로 리턴
# print(*map)으로 출력