def per(y):
    if y == n:
        r[0] += 1
        return
    
    for x in range(n):
        if u[x] or lt_rb[n+x-y] or lb_rt[x+y]:
            continue
        lt_rb[n+x-y] = True
        lb_rt[x+y] = True
        u[x] = True

        per(y+1)

        lt_rb[n+x-y] = False
        lb_rt[x+y] = False
        u[x] = False
        

n = int(input())
u=[False]*n
lt_rb=[False]*(3*n-1)
lb_rt=[False]*(3*n-1)
r = [0]
per(0)
print(*r)