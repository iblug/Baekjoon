n, k = input().split()
n = int(n)
c = 0
for i in range(n+1):
    if i < 10:
        i = '0'+str(i)
    if k in str(i):
        c+=3600
        continue
    for j in range(60):
        if j < 10:
            j = '0'+str(j)
        if k in str(j):
            c+=60
            continue
        for m in range(60):
            if m < 10:
                m = '0'+str(m)
            if k in str(m):
                c += 1
print(c)