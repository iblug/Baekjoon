import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
_, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

C = [[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        r = 0
        for k in range(M):
            r += A[i][k] * B[k][j]
        C[i][j] = r
for e in C:
    print(' '.join(map(str, e)))