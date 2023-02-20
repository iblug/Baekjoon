import sys
input = sys.stdin.readline

def k(s, e):
    if e == 1:
        return
    e //= 3
    for i in range(s+e, s+e*2):
        a[i] = ' '
    k(s,e)
    k(s+2*e, e)

while 1:
    n = input().rstrip()
    if n == '':
        break
    n = int(n)
    a = ['-']*3**n
    k(0, 3**n)
    print(''.join(a))