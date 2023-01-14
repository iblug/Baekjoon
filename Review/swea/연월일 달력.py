T = int(input())

data = [-1 ,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for t in range(1, T + 1):
    ymd = input()

    y = ymd[:4]
    m = ymd[4:6]
    d = ymd[6:]

    if int(m) > 12 or int(d) > data[int(m)]:
        result = -1
    else:
        result = f'{y}/{m}/{d}'
    print(f'#{t} {result}')