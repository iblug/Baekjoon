# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())
data = []
jip , chi = 0, 0 # 갯수
jj = [] # 집의 좌표 정보
cc = [] # 치킨집의 좌표 정보
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 1:
            jip += 1
            jj.append([i, j])
        if data[i][j] == 2:
            chi += 1
            cc.append([i, j])

graph = [[0] * jip for _ in range(chi)] # 거리정보

for i in range(chi):
    for j in range(jip):
        graph[i][j] = abs(cc[i][0] - jj[j][0]) + abs(cc[i][1] - jj[j][1])

candidate = list(combinations(range(chi),m))

count = 0
mm = 99
r = 9999

for x in candidate:
    for i in range(jip):
        for y in range(m):
            mm = min(graph[x[y]][i], mm)
        count += mm
        mm = 99
    r = min(count, r)
    count = 0

print(r)



'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
'''
'''
5
10
11
32
'''