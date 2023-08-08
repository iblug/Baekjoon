import sys
input = sys.stdin.readline

N = int(input())
s = []
for _ in range(N):
    d = list(map(int, input().split()))
    if d[0] == 1:
        s.append(d[1])
    elif d[0] == 2 and s:
        print(s.pop())
    elif d[0] == 2:
        print(-1)
    elif d[0] == 3:
        print(len(s))
    elif d[0] == 4 and s:
        print(0)
    elif d[0] == 4:
        print(1)
    elif d[0] == 5 and s:
        print(s[-1])
    elif d[0]:
        print(-1)