import sys
from collections import deque
q = deque()

n = int(input())

max_ = 0
end_ = 1e6
for _ in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    if x[0] == 1:
        q.append(x[1])
    elif x[0] == 2:
        q.popleft()
    if len(q) > max_:
        max_ = len(q)
        end_ = x[1]
    elif len(q) == max_ and x[1] < end_:
        end_ = x[1]
    
print(max_, end_)