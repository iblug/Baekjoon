from collections import deque

N = int(input())
q = deque([(N, 0)])
v = set()
while True:
    a, cnt = q.popleft()
    if a >= 0:
        if (c:=(a+1)//2) not in v:
            v.add(c)
            q.append((c, cnt+1))
        if (b:=a-1) not in v:
            v.add(b)
            q.append((b, cnt+1))
    else:
        break
print(cnt-1)