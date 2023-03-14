def f(a, b, d):
    a = a + b
    d += 1
    if a > K:
        return (False, False)
    if d > D:
        return (False, False)
    if a == K and d == D:
        return (a, b)
    
    return f(b, a, d)

D, K = map(int, input().split())
flag = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        aa, bb = f(i, j, 2)
        if aa:
            flag = 1
            break
    if flag:
        break
print(i, j, sep='\n')