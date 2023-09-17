import sys
input = sys.stdin.readline

from collections import deque

def r1(d,n):
    new = [deque([0]*n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[i][j] = d[n-j-1][i]
    return new

n = int(input())
d = [deque(input().split()) for _ in range(n)]
q = int(input())
for _ in range(q):
    c = input().split()
    if c[0] == '1':
        d[int(c[1])-1].appendleft(d[int(c[1])-1].pop())
    else:
        d = r1(d, n)
for i in range(n):
    print(' '.join(d[i]))
