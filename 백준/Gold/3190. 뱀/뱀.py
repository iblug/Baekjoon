import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
ap = set(tuple(map(int, input().split())) for _ in range(K))
L = int(input())
d = []
for _ in range(L):
    X, D = input().split()
    X = int(X)
    d.append((X, D))

di = ((0, 1), (1, 0), (0, -1), (-1, 0))

a = 0
go = 0 
t = 0
snake = deque([(1, 1)])
x = y = 1
while True:
    t += 1
    nx = x + di[go][0]
    ny = y + di[go][1]
    if nx <= 0 or nx > N or ny <= 0 or ny > N:
        break
    if (nx, ny) in snake:
        break
    snake.append((nx, ny))
    if (nx, ny) in ap:
        ap.remove((nx, ny))
    else:
        snake.popleft()
    if a < L:
        if t == d[a][0]:
            if d[a][1] == 'L':
                go = (go+3)%4
            else:
                go = (go+1)%4
            a += 1
    x, y = nx, ny
print(t)