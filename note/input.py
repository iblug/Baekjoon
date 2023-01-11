# https://itcrowd2016.tistory.com/81

# 한줄을 읽어서 정수로 변환
N = int(input())
# >>> 5
print(N)
# 5

# '공백으로 구분'된 문자 한줄 입력받기 - split
M = input().split()
# >>> a b c
print(M)
# ['a', 'b', 'c'] # 문자열 # 리스트로 반환됨!!!!!!!

# 공백으로 구분된 한줄을 입력받고 정수로 변환 - map
I, J = map(int, input().split())
# >>> 1 2
print(I, J)
# 1 2




#### 리스트로 입력받기 - list ####

# '이어진 숫자'를 한자리씩 나눠서 리스트에 저장 # 문자열
arr1 = list(input())
# >>> 12345
print(arr1)
# ['1', '2', '3', '4', '5']


# '이어진 숫자'를 한자리씩 나눠서 리스트에 저장 # 숫자형 
# 자릿수 마다 수 필요할 때
arr2 = list(map(int, input()))
# >>> 12345
print(arr2)
# [1, 2, 3, 4, 5]


# '공백으로 구분된 숫자'를 입력받아 리스트에 저장
arr3 = list(map(int, input().split()))
# >>> 1 2 3 4 5
print(arr3)
# [1, 2, 3, 4, ,5] # 숫자형


# N행으로 이뤄진 '2차원' 배열 입력받기
N = int(input()) # N행
# >>> 3
arr4 = [list(map(int, input().split())) for _ in range(N)]
# >>> 1 2 3
# >>> 4 5 6
# >>> 7 8 9
print(arr4)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]













# EOF




# # 문자열을 '~~~ = [-, -, -]' 로 입력 받았을 때
# s = input()
# # 'number_list = [1, 2, 3, 4, 5]' 입력
# for i in range(len(s)):
#     if s[i] == '[':
#         number_list = list(map(int, (s[i + 1:-1]).split(',')))
# print(number_list)













##################################################


import sys

#문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)


##################################################


# 파일로 입력받기
# 표준입력을 파일/읽기로 설정
sys.stdin = open('input.txt','r') # mode r

# # 입출력 읽기 쓰기
# # https://blog.naver.com/khsu777/222811116400


open(0).read() == sys.stdin.read()
# open(0)을 쓰면 import sys 가 필요 없다!!!!!!!!!
# https://it-neicebee.tistory.com/m/118
# 표준 입력 # 그냥 참고
