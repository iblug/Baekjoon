import sys
sys.setrecursionlimit(int(1e6))

def f(t):
    if t == s:
        return True
    if len(t) == L:
        return False
    if t[-1] == 'B':
        return f(t[:-1][::-1])
    else:
        return f(t[:-1])
s = input()
t = input()

L = len(s)
if f(t):
    print(1)
else:
    print(0)