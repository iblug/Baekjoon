import sys
input = sys.stdin.readline

def com(c):
    if len(c) == n//2:
        cc = [p for p in range(n) if p not in c]
        a = 0
        for j in range(n):
            if j in c:
                for k in c:
                    a += g[j][k]
            else:
                for t in cc:
                    a -= g[j][t]
        r.append(abs(a))
        return
    start = c[-1] + 1 if c else 0
    for i in range(start, n):
        c.append(i)
        com(c)
        c.pop()

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

r = []
com([])
print(min(r))