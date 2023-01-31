import sys
input = sys.stdin.readline

n = int(input())

data = [input().rstrip() for _ in range(n)]

cnt1 = 0
for i in data:
    seat = 0
    for j in i:
        if j == '.':
            seat += 1
        elif j == 'X':
            if seat >= 2:
                cnt1 += 1
            seat = 0
    if seat >= 2:
        cnt1 += 1
        
cnt2 = 0
for i in range(n):
    seat = 0
    for j in range(n):
        if data[j][i] == '.':
            seat += 1
        elif data[j][i] == 'X':
            if seat >= 2:
                cnt2 += 1
            seat = 0
    if seat >= 2:
        cnt2 += 1

print(cnt1, cnt2)