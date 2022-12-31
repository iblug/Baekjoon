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