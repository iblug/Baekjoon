d = [[0]*1001 for _ in range(1001)]

n = int(input())

result = [0]*(n+1)
for c in range(1, n+1):
    x, y, a, b = map(int, input().split())
    for i in range(x, x+a):
        for j in range(y, y+b):
            result[d[i][j]] -= 1
            d[i][j] = c
            result[c] += 1
print(*result[1:], sep='\n')