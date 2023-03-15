from collections import deque

def f(t):
    q = deque()
    q.append(t)
    while q:
        t = q.popleft()
        if t == s:
            return True
        if len(t) == L:
            continue
        if t[0] == 'B':
            q.append(t[:0:-1])
        if t[-1] == 'A':
            q.append(t[:-1])
    return False

s = input()
t = input()

L = len(s)

if f(t):
    print(1)
else:
    print(0)