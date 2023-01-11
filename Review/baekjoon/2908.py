# https://www.acmicpc.net/problem/5622
# 다이얼

data = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
n = input()

r = 0
for i in data:
    for j in n:
        if j in i:
            r += data.index(i) + 3
print(r)

# data의 규칙찾기?
# 