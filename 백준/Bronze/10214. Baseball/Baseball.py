import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    yt, kt = 0, 0
    for _ in range(9):
        y , k = map(int, input().split())
        yt += y
        kt += k
    else:
        if yt > kt:
            print('Yonsei')
        elif kt > yt:
            print('Korea')
        else:
            print('Draw')