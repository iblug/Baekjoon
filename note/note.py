# # 아스키코드
# x=['0', '9', 'A', 'Z', 'a', 'z']
# print(x)
# ### 48 ~ 57 / 65 ~ 90 / 97 ~ 122
# for i in range(len(x)):
#     print(ord(x[i]),end=' ')
# print()
# for i in range(32, 127): # 32 ~ 126
#     print(i, chr(i), end=' ')
#     if i%10 == 0:
#         print()

# 대소문자 전환
# string.swapcase()

# # 배열 회전
# n = 5
# k = [[] * n for i in range(n)]

# c = 0
# for i in range(n):
#     for j in range(n):
#         k[i].append(c)
#         c += 1

# print(*k,sep='\n')
# print()

# # 좌회전
# temp_left = [[0] * n for i in range(n)]

# for i in range(n):
#     for j in range(n):
#         temp_left[i][j] = k[j][n-i-1]

# print(*temp_left,sep='\n')

# # 우회전

# temp_right = [[0] * n for i in range(n)]

# for i in range(n):
#     for j in range(n):
#         temp_right[i][j] = k[n-j-1][i]

# print(*temp_right,sep='\n')









#math.ceil() : 소수 부분을 정수로 올려, integer로 만듭니다.
#math.floor() : 소수 부분을 버리고, integer로 만듭니다.
#round() : 소수 0.5 이하는 버리고, 0.5를 초과하면 올립니다.


# 스택 큐 우선큐

# join과 map

# 시퀀스 정리

# sorted() 옵션

# # 출력방법
# w = list(map(int, input().split()))
# a = [1, 1, 2, 2, 2, 8]
# b = list(map(str, a))
# print(' '.join(b))
# for i in range(6):
#     print(a[i] - w[i], end=' ')

# # print( '\n' + (*a)) # 안되는 이유, 고치려면?

# # 체스말 출력 - list for 출력
# w=input().split()
# a=[1,1,2,2,2,8]
# print(*(list(a[i]-int(w[i])for i in range(6))))


# # .index() 와 .find() 차이점


# 최대공약수와 최소공배수(GCD, LCM)
# a, b = map(int, input().split())
# l = a * b
# while a:
#     b, a = a, b % a
# print(b, l // b)

# 리스트안에있는 딕셔너리 정렬
# key lambda
# itemgetter?



'''
# list comprehension 과 람다
# result = [i**3 for i in range(1, 4)]
# print(result)

# numbers = ['1', '2', '3']
# result = lambda x : int(x) in numbers
# print(result)

# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(list(map(lambda n: n % 3, numbers)))
'''

# import
# 큐
# from collections import deque
# 콤비
# from itertools import combinations
# 조합?
# from itertools import permutations
# 정렬
# from operator import itemgetter



# # ===========================================================

# # 기타 등등

# # 문자열로된 리스트
#
# import ast
#
# S = '[[1, 2, 3], [4, 5, 6]' # 문자열으로 입력
# print(S)
# print(type(S))
# N = ast.literal_eval(S)
# print(N)
# print(type(N))





# # 딕셔너리 병합
# # '|' or merge
# merged = {**dictionary_one, **dictionary_two} 
# first_dictionary = {'name': 'Fatos', 'location': 'Munich'}
# second_dictionary = {'name': 'Fatos', 'surname': 'Morina',
#                      'location': 'Bavaria, Munich'}
#
# result = first_dictionary | second_dictionary
# print(result)  
# # {'name': 'Fatos', 'location': 'Bavaria, Munich', 'surname': 'Morina'}
#
# d1.update(d2)
#
# # https://codechacha.com/ko/python-merge-two-dict/
#
# 

# # 문자열 첫시작(index 0 을 사용하지 않고)
# my_string = "abcdef" 
# print(my_string.startswith("b")) # False


# # 딕셔너리 키-값 교환
# dictionary = {"a": 1, "b": 2, "c": 3}
# reversed_dictionary = {j: i for i, j in dictionary.items()}
# print(reversed_dictionary)  # {1: 'a', 2: 'b', 3: 'c'}

# import __ as **
# **.~ 로 쓸 수 있다


# *b이후의 값을 list로 b에 저장
# 숏코딩때 유용
# a,*b=map(int,sys.stdin.readline().split()) # *b

# import sys
# sys.stdin = open('input.txt', 'r')
# a = sys.stdin.read().split()
# print(a)