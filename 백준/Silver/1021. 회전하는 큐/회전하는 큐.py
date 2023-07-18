from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

q = deque([i for i in range(1, n+1)])
r = 0
for i in a:
    while 1:
        if q[0] == i:
            q.popleft()
            n -= 1
            break
        idx = q.index(i)
        if idx <= n//2:
            q.append(q.popleft())
        else:
            q.appendleft(q.pop())
        r += 1
print(r)