while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    else:
        print('YNeos'[n<=m::2])