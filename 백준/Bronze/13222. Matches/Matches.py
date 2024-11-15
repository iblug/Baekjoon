from math import sqrt

N, W, H = map(int, input().split())
d = int(sqrt(W**2 + H**2))

for _ in range(N):
    print('YES' if int(input()) <= d else 'NO')