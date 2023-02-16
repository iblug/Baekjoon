import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def a(s):
    if len(s) == 1:
        return True
    
    l = len(s)
    L = l//2
    
    if l & 1:
        R = l//2+1
    else:
        R = l//2

    if s[:L] != s[R:]:
        return False
    
    return a(s[:L]) & a(s[R:])

S=input().rstrip()
if a(S):
    print('AKARAKA')
else:
    print('IPSELENTI')