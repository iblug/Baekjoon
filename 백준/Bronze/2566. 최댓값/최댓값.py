import sys
input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(9)]
max_ = 0
for i in range(9):
    for j in range(9):
        if data[i][j] >= max_:
            i_ = i
            j_ = j
            max_ = data[i][j]
print(max_)
print(i_+1, j_+1)