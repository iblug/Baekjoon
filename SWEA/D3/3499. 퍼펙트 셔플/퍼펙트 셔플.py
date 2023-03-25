from collections import deque
T = int(input())
for t in range(T):
    n = int(input())
    q = list(input().split())
    result = []
    q1 = deque(q[:(n+1)//2])
    q2 = deque(q[(n+1)//2:])
    while q1:
        result.append(q1.popleft())
        if q2:
            result.append(q2.popleft())
    print(f'#{t+1}', *result)