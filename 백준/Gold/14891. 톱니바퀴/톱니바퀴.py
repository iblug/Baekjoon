import sys
from collections import deque
input = sys.stdin.readline

def right(a, b):
    if a == 4:
        return
    if g[a-1][2] != g[a][6]:
        right(a+1, b*-1)
        g[a].rotate(b*-1)

def left(a, b):
    if a == -1:
        return
    if g[a+1][6] != g[a][2]:
        left(a-1, b*-1)
        g[a].rotate(b*-1)

g = [deque(list(input().rstrip())) for _ in range(4)]
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    
    right(a, b)
    left(a-2, b)
    g[a-1].rotate(b)
c = 1
r = 0
for i in range(4):
    r += int(g[i][0]) * c
    c *= 2
print(r)