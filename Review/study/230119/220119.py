# 2846 오르막길

N = int(input())
p = list(map(int, input().split()))
step = 0 # 높이 차이
result = 0 # 높이 중에 큰 값
for data in range(N-1):
    # 오르막이면
    if p[data+1] > p[data]:
        step += p[data+1] - p[data] # 높이 차이 저장
    else:
        step = 0
    result = max(result, step) # 기존 높이와 현재 높이 중 큰 값
print(result)

############################################################

# 5622 다이얼

# WA 입력시 W(index(7)+3 ) + A(index(0)+3 ) = 13

datas = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
nums = input()

result = 0
for data in datas:
    for num in nums:
        if num in data:
            result += datas.index(data) + 3
print(result)

############################################################

# 11655 ROT13

S = input()
result = ''
for i in S:
    if i.islower(): # -97 + 13 = -84
        result += chr((ord(i)-84) % 26 + 97)
    elif i.isupper(): # -65 + 13 = -52
        result += chr((ord(i)-52) % 26 + 65)
    else:
        result += i
print(result)

############################################################

# 11653 소인수분해

N = int(input())

graph = [0] * (N+1) # 저장할 테이블
for i in range(2, N+1):
    if graph[i] == 0: # 아직 체크한 값이 아니면
        while True:
            if N % i == 0: # 나눠지면
                print(i)   # 출력
                for j in range(i, N+1, i): # i의 배수를
                    graph[j] = 1        # 테이블에 체크하기
                N //= i
            else:
                break

############################################################

#2581 소수

N = int(input())
M = int(input())

graph = [0] * (M+1) # 저장할 테이블
graph[1] = 1 # 1은 소수가 아님
for i in range(2, M+1):
    for j in range(i, M+1, i):
        if j == i:  # 소수는 그냥 넘김
            continue
        else:           # 소수의 배수는
            graph[j] = 1 # 테이블에 체크

# N ~ M의 테이블에서 체크 안된 것 추출
result = [x for x in range(N, M+1) if graph[x] == 0]
### List Comprehension ###
# result = []
# for x in range(M-N+1):
#     if graph[x+N] == 0:
#         result.append(x+N)

if result:
    print(sum(result), result[0], sep='\n')
else:
    print(-1)

############################################################

# 2775 부녀회장이 될테야

# 테이블 초기화
graph = [[0] * 15 for _ in range(15)]
for i in range(15):
    graph[0][i] = i

for x in range(1, 15): # x층
    for y in range(1, 15): # y호
        for y1 in range(1, y+1): # x층y호 += x-1층[1~y]호
            graph[x][y] += graph[x-1][y1]

# print(*graph[::-1], sep='\n')

T = int(input())

for _ in range(T):
    xx = int(input())
    yy = int(input())
    print(graph[xx][yy])