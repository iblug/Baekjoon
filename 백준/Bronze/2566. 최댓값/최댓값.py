import sys
input = sys.stdin.readline

max_ = 0
data = []

for i in range(9):
    data.append(list(map(int, input().split())))
    if max(data[-1]) >= max_:
        i_ = i
        max_ = max(data[-1])
l = data[i_]
print(max_)
print(i_+1, l.index(max_)+1)