def f(a, b, d):
    a = a + b
    d += 1
    if a > K:
        return False
    if d > D:
        return False
    if a == K and d == D:
        return True
    
    return f(b, a, d)

D, K = map(int, input().split())
flag = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        if f(i, j, 2):
            flag = 1
            break
    if flag:
        break
print(i, j, sep='\n')