seat = [0] * 101

n = int(input())
cnt = 0
x = list(map(int, input().split()))
for i in x:
    if seat[i] == 0:
        seat[i] = 1
    else:
        cnt +=1
print(cnt)