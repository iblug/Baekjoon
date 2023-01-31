import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
sum_ = 0
data = [list(map(int, input().split())) for _ in range(n)]
for _ in range(n):
    lst = list(map(int, input().split()))
    data.append(lst)

time = 1e9
height = 256
while height >= 0:
    cnt = 0
    b_p, b_m = 0, 0
    for i in data:
        for j in i:
            if j > height:
                b_m += j - height
            else:
                b_p += height - j
    if b_p <= b_m + b:
        cnt = b_p + b_m*2
        if cnt < time:
            time = cnt
        else:
            break
    height -= 1
print(time, height+1)