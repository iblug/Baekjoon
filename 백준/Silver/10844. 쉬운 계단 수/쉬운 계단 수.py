n = int(input())
d = [[0]+[1]*9 for _ in range(n)]
for i in range(1, n):
    for j in range(10):
        if j == 0:
            d[i][0] = d[i-1][1]
        elif j == 9:
            d[i][9] = d[i-1][8]
        else:
            d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % int(1e9)
print(sum(d[-1]) % int(1e9))