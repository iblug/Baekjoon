import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

c = 0
for i in range(M):
    t, r = map(int, input().split())
    c += r
    if c > K:
        print(i+1, 1)
        break
else:
    print(-1)