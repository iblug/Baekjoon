import sys
input = sys.stdin.readline

M = int(1e6)
p = [1]*(M+1)
for i in range(2, int(M**0.5)+1):
    if p[i]:
        for j in range(i*2, M+1, i):
            p[j] = 0

t = int(input())
for _ in range(t):
    r = 0
    a = int(input())
    if a == 2 or a == 4:
        print(1)
    else:
        for i in range(3, int(a/2)+1, 2):
            if p[i] and p[a-i]:
                r += 1
        print(r)