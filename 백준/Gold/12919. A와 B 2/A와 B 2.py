from collections import deque

def f(t):
    q = deque()
    q.append(t)
    v.add(t)
    while q:
        t = q.popleft()
        if t == s:
            return True
        if len(t) == L:
            continue
        if t[0] == 'B':
            B = t[:0:-1]
            if B not in v:
                q.append(B)
                v.add(B)
        if t[-1] == 'A':
            A = t[:-1]
            if A not in v:
                q.append(A)
                v.add(A)
    return False
    

s = input()
t = input()

L = len(s)
v = set()
if f(t):
    print(1)
else:
    print(0)