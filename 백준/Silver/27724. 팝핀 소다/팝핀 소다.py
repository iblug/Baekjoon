n, m, k = map(int, input().split())

t = 2
c = 0
while t <= n:
    if k < t:
        if m != 0:
            m -= 1
        else:
            break
    
    t *= 2
    c += 1
    
print(c)