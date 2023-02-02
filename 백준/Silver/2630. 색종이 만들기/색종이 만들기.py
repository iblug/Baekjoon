import sys
input = sys.stdin.readline

n = int(input())
s = n
graph = [list(input().split()) for _ in range(n)]
cnt0 = cnt1 = 0
while s > 0:
    for i in range(0,n,s):
        for j in range(0,n,s):
            if graph[i][j] == '1':
                for x in range(0, s):
                    for y in range(0, s):
                        if graph[i+x][j+y] != '1':
                            break
                    if graph[i+x][j+y] != '1':
                        break
                else:
                    cnt1 += 1
                    for x in range(0, s):
                        for y in range(0, s):
                            graph[i+x][j+y] = 2
            if graph[i][j] == '0':
                for x in range(0, s):
                    for y in range(0, s):
                        if graph[i+x][j+y] != '0':
                            break
                    if graph[i+x][j+y] != '0':
                        break
                else:
                    cnt0 += 1
                    for x in range(0, s):
                        for y in range(0, s):
                            graph[i+x][j+y] = 2
    s //= 2
print(cnt0, cnt1)