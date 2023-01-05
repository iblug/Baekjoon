# https://www.acmicpc.net/problem/10809
# 알파벳 찾기
s = input() # 알파벳 소문자로 이루어진 문자열 s 입력받기

# 길이가 26(알파벳 개수)인 리스트를 -1로 초기화
result = [-1 for _ in range(26)] 

# 배열 s의 요소를 탐색
for i in s:
    a_i = ord(i) - ord('a') # result의 index에 각 요소 대입하기 위해 'a'의 유니코드값을 빼줌
    if result[a_i] != -1: 
        continue            # 이미 찾은 알파벳이면 contiue하고 다음 탐색
    result[a_i] = s.index(i)# 처음 찾은 알파벳이면 index를 reault에 할당
print(*result, sep=' ') # 출력 예시대로 출력


#########################################

# find() 활용
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