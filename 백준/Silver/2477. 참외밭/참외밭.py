import sys
input = sys.stdin.readline

k = int(input())

di = [1, -1, -1, 1]

x = y = 0
data = []
xi = []
yi = []
for _ in range(6):
    d, l = map(int, input().split())
    if d<3:
        x += l*di[d-1]
        xi.append(x)
    else:
        y += l*di[d-1]
        yi.append(y)
    data.append((x, y))
xi.sort()
yi.sort()
x_min = xi[0]
x_max = xi[2]
y_min = yi[0]
y_max = yi[2]

area = (x_max-x_min)*(y_max-y_min)
xyi = ((x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max))
for i in xyi:
    if i not in data:
        ex = (i[0]-xi[1])*(i[1]-yi[1])
result = (area - abs(ex)) * k
print(result)