import sys
input = sys.stdin.readline

t = int(input())
lst = [list(map(int, input().split())) for _ in range(t)]
for i in range(1, t):
    for j in range(3):
        if j == 0:
            lst[i][0] = lst[i][0] + min(lst[i-1][1], lst[i-1][2])
        if j == 1:
            lst[i][1] = lst[i][1] + min(lst[i-1][0], lst[i-1][2])
        if j == 2:
            lst[i][2] = lst[i][2] + min(lst[i-1][0], lst[i-1][1])
print(min(lst[-1]))