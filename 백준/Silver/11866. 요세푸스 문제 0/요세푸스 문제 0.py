from collections import deque

N, K = map(int, input().split())
data = [i for i in range(1, N+1)]
r = deque()
index = K-1
for i in range(N):
    r.append(data.pop(index))
    N-=1
    if N > 0:
        index = (index+K)%N - 1
    else:
        index = 0
    if index <0:
        index+=N
print('<'+', '.join(map(str, r))+'>')