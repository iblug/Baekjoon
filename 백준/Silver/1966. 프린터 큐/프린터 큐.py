import sys
input = sys.stdin.readline
from collections import deque
def max_(x):
    return max(x,key=lambda x: x[0])[0]
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    q_ = deque()
    for i in range(n):
        q_.append((q.popleft(), i))
        if i == m:
            k = q_[-1][0]
    m_ = max_(q_)
    cnt = 0
    while True:
        if m_ != k:
            if q_[0][0] == m_:
                q_.popleft()
                cnt += 1
                m_ = max_(q_)
            else:
                q_.append(q_.popleft())
        else:
            if q_[0][0] == m_:
                k_ = q_.popleft()[1]
                cnt += 1
                if k_ == m:
                    break
            else:
                q_.append(q_.popleft())
    print(cnt)