import sys
input = sys.stdin.readline

data = [[0]*100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for x1 in range(x, x+10):
        for y1 in range(y, y+10):
            data[y1][x1] = 1
cnt = 0
for i in data:
    cnt += i.count(1)
print(cnt)