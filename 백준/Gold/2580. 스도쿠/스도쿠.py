def check(a):
    if a == 81:
        return True

    y = a//9
    x = a % 9
    if lst[y][x] != 0:
        return check(a+1)

    for j in range(1, 10):
        if crow[y][j] and ccol[x][j] and ccro[(y // 3) * 3 + (x // 3)][j]:
            crow[y][j] = ccol[x][j] = ccro[(y // 3) * 3 + (x // 3)][j] = 0
            lst[y][x] = j
            if check(a + 1):
                return True
            lst[y][x] = 0
            crow[y][j] = ccol[x][j] = ccro[(y // 3) * 3 + (x // 3)][j] = 1
    return False


lst = list(list(map(int, input().split())) for _ in range(9))
crow = [[1 for _ in range(10)] for _ in range(9)]
ccol = [[1 for _ in range(10)] for _ in range(9)]
ccro = [[1 for _ in range(10)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        if lst[i][j] != 0:
            crow[i][lst[i][j]] = 0
            ccol[j][lst[i][j]] = 0
            ccro[(i//3)*3+(j//3)][lst[i][j]] = 0
check(0)
for i in lst:
    print(*i)