import sys
input = sys.stdin.readline

n = int(input())
c = [tuple(map(int, input().split())) for _ in range(n)]
c = sorted(c, key=lambda x: (x[0], x[1]))
stk = []
for e in c:
    while stk:
        if e[1] < stk[-1][1]:
            stk.pop()
        else:
            break
    if stk:
        if e[0] >= stk[-1][1]:
            stk.append(e)
    else:
            stk.append(e)

print(len(stk))  