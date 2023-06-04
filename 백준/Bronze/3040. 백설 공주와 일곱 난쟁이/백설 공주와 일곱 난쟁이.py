import sys
input = sys.stdin.readline

d = [int(input()) for _ in range(9)]
t = sum(d)-100
f = 0
for i in range(8):
    for j in range(i+1, 9):
        if d[i] + d[j] == t:
            f = 1
            break
    if f:
        break
[print(d[k]) for k in range(9) if k not in (i, j)]