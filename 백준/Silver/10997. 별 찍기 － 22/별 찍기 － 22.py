def star(n, x, y):
    if n == 1:
        for i in range(3):
            ans[x+i][y] = '*'
        return
    r = 4*n-1
    c = 4*n-3

    for i in range(c):
        ans[x][y+i] = '*'
    for i in range(c):
        ans[x+r-1][y+i] = '*'
    for i in range(r):
        ans[x+i][y] = '*'
    for i in range(x+2, x+r):
        ans[i][y+c-1] = '*'
    ans[x+2][y+c-2] = '*'

    star(n-1, x+2, y+2)

N = int(input())
ans = [[' ']*(4*N-3) for _ in range(4*N-1)]
if N == 1:
    print('*')
else:
    star(N, 0, 0)
    ans[1] = ['*']
    for ele in ans:
        print(''.join(ele))