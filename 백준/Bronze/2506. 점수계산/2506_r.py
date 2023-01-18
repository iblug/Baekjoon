# https://www.acmicpc.net/problem/2506
# 점수계산

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
r = input().split()
sum = 0
s = 0
for i in r:
    if i == '1':
        s +=1
        sum += s
    else:
        s = 0
print(sum)


############################다른사람

# 묶음마다 리스트로 만들기
N = int(input())
answer = map(int, input().split())

cnt = 0
list = []
for i in answer:
    if i == 1:
        list.append(i)
        len(list) * 1   # 가산점이 2배수라면 * 2를, 3배수라면 3을 하면 됨
        cnt += len(list)
    else:
        list = []
print(cnt) 

# 리스트로 만들기 2
N = int(input())
n_list = input().split('0')
answer_list = []
for item in n_list : 
    answer_list.append(item.count('1'))
result = 0
for num in answer_list :
    result += sum(range(1,num + 1))
print(result)


####

N = int(input()) # 문제의 수 입력
OX = list(map(int, input().split())) # 채점결과 입력

# 점수 계산
# 1번 문제는 맞추면1: 1점 틀리면0: 0점
# 2번 문제 부터는 맞추면1: 앞문제의 점수 + 1점 , 틀리면0: 0점
for n in range(1, N): # 2번 문제 에서 N 번 문제까지
    if OX[n] :# 맞추면1
        OX[n] = OX[n-1]+1 # 앞문제의 점수 + 1점

print(sum(OX))