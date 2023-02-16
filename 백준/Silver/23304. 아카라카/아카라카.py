def a(s):
    if len(s) == 1:
        return True
    
    l = len(s)//2

    if s[:l] != s[-l:]:
        return False
    
    return a(s[:l])

S=input().rstrip()
if a(S):
    print('AKARAKA')
else:
    print('IPSELENTI')