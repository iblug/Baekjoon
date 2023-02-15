def bur(n, x):
    if n == 0:
        if x == 0:
            return 0
        else:
            return 1
    bb = 2**(n+1)-3
    pp = 2**n-1
    p = 2**(n+1)-1
    
    if x == 0:
        return 0
    elif bb+2 > x:
        return bur(n-1, x-1)
    elif bb+2 == x:
        return pp + 1
    elif bb+2 < x:
        return pp + 1 + bur(n-1, x-bb-2)
    else:
        return p

N, X = map(int, input().split())
print(bur(N, X))