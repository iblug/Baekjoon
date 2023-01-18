# 1110 더하기 사이클

data = int(input())
count = 0
new = -1 # 새로운 수

x = data // 10 # 10의 자리
y = data % 10 # 1의 자리

while new != data:
    new = 10*y + (x + y)%10
    x = new // 10
    y = new % 10
    count += 1
print(count)

##################################################

# 1157 단어 공부

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

##################################################


# 1439 뒤집기

data = input()

temp = data[0] # 이전 수를 저장
count = 0
result = 0

# data를 하나씩 탐색
for num in data: 
    if temp != num: # 이전 수와 다르면
        count += 1
        temp = num   
print(count)

result = (count + 1) // 2
# if count % 2 == 0:
#     result = count // 2
# else:
#     result = (count // 2) + 1

print(result)

# [i],[i-1] 사용하기

##################################################

# 2675 문자열 반복

T = int(input())

for _ in range(T):
    result = ''
    r, s = input().split()

    for i in s:
        for _ in range(int(r)):
            result += i
    print(result)


##################################################

# 2979 트럭 주차

a, b, c = map(int, input().split())
data = [0] * 101
for _ in range(3):
    i, o = map(int, input().split())
    for n in range(i, o):
        data[n] += 1
result = 0
result += data.count(1) * a
result += data.count(2) * b * 2
result += data.count(3) * c * 3
print(result)

##################################################

# 7567 그릇

data = input()

temp = data[0]
count = 10

for dish in data[1:]:
    if temp == dish:
        count += 5
    else:
        count += 10
    temp = dish

print(count)