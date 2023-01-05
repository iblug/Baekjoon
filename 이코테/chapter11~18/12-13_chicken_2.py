from itertools import combinations

n, m = map(int, input().split())
data = []
jj = [] # 집의 좌표 정보
cc = [] # 치킨집의 좌표 정보
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 1:
            jj.append([i, j])
        if data[i][j] == 2:
            cc.append([i, j])

c = list(combinations(cc,m))

def sum_min(candidate):
    count = 0
    for jx, jy in jj:
        mm = 1e9
        for cx, cy in candidate:
            mm = min(mm, abs(cx - jx) + abs(cy - jy))
        count += mm
    return count

r = 1e9
for x in c:
    r = min(r, sum_min(x))
print(r)




# for i in range(chi):
#     for j in range(jip):
#         graph[i][j] = abs(cc[i][0] - jj[j][0]) + abs(cc[i][1] - jj[j][1])
#
# count = 0
# mm = 99
# r = 9999
#
# for x in candidate:
#     for i in range(jip):
#         for y in range(m):
#             mm = min(graph[x[y]][i], mm)
#         count += mm
#         mm = 99
#     r = min(count, r)
#     count = 0

# print(r)



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