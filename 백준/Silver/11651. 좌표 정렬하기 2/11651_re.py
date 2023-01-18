# https://www.acmicpc.net/problem/11651
# 좌표 정렬하기 2

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
s = []
for _ in range(N):
    s.append(list(map(int, input().split())))
s = sorted(s, key = lambda x:x[0])
s = sorted(s, key = lambda x:x[1])

for n in s:
    print(*n)

# lambda 잘쓰기
# 출력?

############ 다른 사람 답

# 

import sys
# readlines()[1:]로 첫 문자를 제외하고 입력받기 [:-1] 안됨!
coordinate = sys.stdin.readlines()[1:]
# ['0 4\n', '2 2\n', '1 -1\n', '1 2\n', '3 3\n']

# 임시로(원본 안바뀜) split해주고 int해주고
coordinate.sort(key=lambda x : int(x.split()[0])) 
coordinate.sort(key=lambda y : int(y.split()[1]))

# \n 이 포함되어 있으므로 
print("".join(coordinate))



#### x,y에 대한 정렬을 함수 하나로 처리 하는법?

import sys

def sort_num(n):
    x, y = n.split()
    return int(x)/10000000 + int(y)

coordinates = sys.stdin.readlines()[1:]
coordinates.sort(key=lambda n: sort_num(n))
print(''.join(coordinates))